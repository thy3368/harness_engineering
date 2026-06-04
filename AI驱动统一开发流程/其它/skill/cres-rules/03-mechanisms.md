# 03 核心机制规则

本文档涵盖 CRES/UFT 代码中必须严格遵守的核心机制：事务处理、并发加锁、M标记、while(true)循环保护、内部变量定义。

---

## 1 事务处理机制

### 1.1 禁止事务嵌套

**规则**：从 `[事务处理开始]` 到 `[事务处理结束]` 之间，调用的任何函数不能再包含 `[事务处理开始]`。

**后果**：事务嵌套会导致当前事务被回滚，数据不一致。

```yaml
# ❌ 错误：事务嵌套
[事务处理开始]
  [LF_权益买卖_委托下达总控][...][...]   # ← 该函数内部包含 [事务处理开始]
[事务处理结束]
# 后果：当前事务被回滚

# ✅ 正确：事务块内调用的函数不含事务处理
[事务处理开始]
  [LF_权益买卖_委托下达总控][...][...]   # ← 该函数内部不包含 [事务处理开始]
[事务处理结束]
```

### 1.2 事务自动回滚

- 若分支判断导致 `[事务处理结束]` 未执行，函数退出时会根据处理结果自动提交或回滚事务
- 业务处理报错时**不需要显式** `[事务回滚]`，正常报错返回即可，服务结束时会自动回滚当前事务
- **只在需要主动回滚的场景才使用** `[事务回滚]`，不要在错误处理中冗余添加

```yaml
# ❌ 错误：错误处理中冗余添加事务回滚
[事务处理开始]
  [获取记录][...][...][...]
  [处理失败]
  {
    [事务回滚]          # ← 冗余！报错返回时自动回滚
    [记录日志][CNST_DLOGERROR][][获取记录失败][@entrust_serial_no]
    [正常返回]
  }
[事务处理结束]

# ✅ 正确：报错返回时自动回滚，无需显式 [事务回滚]
[事务处理开始]
  [获取记录][...][...][...]
  [处理失败]
  {
    [记录日志][CNST_DLOGERROR][][获取记录失败][@entrust_serial_no]
    [正常返回]          # ← 自动回滚当前事务
  }
[事务处理结束]

# ✅ 正确：主动回滚场景——业务校验不通过需要撤销已做操作
[事务处理开始]
  [修改记录][uft_centrusts][entrust_status = '2']
  if(@available_amount < @entrust_amount)
  {
    [事务回滚]          # ← 主动回滚：余额不足，撤销状态修改
    [记录日志][CNST_DLOGERROR][][可用余额不足][@available_amount, @entrust_amount]
    [正常返回]
  }
[事务处理结束]
```

**文档标注**：被上级事务调用的服务，文档中必须标注：
> ⚠️ 本服务可能被上级事务包裹，不能包含[事务处理开始]

### 1.3 调用链事务传递

- 上级服务开启事务后，调用的下级服务/函数**不能再开事务**（否则构成嵌套回滚）
- 分析下级服务时，**必须判断其是否在上级事务内被调用**
- 若是，则下级服务的事务处理由上级接管，下级服务不得包含 `[事务处理开始]`

```yaml
# 上级服务 LS_撤单处理
[事务处理开始]
  [AS_委托状态更新][...]     # ← AS 不能有自己的 [事务处理开始]
  [AS_持仓更新][...]         # ← AS 不能有自己的 [事务处理开始]
[事务处理结束]

# 分析 AS_委托状态更新 时，必须检查：
# 1. 是否被含事务的上级服务调用 → 是 → 不能含 [事务处理开始]
# 2. 是否也有独立调用场景 → 是 → 需在独立入口处自行管理事务
```

---

## 2 并发处理与加锁规则

### 2.1 加锁时机（核心规则）

**规则：必须在获取记录后立即加锁，在业务判断之前加锁。**

- `[修改记录][表名][]` 参数为空 = 仅加锁，不修改任何字段
- 获取记录到加锁之间存在时间窗口，其他接口可能同时修改同一记录

```yaml
# ❌ 错误：先业务处理，后加锁（存在并发窗口）
[获取记录][uft_centrusts(uft_uniq_entrusts_entsrlno)][
  entrust_serial_no = @entrust_serial_no
][
  entrust_status = @entrust_status
]
# ⚠️ 此处有时间窗口！其他接口可能同时获取并修改同一条记录
if(@entrust_status == '3')
{
  [修改记录][uft_centrusts][entrust_status = '5']   # ← 加锁时机过晚
}

# ✅ 正确：获取记录后立即加锁，再进行业务判断
[获取记录][uft_centrusts(uft_uniq_entrusts_entsrlno)][
  entrust_serial_no = @entrust_serial_no
][
  entrust_status = @entrust_status
]
[修改记录][uft_centrusts][]   # ← 立即加锁（空参数=仅加锁）
if(@entrust_status == '3')
{
  [修改记录][uft_centrusts][entrust_status = '5']   # ← 已持有锁，安全修改
}
```

### 2.2 委托表类型识别

**规则：必须通过 `entrust_table_type` 从 `uft_centrustrelation` 获取委托表类型，禁止硬编码表名。**

| 委托表类型常量 | 业务类型 | 委托表名 |
|--------------|---------|---------|
| `DICT_ENTRUSTTYPE_SPOTENTRUST` | 现货/沪深/港股通/ETF | `uft_centrusts` |
| `DICT_ENTRUSTTYPE_NEEQENTRUST` | 股转 | `uft_cneeqentrusts` |
| `DICT_ENTRUSTTYPE_RZRQENTRUST` | 融资融券 | `uft_crzrqentrusts` |
| `DICT_ENTRUSTTYPE_FIXEDINCOMEENTRUST` | 固收 | `uft_cfixedentrusts` |
| `DICT_ENTRUSTTYPE_BULKENTRUST` | 大宗交易 | `uft_cbulkentrusts` |
| `DICT_ENTRUSTTYPE_REFCENTRUST` | 转融通 | `uft_crefcentrusts` |
| `DICT_ENTRUSTTYPE_OPTIONENTRUST` | 个股期权 | `uft_coptionentrust` |

```yaml
# ❌ 错误：硬编码委托表名
[获取记录][uft_centrusts(uft_uniq_entrusts_entsrlno)][...]
# 如果实际委托在股转委托表，会找不到记录

# ✅ 正确：通过委托关系表获取委托表类型，动态选择
[获取记录][uft_centrustrelation(uft_uniq_entrustrelation_srlno)][
  entrust_serial_no = @entrust_serial_no
][
  entrust_table_type = @entrust_table_type
]

switch (@entrust_table_type)
{
  case DICT_ENTRUSTTYPE_SPOTENTRUST:
    [获取记录][uft_centrustrelation.uft_centrusts][...]
    [修改记录][uft_centrusts][]   # 立即加锁
    break;
  case DICT_ENTRUSTTYPE_NEEQENTRUST:
    [获取记录][uft_centrustrelation.uft_cneeqentrusts][...]
    [修改记录][uft_cneeqentrusts][]   # 立即加锁
    break;
  # ... 其他类型
}
```

### 2.3 指令表加锁规则

**规则：如果委托表的 `ins_id > 0`，必须先锁指令表，再锁委托表。**

```yaml
# ❌ 错误：只锁委托表，未锁指令表
[获取记录][uft_centrustrelation.uft_cneeqentrusts][...]
[修改记录][uft_cneeqentrusts][]   # 即使 ins_id > 0 也未锁指令表
# 其他接口（撤成、撤单）可能同时修改指令表，导致指令成交数量计算不准确

# ✅ 正确：ins_id > 0 时，先锁指令表再锁委托表
[获取记录][uft_centrustrelation.uft_centrusts][...]
if(@uft_centrusts.ins_id > 0)
{
  [获取记录][uft_cinstruction(uft_uniq_tinstruction)][
    company_id = @uft_centrusts.company_id,
    ins_id = @uft_centrusts.ins_id,
    index_daily_modify = @uft_centrusts.index_daily_modify
  ]
  [修改记录][uft_cinstruction][]   # 先锁指令表
}
[修改记录][uft_centrusts][]         # 再锁委托表
```

### 2.4 表更新顺序（防死锁）

**所有涉及相同表的接口，必须遵循统一的表更新/加锁顺序：**

1. **指令表** `uft_cinstruction` — 如果 `ins_id > 0`，最先锁定
2. **委托表**（根据委托表类型选择） — 次优先
3. **委托关系表** `uft_centrustrelation` — 中等
4. **持仓表** `uft_cequnitstock` — 中等
5. **资产单元表** `uft_cassetday` — 较低
6. **成交表** `uft_crealdeal` / `uft_cneeqrealdeal` — 较低

**死锁场景**：
```yaml
# 接口A：先锁委托表再锁指令表
[修改记录][uft_centrusts][]
[修改记录][uft_cinstruction][]

# 接口B：先锁指令表再锁委托表
[修改记录][uft_cinstruction][]
[修改记录][uft_centrusts][]
# ❌ 循环等待 → 死锁

# ✅ 解决方案：所有接口统一顺序——先锁指令表再锁委托表
```

### 2.5 各接口加锁规则速查

| 接口类型 | 加锁顺序 | 关键点 |
|---------|---------|--------|
| **撤单** | 委托关系表(获取) → 委托表(获取+**立即加锁**) → 业务处理 | 获取记录后必须立即加锁 |
| **成交** | 委托关系表(获取) → 指令表(如有,获取+加锁) → 委托表(获取+加锁) → 业务处理 | 必须先锁指令表 |
| **废单** | 委托关系表(获取) → 委托表(获取+**立即加锁**) → 业务处理 | 所有废单接口一致 |
| **撤成** | 委托关系表(获取) → 指令表(通过 `AF_报盘回报_指令锁`) → 委托表(获取+加锁) | 使用专用指令锁函数 |

---

## 3 M标记机制

### 3.1 用法一：批量容错

**场景**：`[遍历记录]` 循环中，包装可能失败的操作，使单条记录失败不阻塞整个批量处理。

```yaml
# ✅ 正确：M标记 + [处理失败] + [继续执行] 三件套
[遍历记录开始-无拷贝][对象][条件][输出]
  <M>[AS_可能失败的操作][参数][输出]

  [处理失败]
  {
    [记录日志][CNST_DLOGWARNING][][单个记录处理失败，继续处理下一条][@param, @error_no, @error_info]
    [继续执行]
  }

  [处理成功]
  {
    // 正常处理逻辑
  }
[遍历记录结束-无拷贝]
```

**M标记使用原则**：

| 必须添加 `<M>` | 不需要添加 `<M>` |
|---------------|-----------------|
| 外部数据获取 | 遍历记录本身 |
| 数据验证 | 权限查询 |
| 字段转换 | 基础数据获取（`[获取记录]`） |
| 复杂计算 | |

```yaml
# ❌ 错误：遍历操作加M标记（冗余）
<M>[遍历记录开始-无拷贝][...][...][...]   # ← 遍历操作预期不会失败

# ❌ 错误：可能失败的操作未加M标记
[遍历记录开始-无拷贝][...][...][...]
  [AS_外部数据获取][...][...]   # ← 没有 <M>，单条失败会阻塞整个批量
[遍历记录结束-无拷贝]
```

### 3.2 用法二：记录存在性检查

**场景**：需要判断记录是否存在，根据存在与否执行不同逻辑（典型："存在→更新，不存在→插入"）。

**规则**：必须使用 `<M>[获取记录][...]` + `[继续执行]`，否则记录为空时会直接报错返回，后续 `[记录为空]` 分支无法执行。

```yaml
# ✅ 正确：M标记 + 继续执行 + 记录为空/不为空分支
<M>[获取记录][uft_centrustrelation(uft_uniq_entrustrelation_srlno)][
  entrust_serial_no = @cancelentrust_serial_no
]
[继续执行]                         # ← 记录为空时不报错返回，继续执行
[记录不为空][uft_centrustrelation]
{
  // 记录存在，执行更新逻辑
  <M>[获取记录][uft_cneeqentrusts(uft_uniq_neeqentrusts)][
    entrust_serial_no = @cancelentrust_serial_no
  ]
  [继续执行]                       # ← 嵌套获取记录也需要各自的 <M> + [继续执行]
  [记录不为空][uft_cneeqentrusts]
  {
    [修改记录][uft_cneeqentrusts][entrust_status = @cancel_status]
  }
  [记录为空][uft_cneeqentrusts]
  {
    [记录日志][CNST_DLOGERROR][][委托关系表存在但委托表不存在，数据不一致][@cancelentrust_serial_no]
  }
}
[记录为空][uft_centrustrelation]
{
  // 记录不存在，执行插入逻辑
  [AF_权益业务公共_股转委托数据插入][...]
}

# ❌ 错误：没有M标记和[继续执行]，记录为空时直接报错返回
[获取记录][uft_centrustrelation(uft_uniq_entrustrelation_srlno)][
  entrust_serial_no = @cancelentrust_serial_no
]
# ← 记录不存在时直接报错返回，无法执行后续逻辑
[记录为空][uft_centrustrelation]
{
  // ❌ 这个分支永远无法执行
}
```

**关键要点**：
- `<M>` 和 `[继续执行]` **必须配套使用**，缺一不可
- 嵌套的 `[获取记录]` **必须各自**使用 `<M>` + `[继续执行]`

---

## 4 while(true) 循环保护机制

**规则：所有使用 `while(true)` 循环的查询接口，必须实现完整的保护机制，防止死循环。**

### 4.1 九种保护机制

| # | 保护机制 | 说明 |
|---|---------|------|
| 1 | 总条数限制 | `@row_count >= @request_num` 时跳出循环 |
| 2 | 本次返回条数 | 本次返回记录数 < `request_num` 时终止 |
| 3 | EOF判断 | 同步调用后判断是否EOF |
| 4 | 定位串比较 | 定位串未变化则终止（**最关键**） |
| 5 | error_no检查 | `error_no == -60` 表示无结果，正常返回 |
| 6 | 同步调用失败处理 | 失败时报错返回 |
| 7 | 最大循环次数 | 防止极端情况死循环 |
| 8 | 解包器字段检查 | 访问字段前检查字段是否存在 |
| 9 | 记录跳过处理 | 所有记录都被跳过时终止 |

### 4.2 定位串比较（详细）

**原理**：调用前置机接口前保存定位串，查询结束后比较新旧定位串，相同则说明没有翻页，可能陷入死循环。

```yaml
@max_loop_count = 1000;
@loop_count = 0;
@row_count = 0;

while(true)
{
    @loop_count++;

    # 保护7：最大循环次数
    if(@loop_count > @max_loop_count) { break; }

    # 保护1：总条数足够
    if(@row_count >= @request_num) { break; }

    # 保存定位串
    hs_strncpy(@prev_position_str, @position_str, sizeof(@prev_position_str) - 1);

    # 同步调用
    [同步调用][...][][out_packer = lpUnPacker]
    [处理失败] { [报错返回][ERR_XXX] }

    # 保护8：解包器为空
    if(lpUnPacker == NULL) { break; }

    # 保护5：error_no检查
    if(lpUnPacker->FindColIndex("error_no") >= 0)
    {
        @error_no = lpUnPacker->GetInt("error_no");
        if(@error_no == -60) { break; }
        else if(@error_no != 0) { [报错返回][ERR_XXX] }
    }

    # 保护3：立即EOF
    if(lpUnPacker->IsEOF()) { break; }

    # 遍历返回结果
    @current_batch_count = 0;
    while(!lpUnPacker->IsEOF())
    {
        # 保护8：字段检查
        if(lpUnPacker->FindColIndex("entrust_serial_no") < 0) { continue; }
        @entrust_serial_no = lpUnPacker->GetInt("entrust_serial_no");

        # 业务处理...

        @current_batch_count++;
        @row_count++;
        lpUnPacker->Next();
    }

    # 保护2：本次返回条数 < request_num
    if(@current_batch_count < @request_num) { break; }

    # 保护4：定位串比较（最关键）
    if(hs_strcmp(@position_str, "0") != 0 && length(trim(@position_str)) > 0)
    {
        if(hs_strcmp(@position_str, @prev_position_str) == 0) { break; }
    }
}
```

```yaml
# ❌ 错误：while(true)缺少保护机制
while(true)
{
    # 没有最大循环次数限制
    # 没有定位串比较保护
    # 没有error_no检查
    [同步调用][...][...]
    # 如果定位串不变，会陷入死循环
}
```

### 4.3 必须定义的内部变量

所有 while(true) 循环接口，必须在 `<internalParams>` 中定义以下变量：

| 变量名 | 用途 | 推荐类型 |
|-------|------|---------|
| `prev_position_str` | 上一次定位串，用于比较 | `HsChar64` |
| `position_str_before` | 定位串变更前值 | `HsChar64` |
| `row_count_before` | 循环前已有条数 | `HsPosUInt` |
| `current_batch_count` | 本次返回条数 | `HsPosUInt` |
| `actual_processed_count` | 实际处理条数 | `HsPosUInt` |
| `max_loop_count` | 最大循环次数 | `HsPosUInt` |
| `loop_count` | 当前循环计数 | `HsPosUInt` |

---

## 5 内部变量定义规则

**规则：所有在业务代码逻辑中使用的临时变量，必须在文件的 `<internalParams>` 中定义，否则 UFTDB 工具无法识别。**

```xml
<!-- ✅ 正确：在文件头部定义所有内部变量 -->
<internalParams id="block_amount2_available" name="股份数量2的可用额度"
  paramType="NON_STD_FIELD" type="HsAmount"
  uuid="a1b2c3d4-e5f6-4789-a0b1-c2d3e4f5a6b8"/>
<internalParams id="diffsz" name="差值数量"
  paramType="NON_STD_FIELD" type="HsAmount"
  uuid="b2c3d4e5-f6a7-4890-b1c2-d3e4f5a6b7c9"/>
```

**必须包含的属性**：

| 属性 | 说明 | 示例 |
|------|------|------|
| `id` | 变量名称（与代码中 `@` 后的名称一致） | `block_amount2_available` |
| `name` | 变量中文描述 | `股份数量2的可用额度` |
| `paramType` | 必须为 `"NON_STD_FIELD"` | `NON_STD_FIELD` |
| `type` | 数据类型 | 见下表 |
| `uuid` | 唯一标识符 | `a1b2c3d4-e5f6-4789-a0b1-c2d3e4f5a6b8` |

**常用数据类型**：

| 类型 | 用途 |
|------|------|
| `HsAmount` | 金额、数量 |
| `HsPrice` | 价格 |
| `HsPosUInt` | 无符号整数（位置、计数） |
| `HsSerialNo` | 序列号 |
| `HsDateTime` | 日期时间 |
| `HsFlag` | 标志位 |

```yaml
# ❌ 错误：使用未定义的内部变量
@block_amount2_available = @uft_cszstockholderquota.begin_block_amount2
                          - @uft_cszstockholderquota.block_saled_amount;
# UFTDB工具无法识别 @block_amount2_available，编译/运行会出错

# ✅ 正确：先在 <internalParams> 中定义，再在代码中使用
# 定义见上方 XML 示例
@block_amount2_available = @uft_cszstockholderquota.begin_block_amount2
                          - @uft_cszstockholderquota.block_saled_amount;
```
