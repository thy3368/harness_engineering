---
description: "AI Coding Rules - 数据库编码规范"
globs: *.md,*.sql
alwaysApply: false
version: 1.0.1
author: wangxin49245
created: 2025-9-17
lastUpdated: 2025-11-3
---

# 数据库编码规范

## 约束等级
- `【强制】` - 违反将被认为代码存在严重缺陷，团队必须遵守
- `【推荐】` - 违反将被认为代码存在轻微缺陷，根据具体产品特性选择性遵守  
- `【参考】` - 违反可被认为代码存在优化空间，从持续优化角度参考使用

## 命名规范

### 对象命名模式

| **属性** | **规则** |
|----------|----------|
| 格式 | [前缀_]模块名_对象标识 |
| 最大长度 | 30个字符 |
| 字符要求 | 仅限小写字母、数字、下划线 |
| 分隔符 | 下划线 (_) |
| 命名原则 | 有意义的英文单词，最多4个单词 |

### 对象前缀

| **对象类型** | **对象前缀** | **格式示例** | **说明** |
|------------|-------------|-------------|----------|
| 表 | 无前缀 | user_info | 普通业务表 |
| 临时表 | t_ 或 tmp_ | t_user_temp | 临时数据表 |
| 视图 | v_ | v_user_info | 格式：v_表名 |
| 非唯一索引 | idx_ | idx_user_name | 格式：idx_表名_列名首字母 |
| 唯一索引 | uk_ | uk_user_email | 格式：uk_表名_列名首字母 |
| 主键 | pk_ | pk_user_info | 格式：pk_表名 |
| 存储过程 | p_ 或 sp_ | p_get_user | 存储过程 |
| 函数 | f_ 或 fn_ | f_calc_age | 自定义函数 |

### 字段命名规则
- `【推荐】` 字段命名含义明确，如user表的用户编号应为user_id而非id
- `【推荐】` 布尔字段使用is_前缀，如is_deleted表示"是否删除"
- `【推荐】` 包含多个逗号分隔值的字段加_list后缀，如client_privilege_list
- `【推荐】` 避免数字在下划线之后，防止驼峰转换工具出错

### 通用命名约束
- `【推荐】` 只能使用英文字母、数字和下划线，全部小写
- `【推荐】` 禁止以数字开头，名称前后不能加引号
- `【推荐】` 采用有意义且简短的英文单词，最多4个单词
- `【推荐】` 多个单词用下划线分隔
- `【推荐】` 可使用常见简写如info、cfg等
- `【强制】` 禁止使用数据库关键字和保留字
- `【推荐】` 不使用复数形式名词，除非只有复数形式

### 变量和参数命名
- `【推荐】` 本地变量前缀：v_，如v_begin_date
- `【推荐】` 参数前缀：p_，如p_user_id
- `【强制】` 除循环变量外，禁止使用单个字符命名变量

## 格式规范

### 缩进
- `【强制】` 代码块采用2个空格缩进，禁止使用tab键
- `【推荐】` INSERT语句中字段应与INTO关键字左对齐
- `【推荐】` 字段注释时每个字段单独一行，行尾增加注释

### 大小写规则
- `【推荐】` 除字符串外，统一使用小写字符书写

### 换行
- `【强制】` 一行只写一条语句，不允许把多个短语句写在一行
- `【推荐】` 同一条语句中关键字右对齐
- `【推荐】` 相对独立的程序块之间用一行空行隔开
- `【推荐】` 超过120字符的语句要分行书写，在低优先级操作符处换行
- `【强制】` begin、end等关键字独立成行

### 空格
- `【推荐】` 操作符前后以空格分隔
- `【推荐】` 分隔符之后以空格分隔

### 注释
- `【推荐】` 脚本文件、函数、过程头部包含：创建者、创建日期、功能描述、修改记录
- `【强制】` 注释应紧挨其描述的代码，在其上方或右方
- `【推荐】` 注释如放在代码段上方则应与上面代码段用空行隔开
- `【强制】` 注释与所描述的代码进行同样的缩进
- `【推荐】` 通过合理命名使代码成为自注释的

## 设计规范

### 通用设计规则
- `【推荐】` 选择合适的数据类型及长度，尽量用varchar代替char
- `【推荐】` 字段排列顺序：主键字段 > 常用字段 > 短小字段 > 非空字段 > 其他字段
- `【推荐】` 遵循三范式设计原则，个别情况可考虑反范式设计
- `【推荐】` 表上索引不超过5个，每个索引字段数不超过5个
- `【强制】` 禁止使用外键，外键约束应在应用层处理
- `【推荐】` 主键统一使用无符号整型自增
- `【推荐】` 应用程序中原则上禁止对主键字段进行更新
- `【强制】` 数据库设计应遵循权限最小化原则

### MySQL特有规则
- `【推荐】` 使用InnoDB存储引擎
- `【推荐】` 字符集统一使用UTF8MB4，校对集使用对应的二进制规则
- `【强制】` 所有表都必须有主键
- `【强制】` 禁止使用enum/set/bool类型
- `【推荐】` 尽量不使用text/blobs等大字段类型，使用时不要有默认值
- `【强制】` 禁止使用浮点类型FLOAT和DOUBLE
- `【推荐】` 对较长的字符型字段建立索引时，应使用前缀索引
- `【推荐】` 字段建议定义为not null，并且指定默认值

### Oracle特有规则
- `【推荐】` 表和索引的数据分不同表空间存储
- `【推荐】` 原则上每个表都应该有主键，优先使用业务主键
- `【推荐】` 不建议在分区表上创建全局索引，原则上使用local索引
- `【推荐】` 字段类型使用字符型以保证跨数据库兼容性

## SQL语法规范

### 通用SQL规则
- `【强制】` 使用SQL99语法标准，在多表关联时用join关键字
- `【强制】` 禁止select *，必须将字段名一一列出
- `【强制】` insert语句中必须列出要插入的字段名
- `【强制】` 当SQL涉及多个表时，必须为每个字段指定表名前缀
- `【强制】` 合并多表数据时，如果不需要去除重复数据应使用union all而不是union
- `【推荐】` 尽量避免使用or操作符
- `【强制】` 对于不需要查询的字段，不要放在select子句中，尤其是text/blob等大字段
- `【推荐】` 应避免带in的子查询，尽量改写成join
- `【推荐】` 枚举型的in子句枚举数量不超过1000个，尽量使用子查询替代
- `【强制】` 开发人员禁止私自使用hint
- `【强制】` 外连接一律用left join，禁止使用right join
- `【推荐】` 尽量使用内连接，减少使用外连接
- `【推荐】` where条件列上禁止使用函数和表达式，避免数据类型的隐式转换
- `【推荐】` 避免不必要的排序
- `【推荐】` 使用like进行模糊查询时，%不要放在首位
- `【推荐】` 原则上禁止使用触发器
- `【强制】` update和delete语句必须有where子句
- `【推荐】` 查询表数据量较大时，尽量不使用自定义函数或标量子查询
- `【推荐】` 分页加载逻辑建议使用唯一键进行排序
- `【推荐】` 删除全表数据，建议使用truncate命令

### MySQL特有SQL规则
- `【推荐】` 避免三个表以上的关联查询，避免大表间的join
- `【推荐】` 联表查询时，连接列的数据类型必须一致
- `【推荐】` 不建议使用存储过程、函数

### Oracle特有SQL规则
- `【推荐】` 尽量使用静态SQL，少用动态SQL
- `【强制】` 对于动态SQL，新研发产品应该强制使用绑定变量
- `【推荐】` 原则上避免使用游标变量，必须使用时要及时关闭游标
- `【推荐】` 不要随意使用commit，应保证事务完整性
- `【强制】` 禁止使用goto语句来控制流程
- `【推荐】` 过程、函数中，确保所有的变量和参数都使用到
- `【推荐】` 变量赋值时，尽量使用:= 赋值替代select into

## 跨数据库兼容性

### 版本移植规则
- `【推荐】` 对于单行注释应使用"-- "方式
- `【强制】` 对于字符串应该使用单引号括起来
- `【推荐】` 尽量避免使用full join
- `【推荐】` 避免在group by和having子句中使用列的别名
- `【推荐】` from子句中的子查询要定义别名

## 脚本规范

### 通用脚本规则
- `【推荐】` 脚本必须支持重复执行不报错
- `【推荐】` 脚本名需要加上执行用户作为前缀，以".sql"文件格式存储
- `【推荐】` 数据库中加入特定系统参数表标识数据库环境
- `【强制】` 在修改代码的上一行书写注释，包括：修改日期，修改单编号/QC号：修改说明
- `【强制】` 对于业务依赖的修改，应在代码逻辑上保证其依赖性
- `【推荐】` 在脚本前部应打印脚本名称或标记
- `【推荐】` 在升级前对重要数据进行统一备份
- `【推荐】` 升级脚本集成时，需要将脚本执行日志落地到本地文件
- `【推荐】` 对执行耗时较长的脚本，在执行前进行提示

### MySQL脚本特有
- `【推荐】` 脚本中需要判断执行数据库是否正确
- `【推荐】` 代码中避免使用反引号"`"

### Oracle脚本特有
- `【强制】` PLSQL匿名块脚本后需要增加"/"，顶格书写单独成行
- `【推荐】` 文件头加上set define off; 文件尾加上set define on;
- `【推荐】` 脚本中需要判断执行用户是否正确

### 数据库对象脚本
- `【强制】` 单个表的表结构修改代码写在一个文件中
- `【推荐】` 对表结构的修改应调用专门的过程来处理
- `【强制】` 对数据库对象的创建、修改、删除和数据的新增、修改前，应先进行存在性判断
- `【强制】` 在表上新增字段时，若指定默认值，则必须指定not null
- `【推荐】` 不对表中已存在的字段进行删除，可以使用重命名代替
- `【强制】` 对数据库表进行删除、重建之后，应恢复该表原有的索引和约束
- `【强制】` 对数据库对象进行删除、重建之后，应恢复该对象原有的对外权限
- `【推荐】` 对表进行增加字段时，应同时加上字段备注

### 表数据脚本
- `【强制】` 单个表的表数据修改代码写在一个文件中
- `【强制】` 在书写update和delete语句时，必须带有where条件
- `【推荐】` MySQL脚本前加入开启或关闭自动提交事务的控制语句

## AI代码生成指导

### 验证优先级
1. 首先检查所有`【强制】`规则
2. 然后应用`【推荐】`规则
3. 最后考虑`【参考】`规则

### 代码生成检查清单
- 验证所有命名是否符合前缀和格式规范
- 确保SQL语句符合SQL99标准
- 检查是否有SELECT *语句
- 验证INSERT语句是否列出字段名
- 确认UPDATE/DELETE语句包含WHERE子句
- 检查是否使用了禁止的数据类型
- 验证脚本是否包含存在性判断
- 确保注释格式正确
- 检查缩进是否使用2个空格
- 验证字符串是否使用单引号

### 错误预防
- MySQL：避免ENUM/SET/BOOL/FLOAT/DOUBLE类型
- Oracle：避免GOTO语句，确保使用绑定变量
- 跨数据库：使用兼容语法，避免FULL JOIN
- 安全：始终包含WHERE条件，使用权限最小化原则

### 性能优化
- 优先使用索引友好的查询模式
- 避免在WHERE子句中使用函数
- 合理使用JOIN类型
- 控制索引数量和复杂度

## 附录：脚本示例

*建议将下列示例中的判断存在性和对象操作语句封装在过程中，脚本直接调用过程来进行修改。*

### Oracle脚本示例

#### 新增表
```sql
set define off;
set feedback off;
prompt 脚本文件名或标记

declare
  v_rowcount number;
begin
  -- 20210506 M2021050600001：创建表【表名】
  select count(*)
    into v_rowcount
    from user_tables
   where table_name = upper('表名');
  
  if v_rowcount = 0 then
    execute immediate '具体的建表语句';
  end if;
end;
/
set define on;
set feedback on;
```

#### 删除表
```sql
set define off;
set feedback off;
prompt 脚本文件名或标记

declare
  v_rowcount number;
begin
  -- 20210506 M2021050600001：删除表【表名】
  select count(*)
    into v_rowcount
    from user_tables
   where table_name = upper('表名');
  
  if v_rowcount = 1 then
    execute immediate 'drop table 表名';
  end if;
end;
/
set define on;
set feedback on;
```

#### 新增字段
```sql
set define off;
set feedback off;
prompt 脚本文件名或标记

declare
  v_rowcount number;
begin
  -- 20210506 M2021050600001：新增字段【字段名】
  select count(*)
    into v_rowcount
    from user_tab_columns
   where table_name = upper('表名')
     and column_name = upper('字段名');
  
  if v_rowcount = 0 then
    execute immediate 'alter table 表名 add 字段名 字段类型 default 默认值 not null';
    execute immediate 'comment on column 表名.字段名 is ''字段中文名''';
  end if;
end;
/
set define on;
set feedback on;
```

#### 删除或修改字段
```sql
set define off;
set feedback off;
prompt 脚本文件名或标记

declare
  v_rowcount number;
begin
  -- 20210506 M2021050600001：删除字段【字段名】
  select count(*)
    into v_rowcount
    from user_tab_columns
   where table_name = upper('表名')
     and column_name = upper('字段名');
  
  if v_rowcount = 1 then
    execute immediate 'alter table 表名 drop column 字段名';
  end if;
  
  -- 20210506 M2021050600002：修改字段【字段名】
  select count(*)
    into v_rowcount
    from user_tab_columns
   where table_name = upper('表名')
     and column_name = upper('字段名');
  
  if v_rowcount = 1 then
    execute immediate 'alter table 表名 modify 字段名 字段类型 default 默认值 not null';
  end if;
  
  -- 20210506 M2021050600003：重命名字段【原字段名】为【新字段名】
  select count(*)
    into v_rowcount
    from user_tab_columns
   where table_name = upper('表名')
     and column_name = upper('原字段名');
  
  if v_rowcount = 1 then
    execute immediate 'alter table 表名 rename column 原字段名 to 新字段名';
  end if;
end;
/
set define on;
set feedback on;
```

#### 新增主键
```sql
set define off;
set feedback off;
prompt 脚本文件名或标记

declare
  v_rowcount number;
begin
  -- 20210506 M2021050600001：新增主键
  select count(*)
    into v_rowcount
    from user_constraints
   where table_name = upper('表名')
     and constraint_name = upper('主键名');
  
  if v_rowcount = 0 then
    execute immediate 'alter table 表名 add constraint 主键名 primary key(字段列表)';
  end if;
end;
/
set define on;
set feedback on;
```

#### 删除主键
```sql
set define off;
set feedback off;
prompt 脚本文件名或标记

declare
  v_rowcount number;
begin
  -- 20210506 M2021050600001：删除主键
  select count(*)
    into v_rowcount
    from user_constraints
   where table_name = upper('表名')
     and constraint_name = upper('主键名');
  
  if v_rowcount = 1 then
    execute immediate 'alter table 表名 drop constraint 主键名';
  end if;
end;
/
set define on;
set feedback on;
```

#### 新增索引
```sql
set define off;
set feedback off;
prompt 脚本文件名或标记

declare
  v_rowcount number;
begin
  -- 20210506 M2021050600001：新增索引【索引名】
  select count(*)
    into v_rowcount
    from user_indexes
   where table_name = upper('表名')
     and index_name = upper('索引名');
  
  if v_rowcount = 0 then
    execute immediate 'create index 索引名 on 表名(字段列表) tablespace 表空间名';
  end if;
end;
/
set define on;
set feedback on;
```

#### 删除索引
```sql
set define off;
set feedback off;
prompt 脚本文件名或标记

declare
  v_rowcount number;
begin
  -- 20210506 M2021050600001：删除索引【索引名】
  select count(*)
    into v_rowcount
    from user_indexes
   where table_name = upper('表名')
     and index_name = upper('索引名');
  
  if v_rowcount = 1 then
    execute immediate 'drop index 索引名';
  end if;
end;
/
set define on;
set feedback on;
```

#### 新增数据
```sql
set define off;
set feedback off;
prompt 脚本文件名或标记

declare
  v_rowcount number;
begin
  -- 20210506 M2021050600001：新增配置数据2020001，客户信息明细查询
  select count(*)
    into v_rowcount
    from hscon.uam_menus 
   where menu_id = '2020001';
  
  if v_rowcount = 0 then
    insert into hscon.uam_menus (menu_id, menu_name, page_id, need_show)
    values ('2020001', '客户信息明细查询', '@2020001', 1);
  end if;
  commit;
end;
/
set define on;
set feedback on;
```

#### 修改数据
```sql
set define off;
set feedback off;
prompt 脚本文件名或标记

declare
  v_rowcount number;
begin
  -- 20210506 M2021050600001：修改配置数据2020001菜单名为客户信息明细查询
  select count(*)
    into v_rowcount
    from hscon.uam_menus 
   where menu_id = '2020001';
  
  if v_rowcount = 1 then
    update hscon.uam_menus set menu_name = '客户信息明细查询'
     where menu_id = '2020001';
  end if;
  commit;
end;
/
set define on;
set feedback on;
```

### MySQL脚本示例

#### 新增表
```sql
select '脚本文件名或标记';
use 数据库名;

-- 20210506 M2021050600001：创建表【表名】
create table if not exists 数据库名.表名 (
  具体的建表语句
) engine = 存储引擎 default charset = 字符集 collate = 校对集 comment = '表注释';
```

#### 删除表
```sql
select '脚本文件名或标记';
use 数据库名;

-- 20210506 M2021050600001：删除表【表名】
drop table if exists 数据库名.表名;
```

#### 新增字段
```sql
select '脚本文件名或标记';
use 数据库名;

-- 20210506 M2021050600001：新增字段【字段名】
set @v_count = 0;
select count(*) into @v_count 
  from information_schema.columns 
 where TABLE_SCHEMA='数据库名' 
   and TABLE_NAME='表名' 
   and column_name = '字段名';
set @sql = if(@v_count = 0,"增加字段语句","select '表名.字段名 is OK.'");
prepare stmt from @sql;
execute stmt;
```

#### 删除或修改字段
```sql
select '脚本文件名或标记';
use 数据库名;

-- 20210506 M2021050600001：删除字段【字段名】
set @v_count = 0;
select count(*) into @v_count 
  from information_schema.columns 
 where TABLE_SCHEMA='数据库名' 
   and TABLE_NAME='表名' 
   and column_name = '字段名';
set @sql = if(@v_count = 1,"删除字段语句","select '表名.字段名 is deleted.'");
prepare stmt from @sql;
execute stmt;

-- 20210506 M2021050600002：修改字段【字段名】
set @v_count = 0;
select count(*) into @v_count 
  from information_schema.columns 
 where TABLE_SCHEMA='数据库名' 
   and TABLE_NAME='表名' 
   and column_name = '字段名';
set @sql = if(@v_count = 1,"修改字段语句","select '表名.字段名 is changed.'");
prepare stmt from @sql;
execute stmt;
```

#### 新增主键
```sql
select '脚本文件名或标记';
use 数据库名;

-- 20210506 M2021050600001：新增主键
set @v_count = 0;
select count(*) into @v_count 
  from information_schema.table_constraints 
 where TABLE_SCHEMA='数据库名' 
   and TABLE_NAME='表名' 
   and CONSTRAINT_NAME = 'PRIMARY';
set @sql = if(@v_count = 0,"alter table 表名 add primary key (字段列表)","select '表名 PRIMARY KEY is OK.'");
prepare stmt from @sql;
execute stmt;
```

#### 删除主键
```sql
select '脚本文件名或标记';
use 数据库名;

-- 20210506 M2021050600001：删除主键
set @v_count = 0;
select count(*) into @v_count 
  from information_schema.table_constraints 
 where TABLE_SCHEMA='数据库名' 
   and TABLE_NAME='表名' 
   and CONSTRAINT_NAME = 'PRIMARY';
set @sql = if(@v_count = 1,"alter table 表名 drop primary key","select '表名 PRIMARY KEY is deleted.'");
prepare stmt from @sql;
execute stmt;
```

#### 新增索引
```sql
select '脚本文件名或标记';
use 数据库名;

-- 20210506 M2021050600001：新增索引
set @v_count = 0;
select count(*) into @v_count 
  from information_schema.statistics 
 where TABLE_SCHEMA='数据库名' 
   and TABLE_NAME='表名' 
   and INDEX_NAME = '索引名';
set @sql = if(@v_count = 0,"create index 索引名 on 表名(字段列表)","select '表名.索引名 is OK.'");
prepare stmt from @sql;
execute stmt;
```

#### 删除索引
```sql
select '脚本文件名或标记';
use 数据库名;

-- 20210506 M2021050600001：删除索引
set @v_count = 0;
select count(*) into @v_count 
  from information_schema.statistics 
 where TABLE_SCHEMA='数据库名' 
   and TABLE_NAME='表名' 
   and INDEX_NAME = '索引名';
set @sql = if(@v_count = 1,"alter table 表名 drop index 索引名","select '表名.索引名 is deleted.'");
prepare stmt from @sql;
execute stmt;
```

#### 新增数据
```sql
select '脚本文件名或标记';
use 数据库名;

-- 20210506 M2021050600001：新增数据
set @v_count = 0;
select count(*) into @v_count from 表名 where 主键条件;
set @sql = if(@v_count = 0, "insert into 表名 values 语句", "select '数据已存在.'");
prepare stmt from @sql;
execute stmt;
commit;
```

#### 删除数据
```sql
select '脚本文件名或标记';
use 数据库名;

-- 20210506 M2021050600001：删除数据
set @v_count = 0;
select count(*) into @v_count from 表名 where 主键条件;
set @sql = if(@v_count = 1, "delete from 表名 where 条件", "select '数据已删除.'");
prepare stmt from @sql;
execute stmt;
commit;
```