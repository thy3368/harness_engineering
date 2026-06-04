# CRES/UFT 代码生成 Skill

## 1 描述

根据业务需求，生成符合 CRES/UFT 规范的服务和函数文件（`.uftatomservice`、`.uftatomfunction`、`.uftfunction`、`.uftservice`、`.uftfactorservice`、`.uftfactorfunction`），确保事务安全、并发正确、命名规范。

## 2 适用条件

- 用户要求创建或修改 CRES/UFT 服务/函数文件
- 用户提供了新服务或函数的业务需求
- 用户要求将业务逻辑转换为 CRES 伪代码

## 3 必读规则（10条铁律）

### 铁律1：禁止事务嵌套

`[事务处理开始]` 块内调用的函数**不能**包含 `[事务处理开始]`，否则当前事务会被回滚。

```yaml
# ❌ 错误
[事务处理开始]
  [LF_某函数][...]   # 该函数内部包含 [事务处理开始] → 回滚！
[事务处理结束]

# ✅ 正确
[事务处理开始]
  [LF_某函数][...]   # 该函数内部不包含 [事务处理开始]
[事务处理结束]
```

### 铁律2：禁止行内注释

注释必须独立成行，不能放在代码右侧。行内注释会导致 UFTDB 编译报错。

```yaml
# ❌ 错误
inter_code = @inter_code_temp,  // 委托代码对应的证券内码

# ✅ 正确
// 委托代码对应的证券内码
inter_code = @inter_code_temp,
```

### 铁律3：加锁必须在业务判断之前

`[获取记录]` 后立即 `[修改记录][表名][]` 空加锁，然后再进行 if/switch 业务判断。

```yaml
# ❌ 错误：先判断再加锁
[获取记录][uft_centrusts(uft_uniq_entrusts_entsrlno)][
  entrust_serial_no = @entrust_serial_no
][
  entrust_status = @entrust_status
]
if(@entrust_status == '3')
{
  [修改记录][uft_centrusts][entrust_status = '5']   # 加锁时机过晚
}

# ✅ 正确：获取后立即加锁
[获取记录][uft_centrusts(uft_uniq_entrusts_entsrlno)][
  entrust_serial_no = @entrust_serial_no
][
  entrust_status = @entrust_status
]
[修改记录][uft_centrusts][]   # 立即空加锁
if(@entrust_status == '3')
{
  [修改记录][uft_centrusts][entrust_status = '5']   # 已持有锁，安全修改
}
```

### 铁律4：表更新顺序统一

所有涉及相同表的接口必须遵循统一加锁/更新顺序，防止死锁：

1. **指令表** `uft_cinstruction`（如果 `ins_id > 0`，最先锁定）
2. **委托表**（根据 `entrust_table_type` 选择）
3. **委托关系表** `uft_centrustrelation`
4. **持仓表** `uft_cequnitstock`
5. **资产单元表** `uft_cassetday`
6. **成交表** `uft_crealdeal` / `uft_cneeqrealdeal`

### 铁律5：委托表类型禁止硬编码

必须从 `uft_centrustrelation` 获取 `entrust_table_type`，通过 switch-case 动态选择委托表，禁止直接硬编码表名。

```yaml
# ✅ 正确：通过委托关系表获取类型
[获取记录][uft_centrustrelation(uft_uniq_entrustrelation_srlno)][
  entrust_serial_no = @entrust_serial_no
][
  entrust_table_type = @entrust_table_type
]
switch (@entrust_table_type)
{
  case DICT_ENTRUSTTYPE_SPOTENTRUST:
    [获取记录][uft_centrustrelation.uft_centrusts][...]
    break;
  case DICT_ENTRUSTTYPE_NEEQENTRUST:
    [获取记录][uft_centrustrelation.uft_cneeqentrusts][...]
    break;
  default: break;
}
```

### 铁律6：M标记+继续执行配套

记录存在性检查必须使用 `<M>[获取记录]` + `[继续执行]`，否则记录为空时直接报错返回，后续 `[记录为空]` 分支永远无法执行。

```yaml
# ✅ 正确
<M>[获取记录][uft_centrustrelation(uft_uniq_entrustrelation_srlno)][
  entrust_serial_no = @entrust_serial_no
]
[继续执行]
[记录不为空][uft_centrustrelation]
{
  // 更新逻辑
}
[记录为空][uft_centrustrelation]
{
  // 插入逻辑
}

# ❌ 错误：缺少M标记和继续执行
[获取记录][uft_centrustrelation(uft_uniq_entrustrelation_srlno)][
  entrust_serial_no = @entrust_serial_no
]
[记录为空][uft_centrustrelation]
{
  // 死代码！永远无法执行
}
```

### 铁律7：internalParams必须定义

所有在 `<code>` 中使用的临时变量（`@变量名`），必须在文件头部的 `<internalParams>` 中声明，否则 UFTDB 工具无法识别。

```xml
<internalParams id="tmp_status" name="临时状态" paramType="NON_STD_FIELD" type="HsPosInt" uuid="..."/>
<internalParams id="prev_position_str" name="上一次定位串" paramType="NON_STD_FIELD" type="HsChar64" uuid="..."/>
```

### 铁律8：错误处理不能遗漏

每个 `[获取记录]`/`[修改记录]` 等可能失败的操作后，必须跟 `[处理失败]` 块。

```yaml
[获取记录-无拷贝][uft_centrusts][entrust_serial_no = @serial_no][...]
[处理失败]
{
  [记录日志][CNST_DLOGERROR][][获取委托记录失败][@serial_no, @error_no, @error_info]
  [正常返回]
}

[修改记录][uft_centrusts][entrust_status = '6']
[处理失败]
{
  [记录日志][CNST_DLOGERROR][][修改委托状态失败][@serial_no, @error_no, @error_info]
  [正常返回]
}
```

### 铁律9：批量操作必须容错

遍历中的可能失败操作必须用 `<M>` 包装，单条失败不阻塞整体。

```yaml
[遍历记录开始-无拷贝][uft_centrusts][company_id = @company_id][...]
  <M>[AS_可能失败的操作][参数][输出]
  [处理失败]
  {
    [记录日志][CNST_DLOGWARNING][][单个记录处理失败，继续处理下一条][@param, @error_no, @error_info]
    [继续执行]
  }
[遍历记录结束-无拷贝]
```

### 铁律10：while(true)必须有9种保护

| # | 保护机制 | 说明 |
|---|---------|------|
| 1 | 总条数限制 | `@row_count >= @request_num` 时跳出 |
| 2 | 本次返回条数 | 本次返回 < `request_num` 时终止 |
| 3 | EOF判断 | `lpUnPacker->IsEOF()` |
| 4 | 定位串比较 | 新旧定位串相同则终止（**最关键**） |
| 5 | error_no检查 | `error_no == -60` 表示无结果 |
| 6 | 同步调用失败 | 失败时报错返回 |
| 7 | 最大循环次数 | `@loop_count > @max_loop_count` 时跳出 |
| 8 | 解包器字段检查 | `FindColIndex < 0` 时跳过 |
| 9 | 记录跳过处理 | 全部跳过时终止 |

---

## 4 代码生成流程

### 4.1 需求分析

根据用户需求确定以下要素：

| 要素 | 确定方法 |
|------|---------|
| 服务类型（AS/AF/LF/LS/RS/RF） | 根据功能定位：原子操作→AS/AF，业务逻辑→LF/LS，规则→RS/RF |
| 所属模块和业务域 | 权益/衍生品/固收/基础公共，对应不同目录和 Object ID 范围 |
| 输入参数 | 从 component.xml 获取结构字段，加上 comm_odefault 模板参数（仅 LS/RS） |
| 输出参数 | error_no + error_info + error_pathinfo（标准三件套）+ 业务结果 |
| 内部变量 | 遍历计数器、临时状态、定位串等，按需声明 |
| 是否涉及事务 | 涉及写操作（插入/修改/删除）→ 需要 `[事务处理开始/结束]` |
| 是否涉及加锁 | 并发操作 → `[修改记录][表名][]` 空加锁 |
| 是否涉及批量 | 遍历 → `<M>` 容错 |

### 4.2 参数定义

**输入参数规则**：

| 层级 | 必含输入 | 说明 |
|------|---------|------|
| LS/RS | `comm_odefault` 模板参数 | `login_company`、`login_operator`、`login_ip` 等 |
| 所有层级 | 业务入参 | 从 component.xml 结构中选取所需字段 |
| LF/AF | 仅业务入参 | 不含 comm_odefault |

**输出参数规则**：

| 参数 | 类型 | 说明 |
|------|------|------|
| `error_no` | 标准字段 | 错误码，0 表示成功 |
| `error_info` | 标准字段 | 错误描述 |
| `error_pathinfo` | 标准字段 | 错误路径（仅 LS/LF 需要） |
| 业务输出 | 标准字段或 COMPONENT | 根据业务需求定义 |

**内部参数规则**：

- 所有 `@变量名` 必须在 `<internalParams>` 中声明
- `paramType` 固定为 `"NON_STD_FIELD"`
- 常用类型：`HsAmount`（金额/数量）、`HsPrice`（价格）、`HsPosUInt`（计数）、`HsSerialNo`（序号）、`HsFlag`（标志）、`HsChar64`（字符串）

**获取字段定义的方法**：

```bash
# 从 structdb 查询结构字段
python3 scripts/structdb.py fields <结构名>

# 从 component.xml 搜索字段
grep "<字段名>" metadata/component.xml
```

### 4.3 伪代码编写

按以下步骤编写 `<code>` 中的伪代码：

**步骤1：选择模式模板**

| 业务场景 | 推荐模式 | 参考 |
|---------|---------|------|
| 委托下达 | 服务级标准流程 | `cres-rules/04-patterns.md` §1 |
| 撤单处理 | 撤单模式 | `cres-rules/04-patterns.md` §4 |
| 成交处理 | 成交模式 | `cres-rules/04-patterns.md` §5 |
| 废单处理 | 废单模式 | `cres-rules/04-patterns.md` §6 |
| 数据查询 | while(true) 同步调用 | `cres-rules/04-patterns.md` §10 |
| 数据导出 | 遍历+E标记保护 | `cres-rules/04-patterns.md` §8 |
| 记录存在性判断 | M标记+继续执行 | `cres-rules/04-patterns.md` §9 |

**步骤2：填充业务逻辑**

1. 先写参数校验（`unlikely(@param == NULL)` → `<W>[报错返回]`）
2. 再写核心业务流程（获取记录 → 加锁 → 业务判断 → 修改/插入）
3. 最后写消息通知和日志

**步骤3：校验10条铁律**

逐条检查是否违反铁律1~10。

### 4.4 质量检查

生成代码后必须进行以下检查：

| 检查项 | 检查方法 |
|-------|---------|
| 事务嵌套 | 事务块内调用的函数是否包含 `[事务处理开始]` |
| M标记配套 | 每个 `<M>` 是否有对应的 `[继续执行]` |
| 命名规范 | 文件名前缀是否与扩展名匹配，Object ID 是否在正确范围 |
| 参数引用 | 所有 `@变量名` 是否在 `inputParameters`/`outputParameters`/`internalParams` 中定义 |
| 错误处理 | 每个 `[获取记录]`/`[修改记录]` 后是否有 `[处理失败]` |
| 加锁时机 | `[获取记录]` 后是否立即 `[修改记录][表名][]` 空加锁 |
| 表更新顺序 | 多表操作是否按指令表→委托表→关系表→持仓表→资产单元表→成交表 |
| 行内注释 | 代码行右侧是否无 `//` 注释 |
| uuid 唯一性 | 所有 uuid 是否为不同的合法 UUID |

---

## 5 XML 骨架模板

> **规则**：`cres_template.py` 生成骨架时，遵循与真实源码一致的格式：
> - **所有**根元素（Service 和 Function）都必须有 `id` 属性（UUID）
> - `LS` 额外需要 `useInterFaceFlag="true"`
> - `outputParameters` **无** `xsi:type` 属性（组件输出用 `paramType="COMPONENT"` 区分）
> - **无** `<testData>` 标签
> - **无** `xmlns:xsi` 命名空间声明

### 5.1 原子服务 (.uftatomservice)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<business:Service xmlns:business="http://www.hundsun.com/ares/studio/uft/business/1.0.0" chineseName="AS_模块名_功能描述" description="服务功能描述" objectId="7300XXXX" id="生成的UUID">
  <inputParameters id="entrust_serial_no" uuid="生成的UUID"/>
  <inputParameters id="company_id" uuid="生成的UUID"/>
  <outputParameters id="error_no" uuid="生成的UUID"/>
  <outputParameters id="error_info" uuid="生成的UUID"/>
  <outputParameters id="exist_flag" uuid="生成的UUID"/>
  <outputParameters id="entrust_status" uuid="生成的UUID"/>
  <outputParameters id="uft_centrusts" paramType="COMPONENT" type="uft_centrusts" uuid="生成的UUID"/>
  <internalParams id="tmp_status" name="临时状态变量" paramType="NON_STD_FIELD" type="HsPosInt" uuid="生成的UUID"/>
  <internalParams id="tmp_amount" name="临时数量变量" paramType="NON_STD_FIELD" type="HsAmount" uuid="生成的UUID"/>
  <code>
  @exist_flag = '0';

  <M>[获取记录][uft_centrusts(uft_uniq_entrusts_entsrlno)][
    entrust_serial_no = @entrust_serial_no
  ][
    entrust_status = @entrust_status,
    entrust_amount = @entrust_amount
  ]
  [继续执行]

  [记录不为空][uft_centrusts]
  {
    [修改记录][uft_centrusts][]

    if(@entrust_status == '0')
    {
      [修改记录][uft_centrusts][
        entrust_status = '6'
      ]
      [处理失败]
      {
        [记录日志][CNST_DLOGERROR][][修改委托状态失败][@entrust_serial_no, @error_no, @error_info]
        [正常返回]
      }
      @exist_flag = '1';
    }
  }
  [记录为空][uft_centrusts]
  {
    [记录日志][CNST_DLOGDEBUG][][未找到委托记录][@entrust_serial_no]
  }
  </code>
</business:Service>
```

**关键说明**：
- `objectId`：权益域 730000~739999，衍生品域 740000~749999，基础公共 710000~719999
- `id`：Service 根元素必须有 UUID（如 `a38da1a9-819b-4fde-802e-c16e6cd285b4`）
- `paramType="COMPONENT"` 的输出参数必须指定 `type` 为结构名
- `internalParams` 的 `paramType` 固定为 `"NON_STD_FIELD"`

### 5.2 原子函数 (.uftatomfunction)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<business:Function xmlns:business="http://www.hundsun.com/ares/studio/uft/business/1.0.0" chineseName="AF_模块名_功能描述" objectId="7300XXXX" id="生成的UUID">
  <inputParameters id="market_no" uuid="生成的UUID"/>
  <inputParameters id="report_code" uuid="生成的UUID"/>
  <outputParameters id="inter_code" uuid="生成的UUID"/>
  <outputParameters id="flag0" uuid="生成的UUID"/>
  <internalParams id="tmp_inter_code" name="临时内码" paramType="NON_STD_FIELD" type="HsChar64" uuid="生成的UUID"/>
  <code>
  @flag0 = '0';

  <M>[获取记录][uft_cstockinfo(uft_uniq_stockinfo_reportcode)][
    market_no = @market_no,
    report_code = @report_code
  ][
    inter_code = @inter_code
  ]
  [继续执行]

  [记录不为空][uft_cstockinfo]
  {
    @flag0 = '1';
  }
  [记录为空][uft_cstockinfo]
  {
    [记录日志][CNST_DLOGDEBUG][][未找到证券信息][@market_no, @report_code]
  }
  </code>
</business:Function>
```

**关键说明**：
- 根元素为 `<business:Function>`，不是 `<business:Service>`
- `Function` 根元素也需要 `id` 属性（UUID）
- AF 通常不含 `comm_odefault` 模板参数
- AF 通常不含 `[事务处理开始/结束]`（事务由上级 LS/LF 管理）

### 5.3 逻辑函数 (.uftfunction)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<business:Function xmlns:business="http://www.hundsun.com/ares/studio/uft/business/1.0.0" chineseName="LF_模块名_功能描述" objectId="7300XXXX" id="生成的UUID">
  <inputParameters id="entrust_serial_no" uuid="生成的UUID"/>
  <inputParameters id="entrust_direction" uuid="生成的UUID"/>
  <inputParameters id="entrust_amount" uuid="生成的UUID"/>
  <outputParameters id="error_no" uuid="生成的UUID"/>
  <outputParameters id="error_info" uuid="生成的UUID"/>
  <outputParameters id="error_pathinfo" uuid="生成的UUID"/>
  <outputParameters id="entrust_result" paramType="COMPONENT" type="uft_centrusts" uuid="生成的UUID"/>
  <internalParams id="tmp_entrust_status" name="临时委托状态" paramType="NON_STD_FIELD" type="HsPosInt" uuid="生成的UUID"/>
  <code>
  hs_strncpy(@error_info, "", sizeof(@error_info) - 1);
  hs_strncpy(@error_pathinfo, "", sizeof(@error_pathinfo) - 1);

  [AS_模块名_前置校验][
    entrust_serial_no = @entrust_serial_no
  ][
    error_no = @error_no,
    error_info = @error_info
  ]

  if(@error_no != 0)
  {
    [正常返回]
  }

  [事务处理开始]

  [获取记录-无拷贝][uft_centrusts(uft_uniq_entrusts_entsrlno)][
    entrust_serial_no = @entrust_serial_no
  ][
    entrust_status = @tmp_entrust_status
  ]
  [处理失败]
  {
    [记录日志][CNST_DLOGERROR][][获取委托记录失败][@entrust_serial_no, @error_no, @error_info]
    [正常返回]
  }

  [修改记录][uft_centrusts][
    entrust_status = '6'
  ]
  [处理失败]
  {
    [记录日志][CNST_DLOGERROR][][修改委托状态失败][@entrust_serial_no, @error_no, @error_info]
    [正常返回]
  }

  [事务处理结束]

  <M>[AF_模块名_消息发送][
    entrust_serial_no = @entrust_serial_no
  ]
  [处理失败]
  {
    [记录日志][CNST_DLOGDEBUG][][消息发送失败][@error_no, @error_info]
    [继续执行]
  }
  </code>
</business:Function>
```

**关键说明**：
- LF 包含 `error_no` + `error_info` + `error_pathinfo` 三件套
- LF 通常包含 `[事务处理开始/结束]`，被 LS 调用
- 调用 AS/AF 时注意：事务块内调用的函数不能包含 `[事务处理开始]`
- 代码开头清空 `error_info` 和 `error_pathinfo`

### 5.4 逻辑服务 (.uftservice)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<business:Service xmlns:business="http://www.hundsun.com/ares/studio/uft/business/1.0.0" chineseName="LS_模块名_功能描述" objectId="7300XXXX" useInterFaceFlag="true" id="生成的UUID">
  <inputParameters id="login_company" fromTemplate="true" templateName="comm_odefault" uuid="生成的UUID"/>
  <inputParameters id="login_operator" fromTemplate="true" templateName="comm_odefault" uuid="生成的UUID"/>
  <inputParameters id="login_ip" fromTemplate="true" templateName="comm_odefault" uuid="生成的UUID"/>
  <inputParameters id="mac" fromTemplate="true" templateName="comm_odefault" uuid="生成的UUID"/>
  <inputParameters id="volserial_no" fromTemplate="true" templateName="comm_odefault" uuid="生成的UUID"/>
  <inputParameters id="ws_cpu" fromTemplate="true" templateName="comm_odefault" uuid="生成的UUID"/>
  <inputParameters id="menu_id_op" fromTemplate="true" templateName="comm_odefault" uuid="生成的UUID"/>
  <inputParameters id="device_type" fromTemplate="true" templateName="comm_odefault" uuid="生成的UUID"/>
  <inputParameters id="terminal_info_slit_ext" fromTemplate="true" templateName="comm_odefault" uuid="生成的UUID"/>
  <inputParameters id="entrust_serial_no" uuid="生成的UUID"/>
  <inputParameters id="hsmm_entrustorder" paramType="COMPONENT" type="hsmm_entrustorder" uuid="生成的UUID"/>
  <outputParameters id="error_no" uuid="生成的UUID"/>
  <outputParameters id="error_info" uuid="生成的UUID"/>
  <outputParameters id="error_pathinfo" uuid="生成的UUID"/>
  <outputParameters id="hsmm_entrustdetail" paramType="COMPONENT" type="hsmm_entrustdetail" uuid="生成的UUID"/>
  <internalParams id="starttime" name="开始时间" paramType="NON_STD_FIELD" type="HsPosUInt" uuid="生成的UUID"/>
  <internalParams id="endtime" name="结束时间" paramType="NON_STD_FIELD" type="HsPosUInt" uuid="生成的UUID"/>
  <internalParams id="total_time" name="总耗时" paramType="NON_STD_FIELD" type="HsPosUInt" uuid="生成的UUID"/>
  <code>
  [记录日志][CNST_DLOGEVENT][][LS_模块名_功能描述_开始][@login_company, @login_operator]

  struct timespec starttime, endtime;
  clock_gettime(CLOCK_MONOTONIC, &starttime);
  @starttime = (starttime.tv_sec * 1000000 + starttime.tv_nsec / 1000);

  if(unlikely(@hsmm_entrustorder == NULL))
  {
    <W>[报错返回][ERR_XXXXXXX]
  }

  [AS_系统公共_节点状态检查]
  [AS_权限_操作员合法性验证]

  [LF_模块名_核心业务逻辑][
    entrust_serial_no = @entrust_serial_no
  ][
    error_no = @error_no,
    error_info = @error_info,
    error_pathinfo = @error_pathinfo,
    hsmm_entrustdetail = @hsmm_entrustdetail
  ]

  clock_gettime(CLOCK_MONOTONIC, &endtime);
  @endtime = (endtime.tv_sec * 1000000 + endtime.tv_nsec / 1000);
  @total_time = @endtime - @starttime;

  [记录日志][CNST_DLOGEVENT][][LS_模块名_功能描述_结束, 总计耗时：][@total_time]
  </code>
</business:Service>
```

**关键说明**：
- LS 必须包含 `comm_odefault` 模板参数（`fromTemplate="true"` + `templateName="comm_odefault"`）
- LS 必须包含 `useInterFaceFlag="true"` 属性
- LS 必须包含 `id` 属性（UUID）
- LS 遵循标准流程：日志开始 → 计时 → 参数校验 → 节点状态 → 权限 → 业务逻辑 → 计时结束 → 日志结束
- LS 通常调用 LF，不直接包含 `[事务处理开始/结束]`

---

## 6 基于文档的代码生成流程

> 核心理念：**服务文档 → CRES 代码**，通过解读 design2/ 中已有的 LS/LF/AS/AF 文档中的业务逻辑，结合 CRES 语法规则生成可编译的 `.uft*` 文件。

### 6.1 输入：服务文档结构

每个服务文档（9-10章）包含代码生成所需的关键信息：

| 文档章节 | 对代码生成的作用 |
|---------|----------------|
| Ch1 服务基本信息 | chineseName、objectId、文件类型 |
| Ch2 核心职责 | 确定服务定位和功能边界 |
| Ch3 服务接口 | 输入/输出/内部参数的完整定义 |
| Ch4 业务流程 | **核心**：mermaid 流程图 + 决策点 + 并发/加锁分析 |
| Ch5 关键业务规则 | 字段值常量、分支条件、取值范围 |
| Ch6 下游服务调用 | 子服务/函数的调用序列和参数映射 |
| Ch7 关键数据结构 | 涉及的表、索引、字段定义 |
| Ch8 异常处理 | 错误码、错误信息、处理策略 |
| Ch9 源码位置 | 对应源文件路径（参考对照） |

### 6.2 生成步骤

**步骤1：提取元信息**

从文档 Ch1+Ch3 提取，生成骨架：

```bash
python3 scripts/cres_template.py \
  --type <类型> \
  --name "<chineseName>" \
  --object-id <objectId> \
  --input "<输入参数列表>" \
  --output "<输出参数列表>" \
  --internal "<内部参数列表>" \
  --component-output "<组件输出列表>"
```

**步骤2：解析业务流程**

从文档 Ch4 的 mermaid 流程图和决策点描述，还原为 CRES 伪代码结构：

| mermaid 元素 | CRES 伪代码映射 |
|-------------|----------------|
| 判断节点 (菱形) | `if(condition){...}` / `switch(@var){case ...}` |
| 查询操作 | `<M>[获取记录][表名(索引)][条件][输出]` + `[继续执行]` |
| 写操作 | `[修改记录][表名][字段赋值]` / `[插入记录][表名][字段赋值]` |
| 子服务调用 | `[服务名][输入参数][输出参数]` |
| 循环 | `[遍历记录开始-无拷贝][表名][条件][输出]` ... `[遍历记录结束-无拷贝]` |
| 异步操作 | `<M>[异步服务][参数]` + `[继续执行]` |

**步骤3：应用 CRES 语法规则**

对照 `cres-rules/` 知识库，将步骤2的结构化伪代码转化为合规代码：

1. **事务处理**（`cres-rules/03-mechanisms.md`）：涉及写操作 → 包裹 `[事务处理开始/结束]`，注意铁律1
2. **并发加锁**（`cres-rules/03-mechanisms.md`）：获取记录后立即空加锁，注意铁律3+4
3. **M标记**（`cres-rules/03-mechanisms.md`）：循环内或需要容错 → `<M>` + `[继续执行]`，注意铁律6+9
4. **错误处理**（`cres-rules/03-mechanisms.md`）：每个 DB 操作后跟 `[处理失败]`，注意铁律8
5. **字段赋值**（`cres-rules/01-syntax.md`）：`hs_snprintf` / `hs_strncpy` / 直接赋值
6. **参数引用**：所有 `@变量` 必须在参数声明中有定义，注意铁律7

**步骤4：填充业务规则**

从文档 Ch5 的字段值表（取值/常量名/含义/业务处理）和分支条件，完善伪代码中的：

- `if/switch` 条件中的常量值（如 `DICT_ENTRUSTTYPE_SPOTENTRUST`）
- `[报错返回]` 的错误码（如 `ERR_7300XXXX`）
- 字段赋值的来源和目标

**步骤5：组装并验证**

1. 将步骤1的 XML 骨架中的 `<code>TODO</code>` 替换为步骤2-4生成的完整伪代码
2. 运行 `python3 scripts/cres_validate.py --path <生成文件>` 执行 10 项检查
3. 逐条核对铁律1~10
4. 如有错误，返回步骤3修正

### 6.3 文档到代码的映射示例

**文档描述**：
> Ch4: 根据产品序号、单元序号、组合序号，分别查询产品信息表、资产单元表、组合表，将序号转为代码返回。

**生成代码**：

```xml
<code>
[记录日志][CNST_DLOGDEBUG][][产品单元组合序号:][@fund_id, @asset_id, @combi_id]
<M>[获取记录][uft_cfundinfo(uft_uniq_pk_fundinfo)][fund_id = @fund_id]
[继续执行]
[记录不为空][uft_cfundinfo]
{
  hs_snprintf(@fund_code, sizeof(@fund_code), "%s", @uft_cfundinfo.fund_code);
}

<M>[获取记录][uft_casset(uft_uniq_casset)][asset_id = @asset_id]
[继续执行]
[记录不为空][uft_casset]
{
  hs_snprintf(@asset_code, sizeof(@asset_code), "%s", @uft_casset.asset_code);
}

<M>[获取记录][uft_ccombi(uft_uniq_combi)][combi_id = @combi_id]
[继续执行]
[记录不为空][uft_ccombi]
{
  hs_snprintf(@combi_code, sizeof(@combi_code), "%s", @uft_ccombi.combi_code);
}

[记录日志][CNST_DLOGDEBUG][][产品单元组合代码:][@fund_code, @asset_code, @combi_code]
</code>
```

### 6.4 生成优先级

当信息不完整时，按以下优先级处理：

| 优先级 | 信息来源 | 说明 |
|-------|---------|------|
| P0 | 文档 Ch4 业务流程 + Ch5 业务规则 | 最权威，直接映射为伪代码 |
| P1 | 文档 Ch6 下游调用 + Ch7 数据结构 | 补充调用参数和字段定义 |
| P2 | 文档 Ch8 异常处理 | 补充错误处理块 |
| P3 | `cres-rules/` 知识库 | 填充语法细节和模式 |
| P4 | 同类服务源码参考 | 最后的兜底参考 |

---

## 7 规则知识库引用

生成代码时，根据不确定点查阅对应规则文件：

| 不确定点 | 查阅文件 | 内容 |
|---------|---------|------|
| 伪代码语法不确定 | `cres-rules/01-syntax.md` | 变量/赋值/条件/循环/SQL/函数调用语法 |
| 不确定宏参数签名 | `cres-rules/02-macros.md` | 系统宏+用户宏完整参数与用法 |
| 涉及事务/加锁/M标记 | `cres-rules/03-mechanisms.md` | 事务嵌套、加锁时机、M标记、while保护 |
| 需要代码模式参考 | `cres-rules/04-patterns.md` | 撤单/成交/废单/遍历/导出/指令修改模式 |
| 命名/结构/类型规范 | `cres-rules/05-naming-structure.md` | 文件命名、Object ID、数据类型体系 |
| 数据导出模块 | `cres-rules/06-dep-rules.md` | 导出字段完整性、空值处理、性能约束 |

**查阅命令**：

```bash
# 查询结构字段定义
python3 scripts/structdb.py fields uft_centrusts

# 查询字典值
python3 scripts/structdb.py dict ENTRUSTTYPE

# 查询错误码
python3 scripts/structdb.py errorno 7300

# 搜索已有同类服务作为参考
find src/ -name "as_equitypub_*.uftatomservice" | head -5
```

---

## 7 常见生成错误及修正

### 错误1：忘记定义 internalParams

**现象**：代码中使用了 `@tmp_status` 等变量，但文件头部没有对应的 `<internalParams>` 声明。

**后果**：UFTDB 工具无法识别该变量，编译/运行报错。

**修正**：在 `<code>` 之前添加所有临时变量声明：

```xml
<internalParams id="tmp_status" name="临时状态" paramType="NON_STD_FIELD" type="HsPosInt" uuid="新生成的UUID"/>
```

### 错误2：outputParameters 使用了错误的 xsi:type

**现象**：标准字段输出参数使用了 `xsi:type="business:InternalParam"`，或组件输出参数缺少 `paramType="COMPONENT"`。

**修正**：

```xml
<!-- 标准字段输出（error_no, error_info 等） -->
<outputParameters id="error_no" uuid="..."/>

<!-- 组件输出（结构体） -->
<outputParameters id="uft_centrusts" paramType="COMPONENT" type="uft_centrusts" uuid="..."/>
```

> 注：真实源码中标准字段的 outputParameters **不带** `xsi:type` 属性，仅用 `id` + `uuid` 即可。

### 错误3：Service 和 Function 根元素混淆

**现象**：`.uftatomservice` 文件用了 `<business:Function>`，或 `.uftatomfunction` 文件用了 `<business:Service>`。

**修正**：

| 文件类型 | 根元素 |
|---------|--------|
| `.uftatomservice` / `.uftservice` / `.uftfactorservice` | `<business:Service>` |
| `.uftatomfunction` / `.uftfunction` / `.uftfactorfunction` | `<business:Function>` |

### 错误4：uuid 重复或不规范

**现象**：多个参数使用同一个 uuid，或 uuid 格式不正确。

**修正**：每个 `uuid` 必须是唯一的标准 UUID v4 格式，如 `a38da1a9-819b-4fde-802e-c16e6cd285b4`。可用以下命令生成：

```bash
python3 -c "import uuid; print(uuid.uuid4())"
```

### 错误5：comm_odefault 模板参数遗漏或误用

**现象**：LS 层服务缺少 `comm_odefault` 模板参数，或 AS/AF 层错误添加了模板参数。

**修正**：

| 层级 | comm_odefault | 说明 |
|------|--------------|------|
| LS/RS | 必须包含 | `fromTemplate="true" templateName="comm_odefault"` |
| LF/RF | 不需要 | LF 的入参由调用方传入 |
| AS/AF | 不需要 | AS/AF 只定义业务入参 |

### 错误6：事务回滚冗余

**现象**：在 `[处理失败]` 块中同时写了 `[事务回滚]` 和 `[正常返回]`。

**修正**：报错返回时系统自动回滚，不需要显式 `[事务回滚]`。只在需要主动回滚的场景（如业务校验不通过需撤销已做操作）才使用。

```yaml
# ❌ 错误：错误处理中冗余回滚
[事务处理开始]
  [获取记录-无拷贝][...]
  [处理失败]
  {
    [事务回滚]          # 冗余！
    [正常返回]
  }
[事务处理结束]

# ✅ 正确：报错返回时自动回滚
[事务处理开始]
  [获取记录-无拷贝][...]
  [处理失败]
  {
    [正常返回]          # 自动回滚
  }
[事务处理结束]
```

### 错误7：文件名前缀与扩展名不匹配

**现象**：文件名用 `ls_` 前缀但扩展名是 `.uftatomservice`。

**修正**：

| 前缀 | 对应扩展名 |
|------|-----------|
| `ls_` | `.uftservice` |
| `lf_` | `.uftfunction` |
| `as_` | `.uftatomservice` |
| `af_` | `.uftatomfunction` |
| `rs_` | `.uftfactorservice` |
| `rf_` | `.uftfactorfunction` |

### 错误8：指令表加锁遗漏

**现象**：委托表有 `ins_id > 0`，但只锁了委托表没锁指令表。

**修正**：如果 `ins_id > 0`，必须先锁指令表再锁委托表：

```yaml
[获取记录][uft_centrustrelation.uft_centrusts][...]
if(@uft_centrusts.ins_id > 0)
{
  [获取记录][uft_cinstruction(uft_uniq_tinstruction)][
    company_id = @uft_centrusts.company_id,
    ins_id = @uft_centrusts.ins_id,
    index_daily_modify = @uft_centrusts.index_daily_modify
  ]
  [修改记录][uft_cinstruction][]   // 先锁指令表
}
[修改记录][uft_centrusts][]         // 再锁委托表
```

### 错误9：日志级别使用不当

**现象**：批量处理中单条失败用了 `CNST_DLOGERROR`，或关键操作失败用了 `CNST_DLOGDEBUG`。

**修正**：

| 场景 | 正确级别 |
|------|---------|
| 服务开始/结束/耗时 | `CNST_DLOGEVENT` |
| 关键操作失败（需关注） | `CNST_DLOGERROR` |
| 批量中单条失败（不影响整体） | `CNST_DLOGWARNING` |
| 记录不存在（正常分支） | `CNST_DLOGDEBUG` |

### 错误10：Object ID 范围错误

**现象**：权益业务使用了 710000 范围的 Object ID。

**修正**：

| 域 | Object ID 范围 |
|----|---------------|
| 基础公共 | 710000–719999 |
| 权益业务 | 730000–739999 |
| 衍生品业务 | 740000–749999 |
| 固收业务 | 750000–759999 |
