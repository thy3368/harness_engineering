# 04 典型代码模式

本文档归纳 CRES/UFT 代码中反复出现的业务流程模式，每种模式给出名称、描述和代码模板。核心机制规则（事务嵌套禁止、加锁时机、M标记用法、while(true)保护等）详见 [03-mechanisms.md](03-mechanisms.md)，此处不再重复。

---

## 1 服务级标准流程

**描述**：每个 LS 层服务的固定骨架——日志开始 → 计时开始 → 参数校验 → 节点状态 → 权限检查 → 业务逻辑 → 计时结束 → 日志结束。

```yaml
[记录日志][CNST_DLOGEVENT][][LS_模块_功能_开始][@key_param1, @key_param2]

struct timespec starttime, endtime;
clock_gettime(CLOCK_MONOTONIC, &starttime);
@starttime = (starttime.tv_sec * 1000000 + starttime.tv_nsec / 1000);

if (unlikely(@hsmm_entrustorder == NULL))
{
  <W>[报错返回][ERR_XXXXXXX]
}

[AS_系统公共_节点状态检查][...]
[AS_系统公共_权限校验][...]

// ... 业务逻辑 ...

clock_gettime(CLOCK_MONOTONIC, &endtime);
@endtime = (endtime.tv_sec * 1000000 + endtime.tv_nsec / 1000);
@total_time = @endtime - @starttime;

[记录日志][CNST_DLOGEVENT][][LS_模块_功能_结束, 总计耗时：][@total_time]
```

---

## 2 事务处理模式

### 2.1 简单事务

```yaml
[事务处理开始]
[获取记录-无拷贝][对象][条件][输出]
[修改记录][对象][参数]
[事务处理结束]
```

### 2.2 带错误处理的事务

每个关键操作后跟 `[处理失败]` 块，报错返回时自动回滚（无需显式 `[事务回滚]`）。

```yaml
[事务处理开始]
[获取记录-无拷贝][对象][条件][输出]
[处理失败]
{
  [记录日志][CNST_DLOGERROR][][获取记录失败][@key_param]
  [正常返回]
}

[修改记录][对象][参数]
[处理失败]
{
  [记录日志][CNST_DLOGERROR][][修改记录失败][@key_param]
  [正常返回]
}
[事务处理结束]
```

### 2.3 多表事务（防死锁顺序）

涉及指令表+委托表时，必须按统一顺序加锁：指令表 → 委托表 → 委托关系表。

```yaml
[事务处理开始]

// 1. 获取委托关系表
[获取记录][uft_centrustrelation(uft_uniq_entrustrelation_srlno)][
  entrust_serial_no = @entrust_serial_no
][
  entrust_table_type = @entrust_table_type
]

// 2. 如有指令，先锁指令表
switch (@entrust_table_type)
{
  case DICT_ENTRUSTTYPE_SPOTENTRUST:
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
    break;
}

// 3. 业务处理...

[事务处理结束]
```

---

## 3 遍历处理模式

### 3.1 基本遍历

```yaml
[遍历记录开始-无拷贝][对象][条件][输出]
  if (条件)
  {
    [修改记录][对象][参数]
  }
[遍历记录结束-无拷贝]
```

### 3.2 带空记录检查

```yaml
[遍历记录开始-无拷贝][对象][条件][输出]
  // 处理逻辑
[遍历记录结束-无拷贝]

[遍历记录为空]
{
  [记录日志][CNST_DLOGDEBUG][][未找到记录][@key_param]
}
```

### 3.3 带批量容错

遍历体中用 `<M>` 包装可能失败的操作，单条失败不阻塞整体。

```yaml
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

---

## 4 撤单处理模式

**核心流程**：获取委托关系表 → 获取+锁定委托表 → 状态校验 → 业务处理。

**关键约束**：获取记录后必须立即加锁（`[修改记录][表名][]`），在业务判断之前。

```yaml
// 1. 获取委托关系表
[AF_交易公共_原委托对应关系表获取][
  report_serial_no = @report_serial_no,
  market_no = @market_no
][
  uft_centrustrelation = @uft_centrustrelation
]
@entrust_table_type = @uft_centrustrelation.entrust_table_type;
@entrust_serial_no = @uft_centrustrelation.entrust_serial_no;

// 2. 获取+锁定委托表（立即加锁！）
[获取记录][uft_centrustrelation(uft_uniq_entrustrelation_srlno)][
  entrust_serial_no = @entrust_serial_no
]
switch (@entrust_table_type)
{
  case DICT_ENTRUSTTYPE_SPOTENTRUST:
    [获取记录][uft_centrustrelation.uft_centrusts][...]
    [修改记录][uft_centrusts][]   // 立即加锁
    break;
  case DICT_ENTRUSTTYPE_NEEQENTRUST:
    [获取记录][uft_centrustrelation.uft_cneeqentrusts][...]
    [修改记录][uft_cneeqentrusts][]   // 立即加锁
    break;
}

// 3. 状态校验
if(@entrust_status == CNST_ENTSTATUS_YICHE
  || @entrust_status == CNST_ENTSTATUS_FEIDAN
  || @entrust_status == CNST_ENTSTATUS_YICHENG)
{
  [记录日志][CNST_DLOGERROR][ERR_710018][委托状态不允许撤单][@entrust_status]
  [报错返回][ERR_710018]
}

// 4. 业务处理：更新委托状态为正撤/已撤
[修改记录][uft_centrusts][
  entrust_status = @cancel_status,
  revoke_cause = @revoke_cause
]
```

---

## 5 成交处理模式

**核心流程**：获取委托关系表 → 锁定指令表（如有） → 锁定委托表 → 更新成交数量。

**关键约束**：指令表必须在委托表之前锁定。

```yaml
// 1. 获取委托关系表
[AF_交易公共_原委托对应关系表获取][...][
  uft_centrustrelation = @uft_centrustrelation
]
@entrust_table_type = @uft_centrustrelation.entrust_table_type;

// 2. 锁定指令表（必须在委托表之前）
[AF_报盘回报_指令锁][
  uft_centrustrelation = @uft_centrustrelation,
  entrust_table_type = @entrust_table_type
]

// 3. 锁定委托表
switch (@entrust_table_type)
{
  case DICT_ENTRUSTTYPE_SPOTENTRUST:
    [获取记录][uft_centrustrelation.uft_centrusts][...]
    [修改记录][uft_centrusts][]   // 加锁
    break;
}

// 4. 业务处理：更新成交数量、委托状态
@total_deal_amount = @uft_centrusts.total_deal_amount + @deal_amount;
@total_deal_balance = @uft_centrusts.total_deal_balance + @deal_balance;
[修改记录][uft_centrusts][
  total_deal_amount = @total_deal_amount,
  total_deal_balance = @total_deal_balance,
  entrust_status = @deal_status
]
```

---

## 6 废单处理模式

与撤单模式结构类似，核心区别在于状态转换：委托状态改为"废单"而非"已撤"。

```yaml
// 1. 获取委托关系表
[AF_交易公共_原委托对应关系表获取][...][
  uft_centrustrelation = @uft_centrustrelation
]

// 2. 指令锁 + 委托表锁（与成交一致，先指令后委托）
[AF_报盘回报_指令锁][
  uft_centrustrelation = @uft_centrustrelation,
  entrust_table_type = @entrust_table_type
]

// 3. 获取+锁定委托表
switch (@entrust_table_type)
{
  case DICT_ENTRUSTTYPE_SPOTENTRUST:
    [获取记录][uft_centrustrelation.uft_centrusts][...]
    // 重复废单判断
    if(@uft_centrusts.entrust_status == CNST_ENTSTATUS_FEIDAN)
    {
      [修改记录][uft_centrusts][revoke_cause = @revoke_cause]
      [正常返回]
    }
    break;
}

// 4. 业务处理：状态改为废单，释放可用
[修改记录][uft_centrusts][
  entrust_status = CNST_ENTSTATUS_FEIDAN,
  revoke_cause = @revoke_cause
]
```

---

## 7 指令修改模式

**描述**：修改指令参数（数量/价格/方向）的标准流程。典型调用链：UFT入参准备 → 指令修改数据插入。

```yaml
// 1. 获取指令记录
[获取记录][uft_cinstruction(uft_uniq_tinstruction)][
  company_id = @company_id,
  ins_id = @ins_id,
  index_daily_modify = @index_daily_modify
][
  ins_target_amount = @ins_target_amount,
  ins_target_balance = @ins_target_balance,
  total_deal_amount = @total_deal_amount,
  total_deal_balance = @total_deal_balance
]

// 2. 入参准备（计算修改后的指令数量/金额）
[AS_沪深公共_现货指令修改UFT入参准备][
  ins_target_type = @ins_target_type,
  ins_target_amount = @ins_target_amount,
  ins_target_balance = @ins_target_balance,
  entrust_direction = @entrust_direction,
  market_no = @market_no,
  total_deal_amount = @total_deal_amount,
  total_deal_balance = @total_deal_balance,
  index_daily_modify = @index_daily_modify,
  ins_price = @ins_price
][
  limit_ins_ratio = @limit_ins_ratio,
  ins_amount = @ins_amount,
  ins_balance = @ins_balance
]

// 3. 指令修改数据插入（含原指令状态更新）
[AS_沪深公共_指令修改数据插入][
  ins_id = @ins_id,
  ins_amount = @ins_amount,
  ins_balance = @ins_balance,
  ins_price = @ins_price,
  company_id = @company_id,
  index_daily_modify = @index_daily_modify
]

// 4. 如修改失败，回滚可用
[处理失败]
{
  [AS_沪深公共_现货指令修改回滚可用][...]
  [记录日志][CNST_DLOGERROR][][指令修改失败][@ins_id, @error_no, @error_info]
  [正常返回]
}
```

---

## 8 数据导出异常保护模式

**描述**：数据导出模块中 `<E>[遍历记录开始]` 配合 `<M>` 的标准保护结构。仅对可能失败的操作添加 `<M>`，不保护遍历本身和基础操作。

```yaml
<E>[遍历记录开始][数据表名][条件][输出字段列表]
{
    // 外部数据获取 → 需要 M 标记
    <M>[AF_证券基础_根据内码获取证券信息][内码 = @secu_code][证券信息 = @secu_info]
    [处理失败]
    {
        [记录日志][CNST_DLOGERROR][][获取证券信息失败，跳过当前记录][@secu_code, @error_no, @error_info]
        [继续执行]
        continue;
    }

    // 基础数据获取 → 不需要 M 标记
    [获取记录][uft_cbroker(...)][...]

    // 数据验证 → 需要 M 标记
    <M>[AF_数据导出_有效性验证][...][...]
    [处理失败]
    {
        [记录日志][CNST_DLOGERROR][][数据验证失败，跳过当前记录][关键参数]
        [继续执行]
        continue;
    }

    // 字段转换 → 需要 M 标记
    <M>[AF_数据导出_字段转换][...][...]
    [处理失败]
    {
        [记录日志][CNST_DLOGERROR][][字段转换失败，跳过当前记录][关键参数]
        [继续执行]
        continue;
    }
}
[遍历记录结束]
```

---

## 9 记录存在性检查模式（M标记第二种用法）

**描述**：需要根据记录是否存在执行不同逻辑（存在→更新，不存在→插入），必须使用 `<M>[获取记录]` + `[继续执行]`，否则记录为空时直接报错返回。

```yaml
// 检查撤单委托是否已存在
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
[记录为空][uft_centrustrelation]
{
  // 记录不存在 → 插入
  [AF_权益业务公共_股转委托数据插入][...]
}
```

**要点**：
- `<M>` 和 `[继续执行]` 必须配套使用，缺一不可
- 嵌套的 `[获取记录]` 也必须各自使用 `<M>` + `[继续执行]`

---

## 10 同步调用模式（while(true)循环）

**描述**：分页查询前置机接口的标准循环模式，9种保护机制详见 [03-mechanisms.md §4](03-mechanisms.md)。

```yaml
@max_loop_count = 1000;
@loop_count = 0;
@row_count = 0;

while(true)
{
    @loop_count++;

    // 保护7：最大循环次数
    if(@loop_count > @max_loop_count) { break; }

    // 保护1：总条数足够
    if(@row_count >= @request_num) { break; }

    // 保存定位串
    hs_strncpy(@prev_position_str, @position_str, sizeof(@prev_position_str) - 1);

    // 同步调用
    [同步调用][...][][out_packer = lpUnPacker]
    [处理失败] { [报错返回][ERR_XXX] }

    // 保护8：解包器为空
    if(lpUnPacker == NULL) { break; }

    // 保护5：error_no检查
    if(lpUnPacker->FindColIndex("error_no") >= 0)
    {
        @error_no = lpUnPacker->GetInt("error_no");
        if(@error_no == -60) { break; }
        else if(@error_no != 0) { [报错返回][ERR_XXX] }
    }

    // 保护3：立即EOF
    if(lpUnPacker->IsEOF()) { break; }

    // 遍历返回结果
    @current_batch_count = 0;
    while(!lpUnPacker->IsEOF())
    {
        // 保护8：字段检查
        if(lpUnPacker->FindColIndex("field_name") < 0) { continue; }

        // 业务处理...
        @current_batch_count++;
        @row_count++;
        lpUnPacker->Next();
    }

    // 保护2：本次返回条数 < request_num
    if(@current_batch_count < @request_num) { break; }

    // 保护4：定位串比较（最关键）
    if(hs_strcmp(@position_str, "0") != 0 && length(trim(@position_str)) > 0)
    {
        if(hs_strcmp(@position_str, @prev_position_str) == 0) { break; }
    }
}
```

---

## 11 消息发送模式

### 11.1 委托消息发送（报盘）

委托下达后向交易所发送委托消息。

```yaml
// 1. 消息打包
[AF_权益消息_委托消息打包][
  entrust_serial_no = @entrust_serial_no,
  report_code = @report_code,
  entrust_direction = @entrust_direction,
  entrust_price = @entrust_price,
  entrust_amount = @entrust_amount
]

// 2. 发送到交易所
[AF_权益消息_委托消息发送]
```

### 11.2 客户端通知消息

数据变更后通知客户端更新缓存，各表消息独立发送，均用 `<M>` 保护。

```yaml
<M>[AF_权益消息_客户端缓存_委托表消息发送]
[处理失败]
{
  [记录日志][CNST_DLOGDEBUG][][委托表客户端消息发送失败][@error_no, @error_info]
  [继续执行]
}

<M>[AF_权益消息_客户端缓存_组合持仓表消息发送]
[处理失败]
{
  [记录日志][CNST_DLOGDEBUG][][组合持仓表客户端消息发送失败][@error_no, @error_info]
  [继续执行]
}
```

### 11.3 策略消息

策略委托下达后，更新策略表并发送消息给策略端。

```yaml
// 1. 计算委托金额
if(@entrust_direction == 5 || @entrust_direction == 6)
{
  @entrust_balance = @entrust_amount * 100;
}
else
{
  @entrust_balance = @entrust_amount * @entrust_price;
}

// 2. 组装消息组件
[插入组件][qy_msg_calgoentrust][0][
  entrust_serial_no = @entrust_serial_no,
  entrust_direction = @entrust_direction,
  entrust_price = @entrust_price,
  entrust_amount = @entrust_amount,
  report_code = @report_code,
  market_no = @market_no,
  combi_id = @combi_id
]

// 3. 发送策略消息
[AF_权益消息_策略主推_委托下达消息发送]
```
