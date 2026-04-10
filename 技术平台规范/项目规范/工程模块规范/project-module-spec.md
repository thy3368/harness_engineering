---
description: "AI Coding Rules - 工程模块规范"
globs: "*.md,*.java,*.go,*.ts,*.gradle,*.xml"
alwaysApply: false
version: 1.0.1
author: 架构办
created: 2025-11-3
lastUpdated: 2025-11-3
---

# 工程模块规范

## 概述

本规范为项目级工程模块设计标准规范，参考 Clean Architecture、Maven/Gradle 模块化最佳实践，规定了模块划分、包结构、依赖管理等方面的要求。

## 模块化原则

### 核心原则

| 原则 | 说明 | 来源 |
|------|------|------|
| **高内聚** | 相关代码放一起 | SRP 原则 |
| **低耦合** | 模块间依赖最小化 | DIP 原则 |
| **可重用** | 模块可独立使用 | 通用原则 |
| **可测试** | 模块可独立测试 | 通用原则 |
| **单一职责** | 每个模块只做一件事 | SOLID |

### 模块划分方法

| 方法 | 说明 | 适用场景 |
|------|------|----------|
| **按功能划分** | 按业务功能组织模块 | 业务系统 |
| **按层次划分** | 按架构层次组织模块 | 分层架构 |
| **按领域划分** | 按业务领域组织模块 | Clean Architecture 系统 |
| **按特性划分** | 按产品特性组织模块 | 多租户系统 |

## 模块结构规范

### 精简模块结构（适配层 + 领域层）

```
project-root/
├── domain/                    # 领域层（微内核）
│   ├── domain-core/         # 核心领域
│   └── domain-{biz}/        # 业务领域：order, payment, account...
├── adapter/                 # 适配层（插件）
│   ├── adapter-api/         # 适配器接口
│   ├── adapter-db/         # 数据库适配器
│   ├── adapter-remote/     # 远程适配器（HTTP, RPC）
│   └── adapter-message/    # 消息适配器
├── api/                     # API 接口定义
├── application/              # 应用层（用例）
├── gateway/                 # 网关
└── web/                     # Web 展示层
```

### 架构图

```
Gateway → Application → Domain（领域层） → Adapter（适配层）
         （用例编排）   （微内核）     （插件可插拔）
```

### 依赖规则

| 规则 | 说明 |
|------|------|
| **领域层不依赖适配层** | 领域定义接口，适配实现接口 |
| **依赖接口而非实现** | 使用 SPI 机制 |
| **适配器可插拔** | 切换实现只需替换适配器 |

### 模块命名

| 类型 | 命名规则 | 示例 |
|------|----------|------|
| **父模块** | `{project}-parent` | `cop-parent` |
| **领域层模块** | | |
| └ 核心领域 | `{project}-domain-core` | `cop-domain-core` |
| └ 业务领域 | `{project}-domain-{name}` | `cop-domain-order` |
| **适配层模块** | | |
| └ 适配器接口 | `{project}-adapter-api` | `cop-adapter-api` |
| └ 数据库适配器 | `{project}-adapter-db` | `cop-adapter-mybatis` |
| └ 远程适配器 | `{project}-adapter-remote` | `cop-adapter-http` |
| └ 消息适配器 | `{project}-adapter-message` | `cop-adapter-kafka` |
| **API 模块** | `{project}-api` | `cop-api` |
| **应用模块** | `{project}-application-{name}` | `cop-application-order` |
| **网关模块** | `{project}-gateway-{name}` | `cop-gateway` |
| **Web 模块** | `{project}-web` | `cop-web` |

### 包结构规范

#### 分层包结构（传统）

```
com.example.project/
├── controller/           # 控制层
│   └── OrderController
├── service/             # 服务层
│   ├── IOrderService
│   └── impl/
├── repository/          # 持久层
│   ├── IOrderRepository
│   └── impl/
├── model/               # 模型
│   ├── entity/
│   ├── dto/
│   └── vo/
└── common/              # 公共
    ├── constants/
    └── util/
```

#### 按功能包结构（推荐）

```
com.example.project/
├── order/                    # 功能模块
│   ├── controller/
│   │   └── OrderController
│   ├── service/
│   │   ├── OrderService
│   │   └── OrderQueryService
│   ├── repository/
│   │   └── OrderRepository
│   ├── model/
│   │   ├── Order
│   │   ├── OrderItem
│   │   └── dto/
│   └── config/
├── user/
│   └── ...
└── common/                   # 共享
    ├── constants/
    └── util/
```

## 模块依赖规范

### 依赖原则

| 原则 | 说明 |
|------|------|
| **单向依赖** | 依赖只能从上往下 |
| **依赖抽象** | 依赖接口而非实现 |
| **无循环依赖** | 模块间不能循环依赖 |
| **最小依赖** | 只依赖必需的模块 |

### 层级依赖关系（适配层 + 领域层）

```
┌─────────────────────────────────────────────────────────────────────┐
│                         接入层 (Gateway)                         │
│                    HTTP / RPC / Message / File                   │
├─────────────────────────────────────────────────────────────────┤
│                       应用层 (Application)                        │
│                    用例编排、事务管理、依赖领域                    │
├─────────────────────────────────────────────────────────────────┤
│                     领域层（微内核 Domain）                       │
│    核心领域 │ 业务领域 │ 领域服务接口 │ 领域事件                 │
│             （只依赖领域接口，无外部依赖）                        │
├─────────────────────────────────────────────────────────────────┤
│                       适配层（插件 Adapter）                      │
│     DB适配器 │ HTTP适配器 │ RPC适配器 │ Kafka适配器             │
│           （实现领域接口，依赖领域层）                          │
└─────────────────────────────────────────────────────────────────────┘
```

### 适配层 + 领域层依赖规则

| 规则 | 说明 |
|------|------|
| **领域层不依赖适配层** | 领域层定义接口，适配层实现接口 |
| **依赖接口而非实现** | 使用 SPI（Service Provider Interface） |
| **适配器可插拔** | 切换数据库/远程服务只需替换适配器 |
| **依赖方向** | 应用层 → 领域层 → 适配层（单向） |

### 依赖示例

```java
// 正确：依赖抽象
public class OrderService {
    private OrderRepository repository;  // 依赖接口
    private PaymentGateway paymentGateway;  // 依赖接口
}

// 错误：依赖具体实现
public class OrderService {
    private JdbcOrderRepository repository;  // 依赖实现
}
```

## 模块类型规范

### 领域层（Domain / 微内核）

#### 核心领域模块

| 规范 | 说明 |
|------|------|
| **内容** | 领域模型（实体、值对象）、领域服务、领域事件、领域服务接口 |
| **依赖** | 无外部依赖，仅依赖领域接口 |
| **命名** | `{project}-domain-core` |
| **特点** | 纯业务逻辑，无技术实现 |

#### 业务领域模块

| 规范 | 说明 |
|------|------|
| **内容** | 业务领域模型、业务规则、领域服务实现 |
| **依赖** | 依赖核心领域模块 |
| **命名** | `{project}-domain-{name}` |
| **特点** | 包含业务领域逻辑，可独立运行 |

#### 领域模型示例

```java
// 领域层 - 核心领域
public class Order {                          // 实体
    private OrderId id;
    private Money totalAmount;
    
    public void addItem(OrderItem item) {       // 领域服务
        // 业务规则校验
    }
}

// 领域层 - 领域服务接口（SPI）
public interface PaymentGateway {
    PaymentResult pay(PaymentRequest request);
}
```

### 适配层（Adapter / 插件）

#### 适配器接口模块

| 规范 | 说明 |
|------|------|
| **内容** | 适配器接口定义（SPI） |
| **依赖** | 只依赖领域层接口 |
| **命名** | `{project}-adapter-api` |
| **特点** | 定义适配器接口，无实现 |

#### 数据库适配器

| 规范 | 说明 |
|------|------|
| **内容** | 数据库持久化实现（MyBatis、JPA） |
| **依赖** | 依赖适配器接口、领域层 |
| **命名** | `{project}-adapter-db` |
| **特点** | 实现仓库接口，可插拔 |

#### 远程服务适配器

| 规范 | 说明 |
|------|------|
| **内容** | HTTP、RPC 等远程调用实现 |
| **依赖** | 依赖适配器接口、领域层 |
| **命名** | `{project}-adapter-remote` |
| **特点** | 实现远程服务接口 |

#### 适配器示例

```java
// 适配层 - 适配器接口（SPI）
public interface OrderRepository {
    Optional<Order> findById(OrderId id);
    void save(Order order);
}

// 适配层 - MyBatis 实现
@Repository
public class MybatisOrderRepository implements OrderRepository {
    // 实现数据库操作
}

// 适配层 - HTTP 远程适配器
@Component
public class RemotePaymentAdapter implements PaymentGateway {
    // 实现远程调用
}
```

### API 模块

| 规范 | 说明 |
|------|------|
| **内容** | 存放接口定义、DTO、枚举 |
| **依赖** | 只依赖其他 API 模块 |
| **命名** | `{project}-api` |
| **特点** | 无业务逻辑，仅定义 |

### 核心模块

| 规范 | 说明 |
|------|------|
| **内容** | 领域模型、领域服务、业务逻辑 |
| **依赖** | 依赖 API 模块 |
| **命名** | `{project}-core` |
| **特点** | 包含核心业务，无外部依赖 |

### 服务模块

| 规范 | 说明 |
|------|------|
| **内容** | 应用服务、事务管理 |
| **依赖** | 依赖核心模块、API 模块 |
| **命名** | `{project}-service-{name}` |
| **特点** | 对外提供服务，协调核心模块 |

### 网关模块

| 规范 | 说明 |
|------|------|
| **内容** | HTTP 入口、鉴权、限流 |
| **依赖** | 依赖服务模块 |
| **命名** | `{project}-gateway` |
| **特点** | 处理请求路由、协议转换 |

## 模块设计模式

### 门面模式

```java
// 模块对外暴露的统一入口
public class OrderFacade {
    private OrderService orderService;
    private PaymentService paymentService;
    
    public CreateOrderResult createOrder(CreateOrderRequest request) {
        // 协调多个服务
        orderService.validate(request);
        PaymentResult payment = paymentService.pay(request);
        return orderService.create(request, payment);
    }
}
```

### 策略模式

```java
// 不同支付方式作为策略
public interface PaymentStrategy {
    PaymentResult pay(PaymentRequest request);
}

@Component
public class AlipayStrategy implements PaymentStrategy { }
@Component
public class WechatPayStrategy implements PaymentStrategy { }
```

### 工厂模式

```java
// 统一创建入口
public interface OrderFactory {
    Order createOrder(OrderRequest request);
}

@Component
public class StandardOrderFactory implements OrderFactory { }
```

## Maven/Gradle 规范

### POM 结构

```xml
<project>
    <groupId>com.example</groupId>
    <artifactId>cop-parent</artifactId>
    <version>1.0.0</version>
    <packaging>pom</packaging>
    
    <modules>
        <module>cop-api</module>
        <module>cop-core</module>
        <module>cop-service-order</module>
        <module>cop-web</module>
    </modules>
</project>
```

### 依赖管理

```xml
<!-- 父 POM 统一管理版本 -->
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-dependencies</artifactId>
            <version>${spring-boot.version}</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
```

### 依赖原则

| 原则 | 说明 |
|------|------|
| **版本统一** | 父 POM 管理版本 |
| **scope 正确** | test 依赖用 `<scope>test</scope>` |
| **可选依赖** | 使用 `<optional>true</optional>` 标记可选依赖 |
| **排除传递** | 谨慎使用 `<exclusions>` |

## 多模块构建规范

### 构建配置

```yaml
# CI/CD 多模块构建
stages:
  - build
  
build:
  script:
    - mvn clean package -DskipTests
  artifacts:
    paths:
      - */target/*.jar
```

### 构建顺序

| 顺序 | 模块 | 原因 |
|------|------|------|
| 1 | API 模块 | 被其他模块依赖 |
| 2 | Core 模块 | 包含核心逻辑 |
| 3 | Service 模块 | 依赖 Core |
| 4 | Gateway/Web 模块 | 依赖 Service |

## 模块设计检查清单

### 结构检查

| 检查项 | 说明 |
|--------|------|
| 模块划分清晰 | 按功能/领域/层次划分明确 |
| 包结构规范 | 按推荐方式组织包 |
| 命名统一 | 遵循命名规范 |

### 依赖检查

| 检查项 | 说明 |
|--------|------|
| 依赖方向正确 | 只能上层依赖下层 |
| 无循环依赖 | 模块间无循环 |
| 依赖最小化 | 只依赖必需的 |

### 可维护性检查

| 检查项 | 说明 |
|--------|------|
| 模块可独立构建 | mvn install 单独构建通过 |
| 模块可独立测试 | 单元测试独立运行 |
| 文档完整 | README 说明模块职责 |

## 版本历史

| 版本 | 日期 | 修改内容 | 作者 |
|------|------|----------|------|
| 1.0.1 | 2025-11-3 | 初始版本，参考 Clean Architecture | 架构办 |
