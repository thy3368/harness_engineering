---
description: "AI Coding Rules - 数据库设计规范"
globs: "*.md,*.sql"
alwaysApply: false
version: 1.0.1
author: 架构办
created: 2025-11-3
lastUpdated: 2025-11-3
---

# 数据库设计规范

## 概述

本规范为项目级数据库设计标准规范，参考数据库设计方法论（ER模型、三范式、领域驱动设计），规定了表命名、字段设计、约束规范、索引设计等方面的要求。

详见 [数据库设计示例](./db-design-example.md)

## 设计原则

### 核心原则

| 原则 | 说明 | 来源 |
|------|------|------|
| **规范化** | 遵循数据库范式，减少数据冗余 | 第三范式 (3NF) |
| **命名清晰** | 表名和字段名清晰表达业务含义 | 通用原则 |
| **主键策略** | 统一主键生成策略 | 领域驱动设计 |
| **可扩展性** | 预留扩展字段，适应业务变化 | 开放封闭原则 |
| **多数据库兼容** | 兼容不同数据库类型 | 实际项目需求 |

### 设计方法论

| 方法论 | 说明 | 应用 |
|--------|------|------|
| **ER 模型** | 实体-关系建模 | 概念设计阶段 |
| **三范式** | 消除冗余、依赖传递 | 逻辑设计阶段 |
| **反规范化** | 适度冗余提升性能 | 物理设计阶段 |
| **DDD** | 领域驱动设计 | 表与实体映射 |

详见 [数据库设计示例 - 设计原则](./db-design-example.md)

## 表命名规范

### 命名规则

| 规则 | 要求 | 示例 |
|------|------|------|
| **前缀** | 使用业务前缀 | `cop_t` 表示业务表 |
| **大小写** | 全部小写 | `cop_ttransferinfo` |
| **分隔符** | 不使用下划线 | `cop_taccountcash` |
| **长度** | 不超过 30 字符 | - |

### 命名示例

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

详见 [数据库设计示例 - 表命名约束](./db-design-example.md#表命名约束)

## 字段设计规范

### 字段命名规则

| 规则 | 要求 | 示例 |
|------|------|------|
| **大小写** | 全部小写 | `serial_no` |
| **分隔符** | 使用下划线 | `bank_account_no` |
| **主键** | 优先使用 `serial_no` | 自增序号 |
| **ID 类** | 以 `_id` 结尾 | `fund_id` |
| **编号类** | 以 `_no` 结尾 | `bank_account_no` |
| **时间类** | 使用 `_time` 或 `_date` | `query_time` |
| **金额类** | 以 `_amount` 或 `_balance` | `transfer_amount` |
| **标志类** | 以 `_flag` 或 `_status` | `query_status` |

### 数据类型选择

| 场景 | Oracle/OceanBase | MySQL/OceanBase |
|------|------------------|-----------------|
| 整数 | `NUMBER(10,0)` | `INT` |
| 金额 | `NUMBER(18,2)` | `DECIMAL(20,2)` |
| 大金额 | `NUMBER(20,2)` | `DECIMAL(20,2)` |
| 精度数 | `NUMBER(20,4)` | `DECIMAL(20,4)` |
| 短字符串 | `VARCHAR2(32)` | `VARCHAR(32)` |
| 中字符串 | `VARCHAR2(256)` | `VARCHAR(256)` |
| 长字符串 | `VARCHAR2(1024)` | `VARCHAR(1024)` |
| 标志位 | `CHAR(1)` | `CHAR(1)` |
| 长文本 | `CLOB` | `TEXT` |

### 数据类型映射

详见 [数据库设计示例 - 数据类型对应关系](./db-design-example.md#数据类型对应关系)

## 主键约束规范

### 主键策略

| 规则 | 要求 |
|------|------|
| **单字段主键** | 优先使用 `serial_no`（自增序号） |
| **复合主键** | 按重要性排序 |
| **主键命名** | 长度限制 30 字符 |

### 主键约束命名

| 数据库类型 | 命名规则 | 示例 |
|-----------|----------|------|
| Oracle/OceanBase | `pk_ + 表名去掉前缀`（全小写） | `pk_transferinfo` |
| MySQL/OceanBase | `PK_ + 表名去掉前缀`（全大写） | `PK_TTRANSFERINFO` |

### 语法差异

| 数据库 | 语法 |
|--------|------|
| Oracle | 单独 `ALTER TABLE ... ADD CONSTRAINT ... PRIMARY KEY(...)` |
| OceanBase Oracle | 在 CREATE TABLE 中定义 |
| MySQL/OceanBase MySQL | 使用 `CONSTRAINT ... PRIMARY KEY(...)` |

详见 [数据库设计示例 - 主键约束规范](./db-design-example.md#主键约束规范)

## 索引设计规范

### 索引命名规则

| 类型 | 命名规则 | 示例 |
|------|----------|------|
| **普通索引** | `IDX_表名简称` 或 `IDX_字段名` | `IDX_TRANSFERFLOW` |
| **唯一索引** | `UK_表名简称` | `UK_TRANSFERADJUNCLIST` |
| **复合索引** | `IDX_表名简称` | `IDX_SETTLEINSBOND` |

### 索引设计原则

| 原则 | 说明 |
|------|------|
| **选择性高** | 优先在选择性高的字段上建索引 |
| **覆盖索引** | 考虑覆盖查询，减少回表 |
| **避免冗余** | 避免创建重复索引 |
| **控制数量** | 单表索引不超过 5-7 个 |
| **复合索引** | 遵循最左前缀原则 |

### 索引示例

```sql
-- 普通索引
CREATE INDEX IDX_SETTLEINSBOND ON COP_TSETTLEINSBOND(clear_agent_code_cn, shclearing_trade_ins_id);
CREATE INDEX IDX_TRANSFERFLOW_INSID ON COP_TTRANSFERFLOW(TRANSFER_INS_ID, TRANSFER_INS_MODIFY);

-- 唯一索引
CREATE UNIQUE INDEX UK_TRANSFERADJUNCLIST ON cop_ttransferadjunclist(uuid);
CREATE UNIQUE INDEX UK_AGENCYINFO ON cop_tagencyinfo(agency_code);
```

详见 [数据库设计示例 - 索引命名约束](./db-design-example.md#索引命名约束)

## 脚本约束规范

### 幂等性要求

| 规则 | 说明 |
|------|------|
| **可重复执行** | 脚本必须保证幂等性 |
| **先检查后操作** | 所有操作必须先检查对象是否存在 |
| **避免重复** | 避免重复插入/更新数据 |
| **软删除优先** | 避免直接删除表或字段，优先使用状态标识 |

### 脚本结构

**Oracle/OceanBase Oracle**:
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

**MySQL/OceanBase MySQL**:
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

### 脚本要求

| 规则 | 说明 |
|------|------|
| **批量操作** | 需考虑性能影响 |
| **提交** | 脚本必须以 `commit;` 结尾 |
| **注释** | 关键操作必须有清晰的注释说明 |

详见 [数据库设计示例 - 脚本结构约束](./db-design-example.md#脚本结构约束)

## 字段注释规范

### 注释要求

| 规则 | 说明 |
|------|------|
| **必填** | 每个新增字段必须添加中文注释 |
| **简洁** | 注释内容仅包含字段的字面含义 |
| **禁止** | 禁止在注释中添加额外说明或示例 |

### 注释示例

```sql
-- 正确
COMMENT ON COLUMN cop_tfundinfo.fund_account IS '基金账号'
COMMENT ON COLUMN cop_ttransferinfo.transfer_amount IS '转账金额'

-- 错误  
COMMENT ON COLUMN cop_tfundinfo.fund_account IS '基金账号，用于标识基金在银行的账户信息'
```

详见 [数据库设计示例 - 字段注释约束](./db-design-example.md#字段注释约束)

## 禁止事项

### 严格禁止

| 禁止项 | 说明 |
|--------|------|
| **关键字** | 表名和字段名包含数据库关键字 |
| **DROP TABLE** | 生产脚本中禁止使用 DROP TABLE |
| **外键约束** | 禁止创建外键约束 |
| **触发器/存储过程** | 禁止使用（脚本执行除外） |
| **修改字段** | 禁止直接修改现有字段类型和长度 |
| **删除字段** | 禁止删除现有字段和约束 |
| **中文字符** | 禁止使用中文字符作为表名或字段名 |
| **无提交** | 脚本必须以 commit 结尾 |
| **跳过检查** | 禁止跳过对象存在性检查 |

详见 [数据库设计示例 - 禁止事项](./db-design-example.md#禁止事项)

## 设计检查清单

### 表设计检查

| 检查项 | 说明 |
|--------|------|
| 表名符合命名规范 | 前缀、小写、无下划线 |
| 字段命名清晰 | 符合字段命名规则 |
| 主键策略确定 | serial_no 或复合主键 |
| 数据类型正确 | 选择合适的数据类型 |
| 字段注释完整 | 每个字段有中文注释 |

### 索引设计检查

| 检查项 | 说明 |
|--------|------|
| 主键索引已创建 | 遵循主键约束命名 |
| 查询字段有索引 | 常用查询字段建索引 |
| 避免重复索引 | 检查已有索引 |
| 复合索引顺序 | 遵循最左前缀原则 |

### 脚本检查

| 检查项 | 说明 |
|--------|------|
| 幂等性 | 可重复执行不出错 |
| 对象检查 | 先检查是否存在 |
| 事务完整 | 有 commit 语句 |
| 注释清晰 | 关键操作有注释 |

## 版本历史

| 版本 | 日期 | 修改内容 | 作者 |
|------|------|----------|------|
| 1.0.1 | 2025-11-3 | 初始版本，参考 db-design-example.md | 架构办 |
