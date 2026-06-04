# 01 伪代码语法与函数调用规则

> 规则ID：PCS_001~005, FNC_001~003

---

## 1. 伪代码语法规则 (PCS_*)

### PCS_001 基本语法结构

格式：`[功能名称][输入参数列表][输出参数列表]`

- 三个方括号段依次为：功能名、入参、出参
- 空参数用 `[]` 表示
- 多参数用逗号分隔，可换行

**实际示例**（取自 `ls_secubuysell_entrust.uftservice`）：

    [LF_权益买卖_委托下达总控][
    ][
      error_no = @error_no,
      error_info = @error_info,
      error_pathinfo = @error_pathinfo,
      hsmm_entrustdetail = @hsmm_entrustdetail,
      hsmm_entrust_riskdetail_out = @hsmm_entrust_riskdetail_out
    ]

**无参调用**（取自 `ls_ufxcmcequity_entrust.uftservice`）：

    [LF_UFX公共仿CMC_LIC校验]

**空入参+有出参**（取自 `ls_ufxcmcequity_entrust.uftservice`）：

    [LF_UFX仿CMC普通业务_委托下达][][
      error_no = @error_no,
      error_info = @error_info,
      error_pathinfo = @error_pathinfo,
      ufxcmcequity_entrustreturn = @ufxcmcequity_entrustreturn,
      ufxcmcequity_riskinforeturn = @ufxcmcequity_riskinforeturn
    ]

### PCS_002 参数引用规则

- **引用格式**：`@参数名`
- **变量赋值**：`@变量 = 表达式`
- **参数传递**：`参数名 = @参数名`，逗号分隔
- **组件内字段访问**：`@组件名.字段名`

**实际示例**（取自 `ls_secubuysell_entrust.uftservice`）：

    @starttime = (starttime.tv_sec * 1000000 + starttime.tv_nsec / 1000);
    @endtime = (endtime.tv_sec * 1000000 + endtime.tv_nsec / 1000);
    @total_time = @endtime - @starttime;

**组件字段访问**（取自 `ls_derivatereport_withdrawentrustconfirm.uftservice`）：

    switch (@uft_centrustrelation.entrust_table_type)

**字面量赋值**（取自 `rs_secu_crealdeal.uftfactorservice`）：

    busin_class = '1',

### PCS_003 条件判断语法

#### if 单分支

    if (条件表达式) { 执行逻辑 }

**实际示例**（取自 `ls_secubuysell_entrust.uftservice`）：

    if (unlikely(@hsmm_entrustorder == NULL ))
    {
       <W>[报错返回][ERR_1093104004]
    }

#### if-else 双分支

**实际示例**（取自 `ls_derivatereport_withdrawentrustconfirm.uftservice`）：

    if( lpIUFTContext->nErrorNo != OK_SUCCESS )
    {
      [错误信息获取]
      iRaiseError = 0;
      lpIUFTContext->nErrorNo = OK_SUCCESS;
      if( @error_no == ERR_710018 )
      {
        @error_no = 0;
      }
      else
      {
        @error_no = 5309999;
      }
    }
    else
    {
      if( @error_no == ERR_710018 || @error_no == 0 )
      {
        @error_no = 0;
      }
      else
      {
        @error_no = 5309999;
      }
    }

#### switch-case 分支

用于根据 `entrust_table_type` 等字典字段分发到不同委托表。

**实际示例**（取自 `ls_derivatereport_withdrawentrustconfirm.uftservice`）：

    switch (@uft_centrustrelation.entrust_table_type)
    {
      case DICT_ENTRUSTTYPE_OPTIONENTRUST:
        [获取记录][uft_centrustrelation.uft_coptionentrust]
        hs_strncpy((char*)@confirm_codeno,@uft_coptionentrust.confirm_codeno,32);
        break;
      case DICT_ENTRUSTTYPE_FUTUREENTRUST:
        [获取记录][uft_centrustrelation.uft_cfutentrust]
        hs_strncpy((char*)@confirm_codeno,@uft_cfutentrust.confirm_codeno,32);
        break;
      default:
        break;
    }

#### unlikely() 宏

用于标记概率极低的分支（空指针检查），提示编译器优化。

**实际示例**（取自 `ls_secubuysell_entrust.uftservice`）：

    if (unlikely(@hsmm_entrustorder == NULL ))

（取自 `ls_derivatereport_orderconfirm.uftservice`）：

    if(unlikely(lpIUFTContext->nErrorNo != OK_SUCCESS))

### PCS_004 错误处理语法

#### 处理失败块

    [处理失败]
    {
      [记录日志][级别][][描述][参数]
      [正常返回]
    }

**实际示例**（取自 `rs_secu_centrusts.uftfactorservice`）：

    <M>[获取组件][jypub_msgpushtpye][0][push_msg_type = @push_msg_type]
    [处理失败]
    {
      lpIUFTContext->nErrorNo = OK_SUCCESS;
      @push_msg_type = '\0';
    }

#### 报错返回

- `<W>[报错返回][ERR_XXX]`：立即错误返回，中断当前流程
- `[报错返回][ERR_XXX][错误描述]`：带描述的错误返回

**实际示例**（取自 `ls_secubuysell_entrust.uftservice`）：

    <W>[报错返回][ERR_1093104004]

（取自 `ls_ufxequityquery_hsunitstockquery.uftservice`）：

    [报错返回][ERR_730000][公司序号不能为空]
    [报错返回][ERR_730000][操作员序号不能为空]

### PCS_005 日志记录语法

格式：`[记录日志][日志级别][][描述][参数列表]`

日志级别常量：

| 常量 | 用途 |
|------|------|
| `CNST_DLOGEVENT` | 业务事件（服务开始/结束） |
| `CNST_DLOGERROR` | 错误信息 |
| `CNST_DLOGWARNING` | 警告信息 |
| `CNST_DLOGDEBUG` | 调试信息 |

#### 服务开始/结束日志模式

**实际示例**（取自 `ls_secubuysell_entrust.uftservice`）：

    [记录日志][CNST_DLOGEVENT][][LS_权益买卖_委托下达_开始][@login_company,@login_operator]

    // ... 业务逻辑 ...

    [记录日志][CNST_DLOGEVENT][][LS_权益买卖_委托下达_结束,总计耗时：][@total_time]

#### 调试级日志

**实际示例**（取自 `ls_xhkgpub_entcancelrollback.uftservice`）：

    [记录日志][CNST_DLOGDEBUG][][LS_港股通公共_委托撤单可用回滚_开始...]
    [记录日志][CNST_DLOGDEBUG][][LS_港股通公共_委托撤单可用回滚_结束...]

#### 错误级日志

**实际示例**（取自 `ls_derivatereport_withdrawentrustconfirm.uftservice`）：

    [记录日志][CNST_DLOGERROR][][获取到的股东为:][@stockholder_id]

---

## 2. 函数调用规则 (FNC_*)

### FNC_001 原子服务调用

- 带 `<M>` 标记：允许失败后继续（批量容错）
- 不带 `<M>` 标记：失败即中断

**无参原子服务**（取自 `ls_secubuysell_entrust.uftservice`）：

    [AS_系统公共_节点状态验证]
    [AS_权限_操作员合法性验证]

**带M标记的原子服务**（取自 `ls_derivatereport_withdrawentrustconfirm.uftservice`）：

    <M>[LF_衍生品公共_报盘_撤成][
      market_no          = @market_no,
      confirm_codeno     = @confirm_codeno,
      capital_account_no = @capital_account_no,
      stockholder_id     = @stockholder_id,
      cancel_amount      = @cancel_amount,
      bs_direction       = @bs_direction,
      func_id            = @func_id,
      sys_branch_code    = @sys_branch_code
    ][
      error_no           = @error_no,
      error_info         = @error_info,
      error_pathinfo     = @error_pathinfo
    ]

### FNC_002 逻辑函数调用

格式：`[LF_模块名_功能描述][输入参数][输出参数]`

**实际示例**（取自 `ls_secubuysell_entrust.uftservice`）：

    [LF_权益买卖_委托下达总控][
    ][
      error_no = @error_no,
      error_info = @error_info,
      error_pathinfo = @error_pathinfo,
      hsmm_entrustdetail = @hsmm_entrustdetail,
      hsmm_entrust_riskdetail_out = @hsmm_entrust_riskdetail_out
    ]

**组件传参**（取自 `ls_secuquery_bizquery_sesz_asset.uftservice`）：

    [LF_沪深查询_沪深市场业务资产信息查询][
      qypub_bizqueryspotqryin = @qypub_bizqueryspotqryin
    ]

### FNC_003 因子函数调用

格式：`[RF_模块名_功能描述][输入参数][输出参数]`

**实际示例**（取自 `rs_secu_centrusts.uftfactorservice`）：

    [RF_主推消息_现货委托表]

（取自 `rs_secu_crealdeal.uftfactorservice`）：

    [RF_UFX成交消息_消息总控][
      ufxpub_dealmsg_totalctrl = @ufxpub_dealmsg_totalctrl
    ]

---

## 3. 特殊语法

### 3.1 行内注释禁止

UFT伪代码中**禁止行内注释**（`//` 只能独占一行），否则会导致编译错误。

错误：

    [LF_某功能][// 这里写注释会导致编译错误

正确：

    // 这是一行注释
    [LF_某功能]

### 3.2 C混合语法

UFT伪代码中可直接嵌入C语言表达式，常见模式：

| 用法 | 示例 |
|------|------|
| 时间测量 | `struct timespec`, `clock_gettime` |
| 字符串比较 | `hs_strcmp(@a, @b)` |
| 字符串拷贝 | `hs_strncpy(@dst, @src, sizeof(@dst) - 1)` |
| 大小计算 | `sizeof(@var)` |
| 分支预测 | `unlikely(expr)` |
| 上下文错误码 | `lpIUFTContext->nErrorNo` |
| 组件遍历 | `@rowid++` |

**时间测量完整示例**（取自 `ls_secubuysell_entrust.uftservice`）：

```c
struct timespec starttime , endtime ;
clock_gettime(CLOCK_MONOTONIC, &starttime);
@starttime = (starttime.tv_sec * 1000000 + starttime.tv_nsec / 1000);

// 业务逻辑

clock_gettime(CLOCK_MONOTONIC, &endtime);
@endtime = (endtime.tv_sec * 1000000 + endtime.tv_nsec / 1000);
@total_time = @endtime - @starttime;
```

**字符串比较示例**（取自 `ls_derivatereport_withdrawentrustconfirm.uftservice`）：

    if( hs_strcmp(@confirm_codeno,"") == 0 || hs_strcmp(@confirm_codeno," ") == 0 )

**字符串拷贝示例**（取自 `lf_ufxreportmsgdeal_dirivatewthdrwok.uftfunction`）：

    hs_strncpy(@confirm_codeno_tmp, @confirm_codeno, sizeof(@confirm_codeno_tmp) - 1);
    hs_strncpy(@revoke_cause, "O32正报委托撤单，作废单处理。", sizeof(@revoke_cause)-1);

**同步调用+解包示例**（取自 `lf_interbanktrade_pmdealconfirmufrrollback.uftfunction`）：

```c
HsUnPacker lpUnPacker = NULL;
[同步调用][function_id = 419128,service = "ufrdb_ls_a",group = "g",version = "v"][@interbankdealconfirmufrrollback][out_packer = lpUnPacker]

lpUnPacker->SetCurrentDatasetByIndex(0);
@error_no = lpUnPacker->GetInt("error_no");
hs_strncpy(@error_info, lpUnPacker->GetStr("error_info"), sizeof(@error_info));
hs_strncpy(@error_pathinfo, lpUnPacker->GetStr("error_pathinfo"), sizeof(@error_pathinfo));
```

**同步调用多结果集解包模式**（取自 `lf_interbanktrade_ufrpmdealcomfirmcall.uftfunction`）：

```c
HsUnPacker lpUnPacker = NULL;
[同步调用][function_id = 417894,service = "ufrdb_ls_a",group = "g",version = "v",timeout=60000][@interbank_dealconfirm_inparam][out_packer = lpUnPacker]

@rowid = 0;
lpUnPacker->SetCurrentDatasetByIndex(1);
for(; !lpUnPacker->IsEOF(); lpUnPacker->Next())
{
    [手工解包体][@deal_confirm_no,@risk_warning_flag,@risk_serial_no,@error_no,@error_info,@error_pathinfo][lpUnPacker]
    [插入组件][interbank_dealconfirm_detail][@rowid][
      error_no=@error_no,
      error_info=@error_info,
      deal_confirm_no=@deal_confirm_no
    ]
    @rowid ++;
}
```

### 3.3 内部变量赋值

- 赋值：`@var = expression`
- 自增：`@rowid++`
- 条件赋值需在 if 块内

**实际示例**（取自 `rs_secu_centrusts.uftfactorservice`）：

    @rowid = 0;
    [遍历组件开始][qy_msg_centrusts][][...]
    {
      [插入组件][ufxpub_entrustmsg_totalctrl][@rowid][...]
      @rowid++;
    }
    [遍历组件结束]

**清空错误信息**（取自 `lf_ufxequityentrusts_entrustriskdeal.uftfunction`）：

    hs_strncpy(@error_info, "", sizeof(@error_info) - 1);
    hs_strncpy(@error_pathinfo, "", sizeof(@error_pathinfo) - 1);
