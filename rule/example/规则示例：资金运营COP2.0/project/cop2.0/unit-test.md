---
description: "AI Coding Rules - 单元测试规范"
globs: *.md,*.java
alwaysApply: false
version: 1.0.0
author: liangzp35600
created: 2025-9-16
lastUpdated: 2025-9-16
---

# 单元测试规范

## 强制约束

### 1. 测试框架要求

**必须**使用以下技术栈进行单元测试：
- **JUnit**: 4.13.1版本（已配置）
- **Spring Boot Test**: hs.2.2.13.1.RELEASE（已配置）
- **MockMvc**: 用于Controller层测试（已配置）
- **JUnit Assert**: 用于断言验证（**禁止使用AssertJ**）
- **net.sf.json.JSONObject**: JSON处理（**禁止使用com.alibaba.fastjson**）

### 2. 测试目录结构要求

**必须**严格按照以下目录结构组织测试代码：
```
src/test/java/com/hundsun/cop/
├── controller/          # 控制器测试
├── service/            # 服务层测试  
├── dao/               # 数据访问层测试
├── util/              # 工具类测试
├── common/            # 公共组件测试
└── base/              # 基础测试类
```

### 3. 测试类命名规范

**必须**遵循以下命名约定：
- 单元测试类：`[被测类名]Test.java`
- 集成测试类：`[被测类名]IntegrationTest.java`
- 测试方法：`test[功能描述]_[场景描述]_[预期结果]()`

示例：
```java
// 正确命名
UserServiceTest.java
testCreateUser_ValidInput_ReturnsSuccess()

// 错误命名 - 禁止
UserTest.java
testUser()
```

### 4. 测试覆盖率要求

**必须**达到以下测试覆盖率标准：
- **行覆盖率**: 最低80%
- **分支覆盖率**: 最低70%  
- **方法覆盖率**: 最低90%

**关键模块**（交易、支付、风控）**必须**达到90%行覆盖率。

### 5. 基础测试类规范

**必须**继承现有的统一基础测试类：

#### 5.1 所有测试必须继承ControllerTest
**所有测试类**（包括Service测试和Controller测试）**必须**继承现有的`ControllerTest`：

```java
// 现有基础测试类（位于：cop-server/src/test/java/com/hundsun/cop/controller/ControllerTest.java）
@RunWith(SpringRunner.class)
@SpringBootTest
@ContextConfiguration
@Slf4j
public class ControllerTest {
    
    @Autowired
    private WebApplicationContext wac;
    
    protected MockMvc mockMvc;
    protected Cookie cookie;
    protected String operatorNo;
    
    @Autowired
    private UserService userService;
    
    @Before
    public void setup() {
        // 自动认证设置
        Operator operator = userService.login("10101010", "admin@1234", null,
                "192.168.163.105", "PC", null);
        cookie = new Cookie("token", operator.getUser_token());
        operatorNo = String.valueOf(operator.getOperator_no());
    }
    
    // 提供的请求方法
    protected String getFrom(String requestPath, MultiValueMap paramMap) { /* 已实现 */ }
    protected String postTo(String requestPath, MultiValueMap paramMap) { /* 已实现 */ }
    protected String failGet(String requestPath, MultiValueMap paramMap) { /* 已实现 */ }
    protected String failPost(String requestPath, MultiValueMap paramMap) { /* 已实现 */ }
}
```

#### 5.2 测试类继承示例

**Service测试示例**：
```java
@FixMethodOrder(MethodSorters.NAME_ASCENDING)
@Slf4j
public class YourServiceTest extends ControllerTest {
    
    @Autowired
    private YourService yourService;
    
    @Test
    public void test01_YourMethod_ValidInput_ReturnsSuccess() {
        // 测试逻辑
    }
}
```

**Controller测试示例**：
```java
@FixMethodOrder(MethodSorters.NAME_ASCENDING)  
@Slf4j
public class YourControllerTest extends ControllerTest {
    
    @Test
    public void test01_YourEndpoint_ValidRequest_ReturnsSuccess() {
        // 使用继承的getFrom()或postTo()方法
        String result = getFrom("/your/endpoint", params);
    }
}
```

### 6. 测试数据管理规范

#### 6.1 测试数据隔离
**必须**确保测试数据完全隔离：
- **禁止**使用生产数据进行测试
- **必须**使用`@Transactional`和`@Rollback`确保数据回滚
- **必须**使用独立的测试数据库或内存数据库

#### 6.2 测试数据构造
**必须**使用Builder模式构造测试数据：

```java
// 必须提供统一的测试数据构造器
public class TestDataBuilder {
    public static TransferOrder.TransferOrderBuilder validTransferOrder() {
        return TransferOrder.builder()
            .transferNo("TEST_" + System.currentTimeMillis())
            .amount(BigDecimal.valueOf(1000.00))
            .fromAccount("1234567890")
            .toAccount("0987654321")
            .status(TransferStatus.PENDING);
    }
}

// 测试中使用
TransferOrder order = TestDataBuilder.validTransferOrder()
    .amount(BigDecimal.valueOf(2000.00))
    .build();
```

### 7. Mock使用规范

#### 7.1 Mock原则
**必须**遵循以下Mock原则：
- **只Mock依赖**，不Mock被测试的对象
- **外部服务调用**必须Mock
- **数据库操作**在单元测试中必须Mock
- **系统时间、随机数**等不确定因素必须Mock

#### 7.2 Mock示例
```java
@MockBean
private PaymentGatewayService paymentGatewayService;

@MockBean
private NotificationService notificationService;

@Test
public void testTransferMoney_ValidRequest_ReturnsSuccess() {
    // Given - 必须明确定义Mock行为
    when(paymentGatewayService.transfer(any()))
        .thenReturn(PaymentResult.success("TXN123456"));
    when(notificationService.sendNotification(any()))
        .thenReturn(true);
    
    // When - 执行被测试方法
    TransferResult result = transferService.transfer(validTransferRequest());
    
    // Then - 必须验证所有Mock调用
    verify(paymentGatewayService, times(1)).transfer(any());
    verify(notificationService, times(1)).sendNotification(any());
    assertThat(result.isSuccess()).isTrue();
}
```

### 8. 异常测试规范

**必须**为每个方法编写异常场景测试：

```java
@Test(expected = IllegalArgumentException.class)
public void testTransferMoney_NullRequest_ThrowsException() {
    // When & Then
    transferService.transfer(null);
}

@Test
public void testTransferMoney_InsufficientBalance_ReturnsFailure() {
    // Given
    when(accountService.getBalance(anyString()))
        .thenReturn(BigDecimal.ZERO);
    
    // When
    TransferResult result = transferService.transfer(validTransferRequest());
    
    // Then
    assertThat(result.isSuccess()).isFalse();
    assertThat(result.getErrorCode()).isEqualTo("INSUFFICIENT_BALANCE");
}
```

### 9. 断言规范

#### 9.1 断言原则
**必须**遵循以下断言原则：
- **每个测试**必须包含至少一个断言
- **断言消息**必须清晰描述期望结果
- **使用具体值**而非范围断言

#### 9.2 断言示例
```java
// 必须使用JUnit Assert - 正确的断言方式
Assert.assertEquals("金额应该相等", BigDecimal.valueOf(1000.00), result.getAmount());
Assert.assertEquals("状态应该为成功", TransferStatus.SUCCESS, result.getStatus());
Assert.assertNotNull("交易ID不应为空", result.getTransactionId());
Assert.assertTrue("金额应该大于0", result.getAmount().compareTo(BigDecimal.ZERO) > 0);

// 错误的断言方式 - 禁止使用AssertJ
// assertThat(result.getAmount()).isEqualTo(BigDecimal.valueOf(1000.00)); // 禁止
// assertThat(result.getStatus()).isEqualTo(TransferStatus.SUCCESS);     // 禁止
```

### 10. 性能测试规范

**关键方法**必须包含性能测试：

```java
@Test(timeout = 5000) // 必须设置超时时间
public void testTransferMoney_Performance_CompleteWithin5Seconds() {
    // Given
    setupLargeDataSet();
    
    // When
    long startTime = System.currentTimeMillis();
    TransferResult result = transferService.batchTransfer(largeTransferList);
    long endTime = System.currentTimeMillis();
    
    // Then
    assertThat(result.isSuccess()).isTrue();
    assertThat(endTime - startTime).isLessThan(5000L);
}
```

### 11. 测试顺序规范

**必须**使用`@FixMethodOrder`确保测试执行顺序：

```java
@FixMethodOrder(MethodSorters.NAME_ASCENDING)
public class TransferServiceTest {
    
    @Test
    public void test01_CreateTransfer_ValidInput_Success() { /* ... */ }
    
    @Test  
    public void test02_ProcessTransfer_ValidTransfer_Success() { /* ... */ }
    
    @Test
    public void test03_CancelTransfer_ProcessedTransfer_Success() { /* ... */ }
}
```

### 12. 日志测试规范

**必须**验证关键操作的日志记录：

```java
@Test
public void testTransferMoney_Success_LogsCorrectly() {
    // Given
    TestAppender testAppender = new TestAppender();
    Logger logger = (Logger) LoggerFactory.getLogger(TransferService.class);
    logger.addAppender(testAppender);
    
    // When
    transferService.transfer(validTransferRequest());
    
    // Then
    assertThat(testAppender.getMessages())
        .contains("Transfer completed successfully: TXN123456");
}
```

---

## Maven配置要求

### 测试执行配置

**注意**：COP系统的Maven surefire插件默认配置了`<skip>true</skip>`，会跳过所有测试执行。

**运行测试的正确方法**：

#### 方法1：临时运行测试
```bash
# 运行所有测试
mvn test -Dmaven.test.skip=false -f cop-server/pom.xml

# 运行特定测试类
mvn test -Dtest=YourServiceTest -Dmaven.test.skip=false -f cop-server/pom.xml

# 运行特定测试方法
mvn test -Dtest=YourServiceTest#test01_Method -Dmaven.test.skip=false -f cop-server/pom.xml
```

#### 方法2：修改pom.xml配置（长期方案）
如需长期运行测试，修改`cop-server/pom.xml`：
```xml
<plugin>
    <artifactId>maven-surefire-plugin</artifactId>
    <version>${plugin.surefire.version}</version>
    <configuration>
        <skip>false</skip>  <!-- 改为false启用测试 -->
    </configuration>
</plugin>
```

---

## 禁止行为

### 绝对禁止以下行为：

1. **禁止**在测试中使用`System.out.println()`进行调试
2. **禁止**在测试中进行真实的网络请求  
3. **禁止**在测试中操作生产数据库
4. **禁止**编写没有断言的测试方法
5. **禁止**使用`Thread.sleep()`等待异步操作
6. **禁止**在测试中使用硬编码的环境特定配置
7. **禁止**编写相互依赖的测试用例
8. **禁止**忽略测试失败，必须修复后再提交代码
9. **禁止**使用AssertJ断言库（必须使用JUnit Assert）
10. **禁止**使用不存在的类或方法编写测试
