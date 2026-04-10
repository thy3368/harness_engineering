---
description: "AI Coding Rules - Java 单元测试规范"
globs: "*.java"
alwaysApply: false
version: 1.0.1
author: 架构办
created: 2025-11-3
lastUpdated: 2025-11-3
---

# Java 单元测试规范

## 概述

本规范为 Java 项目单元测试的标准规范，规定了测试框架、测试结构、测试编写等方面的要求。

详见 [单元测试规范](unit-test-spec2.md)

## 测试框架要求

### 技术栈

| 框架 | 版本 | 说明 |
|------|------|------|
| JUnit | 4.12+ | 单元测试框架 |
| JUnit 5 | 5.x | 可选新一代测试框架 |
| Spring Boot Test | 2.7.x | Spring Boot 测试支持 |
| Mockito | 3.x+ | Mock 框架 |
| AssertJ | 3.x+ | 断言库（推荐） |

### Maven 依赖

```xml
<dependency>
    <groupId>junit</groupId>
    <artifactId>junit</artifactId>
    <version>4.13.2</version>
    <scope>test</scope>
</dependency>

<dependency>
    <groupId>org.mockito</groupId>
    <artifactId>mockito-core</artifactId>
    <version>4.11.0</version>
    <scope>test</scope>
</dependency>

<dependency>
    <groupId>org.assertj</groupId>
    <artifactId>assertj-core</artifactId>
    <version>3.24.2</version>
    <scope>test</scope>
</dependency>
```

详见 [单元测试规范 - 测试框架要求](unit-test-spec2.md#1-测试框架要求)

## 测试目录结构

### 标准目录

| 目录 | 说明 |
|------|------|
| `src/test/java/` | 测试代码根目录 |
| `src/test/resources/` | 测试资源目录 |

### 包结构规范

| 规则 | 说明 |
|------|------|
| **强制** | 测试类包路径与被测类一致 |
| **强制** | 测试类放在 test 包下对应位置 |
| **强制** | 测试资源文件与被测代码分离 |

### 目录示例

```
src/test/java/com/example/project/
├── service/
│   └── UserServiceTest.java
├── repository/
│   └── UserRepositoryTest.java
├── controller/
│   └── UserControllerTest.java
└── util/
    └── DateUtilTest.java
```

## 测试类命名规范

### 命名规则

| 类型 | 规则 | 示例 |
|------|------|------|
| 测试类 | `[被测类名]Test` | `UserServiceTest` |
| 测试类 | `[被测类名]Tests`（JUnit5） | `UserServiceTests` |
| 基类 | `[被测类名]TestBase` | `UserServiceTestBase` |
| 参数化测试 | `[被测类名]ParamTest` | `UserServiceParamTest` |

### 测试方法命名

| 规则 | 说明 |
|------|------|
| **强制** | 使用 `test` 前缀或 JUnit 5 的 `@Test` 注解 |
| **强制** | 方法名描述测试场景 |
| **推荐** | 使用 `test[场景]_[预期结果]` 格式 |

### 方法命名示例

```java
// JUnit 4
public void testSave_UserIsValid_ReturnsSuccess()
public void testSave_UserIsNull_ThrowsException()
public void testFindById_UserExists_ReturnsUser()
public void testFindById_UserNotExists_ReturnsNull()

// JUnit 5
void save_WithValidUser_ReturnsSuccess()
void save_WithNullUser_ThrowsException()
void findById_WithExistingId_ReturnsUser()
void findById_WithNonExistingId_ReturnsNull()
```

详见 [单元测试规范 - 测试类命名规范](unit-test-spec2.md#3-测试类命名规范)

## 测试注解规范

### JUnit 4 标准注解

```java
@Slf4j
@SpringBootTest
@RunWith(SpringRunner.class)
public class UserServiceTest {
    
    @Autowired
    private UserService userService;
    
    @Before
    public void setUp() {
        log.info("测试开始");
    }
    
    @After
    public void tearDown() {
        log.info("测试结束");
    }
    
    @Test
    public void testSave() {
        // 测试逻辑
    }
}
```

### JUnit 5 标准注解

```java
@ExtendWith(SpringExtension.class)
@SpringBootTest
class UserServiceTest {
    
    @Autowired
    private UserService userService;
    
    @BeforeEach
    void setUp() {
        // 初始化逻辑
    }
    
    @AfterEach
    void tearDown() {
        // 清理逻辑
    }
    
    @Test
    void save_WithValidUser_ReturnsSuccess() {
        // 测试逻辑
    }
}
```

### 常用注解

| 注解 | 说明 |
|------|------|
| `@Test` | 标记测试方法 |
| `@Before` | 每个测试方法前执行（JUnit 4） |
| `@After` | 每个测试方法后执行（JUnit 4） |
| `@BeforeEach` | 每个测试方法前执行（JUnit 5） |
| `@AfterEach` | 每个测试方法后执行（JUnit 5） |
| `@BeforeAll` | 所有测试方法前执行一次 |
| `@AfterAll` | 所有测试方法后执行一次 |
| `@Disabled` | 禁用测试 |
| `@Tag` | 测试分组标记 |
| `@ParameterizedTest` | 参数化测试 |

详见 [单元测试规范 - 基础测试类规范](unit-test-spec2.md#4-基础测试类规范)

## 测试数据管理

### 数据构造方法

| 规则 | 说明 |
|------|------|
| **强制** | 使用工厂方法构造测试数据 |
| **强制** | 测试数据应具有代表性 |
| **强制** | 使用日期时间戳生成唯一标识 |
| **强制** | 测试数据与生产数据隔离 |

### 数据构造示例

```java
public class UserServiceTest {
    
    // 工厂方法
    public static User createValidUser() {
        User user = new User();
        user.setId(1L);
        user.setUsername("testuser");
        user.setEmail("test@example.com");
        user.setStatus(UserStatus.ACTIVE);
        return user;
    }
    
    public static User createUserWithNullEmail() {
        User user = createValidUser();
        user.setEmail(null);
        return user;
    }
    
    public static List<User> createUserList(int size) {
        List<User> users = new ArrayList<>();
        for (int i = 0; i < size; i++) {
            User user = createValidUser();
            user.setId((long) i);
            user.setUsername("user" + i);
            users.add(user);
        }
        return users;
    }
}
```

### 测试数据原则

| 规则 | 说明 |
|------|------|
| **强制** | 每个测试方法独立准备数据 |
| **强制** | 测试后清理数据 |
| **强制** | 不依赖测试执行顺序 |
| **推荐** | 使用 `@Transactional` 确保测试后回滚 |

详见 [单元测试规范 - 测试数据管理规范](unit-test-spec2.md#5-测试数据管理规范)

## Mock 使用规范

### Mockito 常用方法

| 方法 | 说明 |
|------|------|
| `@Mock` | 创建 Mock 对象 |
| `@MockBean` | 创建 Spring 管理的 Mock Bean |
| `@InjectMocks` | 注入 Mock 对象 |
| `when()` | 设置 Mock 行为 |
| `thenReturn()` | 设置返回值 |
| `verify()` | 验证调用 |
| `times()` | 验证调用次数 |
| `never()` | 验证从未调用 |
| `atLeast()` | 验证至少调用次数 |

### Mock 示例

```java
@ExtendWith(MockitoExtension.class)
class UserServiceTest {
    
    @Mock
    private UserRepository userRepository;
    
    @Mock
    private EmailService emailService;
    
    @InjectMocks
    private UserService userService;
    
    @Test
    void save_WithValidUser_CallsRepositoryAndSendsEmail() {
        // Given
        User user = createValidUser();
        when(userRepository.save(any(User.class))).thenReturn(user);
        doNothing().when(emailService).sendWelcomeEmail(anyString());
        
        // When
        User result = userService.save(user);
        
        // Then
        assertNotNull(result);
        verify(userRepository, times(1)).save(user);
        verify(emailService, times(1)).sendWelcomeEmail(user.getEmail());
    }
}
```

### Spring Boot 测试 Mock

```java
@SpringBootTest
class UserControllerTest {
    
    @MockBean
    private UserService userService;
    
    @Autowired
    private MockMvc mockMvc;
    
    @Test
    void getUser_WithExistingId_ReturnsUser() throws Exception {
        // Given
        User user = createValidUser();
        when(userService.findById(1L)).thenReturn(user);
        
        // When & Then
        mockMvc.perform(get("/users/1"))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.id").value(1))
            .andExpect(jsonPath("$.username").value("testuser"));
    }
}
```

详见 [单元测试规范 - Mock使用规范](unit-test-spec2.md#6-mock使用规范)

## 断言规范

### AssertJ 断言

| 断言 | 说明 |
|------|------|
| `assertThat(obj).isEqualTo(expected)` | 相等断言 |
| `assertThat(obj).isNotNull()` | 非空断言 |
| `assertThat(obj).isNull()` | 空断言 |
| `assertThat(list).hasSize(size)` | 集合大小断言 |
| `assertThat(list).isEmpty()` | 空集合断言 |
| `assertThat(list).isNotEmpty()` | 非空集合断言 |
| `assertThatThrownBy(() -> {...}).isInstanceOf(Exception.class)` | 异常断言 |

### 断言示例

```java
// 基本断言
assertThat(user.getId()).isEqualTo(1L);
assertThat(user.getUsername()).isEqualTo("testuser");
assertThat(user.getEmail()).isNotNull();

// 布尔断言
assertThat(user.isActive()).isTrue();
assertThat(user.isDeleted()).isFalse();

// 集合断言
assertThat(users).hasSize(10);
assertThat(users).contains(user1, user2);
assertThat(users).doesNotContain(deletedUser);
assertThat(users).allMatch(u -> u.getStatus() == UserStatus.ACTIVE);

// 异常断言
assertThatThrownBy(() -> userService.save(null))
    .isInstanceOf(IllegalArgumentException.class)
    .hasMessageContaining("User cannot be null");

// 软断言（多个断言同时检查）
assertSoftly(softly -> {
    softly.assertThat(user.getId()).isEqualTo(1L);
    softly.assertThat(user.getUsername()).isEqualTo("testuser");
    softly.assertThat(user.getEmail()).isNotNull();
});
```

### JUnit 断言

```java
// 基本断言
Assert.assertEquals("期望值", actualValue);
Assert.assertNotNull(object);
Assert.assertTrue(condition);
Assert.assertFalse(condition);

// 集合断言
Assert.assertFalse(list.isEmpty());
Assert.assertEquals(2, list.size());

// 异常断言（JUnit 4）
@Test(expected = IllegalArgumentException.class)
public void testSave_NullUser_ThrowsException() {
    userService.save(null);
}

// 异常断言（JUnit 5）
assertThrows(IllegalArgumentException.class, () -> userService.save(null));
```

详见 [单元测试规范 - 断言规范](unit-test-spec2.md#8-断言规范)

## 测试分类

### 单元测试

| 规则 | 说明 |
|------|------|
| **强制** | 测试单个类或方法 |
| **强制** | 使用 Mock 隔离依赖 |
| **强制** | 快速执行（毫秒级） |
| **强制** | 无外部依赖（数据库、网络） |

### 集成测试

| 规则 | 说明 |
|------|------|
| **强制** | 测试多个组件交互 |
| **强制** | 可使用内存数据库 |
| **强制** | 需要 Spring 上下文 |
| **推荐** | 使用 `@SpringBootTest` |

### Web 层测试

```java
@WebMvcTest(UserController.class)
class UserControllerTest {
    
    @Autowired
    private MockMvc mockMvc;
    
    @MockBean
    private UserService userService;
    
    @Test
    void getUser_ReturnsJson() throws Exception {
        mockMvc.perform(get("/api/users/1"))
            .andExpect(status().isOk())
            .andExpect(content().contentType(MediaType.APPLICATION_JSON))
            .andExpect(jsonPath("$.id").value(1));
    }
}
```

### 数据层测试

```java
@DataJpaTest
class UserRepositoryTest {
    
    @Autowired
    private TestEntityManager entityManager;
    
    @Autowired
    private UserRepository userRepository;
    
    @Test
    void findByEmail_WhenUserExists_ReturnsUser() {
        // Given
        User user = createValidUser();
        entityManager.persist(user);
        
        // When
        Optional<User> result = userRepository.findByEmail("test@example.com");
        
        // Then
        assertThat(result).isPresent();
        assertThat(result.get().getUsername()).isEqualTo("testuser");
    }
}
```

## 异常测试规范

| 规则 | 说明 |
|------|------|
| **强制** | 为每个关键方法编写异常测试 |
| **强制** | 测试边界条件 |
| **强制** | 测试非法输入 |
| **强制** | 验证异常消息 |

### 异常测试示例

```java
@Test
void save_WithNullUser_ThrowsIllegalArgumentException() {
    assertThrows(IllegalArgumentException.class, () -> userService.save(null));
}

@Test
void save_WithNullUser_ThrowsExceptionWithMessage() {
    IllegalArgumentException exception = assertThrows(
        IllegalArgumentException.class, 
        () -> userService.save(null)
    );
    assertThat(exception.getMessage()).contains("User cannot be null");
}

@Test
void save_WithDuplicateEmail_ThrowsBusinessException() {
    // Given
    User existingUser = createValidUser();
    userService.save(existingUser);
    
    User duplicateUser = createValidUser();
    duplicateUser.setId(null);
    
    // When & Then
    BusinessException exception = assertThrows(
        BusinessException.class, 
        () -> userService.save(duplicateUser)
    );
    assertThat(exception.getCode()).isEqualTo(ErrorCode.DUPLICATE_EMAIL);
}
```

详见 [单元测试规范 - 异常测试规范](unit-test-spec2.md#7-异常测试规范)

## 性能测试规范

### 超时测试

```java
@Test(timeout = 5000)  // 5秒超时
void processBatch_With1000Items_CompletesInTime() {
    List<Item> items = createItems(1000);
    
    long startTime = System.currentTimeMillis();
    processor.processBatch(items);
    long duration = System.currentTimeMillis() - startTime;
    
    assertThat(duration).isLessThan(5000);
}
```

### 性能基准测试

```java
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@Benchmark
public void benchmarkSaveOperation() {
    User user = createValidUser();
    userService.save(user);
}
```

详见 [单元测试规范 - 性能测试规范](unit-test-spec2.md#10-性能测试规范)

## 禁止行为

| 规则 | 说明 |
|------|------|
| **禁止** | 在测试中使用生产环境数据 |
| **禁止** | 在测试中进行真实的网络通信 |
| **禁止** | 在测试中操作生产数据库 |
| **禁止** | 编写没有断言的测试方法 |
| **禁止** | 使用 `Thread.sleep()` 等待异步操作 |
| **禁止** | 在测试中使用硬编码的生产配置 |
| **禁止** | 编写相互依赖的测试用例 |
| **禁止** | 忽略测试失败 |
| **禁止** | 测试方法中包含业务逻辑代码 |

详见 [单元测试通用规范 - 禁止行为](./unit-test-spec.md#禁止行为)

## 版本历史

| 版本 | 日期 | 修改内容 | 作者 |
|------|------|----------|------|
| 1.0.1 | 2025-11-3 | 初始版本，引用单元测试通用规范 | 架构办 |

---

> 更多通用规范请参阅：[单元测试通用规范](./unit-test-spec.md)
