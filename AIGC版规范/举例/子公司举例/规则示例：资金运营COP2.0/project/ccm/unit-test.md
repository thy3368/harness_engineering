---
description: "AI Coding Rules - 单元测试规范"
globs: *.md,*.java
alwaysApply: false
version: 1.0.0
author: liulm50695
created: 2025-09-19
lastUpdated: 2025-09-19
---

# CCM单元测试规范

## 强制约束

### 1. 测试框架要求

**必须**使用以下技术栈进行单元测试：
- **JUnit**: 4.12版本（已配置）
- **Spring Boot Test**: 2.7.18版本（通过JResCloud集成）
- **Spring Test**: 用于集成测试（已配置）
- **JUnit Assert**: 用于断言验证（**推荐使用**）
- **Lombok**: @Slf4j用于日志记录
- **FastJSON**: com.alibaba.fastjson.JSON用于JSON处理
- **XStream**: 用于XML序列化处理

### 2. 测试目录结构要求

**必须**严格按照以下目录结构组织测试代码：
```
src/test/java/com/hundsun/ccm/fundtransfer/
├── [银行代码]/                    # 按银行分类的测试
│   ├── service/                   # 银行特定服务测试
│   │   └── MoneyOrderServiceTest.java
│   └── [bank_code]rec/           # 银行报文处理测试
│       └── [Bank]SendTest.java
├── integration/                   # 集成模块测试
│   └── stragy/                   # 策略模块测试
│       └── BankLimiterStrategyManagerTest.java
├── test/                         # 通用测试工具
│   └── DozerMapperTest.java
└── [其他银行目录]/
    ├── service/
    └── [bank_code]rec/
```

**银行代码目录示例**：
- `Icbc/` - 工商银行
- `abc/` - 农业银行
- `ccb/` - 建设银行
- `boc/` - 中国银行
- `cmb/` - 招商银行
- `citic/` - 中信银行
- `xy/` - 兴业银行
- `sh/` - 上海银行

### 3. 测试类命名规范

**必须**遵循以下命名约定：
- 服务测试类：`MoneyOrderServiceTest.java`（按银行目录组织）
- 报文处理测试类：`[Bank]SendTest.java`（如IcbcSendTest.java）
- 工具类测试：`[工具类名]Test.java`（如DozerMapperTest.java）
- 策略测试类：`[策略类名]Test.java`
- 测试方法：`test[功能描述]()`或具体的业务方法名

示例：
```java
// 正确命名
MoneyOrderServiceTest.java
IcbcSendTest.java
BankLimiterStrategyManagerTest.java

// 测试方法命名
public void testMoneyOrder()
public void test1251()
public void testParseBankConfig()
```

### 4. 基础测试类规范

#### 4.1 标准Spring Boot测试注解
**所有测试类**必须使用以下标准注解组合：

```java
@Slf4j
@SpringBootTest
@RunWith(SpringRunner.class)
public class MoneyOrderServiceTest {
    
    @Autowired
    private MoneyOrderServiceImpl moneyOrderService;
    
    @Before
    public void setUp() throws Exception {
        log.info("测试开始");
    }

    @After
    public void tearDown() throws Exception {
        log.info("测试结束");
    }
}
```

#### 4.2 JUnit 5风格测试（可选）
对于新的测试类，可以使用JUnit 5风格：

```java
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class BankLimiterStrategyManagerTest {
    
    @BeforeEach
    void setUp() {
        // 初始化逻辑
    }
    
    @Test
    void testParseBankConfig() {
        // 测试逻辑
    }
}
```

### 5. 测试数据管理规范

#### 5.1 银行业务测试数据构造
**必须**为每个银行提供标准的测试数据构造方法：

```java
@Slf4j
@SpringBootTest
@RunWith(SpringRunner.class)
public class MoneyOrderServiceTest {
    
    // 工行划款测试数据
    public static MoneyOrderReqFindDTO setIcbcMoneyOrder() throws IOException {
        MoneyOrderReqFindDTO dto = new MoneyOrderReqFindDTO();
        dto.setInstCode("102");  // 工行代码
        dto.setCash(new BigDecimal("1.6"));
        dto.setFundId("T150204686");
        dto.setDeptCode("1");
        dto.setOutAcntNo("609767935");
        dto.setOutAcntName("COS测试1");
        dto.setInAcntNo("6225380099862627");
        dto.setInAcntName("帐户二一BPXSM");
        dto.setPayDate("20190118");
        dto.setRemark("工行划款测试");
        dto.setOperationType("1");
        dto.setSubsysNo("1234");
        return dto;
    }
    
    // 工行当日明细测试数据
    public static AccTodayDetailFindDTO setIcbcAccTodey() {
        AccTodayDetailFindDTO dto = new AccTodayDetailFindDTO();
        dto.setInstCode("102");
        dto.setAcntName("COS测试1");
        dto.setAcntCode("609767935");
        dto.setFundId("1");
        dto.setBeginDate("20190118");
        dto.setDeptCode("1");
        dto.setSubsysNo("111");
        return dto;
    }
    
    // 工行余额查询测试数据
    public static AccBalanceDetailFindDTO setAccBalance() {
        AccBalanceDetailFindDTO dto = new AccBalanceDetailFindDTO();
        dto.setFundId("1");
        dto.setInstCode("102");
        dto.setBeginDate("20190118");
        dto.setEndDate("20190118");
        dto.setDeptCode("1");
        dto.setAcntCode("609767935");
        dto.setAcntName("COS测试1");
        dto.setSubsysNo("11");
        return dto;
    }
}
```

#### 5.2 测试数据隔离
**必须**确保测试数据完全隔离：
- **使用测试专用的机构代码和账户**
- **测试数据不能影响其他测试**
- **使用日期时间戳生成唯一标识**

### 6. Mock使用规范

#### 6.1 银行适配器测试Mock
```java
@Slf4j
@SpringBootTest
@RunWith(SpringRunner.class)
public class IcbcSendTest {
    
    @Autowired
    private IcbcBackDataProcessor processRevMsg;
    
    @Test
    public void test1251() throws Exception {
        // 模拟深证通参数
        Map<String, Object> testMap = new HashMap<>();
        testMap.put("STZ_USER_ID", "testUser");
        testMap.put("STZ_APP_ID", "testApp");
        
        // 模拟银行返回的XML报文
        String mockXmlResponse = "<OUT>" +
                "<FILE_TYPE>1251</FILE_TYPE>" +
                "<FUND_ID>4686</FUND_ID>" +
                "<REPORT_TYPE>01</REPORT_TYPE>" +
                "<BEGIN_DATE>20190130</BEGIN_DATE>" +
                "</OUT>";
        
        // 执行测试
        processRevMsg.onRevMsg(TghCodeEnum.ICBC, compressXml(mockXmlResponse), testMap);
    }
    
    // 压缩XML工具方法
    private String compressXml(String xml) throws IOException {
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        GZIPOutputStream gzip = new GZIPOutputStream(out);
        gzip.write(xml.getBytes());
        gzip.close();
        return Base64.getEncoder().encodeToString(out.toByteArray());
    }
}
```

#### 6.2 服务层测试Mock
```java
@MockBean
private BankProviderApi bankProviderApi;

@MockBean
private ChannelProviderApi channelProviderApi;

@Test
public void testMoneyOrderReq() {
    // Given - 设置Mock行为
    when(bankProviderApi.packageMsg(any()))
        .thenReturn("mock银行报文");
    when(channelProviderApi.sendMsg(any(), any(), any()))
        .thenReturn(true);
    
    // When - 执行测试
    String result = moneyOrderService.moneyOrderReq(setIcbcMoneyOrder());
    
    // Then - 验证结果
    assertNotNull("返回结果不应为空", result);
    verify(bankProviderApi, times(1)).packageMsg(any());
    verify(channelProviderApi, times(1)).sendMsg(any(), any(), any());
}
```

### 7. 异常测试规范

**必须**为每个关键方法编写异常场景测试：

```java
@Test(expected = ServiceException.class)
public void testMoneyOrderReq_NullInput_ThrowsException() {
    // When & Then
    moneyOrderService.moneyOrderReq(null);
}

@Test
public void testMoneyOrderReq_InvalidInstCode_ReturnsError() {
    // Given
    MoneyOrderReqFindDTO invalidDto = setIcbcMoneyOrder();
    invalidDto.setInstCode("999"); // 无效机构代码
    
    // When & Then
    try {
        moneyOrderService.moneyOrderReq(invalidDto);
        fail("应该抛出异常");
    } catch (ServiceException e) {
        assertTrue("错误信息应包含机构代码", 
                   e.getMessage().contains("机构代码"));
    }
}
```

### 8. 断言规范

#### 8.1 JUnit断言示例
```java
// 基本断言
Assert.assertNotNull("UUID不应为空", uuid);
Assert.assertEquals("机构代码应该匹配", "102", result.getInstCode());
Assert.assertTrue("金额应该大于0", result.getAmount().compareTo(BigDecimal.ZERO) > 0);

// 集合断言
Assert.assertFalse("列表不应为空", resultList.isEmpty());
Assert.assertEquals("列表大小应该为2", 2, resultList.size());

// JSON断言
JSONObject jsonResult = JSON.parseObject(result);
Assert.assertEquals("状态应该为成功", "SUCCESS", jsonResult.getString("status"));
```

#### 8.2 JUnit 5断言示例
```java
// 现代断言风格
assertNotNull(result, "结果不应为空");
assertEquals("SUCCESS", result.getStatus(), "状态应该为成功");
assertTrue(result.getAmount().compareTo(BigDecimal.ZERO) > 0, "金额应该大于0");

// 断言异常
assertThrows(ServiceException.class, () -> {
    service.processInvalidData(null);
}, "空数据应该抛出ServiceException");
```

### 9. 银行适配器测试规范

**必须**为每个银行适配器编写专门的测试：

```java
@Slf4j
@SpringBootTest
@RunWith(SpringRunner.class)
public class IcbcSendTest {
    
    @Autowired
    private IcbcBackDataProcessor processRevMsg;
    
    @Test
    public void test1251() throws Exception {
        // 测试工行划款回执处理
        testBankResponse("1251", buildIcbcTransferResponse());
    }
    
    @Test
    public void test1061() throws Exception {
        // 测试工行当日明细回执处理
        testBankResponse("1061", buildIcbcDetailResponse());
    }
    
    @Test
    public void test1341() throws Exception {
        // 测试工行指令作废回执处理
        testBankResponse("1341", buildIcbcCancelResponse());
    }
    
    private void testBankResponse(String fileType, String xmlResponse) throws Exception {
        Map<String, Object> params = new HashMap<>();
        params.put("STZ_USER_ID", "testUser");
        params.put("STZ_APP_ID", "testApp");
        
        // 执行银行回执处理
        processRevMsg.onRevMsg(TghCodeEnum.ICBC, compressXml(xmlResponse), params);
        
        log.info("{}类型报文处理完成", fileType);
    }
}
```

### 10. 性能测试规范

**关键方法**必须包含性能测试：

```java
@Test(timeout = 10000) // 10秒超时
public void testBatchMoneyOrder_Performance() {
    // Given
    List<MoneyOrderReqFindDTO> batchOrders = new ArrayList<>();
    for (int i = 0; i < 100; i++) {
        batchOrders.add(setIcbcMoneyOrder());
    }
    
    // When
    long startTime = System.currentTimeMillis();
    List<String> results = new ArrayList<>();
    for (MoneyOrderReqFindDTO order : batchOrders) {
        results.add(moneyOrderService.moneyOrderReq(order));
    }
    long endTime = System.currentTimeMillis();
    
    // Then
    assertEquals("批量处理结果数量应正确", 100, results.size());
    assertTrue("批量处理应在10秒内完成", (endTime - startTime) < 10000);
    log.info("批量处理100笔指令耗时: {}ms", (endTime - startTime));
}
```

### 11. 日志测试规范

**必须**验证关键操作的日志记录：

```java
@Test
public void testMoneyOrderReq_LogsCorrectly() {
    // Given
    MoneyOrderReqFindDTO order = setIcbcMoneyOrder();
    
    // When
    String result = moneyOrderService.moneyOrderReq(order);
    
    // Then
    assertNotNull("处理结果不应为空", result);
    // 注意: 实际项目中应使用日志测试框架验证日志内容
    log.info("测试划款指令处理完成, UUID: {}", result);
}
```

---

## Maven配置要求

### 测试执行配置

**注意**：CCM系统的Maven配置默认跳过测试执行（`<maven.test.skip>true</maven.test.skip>`）。

**运行测试的正确方法**：

#### 方法1：临时运行测试
```bash
# 运行所有测试
mvn test -Dmaven.test.skip=false

# 运行特定测试类
mvn test -Dtest=MoneyOrderServiceTest -Dmaven.test.skip=false

# 运行特定银行的测试
mvn test -Dtest=com.hundsun.ccm.fundtransfer.Icbc.service.MoneyOrderServiceTest -Dmaven.test.skip=false

# 运行特定测试方法
mvn test -Dtest=MoneyOrderServiceTest#testMoneyOrder -Dmaven.test.skip=false
```

#### 方法2：修改pom.xml配置（开发环境）
如需长期运行测试，修改`ccm-capitalchannel/pom.xml`：
```xml
<properties>
    <maven.test.skip>false</maven.test.skip>  <!-- 改为false启用测试 -->
</properties>
```

### 测试依赖配置

当前已配置的测试相关依赖：
```xml
<dependency>
    <groupId>junit</groupId>
    <artifactId>junit</artifactId>
    <version>4.12</version>
    <scope>test</scope>
</dependency>

<!-- Spring Boot Test自动配置 -->
<dependency>
    <groupId>com.hundsun.jrescloud</groupId>
    <artifactId>jrescloud-starter</artifactId>
    <!-- 包含Spring Boot Test支持 -->
</dependency>
```

---

## CCM特有测试规范

### 1. 银行代码枚举测试
```java
@Test
public void testBankCodeEnum() {
    // 验证银行代码枚举
    assertEquals("工行代码应为102", "102", TghCodeEnum.ICBC.getCode());
    assertEquals("农行代码应为103", "103", TghCodeEnum.ABC.getCode());
    assertEquals("建行代码应为105", "105", TghCodeEnum.CCB.getCode());
}
```

### 2. 深证通参数测试
```java
@Test
public void testSztParams() {
    Map<String, Object> sztParams = new HashMap<>();
    sztParams.put("STZ_USER_ID", "testUser");
    sztParams.put("STZ_APP_ID", "testApp");
    
    assertNotNull("深证通用户ID不应为空", sztParams.get("STZ_USER_ID"));
    assertNotNull("深证通应用ID不应为空", sztParams.get("STZ_APP_ID"));
}
```

### 3. XML处理测试
```java
@Test
public void testXmlProcessing() {
    // 测试XStream XML处理
    XStream xstream = new XStream(new XppDriver(new NoNameCoder()));
    xstream.autodetectAnnotations(true);
    
    // 测试XML序列化和反序列化
    String xml = "<test><value>123</value></test>";
    Object result = xstream.fromXML(xml);
    assertNotNull("XML解析结果不应为空", result);
}
```

### 4. 对象映射测试
```java
@Test
public void testDozerMapping() {
    // 测试Dozer对象映射
    HkAccDetailRet source = new HkAccDetailRet();
    source.setAcntCode("1234567890");
    
    AccDetailRetStandDTO target = new AccDetailRetStandDTO();
    dozerBeanMapper.map(source, target);
    
    assertEquals("账户代码应正确映射", "1234567890", target.getBankAccountNo());
}
```

---

## 禁止行为

### 绝对禁止以下行为：

1. **禁止**在测试中使用生产环境的机构代码和账户
2. **禁止**在测试中进行真实的银行通信
3. **禁止**在测试中操作生产数据库
4. **禁止**编写没有断言的测试方法
5. **禁止**使用`Thread.sleep()`等待异步操作
6. **禁止**在测试中使用硬编码的生产配置
7. **禁止**编写相互依赖的测试用例
8. **禁止**忽略测试失败，必须修复后再提交代码
9. **禁止**在测试中使用真实的文件路径和网络资源
10. **禁止**测试方法中包含业务逻辑代码

---

## 强制检查清单

### 测试类创建检查清单
- [ ] 类名遵循命名规范（MoneyOrderServiceTest等）
- [ ] 添加正确的注解（@SpringBootTest、@RunWith等）
- [ ] 按银行目录正确组织测试文件
- [ ] 添加@Slf4j日志注解
- [ ] 实现@Before和@After方法

### 测试方法检查清单
- [ ] 测试方法名称清晰描述测试内容
- [ ] 每个测试方法包含至少一个断言
- [ ] 使用标准的测试数据构造方法
- [ ] 添加适当的异常测试
- [ ] 验证Mock对象的调用

### 银行适配器测试检查清单
- [ ] 为每个支持的FILE_TYPE编写测试
- [ ] 测试XML报文的压缩和解压
- [ ] 验证深证通参数的正确传递
- [ ] 测试银行枚举代码的正确使用
- [ ] 验证报文处理的完整流程

### 性能和日志检查清单
- [ ] 关键方法添加性能测试和超时设置
- [ ] 验证重要操作的日志输出
- [ ] 批量操作的性能测试
- [ ] 异常情况的日志记录测试