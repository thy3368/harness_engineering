---
description: "AI Coding Rules - Spring Boot规范"
globs: *.md,*.java
alwaysApply: false
version: 1.0.1
author: wangxin49245
created: 2025-9-17
lastUpdated: 2025-11-3
---

# Spring Boot规范

## 约束等级
- `【强制】` - 违反将被认为代码存在严重缺陷，团队必须遵守
- `【推荐】` - 违反将被认为代码存在轻微缺陷，根据具体产品特性选择性遵守  
- `【参考】` - 违反可被认为代码存在优化空间，从持续优化角度参考使用

## 编码原则
- `【推荐】` 遵循Spring Boot最佳实践，包括但不限于：
  - 约定优于配置：充分利用Spring Boot的自动配置机制
  - 单一职责原则：每个组件只负责一个明确的职责
  - 依赖注入：优先使用构造器注入，避免字段注入
  - 分层架构：严格按照Controller、Service、Mapper/DAO分层
  - 统一异常处理：使用@ControllerAdvice全局异常处理
  - 配置外部化：使用application.properties/application.yml管理配置
  - 健康检查：实现Actuator端点监控应用状态
  - 日志规范：统一使用SLF4J进行日志记录

## 项目结构规范

### 包结构组织

| **包名** | **用途** | **示例** | **说明** |
|---------|----------|----------|----------|
| controller | REST接口控制器 | com.example.controller | 处理HTTP请求响应 |
| service | 业务逻辑服务层 | com.example.service | 核心业务逻辑处理 |
| mapper | MyBatis接口层 | com.example.mapper | MyBatis数据访问接口 |
| dao | 数据访问对象层 | com.example.dao | 复杂查询和数据访问逻辑 |
| entity/domain | 实体类 | com.example.entity | 数据库实体或领域对象 |
| dto | 数据传输对象 | com.example.dto | 接口传输对象 |
| vo | 视图对象 | com.example.vo | 前端展示对象 |
| config | 配置类 | com.example.config | Spring配置类 |
| common | 通用组件 | com.example.common | 工具类、常量等 |
| exception | 异常处理 | com.example.exception | 自定义异常类 |

### 文件命名规范
- `【强制】` Controller类以Controller结尾，如UserController
- `【强制】` Service接口以Service结尾，实现类以ServiceImpl结尾
- `【强制】` Mapper接口以Mapper结尾，如UserMapper
- `【推荐】` DAO类以DAO结尾，如UserDAO
- `【强制】` 配置类以Config结尾，如DatabaseConfig
- `【强制】` 异常类以Exception结尾，如BusinessException
- `【推荐】` DTO类以DTO/Request/Response结尾
- `【推荐】` VO类以VO结尾，如UserVO

## 注解使用规范

### Spring核心注解

| **注解** | **使用场景** | **约束等级** | **说明** |
|---------|-------------|-------------|----------|
| @SpringBootApplication | 主启动类 | 【强制】 | 仅用于主启动类 |
| @RestController | REST控制器 | 【推荐】 | 组合@Controller+@ResponseBody |
| @Controller | MVC控制器 | 【推荐】 | 传统MVC模式使用 |
| @Service | 业务服务层 | 【强制】 | 标识业务逻辑组件 |
| @Repository | 数据访问层 | 【推荐】 | 标识Mapper或DAO组件 |
| @Component | 通用组件 | 【推荐】 | 其他Spring管理的Bean |
| @Configuration | 配置类 | 【强制】 | Java配置类 |
| @Autowired | 依赖注入 | 【参考】 | 推荐构造器注入 |

### 注解使用规则
- `【强制】` 每个类只能使用一个主要的Spring组件注解
- `【强制】` @Autowired优先使用构造器注入，避免字段注入
- `【推荐】` 使用@RequiredArgsConstructor代替@Autowired构造器注入
- `【强制】` @Transactional注解应在Service层使用，不在Controller层使用
- `【推荐】` 使用@Valid/@Validated进行参数校验
- `【强制】` @RequestMapping指定具体的HTTP方法，如@GetMapping、@PostMapping
- `【强制】` 禁止使用@PutMapping、@PatchMapping、@DeleteMapping

## 依赖注入规范

### 注入方式优先级
1. `【推荐】` 构造器注入（强制依赖）
2. `【参考】` Setter注入（可选依赖）
3. `【避免】` 字段注入（降低测试性）

### 构造器注入示例
```java
@Service
@RequiredArgsConstructor
public class UserService {
    private final UserMapper userMapper;
    private final EmailService emailService;
    
    // Spring会自动注入依赖
}
```

### 注入规则
- `【强制】` 必需的依赖使用构造器注入
- `【推荐】` 使用Lombok的@RequiredArgsConstructor简化构造器
- `【强制】` 避免循环依赖，通过重构或@Lazy解决
- `【推荐】` 接口依赖而非具体实现类
- `【强制】` 不要在配置类中进行复杂的业务逻辑处理

## Controller层规范

### REST接口设计

| **HTTP方法** | **用途** | **URL示例** | **说明** |
|-------------|----------|-------------|----------|
| GET | 查询资源 | GET /api/users | 获取用户列表 |
| POST | 创建资源 | POST /api/users | 创建新用户 |

### Controller编码规范
- `【强制】` 控制器只负责请求响应处理，不包含业务逻辑
- `【强制】` 使用@Valid进行参数校验
- `【强制】` 统一返回结果格式，使用ResponseEntity或自定义Result
- `【推荐】` 使用@PathVariable接收路径参数
- `【推荐】` 使用@RequestParam接收查询参数
- `【强制】` 异常处理委托给@ControllerAdvice
- `【推荐】` 接口文档使用Swagger/OpenAPI注解
- `【强制】` 禁止使用PUT、PATCH、DELETE方法，仅使用GET和POST
- `【强制】` 增删改操作统一使用POST方法，通过URL路径或参数区分操作类型

```java
@RestController
@RequestMapping("/api/users")
@RequiredArgsConstructor
@Validated
public class UserController {
    
    private final UserService userService;
    
    @GetMapping("/{id}")
    public ResponseEntity<UserVO> getUser(@PathVariable @Min(1) Long id) {
        UserVO user = userService.getUserById(id);
        return ResponseEntity.ok(user);
    }
    
    @PostMapping("/create")
    public ResponseEntity<UserVO> createUser(@Valid @RequestBody UserCreateRequest request) {
        UserVO user = userService.createUser(request);
        return ResponseEntity.status(HttpStatus.CREATED).body(user);
    }

}
```

## Service层规范

### 业务逻辑处理
- `【强制】` Service层包含主要的业务逻辑
- `【强制】` 使用@Transactional管理事务
- `【推荐】` 接口与实现分离，面向接口编程
- `【强制】` 不直接返回Entity对象，转换为DTO/VO
- `【推荐】` 复杂业务逻辑拆分为多个私有方法
- `【强制】` 异常处理要明确具体的业务异常

```java
@Service
@RequiredArgsConstructor
@Transactional(readOnly = true)
public class UserServiceImpl implements UserService {
    
    private final UserMapper userMapper;
    private final UserDAO userDAO; // 可选，复杂查询情况下使用
    
    @Override
    public UserVO getUserById(Long id) {
        User user = userMapper.selectById(id);
        if (user == null) {
            throw new UserNotFoundException("用户不存在: " + id);
        }
        return UserConverter.toVO(user);
    }
    
    @Override
    @Transactional
    public UserVO createUser(UserCreateRequest request) {
        User user = UserConverter.toEntity(request);
        userMapper.insert(user);
        return UserConverter.toVO(user);
    }

}
```

### 事务管理规范
- `【强制】` 在Service层使用@Transactional注解
- `【推荐】` 只读操作使用@Transactional(readOnly = true)
- `【强制】` 指定事务传播行为和隔离级别
- `【推荐】` 使用rollbackFor指定回滚异常类型
- `【强制】` 避免在事务方法中调用外部服务

## 数据访问层规范

### 分层职责划分

| **层级** | **职责** | **说明** | **示例** |
|---------|----------|----------|----------|
| Mapper层 | 基础数据访问 | 单表CRUD、简单查询 | UserMapper.selectByEmail() |
| DAO层 | 复杂数据访问 | 多表关联、复杂业务查询 | UserDAO.selectByConditions() |

### 使用场景选择
- `【推荐】` 简单项目：仅使用Mapper层即可满足需求
- `【推荐】` 复杂项目：Mapper层 + DAO层，DAO层封装复杂查询逻辑
- `【强制】` 禁止跨层调用，Service层统一调用数据访问层

## Mapper层规范

### MyBatis Mapper使用
- `【强制】` 使用@Mapper注解标识Mapper接口
- `【推荐】` 使用@Repository注解增强可读性
- `【推荐】` 优先使用XML映射文件进行SQL配置，提高可维护性
- `【参考】` 简单查询可使用注解方式，但不推荐
- `【推荐】` 分页查询使用PageHelper的Page参数

```java
@Mapper
@Repository
public interface UserMapper extends BaseMapper<User> {
    
    // 推荐使用XML映射文件配置SQL
    User selectByEmail(String email);
    
    List<User> selectByConditions(UserQueryCondition condition);
}
```

**对应的XML映射文件 UserMapper.xml:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.example.mapper.UserMapper">
    
    <!-- 基础查询 -->
    <select id="selectByEmail" parameterType="string" resultType="User">
        SELECT * FROM user WHERE email = #{email}
    </select>
    
    <!-- 复杂查询 -->
    <select id="selectByConditions" parameterType="UserQueryCondition" resultType="User">
        SELECT * FROM user
        <where>
            <if test="condition.name != null and condition.name != ''">
                AND name LIKE CONCAT('%', #{condition.name}, '%')
            </if>
            <if test="condition.status != null">
                AND status = #{condition.status}
            </if>
        </where>
        ORDER BY create_time DESC
    </select>
    
</mapper>
```

### DAO层规范

#### DAO层职责
- `【推荐】` DAO层处理复杂的数据访问逻辑
- `【推荐】` 封装多表关联查询和复杂业务查询
- `【推荐】` 提供统一的数据访问封装和异常处理
- `【强制】` DAO层不包含业务逻辑，只负责数据访问

```java
@Component
@RequiredArgsConstructor
public class UserDAO {
    
    private final UserMapper userMapper;
    
    /**
     * 根据条件查询用户列表
     */
    public List<User> findUsersByCondition(UserQueryCondition condition) {
        return userMapper.selectByConditions(condition);
    }
    
}
```

### 数据访问规范
- `【强制】` Mapper接口不包含业务逻辑
- `【推荐】` 使用Optional包装可能为空的查询结果
- `【强制】` 批量操作使用@Transactional注解
- `【推荐】` 使用@DS注解切换数据源（多数据源情况下）
- `【强制】` 避免在Mapper中使用@Transactional

## 配置管理规范

### 配置文件结构

| **文件** | **用途** | **优先级** | **说明** |
|---------|----------|----------|----------|
| application.properties | 主配置文件 | 推荐 | 通用配置，主流格式 |
| application.yml | 主配置文件 | 可选 | 部分项目使用 |

### 配置规范
- `【强制】` 敏感信息使用环境变量或配置中心
- `【推荐】` 使用@ConfigurationProperties绑定配置
- `【推荐】` 配置项使用点分隔命名方式
- `【推荐】` 为自定义配置类提供默认值

## 异常处理规范

### 异常体系设计

| **异常类型** | **基类** | **使用场景** | **HTTP状态码** |
|-------------|----------|-------------|---------------|
| 业务异常 | BusinessException | 业务规则违反 | 400 Bad Request |
| 资源未找到 | ResourceNotFoundException | 资源不存在 | 404 Not Found |
| 参数校验异常 | ValidationException | 参数验证失败 | 400 Bad Request |
| 权限异常 | PermissionException | 权限不足 | 403 Forbidden |
| 系统异常 | SystemException | 系统内部错误 | 500 Internal Error |

### 全局异常处理
```java
@ControllerAdvice
@Slf4j
public class GlobalExceptionHandler {
    
    @ExceptionHandler(BusinessException.class)
    public ResponseEntity<ErrorResponse> handleBusinessException(BusinessException e) {
        log.warn("业务异常: {}", e.getMessage());
        ErrorResponse error = ErrorResponse.builder()
            .code("BUSINESS_ERROR")
            .message(e.getMessage())
            .timestamp(LocalDateTime.now())
            .build();
        return ResponseEntity.badRequest().body(error);
    }
    
    @ExceptionHandler(Exception.class)
    public ResponseEntity<ErrorResponse> handleSystemException(Exception e) {
        log.error("系统异常", e);
        ErrorResponse error = ErrorResponse.builder()
            .code("SYSTEM_ERROR")
            .message("系统内部错误")
            .timestamp(LocalDateTime.now())
            .build();
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(error);
    }
}
```

## 数据校验规范

### 校验注解使用

| **注解** | **用途** | **示例** | **说明** |
|---------|----------|----------|----------|
| @NotNull | 非空校验 | @NotNull String name | 不能为null |
| @NotEmpty | 非空集合 | @NotEmpty List<String> items | 集合不能为空 |
| @NotBlank | 非空字符串 | @NotBlank String email | 字符串不能为空白 |
| @Size | 长度校验 | @Size(min=2, max=50) String name | 长度范围 |
| @Min/@Max | 数值范围 | @Min(0) @Max(120) Integer age | 数值范围 |
| @Email | 邮箱格式 | @Email String email | 邮箱格式校验 |
| @Pattern | 正则校验 | @Pattern(regexp="^1[3-9]\\d{9}$") | 正则表达式 |
| @Valid | 嵌套校验 | @Valid UserAddress address | 嵌套对象校验 |

### 校验规范
- `【强制】` 在Controller层使用@Valid进行参数校验
- `【推荐】` 在Service层使用@Validated进行方法级校验
- `【强制】` 自定义校验注解要提供清晰的错误信息
- `【推荐】` 分组校验用于不同场景的参数校验
- `【强制】` 校验失败要返回具体的错误信息