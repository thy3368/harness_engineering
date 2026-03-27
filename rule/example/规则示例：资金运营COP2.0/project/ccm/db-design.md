---
description: "AI Coding Rules - 数据库设计规范"
globs: *.md,*.sql
alwaysApply: false
version: 1.0.0
author: liulm50695
created: 2025-09-19
lastUpdated: 2025-09-19
---

# CCM数据库脚本约束规范

## 数据库类型支持

**必须支持以下7种数据库类型**：
- `mysql` - MySQL数据库 5.7+
- `oracle` - Oracle数据库 11g+  
- `dm` - 达梦数据库 DM8+
- `gaussdbopengauss` - 华为GaussDB/OpenGauss数据库
- `obmysql` - OceanBase MySQL兼容模式 3.2+/4.2+
- `oboracle` - OceanBase Oracle兼容模式 3.2+/4.2+
- `tdsqlmysql` - 腾讯TDSQL MySQL兼容版

## 表命名约束

**强制要求**：
- 核心业务表以`T_HK_`作为前缀（如T_HK_MAIN、T_HK_ACC_DETAIL）
- 配置类表以`TS_`作为前缀（如TS_TGH_CONFIG、TS_SZT_LOG）
- 表名必须全部使用大写字母
- 业务词汇使用下划线分隔
- 表名长度不得超过20个字符
- 脚本都要支持可重复执行

**命名示例**：
```sql
-- 正确
CREATE TABLE T_HK_MAIN                    -- 划款指令主表
CREATE TABLE T_HK_ACC_BALANCE            -- 账户余额指令表
CREATE TABLE TS_TGH_CONFIG               -- 托管行配置表
CREATE TABLE TS_SZT_LOG                  -- 深证通日志表

-- 错误
CREATE TABLE t_hk_main                   -- 小写
CREATE TABLE HK_MAIN                     -- 缺少前缀
CREATE TABLE T_HK_MAININFO               -- 不规范的词汇组合
```

## 字段命名约束

**强制要求**：
- 字段名必须全部使用小写字母
- 多个单词之间必须使用下划线分隔
- 主键字段优先使用业务主键（如main_id、balance_id、detail_id）
- ID类字段以`_id`结尾
- 编号类字段以`_no`、`_code`结尾
- 时间类字段使用`_date`、`_time`后缀  
- 金额类字段以`_amount`、`balance`、`cash`命名
- 标志类字段以`_flag`、`istate`、`_status`命名

**命名示例**：
```sql
-- 正确
main_id                -- 主键ID
inst_code              -- 机构代码
subsys_no              -- 子系统编号
fund_id                -- 基金ID
out_acnt_no            -- 出账账号
create_date            -- 创建时间
send_date              -- 发送时间
cash                   -- 金额
balance                -- 余额
istate                 -- 状态

-- 错误
MainId                 -- 大写
instCode               -- 驼峰命名
fundaccount            -- 缺少下划线
transferAmount         -- 驼峰+缺少下划线
```

## 数据类型约束

### Oracle/OceanBase Oracle/达梦模式

**使用的数据类型**：
- `varchar2(n)` - 变长字符串，常见长度：4、10、20、32、64、100、256、1000、4000
- `number(p,s)` - 数值类型，常见规格：
  - `number(10,0)` - 整数
  - `number(14,6)` - 时间戳(YYYYMMDD.HHMMSS)
  - `number(18,0)` - 长整数
  - `number(19,2)` - 金额字段
  - `number(30,0)` - 特大整数
- `clob` - 大文本字段
- `char(1)` - 固定长度字符，用于标志字段

### MySQL/OceanBase MySQL/TDSQL/GaussDB模式

**使用的数据类型**：
- `varchar(n)` - 变长字符串，常见长度：4、10、20、32、64、100、256、1000、4000
- `decimal(p,s)` - 精确数值，常见规格：
  - `decimal(10,0)` - 整数
  - `decimal(14,6)` - 时间戳
  - `decimal(18,0)` - 长整数
  - `decimal(19,2)` - 金额字段
  - `decimal(30,0)` - 特大整数
- `LONGTEXT` - 大文本字段（MySQL）
- `TEXT` - 大文本字段（GaussDB）
- `char(1)` - 固定长度字符，用于标志字段

## 主键约束规范

**强制要求**：
- 单字段主键使用业务主键（如main_id、balance_id、detail_id）
- 复合主键按重要性排序字段
- 主键命名长度限制在30个字符以内

**主键约束命名规则**：
- **Oracle/达梦/OceanBase Oracle**：使用`pk_ + 表名去除前缀并转小写`
- **MySQL/GaussDB/OceanBase MySQL/TDSQL**：使用`PRIMARY KEY`（不指定约束名）

**主键约束示例**：
```sql
-- Oracle/达梦/OceanBase Oracle
ALTER TABLE T_HK_MAIN ADD CONSTRAINT pk_hk_main PRIMARY KEY(main_id);
ALTER TABLE TS_TGH_CONFIG ADD CONSTRAINT pk_tgh_config PRIMARY KEY(config_id);
ALTER TABLE TS_HK_SEQ_NO ADD CONSTRAINT pk_hk_seq_no PRIMARY KEY(fund_id,pay_date,seq_no);

-- MySQL/GaussDB/OceanBase MySQL/TDSQL
CREATE TABLE T_HK_MAIN (
    main_id varchar(20) NOT NULL,
    -- 其他字段...
    PRIMARY KEY(main_id)
);
```

## 索引命名约束

### 普通索引命名规则

**强制要求**：
- 索引名称必须全部使用大写字母
- **统一使用`INDEX_表名_字段描述`格式**
- 索引命名长度限制在30个字符以内

**普通索引示例**：
```sql
-- 标准索引格式
CREATE INDEX INDEX_T_HK_MAIN_UUID ON T_HK_MAIN(uuid);
CREATE INDEX INDEX_TS_SZT_LOG_LOG_ID ON TS_SZT_LOG(log_id);
CREATE INDEX INDEX_T_HK_ACC_DETAIL_FUND_ID ON T_HK_ACC_DETAIL(fund_id, inst_code);

-- 唯一索引
CREATE UNIQUE INDEX UK_INST_PARAM_CONFIG ON TS_INST_PARAM_CONFIG(inst_code, biz_type, filed_name_en);
```

### 主键索引说明

**注意事项**：
- 主键索引由数据库自动创建，不需要手动创建INDEX
- 主键约束名称规则见"主键约束规范"章节

## 通用脚本约束

**强制要求**：
- 脚本必须保证幂等性（可重复执行不出错）
- 所有操作必须先检查对象是否存在
- 避免重复创建表、索引、约束等对象
- 避免直接删除表或字段，优先使用状态标识
- 脚本必须以`commit;`结尾，除了gaussdbopengauss
- 关键操作必须有清晰的注释说明

## 脚本结构约束

### Oracle/达梦/OceanBase Oracle格式

**创建表脚本示例**：
```sql
declare
    v_rowcount number(10);
    v_sql varchar2(32767);
begin
    --账户余额指令表
    select count(*) into v_rowcount from dual where exists(
        select * from user_objects where object_name = upper('T_HK_ACC_BALANCE')
    );
    if v_rowcount = 0 then
        v_sql := 'CREATE TABLE T_HK_ACC_BALANCE('||
                'balance_id varchar2(20) DEFAULT '''' NOT NULL,'||
                'subsys_no varchar2(10) DEFAULT '''' NOT NULL,'||
                'inst_code varchar2(4) DEFAULT '''' NOT NULL,'||
                'fund_id varchar2(32) DEFAULT '''' ,'||
                'create_date number(14,6) DEFAULT to_number(to_char(sysdate,''YYYYMMDD.HH24MISS'')) '||
                ')';
        execute immediate v_sql;
        execute immediate 'ALTER TABLE T_HK_ACC_BALANCE ADD CONSTRAINT pk_hk_acc_balance PRIMARY KEY(balance_id)';
        commit;
    end if;
end;
/
```

**创建索引脚本示例**：
```sql
declare
    iCount number:=0;
begin
    select count(1) into iCount from user_indexes 
    where upper(table_name) = upper('T_HK_MAIN') 
    and upper(index_name) = 'INDEX_T_HK_MAIN_UUID';
    
    if iCount = 0 then
        execute immediate 'create index INDEX_T_HK_MAIN_UUID on T_HK_MAIN (uuid)';
    end if;
end;
/
commit;
```

### MySQL/GaussDB/OceanBase MySQL/TDSQL格式

**创建表脚本示例**：
```sql
SELECT 'CREATE TABLE T_HK_ACC_BALANCE 账户余额指令表...';
CREATE TABLE IF NOT EXISTS T_HK_ACC_BALANCE
(
    balance_id                     varchar(20)    DEFAULT ''         NOT NULL,
    subsys_no                      varchar(10)    DEFAULT ''         NOT NULL,
    inst_code                      varchar(4)     DEFAULT ''         NOT NULL,
    fund_id                        varchar(32)    DEFAULT ''         ,
    create_date                    decimal(14,6)    ,
    PRIMARY KEY(balance_id)
);
```

**创建索引脚本示例**：
```sql
DROP PROCEDURE IF EXISTS sp_db_mysql;
DELIMITER $$
CREATE PROCEDURE sp_db_mysql()
BEGIN
    DECLARE v_rowcount INT;
    DECLARE database_name VARCHAR(100);
    SELECT DATABASE() INTO database_name;
    SELECT COUNT(1) INTO v_rowcount
    FROM information_schema.statistics
    WHERE table_schema = database_name
      AND upper(table_name) = 'T_HK_MAIN'
      AND upper(index_name) = 'INDEX_T_HK_MAIN_UUID';
    IF v_rowcount = 0 THEN
        create index INDEX_T_HK_MAIN_UUID on T_HK_MAIN(uuid);
    END IF;
END$$
DELIMITER ;
CALL sp_db_mysql();
DROP PROCEDURE IF EXISTS sp_db_mysql;
```

## 脚本生成位置约束

### 版本目录结构
```
capitalchannelmanager/ccm-acm/sqls/[数据库类型]/ccmserver/
├── [版本号]/                     # 版本目录，如COP2.0-CCM.V202506.00.000
│   ├── 01.[数据库类型].ddl.sql   # DDL脚本（表结构、索引）
│   └── 02.[数据库类型].dml.sql   # DML脚本（数据插入、更新）
```

**版本命名规则**：
- 格式：`COP2.0-CCM.V{年月}.{序号}.{补丁号}`
- 示例：`COP2.0-CCM.V202506.00.000`

**脚本文件命名规则**：
- DDL脚本：`01.{数据库类型}.ddl.sql`
- DML脚本：`02.{数据库类型}.dml.sql`
- 示例：
  - `01.mysql.ddl.sql`
  - `01.oracle.ddl.sql`
  - `02.gaussdbopengauss.dml.sql`

## 字段注释约束

**强制要求**：
- MySQL系列数据库直接在CREATE TABLE中添加注释
- Oracle系列数据库使用COMMENT ON COLUMN语句
- 注释内容仅包含字段的字面含义，使用中文
- 禁止在注释中添加额外说明或示例

**注释示例**：
```sql
-- MySQL格式
CREATE TABLE T_HK_MAIN
(
    main_id varchar(20) NOT NULL COMMENT '主键ID',
    inst_code varchar(4) NOT NULL COMMENT '机构代码',
    fund_id varchar(32) COMMENT '基金ID',
    cash decimal(19,2) COMMENT '金额'
);

-- Oracle格式（在创建表后添加）
COMMENT ON COLUMN T_HK_MAIN.main_id IS '主键ID';
COMMENT ON COLUMN T_HK_MAIN.inst_code IS '机构代码';
COMMENT ON COLUMN T_HK_MAIN.fund_id IS '基金ID';
COMMENT ON COLUMN T_HK_MAIN.cash IS '金额';
```

## 禁止事项

**严格禁止**：
- 表名和字段名包含数据库关键字（如usage字段需使用反引号）
- 在生产脚本中使用DROP TABLE语句
- 创建外键约束
- 使用触发器、存储过程（脚本执行除外）
- 直接修改现有字段类型和长度
- 删除现有字段和约束
- 使用中文字符作为表名或字段名
- 脚本不以commit结尾
- 跳过对象存在性检查
- 重复执行导致数据错误

## 数据类型对应关系

**Oracle ↔ MySQL 类型映射**：
- `varchar2(n)` ↔ `varchar(n)`
- `number(10,0)` ↔ `decimal(10,0)`
- `number(14,6)` ↔ `decimal(14,6)` (时间戳)
- `number(18,0)` ↔ `decimal(18,0)`
- `number(19,2)` ↔ `decimal(19,2)` (金额)
- `number(30,0)` ↔ `decimal(30,0)`
- `clob` ↔ `LONGTEXT`
- `char(1)` ↔ `char(1)`

**时间字段特殊处理**：
- Oracle: `number(14,6) DEFAULT to_number(to_char(sysdate,'YYYYMMDD.HH24MISS'))`
- MySQL: `decimal(14,6)` (无默认值，应用层处理)

## CCM特有表结构模式

### 核心业务表模式
```sql
-- 主业务表模式（以T_HK_MAIN为例）
main_id                        -- 主键ID
subsys_no                      -- 子系统编号
inst_code                      -- 机构代码
uuid                           -- 全局唯一标识
istate                         -- 状态字段
create_date                    -- 创建时间
update_date                    -- 更新时间
send_date                      -- 发送时间
back_date                      -- 回复时间
result_date                    -- 结果时间
remark                         -- 备注
```

### 配置表模式
```sql
-- 配置表模式（以TS_TGH_CONFIG为例）
config_id                      -- 配置ID（主键）
inst_code                      -- 机构代码
business_type                  -- 业务类型
update_date                    -- 更新时间
```

### 日志表模式
```sql
-- 日志表模式（以TS_SZT_LOG为例）
log_id                         -- 日志ID（主键）
ref_id                         -- 关联ID
source_data                    -- 源数据（大文本）
handle_data                    -- 处理后数据（大文本）
create_date                    -- 创建时间
send_status                    -- 发送状态
```

## 强制检查清单

### 表创建检查清单
- [ ] 表名使用正确前缀（T_HK_或TS_）
- [ ] 表名全部大写，字段名全部小写
- [ ] 使用下划线分隔多个单词
- [ ] 必要字段添加NOT NULL约束
- [ ] 主键字段设置正确
- [ ] 时间字段使用正确的数据类型和格式
- [ ] 大文本字段使用CLOB/LONGTEXT
- [ ] 添加适当的字段注释

### 索引创建检查清单
- [ ] 索引名称全部大写
- [ ] 使用INDEX_表名_字段描述格式
- [ ] 添加存在性检查逻辑
- [ ] 索引字段选择合理（常用查询字段）
- [ ] 避免创建重复索引

### 脚本质量检查清单
- [ ] 脚本具有幂等性
- [ ] 添加对象存在性检查
- [ ] 使用正确的数据库语法格式
- [ ] 脚本以commit结尾
- [ ] 添加必要的注释说明
- [ ] 版本目录和文件命名正确