# 05 命名规范、文件结构与数据类型

> 规则ID：SVC_001~003, NAME_001~003, DTY_001~002

---

## 1. 服务命名规范 (NAME_*)

### NAME_001 服务命名

| 层级 | 格式 | 说明 |
|------|------|------|
| 逻辑服务 | `LS_模块名_功能描述` | 业务入口 |
| 原子服务 | `AS_模块名_功能描述` | 原子操作 |
| 逻辑函数 | `LF_模块名_功能描述` | 逻辑复用 |
| 原子函数 | `AF_模块名_功能描述` | 原子复用 |
| 因子服务 | `RS_模块名_功能描述` | 规则入口 |
| 因子函数 | `RF_模块名_功能描述` | 规则复用 |

模块名示例：权益公共、沪深公共、系统公共、权限、策略公共、证券基础、权益买卖、权益担保、权益清算等。

### NAME_002 参数命名

- **下划线分隔**：`login_company`、`hsmm_entrustorder`
- **组件参数匹配结构名**：`uft_centrusts`、`uft_cinstruction`
- **内部临时变量**：`tmp_status`、`tmp_amount`、`prev_position_str`

### NAME_003 常量命名

| 前缀 | 用途 | 示例 |
|------|------|------|
| `CNST_` | 系统常量 | `CNST_DLOGEVENT`、`CNST_DLOGERROR` |
| `DICT_` | 数据字典常量 | `DICT_ENTRUSTTYPE_SPOTENTRUST` |
| `ERR_` | 错误码 | `ERR_1093104004` |

---

## 2. 文件结构规范 (SVC_*)

### SVC_001 服务定义

XML根元素：`<business:Service>`

```xml
<business:Service
  xmlns:business="http://www.hundsun.com/ares/studio/uft/business/1.0.0"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  chineseName="服务中文名"
  description="服务描述"
  objectId="73001234"
  id="uuid-string">
```

必含属性：`chineseName`、`description`、`objectId`、`id`

### SVC_002 参数定义

| 参数类型 | XML元素 | 关键属性 |
|----------|---------|----------|
| 输入参数 | `<inputParameters>` | `id`, `uuid` |
| 输出参数（标准字段） | `<outputParameters>` | `xsi:type="business:InternalParam"`, `id`, `uuid` |
| 输出参数（组件） | `<outputParameters>` | `paramType="COMPONENT"`, `type="结构名"`, `id`, `uuid` |
| 内部临时变量 | `<internalParams>` | `id`, `name`, `paramType="NON_STD_FIELD"`, `type`, `uuid` |
| 模板参数 | `<inputParameters>` | `fromTemplate="true"`, `templateName="comm_odefault"` |

示例：

```xml
<inputParameters id="hsmm_entrustorder" uuid="..."/>
<outputParameters xsi:type="business:InternalParam" id="error_no" uuid="..."/>
<outputParameters paramType="COMPONENT" type="uft_centrusts" id="hsmm_entrusts" uuid="..."/>
<internalParams id="tmp_status" name="tmp_status" paramType="NON_STD_FIELD" type="HsPosInt" uuid="..."/>
<inputParameters fromTemplate="true" templateName="comm_odefault" id="login_company" uuid="..."/>
```

### SVC_003 文件命名规范

- **模式**：`<前缀>_<业务>_<功能>.<扩展名>`
- **前缀与扩展名对应**：

| 前缀 | 扩展名 | 层级 |
|------|--------|------|
| `ls_` | `.uftservice` | LS |
| `lf_` | `.uftfunction` | LF |
| `as_` | `.uftatomservice` | AS |
| `af_` | `.uftatomfunction` | AF |
| `rs_` | `.uftfactorservice` | RS |
| `rf_` | `.uftfactorfunction` | RF |

- **文件名示例**：`as_equitypub_swapentrustget.uftatomservice`、`lf_secubond_ufrinsmodifyriskdeal.uftfunction`
- **Object ID范围**：

| 域 | 范围 |
|----|------|
| 基础公共 | 710000–719999 |
| 权益业务 | 730000–739999 |
| 衍生品业务 | 740000–749999 |
| 固收业务 | 750000–759999 |

---

## 3. 数据类型 (DTY_*)

### DTY_001 标准数据类型

| 类型 | 说明 | 典型用途 |
|------|------|----------|
| `HsPosUInt` | 无符号整数 | 计数、序号 |
| `HsPosInt` | 有符号整数 | 差值、状态码 |
| `HsSerialNo` | 序列号 | 委托序号、成交序号 |
| `HsAmount` | 数量/份额 | 交易数量、持仓数量 |
| `HsPrice` | 价格 | 委托价格、成交价格 |
| `HsDateTime` | 时间戳 | 记录时间 |
| `HsFlag` | 标志位 | 布尔类型 |
| `HsChar32` | 短字符串 | 描述、备注 |
| `HsChar64` | 中字符串 | 扩展描述 |
| `HsChar128` | 长字符串 | 详细信息 |
| `HsPosString` | 变长字符串 | 动态内容 |

### DTY_002 组件类型

- 声明方式：`paramType="COMPONENT"`，`type` 属性匹配结构名
- 常用结构：`uft_centrusts`、`uft_cinstruction`、`uft_centrustrelation`、`uft_cequnitstock`、`uft_cassetday`
- 字段访问：`@组件名.字段名`

---

## 4. 项目目录结构

```
src/
├── uftbusiness/          # 业务逻辑服务（LS/LF）
│   ├── equitydb/secu/    # 权益-证券
│   ├── equitydb/bond/    # 权益-债券
│   └── businpub/         # 业务公共
├── uftatom/              # 原子服务（AS/AF）
│   └── atom_equity_manage/  # 权益管理原子操作
├── uftfactor/            # 因子服务（RS/RF）
├── uftstructure/         # 结构定义（622个）
└── metadata/             # 元数据
    ├── stdfield          # 标准字段
    ├── datatype          # 数据类型
    ├── dict.dict         # 数据字典
    ├── component.xml     # 组件定义
    └── errorno.errorno   # 错误码
```

**关键元数据文件**：

| 文件 | 用途 |
|------|------|
| `component.xml` | 组件（数据结构）定义与字段 |
| `dict.dict` | 枚举值、常量定义 |
| `errorno.errorno` | 错误码定义 |
| `module.xml` | 模块依赖配置 |
