# CRES/UFT 宏系统完整参考

> 系统内置宏 (SMAC) + 用户自定义宏 (UMAC) + 宏使用模式 (MUP)

---

## 1. 系统内置宏 (SMAC_*)

### SMAC_001 事务处理宏

| 宏 | 签名 | 说明 |
|----|------|------|
| 事务处理开始 | `[事务处理开始]` | 开启事务，必须与 `[事务处理结束]` 配对 |
| 事务处理结束 | `[事务处理结束]` | 提交事务 |
| 事务回滚 | `[事务回滚]` | 主动回滚当前事务 |

**关键约束**：

1. **禁止嵌套**：`[事务处理开始]` 到 `[事务处理结束]` 之间调用的函数，绝对不能包含 `[事务处理开始]`，否则当前事务会被回滚
2. **自动回滚**：若分支判断导致 `[事务处理结束]` 未执行，函数结束时会根据处理结果自动提交或回滚
3. **无需冗余回滚**：业务处理报错时不需要显式 `[事务回滚]`，正常报错返回即可，服务结束时自动回滚
4. **调用链传递**：上级服务开启事务后，下级服务/函数不能再开事务；文档中应标注"⚠️ 本服务可能被上级事务包裹，不能包含[事务处理开始]"

```yaml
# ✅ 正确：标准事务处理
[事务处理开始]
  [获取记录-无拷贝][uft_centrusts][entrust_serial_no = @serial_no][entrust_status = @status]
  [修改记录][uft_centrusts][entrust_status = '6']
[事务处理结束]

# ✅ 正确：只在需要主动回滚时使用
[事务处理开始]
  [获取记录-无拷贝][uft_centrusts][...][...]
  if (@entrust_status == '3') {
    [修改记录][uft_centrusts][entrust_status = '6']
  }
  else {
    [事务回滚]
    [记录日志][CNST_DLOGERROR][][委托状态不允许操作][@entrust_serial_no]
    [正常返回]
  }
[事务处理结束]

# ❌ 错误：事务嵌套（绝对禁止）
[事务处理开始]
  [LF_某逻辑函数][...]   # 该函数内部包含 [事务处理开始] → 回滚！
[事务处理结束]

# ❌ 错误：冗余回滚
[事务处理开始]
  [获取记录-无拷贝][...][...][...]
  [处理失败] {
    [事务回滚]          # 多余！报错返回时系统自动回滚
    [正常返回]
  }
[事务处理结束]
```

### SMAC_002 内存数据操作宏

UFTDB 所有数据操作都在内存中进行，不是直接的数据库交互。

| 宏 | 签名 | 说明 |
|----|------|------|
| 获取记录-无拷贝 | `[获取记录-无拷贝][对象][条件][输出]` | 读取记录，不产生内存拷贝，**优先使用** |
| 插入记录 | `[插入记录][对象][参数]` | 向内存表插入新记录 |
| 修改记录 | `[修改记录][对象][参数]` | 修改记录，**空参数时仅加锁** |
| 删除记录 | `[删除记录][对象]` | 从内存表删除记录 |

**参数说明**：

- **对象**：内存表名，可带索引名如 `uft_centrusts(uft_uniq_entrusts_entsrlno)`
- **条件**：`字段 = @变量` 格式，逗号分隔
- **输出**：`输出字段 = @变量` 格式，逗号分隔
- **参数**：`字段 = 值` 格式，逗号分隔

```yaml
# 获取记录（优先使用无拷贝版本）
[获取记录-无拷贝][uft_centrusts(uft_uniq_entrusts_entsrlno)][
  entrust_serial_no = @entrust_serial_no
][
  entrust_status = @entrust_status,
  entrust_amount = @entrust_amount
]

# 插入记录
[插入记录][uft_centrusts][
  company_id = @company_id,
  entrust_serial_no = @new_serial_no,
  entrust_status = '0'
]

# 修改记录（含参数）
[修改记录][uft_centrusts][
  entrust_status = '6',
  deal_amount = @deal_amount
]

# 修改记录（仅加锁 — 关键并发控制手段）
[修改记录][uft_centrusts][]

# 删除记录
[删除记录][uft_centrusts]
```

### SMAC_003 遍历操作宏

| 宏 | 签名 | 说明 |
|----|------|------|
| 遍历开始 | `[遍历记录开始-无拷贝][对象][条件][输出]` | 开始遍历，无拷贝版本优先 |
| 遍历结束 | `[遍历记录结束-无拷贝]` | 结束遍历 |
| 遍历为空 | `[遍历记录为空]` | 遍历结果为空时执行 |
| 逆序遍历 | `<R>[遍历记录开始-无拷贝][对象][条件][输出]` | `<R>` 前缀表示逆序遍历 |

```yaml
[遍历记录开始-无拷贝][uft_centrusts(uft_idx_company_id)][
  company_id = @company_id
][
  entrust_serial_no = @entrust_serial_no,
  entrust_status = @entrust_status
]
  if (@entrust_status == '0') {
    [修改记录][uft_centrusts][entrust_status = '5']
  }
[遍历记录结束-无拷贝]

[遍历记录为空]
{
  [记录日志][CNST_DLOGDEBUG][][未找到符合条件的委托记录][@company_id]
}

# 逆序遍历（常用于按时间倒序处理）
<R>[遍历记录开始-无拷贝][uft_centrusts][...][...]
  // 处理逻辑
[遍历记录结束-无拷贝]
```

### SMAC_004 结果集操作宏

| 宏 | 签名 | 说明 |
|----|------|------|
| 结果集开始 | `[结果集语句开始][对象名][条件][输出]` | 初始化结果集 |
| 结果集结束 | `[结果集语句结束]` | 关闭结果集 |
| 结果集返回 | `[结果集返回]` | 返回当前结果集记录 |

```yaml
[结果集语句开始][entrust_list][
  company_id = @company_id,
  entrust_status = '0'
][
  entrust_serial_no = @serial_no,
  stock_code = @stock_code,
  entrust_amount = @amount
]
  // 结果集处理逻辑
  [结果集返回]
[结果集语句结束]
```

### SMAC_005 文件操作宏

| 宏 | 签名 | 说明 |
|----|------|------|
| 写文件头 | `[写记录文件头][dirname=目录, filename=文件名][输出字段]` | 写入文件头（列名） |
| 写记录 | `[写记录文件][输出字段]` | 写入一条数据记录 |
| 写文件结束 | `[写记录文件结束]` | 关闭文件 |

```yaml
[写记录文件头][dirname=entrust_export, filename=entrust_data][
  entrust_serial_no = @serial_no,
  stock_code = @stock_code,
  entrust_amount = @amount
]

[遍历记录开始-无拷贝][uft_centrusts][company_id = @company_id][...]
  [写记录文件][
    entrust_serial_no = @serial_no,
    stock_code = @stock_code,
    entrust_amount = @amount
  ]
[遍历记录结束-无拷贝]

[写记录文件结束]
```

---

## 2. 用户自定义宏 (UMAC_*)

### UMAC_001 流程控制宏

| 宏 | 签名 | 说明 |
|----|------|------|
| 正常返回 | `[正常返回]` | 函数正常结束返回 |
| 继续执行 | `[继续执行]` | 跳过当前错误，继续后续逻辑（与 `<M>` 配套） |
| 处理成功 | `[处理成功]` | 标记操作成功，后接成功处理块 |
| 处理失败 | `[处理失败]` | 标记操作失败，后接失败处理块 |

```yaml
# 正常返回：业务处理完成后退出
[事务处理结束]
[记录日志][CNST_DLOGEVENT][][委托处理完成][@entrust_serial_no]
[正常返回]

# 继续执行：与<M>配套，记录不存在时继续后续逻辑
<M>[获取记录][uft_centrustrelation][entrust_serial_no = @serial_no]
[继续执行]
[记录为空][uft_centrustrelation] { /* 插入逻辑 */ }
[记录不为空][uft_centrustrelation] { /* 更新逻辑 */ }

# 处理成功/失败：分支处理
[获取记录-无拷贝][uft_centrusts][...][...]
[处理成功]
{
  [修改记录][uft_centrusts][entrust_status = '6']
}
[处理失败]
{
  [记录日志][CNST_DLOGERROR][][获取委托记录失败][@entrust_serial_no, @error_no, @error_info]
  [正常返回]
}
```

### UMAC_002 记录操作宏

| 宏 | 签名 | 说明 |
|----|------|------|
| 记录为空 | `[记录为空][对象]` | 判断记录是否为空，后接空记录处理块 |
| 记录不为空 | `[记录不为空][对象]` | 判断记录是否非空，后接非空处理块 |
| 记录赋值 | `[记录赋值][目标][源]` | 将源记录内容赋值给目标记录 |

```yaml
# 记录为空/不为空判断（需配合 <M> + [继续执行]）
<M>[获取记录][uft_centrustrelation(uft_uniq_entrustrelation_srlno)][
  entrust_serial_no = @cancelentrust_serial_no
]
[继续执行]
[记录不为空][uft_centrustrelation]
{
  // 记录存在，执行更新
  [修改记录][uft_centrustrelation][status = 'updated']
}
[记录为空][uft_centrustrelation]
{
  // 记录不存在，执行插入
  [插入记录][uft_centrustrelation][entrust_serial_no = @serial_no]
}

# 记录赋值
[记录赋值][@target_record][@source_record]
```

### UMAC_003 时间操作宏

| 宏 | 签名 | 说明 |
|----|------|------|
| 获取时间(毫秒) | `[获取时间(毫秒)][标准字段]` | 获取当前时间（毫秒精度） |
| 获取时间(微秒) | `[获取时间(微秒)][标准字段]` | 获取当前时间（微秒精度） |

```yaml
# 服务入口记录开始时间
[获取时间(微秒)][@starttime]

// ... 业务逻辑 ...

# 服务出口记录结束时间并计算耗时
[获取时间(微秒)][@endtime]
@total_time = @endtime - @starttime
[记录日志][CNST_DLOGEVENT][][服务处理完成, 耗时][@total_time]
```

### UMAC_004 错误处理宏

| 宏 | 签名 | 说明 |
|----|------|------|
| 错误信息获取 | `[错误信息获取]` | 获取最近一次操作的错误信息 |
| 清空循环内错误信息 | `[清空循环内错误信息]` | 清空遍历循环中累积的错误信息 |
| 设置错误路径 | `[设置错误路径]` | 设置错误返回路径 |

```yaml
# 遍历中清空错误信息（防止上一次错误污染）
[遍历记录开始-无拷贝][uft_centrusts][...][...]
  [清空循环内错误信息]
  <M>[AS_某操作][...][...]
  [处理失败] {
    [记录日志][CNST_DLOGWARNING][][单条处理失败][@error_no, @error_info]
    [继续执行]
  }
[遍历记录结束-无拷贝]
```

### UMAC_005 日志记录宏

| 宏 | 签名 | 说明 |
|----|------|------|
| 记录日志 | `[记录日志][级别][错误号][信息][字段]` | 通用日志记录 |
| 记录业务日志 | `[记录业务日志][错误号][信息][参数][remark]` | 业务日志（含错误码和备注） |
| 异步记录分组日志 | `[异步记录分组日志][分组][等级][信息][字段]` | 异步分组日志（高性能场景） |

**日志级别常量**：

| 常量 | 用途 |
|------|------|
| `CNST_DLOGEVENT` | 关键业务事件（服务进出、耗时） |
| `CNST_DLOGERROR` | 错误（操作失败，需关注） |
| `CNST_DLOGWARNING` | 警告（批量处理中单条失败，可忽略） |
| `CNST_DLOGDEBUG` | 调试信息（记录不存在等常规情况） |

```yaml
# 通用日志 — 服务开始/结束
[记录日志][CNST_DLOGEVENT][][LS_权益买卖_委托下达_开始][@company_id, @entrust_serial_no]

# 通用日志 — 错误
[记录日志][CNST_DLOGERROR][][获取委托记录失败][@entrust_serial_no, @error_no, @error_info]

# 通用日志 — 批量中单条失败（用WARNING，不用ERROR）
[记录日志][CNST_DLOGWARNING][][单个记录处理失败，继续处理下一条][@param, @error_no, @error_info]

# 业务日志
[记录业务日志][ERR_1093104004][委托状态不允许撤单][@entrust_serial_no, @entrust_status][撤单校验]

# 异步分组日志
[异步记录分组日志][group_risk_check][CNST_DLOGEVENT][风控检查完成][@check_result]
```

### UMAC_006 系统操作宏

| 宏 | 签名 | 说明 |
|----|------|------|
| 设置系统状态 | `[设置系统状态][状态]` | 设置系统运行状态 |
| 获取序列号 | `[获取序列号][字段][类型]` | 获取指定类型的序列号 |
| 设置序列号 | `[设置序列号][类型][值]` | 设置指定类型的序列号值 |

```yaml
# 获取委托流水号
[获取序列号][@entrust_serial_no][entrust_serial_type]

# 设置序列号
[设置序列号][batch_serial_type][@new_batch_no]
```

### UMAC_007 数据验证宏

| 宏 | 签名 | 说明 |
|----|------|------|
| 判断字符为空 | `[判断字符为空][字段]` | 判断字段值是否为空字符 |
| 判断字符串为空 | `[判断字符串为空][字符串]` | 判断字符串是否为空 |
| 索引冲突 | `[索引冲突]` | 检测索引冲突（插入时唯一键重复） |

```yaml
# 参数非空校验
if (unlikely(@hsmm_entrustorder == NULL)) {
  <W>[报错返回][ERR_1093104004]
}

# 索引冲突检测
[插入记录][uft_centrusts][entrust_serial_no = @serial_no, ...]
[处理失败]
{
  [索引冲突]
  {
    [记录日志][CNST_DLOGWARNING][][委托记录已存在，跳过插入][@serial_no]
    [继续执行]
  }
}
```

### UMAC_008 异步调用宏

| 宏 | 签名 | 说明 |
|----|------|------|
| 异步调用因子 | `[异步调用因子][功能号][组件]` | 异步调用单个组件的因子 |
| 异步调用因子(多参数) | `[异步调用因子(多参数)][功能号][组件1][组件2]` | 异步调用多组件因子 |

```yaml
# 单参数异步调用
[异步调用因子][730001][@risk_check_param]

# 多参数异步调用
[异步调用因子(多参数)][730002][@entrust_param][@position_param]
```

### UMAC_009 M标记宏

`<M>` 标记是 UFT 批量处理容错和记录存在性检查的核心机制。

**签名**：`<M>[操作][参数][输出]`

**两种用法**：

#### 用法一：批量容错

在遍历/批量处理中，`<M>` 将单条记录的错误隔离，不阻塞整个流程。

**必须添加 M 标记的场景**：
- 外部数据获取（调用其他服务/函数）
- 数据验证操作
- 字段转换操作
- 复杂计算操作

**不需要 M 标记的场景**：
- 遍历记录操作
- 权限查询操作
- 基础数据获取（内存表直接读取）

```yaml
[遍历记录开始-无拷贝][uft_centrusts][company_id = @company_id][...]
  # 外部数据获取 — 需要 M 标记
  <M>[AS_证券基础_根据内码获取证券信息][inter_code = @secu_code][secu_info = @secu_info]
  [处理失败]
  {
    [记录日志][CNST_DLOGWARNING][][获取证券信息失败，跳过当前记录][@secu_code, @error_no, @error_info]
    [继续执行]
  }

  # 基础数据获取 — 不需要 M 标记
  [获取记录-无拷贝][uft_cbroker][company_id = @company_id][broker_name = @broker_name]

  # 数据验证 — 需要 M 标记
  <M>[AF_数据导出_有效性验证][...][...]
  [处理失败]
  {
    [记录日志][CNST_DLOGWARNING][][数据验证失败，跳过当前记录][关键参数]
    [继续执行]
  }
[遍历记录结束-无拷贝]
```

#### 用法二：记录存在性检查

当需要判断记录是否存在、根据存在与否执行不同逻辑时，`<M>` + `[继续执行]` 缺一不可。没有 `<M>` 时，记录为空会直接报错返回，后续 `[记录为空]` 分支永远无法执行。

```yaml
# ✅ 正确：<M> + [继续执行] 确保记录为空时能继续
<M>[获取记录][uft_centrustrelation(uft_uniq_entrustrelation_srlno)][
  entrust_serial_no = @cancelentrust_serial_no
]
[继续执行]
[记录不为空][uft_centrustrelation]
{
  // 记录存在 → 更新
  <M>[获取记录][uft_cneeqentrusts(uft_uniq_neeqentrusts)][
    entrust_serial_no = @cancelentrust_serial_no
  ]
  [继续执行]
  [记录不为空][uft_cneeqentrusts]
  {
    [修改记录][uft_cneeqentrusts][entrust_status = @cancel_status]
  }
  [记录为空][uft_cneeqentrusts]
  {
    [记录日志][CNST_DLOGERROR][][委托关系表存在但委托表不存在，数据不一致][@cancelentrust_serial_no]
  }
}
else
{
  // 记录不存在 → 插入
  [AF_权益业务公共_股转委托数据插入][...]
}

# ❌ 错误：没有 <M> 和 [继续执行]
[获取记录][uft_centrustrelation][entrust_serial_no = @serial_no]
# 记录为空时直接报错返回，下面分支永远无法执行
[记录为空][uft_centrustrelation]
{
  // 死代码！
}
```

**关键要点**：
- `<M>` 和 `[继续执行]` **必须配套**，缺一不可
- 嵌套的 `[获取记录]` 也必须各自使用 `<M>` + `[继续执行]`
- 典型场景：检查撤单委托是否已存在（存在则更新，不存在则插入）

---

## 3. 宏使用模式 (MUP_*)

### MUP_001 服务级标准流程

每个 LS 服务应遵循以下标准流程：

```yaml
# 1. 日志记录开始
[记录日志][CNST_DLOGEVENT][][LS_权益买卖_委托下达_开始][@company_id, @entrust_serial_no]

# 2. 时间测量开始
struct timespec starttime, endtime;
clock_gettime(CLOCK_MONOTONIC, &starttime);
@starttime = (starttime.tv_sec * 1000000 + starttime.tv_nsec / 1000);

# 3. 参数验证
if (unlikely(@hsmm_entrustorder == NULL))
{
  <W>[报错返回][ERR_1093104004]
}

# 4. 业务逻辑处理
[事务处理开始]
  [获取记录-无拷贝][uft_centrusts][...][...]
  [修改记录][uft_centrusts][entrust_status = '6']
[事务处理结束]

# 5. 时间测量结束
clock_gettime(CLOCK_MONOTONIC, &endtime);
@endtime = (endtime.tv_sec * 1000000 + endtime.tv_nsec / 1000);
@total_time = @endtime - @starttime;

# 6. 日志记录结束
[记录日志][CNST_DLOGEVENT][][LS_权益买卖_委托下达_结束, 总计耗时：][@total_time]
[正常返回]
```

### MUP_002 错误处理模式

三种错误处理模式，按场景选择：

```yaml
# 模式A：参数验证 — unlikely + <W>报错返回
if (unlikely(@hsmm_entrustorder == NULL))
{
  <W>[报错返回][ERR_1093104004]
}

# 模式B：业务失败 — [处理失败] + 日志 + [正常返回]
[获取记录-无拷贝][uft_centrusts][entrust_serial_no = @serial_no][...]
[处理失败]
{
  [记录日志][CNST_DLOGERROR][][获取委托记录失败][@serial_no, @error_no, @error_info]
  [正常返回]
}

# 模式C：批量失败 — <M> + [处理失败] + [继续执行]
<M>[AS_可能失败的操作][参数][输出]
[处理失败]
{
  [记录日志][CNST_DLOGWARNING][][单个记录处理失败，继续处理下一条][@param, @error_no, @error_info]
  [继续执行]
}
```

**日志级别选择**：

| 场景 | 级别 | 原因 |
|------|------|------|
| 参数为空、关键操作失败 | `CNST_DLOGERROR` | 需要关注和处理 |
| 批量处理中单条失败 | `CNST_DLOGWARNING` | 不影响整体流程 |
| 记录不存在（正常业务分支） | `CNST_DLOGDEBUG` | 非异常情况 |

### MUP_003 内存数据操作模式

```yaml
# 模式A：事务 + 获取 + 修改
[事务处理开始]
  [获取记录-无拷贝][uft_centrusts(uft_uniq_entrusts_entsrlno)][
    entrust_serial_no = @entrust_serial_no
  ][
    entrust_status = @entrust_status
  ]
  [处理失败]
  {
    [记录日志][CNST_DLOGERROR][][获取委托记录失败][@entrust_serial_no, @error_no, @error_info]
    [正常返回]
  }

  [修改记录][uft_centrusts][entrust_status = '6']
  [处理失败]
  {
    [记录日志][CNST_DLOGERROR][][修改委托状态失败][@entrust_serial_no, @error_no, @error_info]
    [正常返回]
  }
[事务处理结束]

# 模式B：遍历 + 条件修改
[遍历记录开始-无拷贝][uft_centrusts(uft_idx_company_id)][
  company_id = @company_id
][
  entrust_serial_no = @serial_no,
  entrust_status = @status
]
  if (@status == '0')
  {
    [修改记录][uft_centrusts][entrust_status = '5']
    [处理失败]
    {
      [记录日志][CNST_DLOGERROR][][修改委托状态失败][@serial_no, @error_no, @error_info]
    }
  }
[遍历记录结束-无拷贝]

[遍历记录为空]
{
  [记录日志][CNST_DLOGDEBUG][][未找到符合条件的委托记录][@company_id]
}
```

### MUP_004 批量查询接口模式

```yaml
# 模式A：遍历 + M标记容错
[遍历记录开始-无拷贝][uft_centrusts][company_id = @company_id][
  entrust_serial_no = @serial_no,
  stock_code = @stock_code
]
  <M>[AS_证券基础_根据内码获取证券信息][
    inter_code = @stock_code
  ][
    secu_info = @secu_info
  ]

  [处理失败]
  {
    [记录日志][CNST_DLOGWARNING][][获取证券信息失败，跳过当前记录][@stock_code, @error_no, @error_info]
    [继续执行]
  }

  [处理成功]
  {
    [记录日志][CNST_DLOGDEBUG][][记录处理成功][@serial_no, @stock_code]
  }
[遍历记录结束-无拷贝]

# 模式B：结果集批量处理
[结果集语句开始][entrust_list][
  company_id = @company_id,
  entrust_status = '0'
][
  entrust_serial_no = @serial_no,
  stock_code = @stock_code
]
  <M>[AS_批量处理操作][
    batch_param = @batch_param
  ][
    process_result = @process_result
  ]

  [处理失败]
  {
    [记录日志][CNST_DLOGWARNING][][批量处理中单个项目失败][@batch_param, @error_no, @error_info]
    [继续执行]
  }

  [处理成功]
  {
    [记录日志][CNST_DLOGDEBUG][][批量处理项目成功][@batch_param, @process_result]
  }

  [结果集返回]
[结果集语句结束]
```

---

## 速查表

### 宏 → 典型场景映射

| 宏 | 典型场景 |
|----|---------|
| `[事务处理开始/结束]` | 涉及写操作（插入/修改/删除）的业务流程 |
| `[获取记录-无拷贝]` | 读取内存表记录（优先于有拷贝版本） |
| `[修改记录][表名][]` | 空参数修改 = **加锁**，防止并发问题 |
| `[遍历记录开始-无拷贝]` | 批量查询、逐条处理 |
| `<M>` + `[继续执行]` | 批量容错 或 记录存在性检查 |
| `[处理失败]` | 任何可能失败的操作后必须添加 |
| `[记录为空]` / `[记录不为空]` | 需配合 `<M>` + `[继续执行]` 使用 |
| `[记录日志]` | 服务进出用 EVENT，业务失败用 ERROR，批量单条失败用 WARNING |
