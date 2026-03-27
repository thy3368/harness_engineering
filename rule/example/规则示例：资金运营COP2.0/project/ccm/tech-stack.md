---
description: "AI Coding Rules - 技术栈规范"
globs: *.md,*.java
alwaysApply: false
version: 1.0.0
author: wangxin49245
created: 2025-9-18
lastUpdated: 2025-9-18
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

- **MySQL**: 开源数据库，支持`5.7+`
- **Oracle**: 商业数据库支持，支持`11g+`
- **达梦数据库(DM)**: 国产数据库支持，支持`DM8+`
- **高斯数据库(OpenGauss)**: 华为开源数据库
- **OceanBase**: 阿里分布式数据库，支持`3.2.x`、`4.2.x`
- **TDSQL**: 腾讯分布式数据库

### 消息中间件

- **RabbitMQ**: AMQP协议消息队列
- **东方通HTP**: 国产信创消息中间件 
- **宝兰德MQ**: 国产信创消息中间件

### 缓存与协调

- **Redis**: 分布式缓存和锁服务 (v5.0+)
- **Zookeeper**: 分布式协调服务 (Zookeeper客户端：v3.4.14)

### 限流与监控

- **Bucket4j**: 限流控制库 (v7.0.0)
- **Spring Actuator**: 应用监控和管理

### 序列化与工具

- **Lombok**: 代码简化工具 (v1.18.16)
- **FastJSON**: JSON处理 (v1.2.83)
- **Jackson**: JSON处理 (v2.18.0)
- **XStream**: XML处理 (v1.4.21)
- **Dozer**: Bean映射工具 (v5.5.1)
- **Druid**: 数据库连接池 (v1.1.13)

### 应用服务器支持

- **Undertow**: 默认Web容器
- **宝兰德BES**: 国产信创应用Web容器
- **东方通TongWeb**: 国产信创Web容器

### 日志框架

- **Log4j2**: 日志记录框架 (v2.18.0)

### 单元测试框架

- **JUnit**: 单元测试框架 (v4.12)
- **Spring Boot Test**: 集成测试支持
