---
description: "AI Coding Rules - 数据库设计规范"
globs: *.md,*.sql
alwaysApply: false
version: 1.0.0
author: liangzp35600
created: 2025-9-16
lastUpdated: 2025-9-16
---

# 数据库脚本约束规范

## 数据库类型支持

**必须支持以下4种数据库类型**：
- `oracle` - Oracle数据库
- `oboracle` - OceanBase Oracle兼容模式  
- `mysql` - MySQL数据库
- `obmysql` - OceanBase MySQL兼容模式

## 表命名约束

**强制要求**：
- 表名必须以`cop_t`作为前缀
- 表名必须全部使用小写字母
- 业务词汇直接连接，不使用下划线分隔
- 表名长度不得超过30个字符

**命名示例**：
```sql
-- 正确
CREATE TABLE cop_ttransferinfo
CREATE TABLE cop_taccountcash 
CREATE TABLE cop_tbankinfo

-- 错误
CREATE TABLE COP_TTRANSFERINFO  -- 大写
CREATE TABLE cop_transfer_info  -- 使用下划线
CREATE TABLE transferinfo       -- 缺少前缀
```

## 字段命名约束

**强制要求**：
- 字段名必须全部使用小写字母
- 多个单词之间必须使用下划线分隔
- 主键字段优先使用`serial_no`（自增序号）
- ID类字段以`_id`结尾
- 编号类字段以`_no`结尾  
- 时间类字段使用`_time`或`_date`后缀
- 金额类字段以`_amount`、`_balance`结尾
- 标志类字段以`_flag`、`_status`结尾

**命名示例**：
```sql
-- 正确
serial_no           -- 主键序号
fund_id             -- 基金ID  
bank_account_no     -- 银行账号
query_time          -- 查询时间
transfer_amount     -- 转账金额
query_status        -- 查询状态

-- 错误
SerialNo            -- 大写
fundId              -- 驼峰命名
transferamount      -- 缺少下划线
```

## 数据类型约束

### Oracle/OceanBase Oracle模式

**使用的数据类型**：
- `NUMBER(p,s)` - 数值类型，常见规格：`NUMBER(10,0)`、`NUMBER(10)`、`NUMBER(18,2)`、`NUMBER(20,2)`、`NUMBER(20,4)`
- `VARCHAR2(n)` - 变长字符串，常见长度：32、128、256、1024等
- `CHAR(n)` - 定长字符串，标志字段使用`CHAR(1)`

### MySQL/OceanBase MySQL模式

**使用的数据类型**：
- `INT` - 整数类型，用于时间戳等字段
- `DECIMAL(p,s)` - 精确数值，常见规格：`DECIMAL(10)`、`DECIMAL(20,2)`
- `VARCHAR(n)` - 变长字符串，常见长度：100、200、500等
- `CHAR(n)` - 定长字符串，标志字段使用`CHAR(1)`  
- `TEXT` - 长文本字段

## 主键约束规范

**强制要求**：
- 单字段主键优先使用`serial_no`
- 复合主键按重要性排序字段
- 主键命名长度限制在30个字符（字节）以内

**主键约束命名规则**：
- **Oracle/OceanBase Oracle**：使用`pk_ + 表名去除cop_t前缀`（全小写）
- **MySQL/OceanBase MySQL**：使用`PK_ + 表名去除COP_T前缀`（全大写）

**主键约束示例**：
```sql
-- Oracle/OceanBase Oracle
ALTER TABLE cop_toprolerights ADD CONSTRAINT pk_oprolerights PRIMARY KEY(role_id,operator_no);
ALTER TABLE cop_ttransferinfo ADD CONSTRAINT pk_transferinfo PRIMARY KEY(serial_no);

-- MySQL/OceanBase MySQL
ALTER TABLE cop_toprolerights ADD CONSTRAINT PK_TOPROLERIGHTS PRIMARY KEY(role_id,operator_no);
ALTER TABLE cop_ttransferinfo ADD CONSTRAINT PK_TTRANSFERINFO PRIMARY KEY(serial_no);
```

**语法差异**：
- **Oracle**：使用单独的`ALTER TABLE ... ADD CONSTRAINT ... PRIMARY KEY(...)`
- **OceanBase Oracle**：在CREATE TABLE中定义`CONSTRAINT ... PRIMARY KEY(...)`
- **MySQL/OceanBase MySQL**：使用`CONSTRAINT ... PRIMARY KEY(...)`

## 索引命名约束

### 普通索引命名规则

**强制要求**：
- 索引名称必须全部使用大写字母
- **统一使用`IDX_表名简称`或`IDX_字段名`格式**
- 唯一索引使用`UK_表名简称`格式
- 索引命名长度限制在30个字符（字节）以内

**普通索引示例**：
```sql
-- 标准索引格式（推荐使用）
CREATE INDEX IDX_SETTLEINSBOND ON COP_TSETTLEINSBOND(clear_agent_code_cn,shclearing_trade_ins_id);
CREATE INDEX IDX_TRANSFERFLOW_INSID ON COP_TTRANSFERFLOW(TRANSFER_INS_ID, TRANSFER_INS_MODIFY);
CREATE INDEX IDX_RIVAL_CODE ON cop_ttraderival(rival_code);

-- 唯一索引  
CREATE UNIQUE INDEX UK_TRANSFERADJUNCLIST ON cop_ttransferadjunclist(uuid);
CREATE UNIQUE INDEX UK_AGENCYINFO ON cop_tagencyinfo(agency_code);
```

### 主键索引说明

**注意事项**：
- 主键索引由数据库自动创建，不需要手动创建INDEX
- 主键约束名称规则见"主键约束规范"章节
- 禁止手动创建主键相关的索引

**历史格式说明**：
现有脚本中存在多种历史格式（如INDEX_COP_、COP_INDEX_等），但新增索引必须统一使用IDX_前缀。

## 通用脚本约束

**强制要求**：
- 脚本必须保证幂等性（可重复执行不出错）
- 所有操作必须先检查对象是否存在
- 避免重复插入/更新数据
- 避免直接删除表或字段，优先使用状态标识
- 批量操作需考虑性能影响
- 脚本必须以`commit;`结尾
- 关键操作必须有清晰的注释说明

## 脚本结构约束

**Oracle/OceanBase Oracle格式**：
```sql
prompt begin [操作描述]
declare
  iCount number := 0;
begin
  select count(*) into iCount from [检查条件];
  if iCount = 0 then
    execute immediate '[SQL操作语句]';
  end if;
end;
/
prompt end
```

**MySQL/OceanBase MySQL格式**：
```sql
SELECT '[操作描述]';
delimiter $$
drop procedure IF EXISTS executUpdateSql $$
create procedure executUpdateSql()
begin
  declare iCount int;
  select count(*) into iCount from [检查条件];
  if iCount = 0 then
    [SQL操作语句];
  end if;
end $$
call executUpdateSql() $$
drop procedure IF EXISTS executUpdateSql $$
delimiter ;
```

## 脚本生成位置约束

**版本目录结构**：
```
cop-server/deploy/sqls/[数据库类型]/
├── dbsqls/                    # 主要数据库脚本目录
│   └── [版本号]/                  # 版本目录，如COP2.0V202505.00.000
│       ├── [版本号].sql           # 主要升级脚本
│       ├── version.sql            # 版本信息记录脚本
│       ├── personalize.sql.vm     # 客户个性化脚本
│       ├── backup/                # 备份脚本目录
│       └── rollback/              # 回滚脚本目录
└── bizframe/                  # 权限相关脚本目录
    └── [版本号]/                  # 对应版本目录
        ├── cop-right.sql.vm       # COP用户权限脚本
        └── cop-menu.sql.vm        # COP菜单权限脚本
```

**脚本放置规则**：
- **主要脚本**：放置在`dbsqls/[版本号]/[版本号].sql`（如：dbsqls/COP2.0V202505.00.000/COP2.0V202505.00.000.sql）
- **个性化脚本**：`personalize.sql.vm`包含客户特定配置，使用Velocity模板语法
- **权限脚本**：放置在`bizframe/[版本号]/`目录下
  - `cop-right.sql.vm`：用户权限配置
  - `cop-menu.sql.vm`：菜单权限配置

**系统自动生成文件（禁止修改）**：
- **版本脚本**：`version.sql`由程序自动生成，记录版本信息，仅供参考
- **备份脚本**：`backup/`目录下的备份脚本由系统自动生成
- **回滚脚本**：`rollback/`目录下的回滚脚本由系统自动生成

## 字段注释约束

**强制要求**：
- 每个新增字段必须添加中文注释
- 注释内容仅包含字段的字面含义
- 禁止在注释中添加额外说明或示例

**注释示例**：
```sql
-- 正确
COMMENT ON COLUMN cop_tfundinfo.fund_account IS '基金账号'
COMMENT ON COLUMN cop_ttransferinfo.transfer_amount IS '转账金额'

-- 错误  
COMMENT ON COLUMN cop_tfundinfo.fund_account IS '基金账号，用于标识基金在银行的账户信息'
```

## 禁止事项

**严格禁止**：
- 表名和字段名包含数据库关键字
- 在生产脚本中使用DROP TABLE语句
- 创建外键约束
- 使用触发器、存储过程（脚本执行除外）
- 直接修改现有字段类型和长度
- 删除现有字段和约束
- 使用中文字符作为表名或字段名
- 脚本不以commit结尾
- 跳过对象存在性检查
- 重复执行导致数据错误
- 修改或生成version.sql版本脚本
- 修改或新增backup备份脚本
- 修改或新增rollback回滚脚本

## 数据类型对应关系

**Oracle ↔ MySQL 类型映射**：
- `NUMBER(10,0)` ↔ `INT`
- `NUMBER(18,2)` ↔ `DECIMAL(20,2)`
- `NUMBER(20,2)` ↔ `DECIMAL(20,2)`
- `NUMBER(20,4)` ↔ `DECIMAL(20,4)`
- `VARCHAR2(n)` ↔ `VARCHAR(n)`
- `CHAR(1)` ↔ `CHAR(1)`
- 大文本字段 ↔ `TEXT`