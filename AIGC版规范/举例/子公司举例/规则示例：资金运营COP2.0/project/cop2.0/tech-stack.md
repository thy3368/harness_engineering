---
description: "AI Coding Rules - 技术栈规范"
globs: *.md,*.java
alwaysApply: false
version: 1.0.0
author: wangxin49245
created: 2025-9-19
lastUpdated: 2025-9-19
---

## 项目技术栈

### 核心框架

- **JResCloud**: 恒生云原生微服务框架 (v3.1.7.x.x)
- **Spring Boot**: 2.7.18 (通过JResCloud集成，支持springboot-2.7-adaptor兼容适配)
- **Spring Framework**: 企业级应用开发框架 (v5.3.39，通过Spring Boot集成)
- **MyBatis**: 数据持久化框架 (v3.5.6)

### 开发语言与工具

- **Java**: JDK 1.8
- **Maven**: 项目构建管理工具 (v3.8+)
- **Git**: 版本控制工具

### 构建与部署

#### Maven插件
- **maven-compiler-plugin**: 编译插件 (v3.8.1)
- **maven-jar-plugin**: JAR打包插件 (v3.4.2)
- **maven-dependency-plugin**: 依赖管理插件 (v3.8.1)
- **maven-assembly-plugin**: 打包插件 (v3.7.1)
- **maven-enforcer-plugin**: 依赖冲突检测插件 (v3.5.0)


### 数据存储

#### 关系型数据库
- **Oracle**: 商业数据库支持，支持`11g+`
- **MySQL**: 开源数据库，支持`5.7+`
- **达梦数据库(DM)**: 国产数据库，支持`DM8+`
- **OceanBase**: 阿里分布式数据库，支持`3.2.x`、`4.2.x`

#### 数据库连接池

- **HikariCP**: 高性能数据库连接池 (v4.0.3)

### 消息中间件

#### 开源消息中间件

- **RabbitMQ**: AMQP协议消息队列
- **东方通HTP**: 国产信创消息中间件
- **宝兰德MQ**: 国产信创消息中间件

### 缓存与协调服务

- **Redis**: 分布式缓存和锁服务 (v5.0+)
- **Zookeeper**: 分布式协调服务 (Zookeeper客户端：v3.4.14)

### 限流与监控

- **JResCloud Monitor**: 恒生框架内置监控组件
- **Spring Actuator**: 应用监控和管理

### 序列化与数据处理

- **FastJSON**: JSON处理 (v1.2.83)
- **Jackson**: JSON处理 (v2.18.0)
- **XStream**: XML处理 (v1.4.21)
- **SnakeYAML**: YAML文件处理 (v2.0)

### 应用服务器支持

#### 嵌入式服务器
- **Tomcat**: 默认Web容器
- **宝兰德BES**: 国产信创Web容器
- **东方通TongWeb**: 国产信创Web容器

### 日志框架

- **Log4j2**: 日志记录框架 (v2.18.0)

### 单元测试框架

- **JUnit**: 单元测试框架 (v4.13.1)
- **Spring Boot Test**: 集成测试支持

### 文件处理与文档

#### PDF处理

- **Apache PDFBox**: PDF处理库 (v2.0.26)
- **iText**: PDF生成和处理
  - `xmlworker` (v5.5.13.3)
  - `forms` (v7.0.3)
- **Aspose Words**: 文档处理工具 (v23.1)
- **Knife4j**: API文档和接口测试工具 (v4.5.0)

#### Excel处理

- **Apache POI**: Office文档处理
  - `poi` (v3.17)
  - `poi-ooxml` (v3.17)
  - `poi-scratchpad` (v3.17)
- **EasyExcel**: 阿里Excel处理工具 (v3.1.2)

#### 文档转换

- **OpenSagres XDocReport**: Word转PDF工具 (v2.0.1)
- **docx4j**: Word文档处理 (v6.1.2)

### 网络通信与集成

#### HTTP客户端

- **Apache HttpClient**: HTTP客户端 (v4.5.13)
- **Apache HttpMime**: HTTP文件上传 (v4.5.6)

#### T2协议

- **JRESCloud T2SDK**: 恒生T2协议SDK
- **T2 SSL**: T2协议SSL安全传输支持

#### 邮件服务

- **JavaMail**: 邮件发送服务 (v1.4.7)

### 工具类库

- **Apache Commons**: 常用工具类集合
  - `commons-lang3` (v3.18.0)
  - `commons-io` (v2.14.0)
  - `commons-codec` (v1.15)
  - `commons-compress` (v1.26.0)
  - `commons-text` (v1.4)
  - `commons-collections4` (v4.4)
  - `commons-dbutils` (v1.7)
- **Hutool**: 国产Java工具库 (v5.8.24)
- **Guava**: Google工具库 (v32.1.1-jre)
- **JSoup**: HTML解析工具 (v1.15.3)
- **Lombok**: 代码简化工具 (v1.18.16)
- **MapStruct**: Bean映射工具 (v1.4.2.Final)
- **PageHelper**: MyBatis分页插件 (v1.2.5)

### 安全认证

- **Apache Shiro**: 安全框架 (v1.13.0)
- **CAS Client**: 单点登录客户端 (v3.5.0)

### 业务集成组件

#### 恒生业务框架
- **JRES BizFrame**: 操作员中心框架 (v2.1.6)
- **JRES Workflow**: 工作流引擎 (v1.2.230)
- **JRES Scheduler**: 定时任务调度 (v1.1.117)

#### 外部系统接口
- **CCM**: 支付网关接口 (ccm-capitalchannelapi v1.0.14-RELEASE)
- **传真网关**: 传真服务接口 (fax-gateway-api v1.1.0-RELEASE) 
- **结算网关**: 结算服务接口 (finpss-cbsch-api v10.12.0.0-SNAPSHOT)
- **O45投资系统**: 基础服务接口 (basic_service_api vIPS1.0-basicV202501.03.007)
- **OIS**: 场外系统接口 (ois-api vOISV202001.00.000-SNAPSHOT)
