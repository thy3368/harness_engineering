---
description: "AI Coding Rules - API设计规范"
globs: *.md,*.java
alwaysApply: false
version: 1.0.0
author: liulm50695
created: 2025-09-19
lastUpdated: 2025-09-19
---

# CCM API设计强制约束规则

## 第一部分：控制层接口约束（Web API）

### 控制器类约束
- **类名必须以Controller结尾**：如`MoneyOrderController`、`AccBalanceController`
- **必须添加**：`@RestController`
- **必须添加**：`@RequestMapping(value = "/capitalchannelmanager")`
- **必须添加**：`@Slf4j`注解用于日志记录
- **建议实现相应的接口**：如`implements MoneyOrderService`

### 控制层接口示例

#### 标准POST接口示例
```java
@Slf4j
@RestController
@RequestMapping(value = "/capitalchannelmanager")
public class MoneyOrderController implements MoneyOrderService {
    
    @Autowired
    private MoneyOrderService moneyOrderService;
    @Autowired
    private DozerBeanMapper dozerBeanMapper;
    
    @Override
    @PostMapping(value = "/moneyOrderReq")
    public ResponseData<String> moneyOrderReq(@RequestBody MoneyOrderStandDTO moneyOrderStandDTO) {
        // 数据有效性验证
        if (StringUtils.isBlank(moneyOrderStandDTO.getCustodianBankNo())) {
            throw new ServiceException(CCMResultCodeConstant.getMessage(
                CCMResultCodeConstant.Status.ERROR_MISS_ORDERPARAMS, "CUSTODIAN_BANK_NO[托管行代码]"));
        }
        log.info("[划款请求入参] " + moneyOrderStandDTO.toString());
        try {
            // 业务逻辑处理
            MoneyOrderReqFindDTO dto = new MoneyOrderReqFindDTO();
            dozerBeanMapper.map(moneyOrderStandDTO, dto);
            return ResponseData.ok(moneyOrderService.moneyOrderReq(dto));
        } catch (ServiceException ex) {
            return ResponseData.fail(500, ex.getError() != null ? 
                ex.getError().getErrorCode() : null, ex.getMessage());
        } catch (SQLException ex) {
            return ResponseData.fail(500, "数据库SQL执行异常");
        } catch (Exception ex) {
            return ResponseData.fail(500, ex.getMessage());
        }
    }
}
```

#### 标准GET接口示例
```java
@GetMapping(value = "/sztConfigSynchronize")
public ResponseData<String> sztConfigSynchronize(@RequestParam(required = false) String bicCode) {
    log.info("[深圳通配置同步] bicCode={}", bicCode);
    try {
        // 业务逻辑处理
        return ResponseData.ok(sztConfigSynchronizeService.synchronize(bicCode));
    } catch (Exception ex) {
        log.error("深圳通配置同步失败", ex);
        return ResponseData.fail(500, ex.getMessage());
    }
}
```

### 控制层强制约束
- **URL路径必须以功能名称命名**：如`/moneyOrderReq`、`/detailsAccBalance`
- **POST请求必须使用**：`@RequestBody`接收JSON参数
- **GET请求必须使用**：`@RequestParam`接收参数
- **必须启用参数校验**：使用`StringUtils.isBlank()`等进行非空校验
- **必须返回**：`ResponseData<T>`统一格式
- **必须添加日志记录**：使用`log.info()`记录请求参数和处理结果
- **必须进行异常处理**：分类处理`ServiceException`、`SQLException`等异常

## 第二部分：RPC接口约束（对外服务）

### RPC接口示例

#### 标准RPC接口定义
```java
@CloudService
public interface MoneyOrderService {
    
    /**
     * 划款指令请求
     */
    @CloudFunction(functionId = "moneyOrderReq")
    ResponseData<String> moneyOrderReq(@CloudFunctionParam("moneyOrderStandDTO") MoneyOrderStandDTO param);
    
    /**
     * 批量划款指令请求
     */
    @CloudFunction(functionId = "moneyOrderReqPatch")
    ResponseData<String> moneyOrderReqPatch(@CloudFunctionParam("moneyOrderStandPatchDTO") MoneyOrderStandPatchDTO param);
    
    /**
     * 划款指令查询
     */
    @CloudFunction(functionId = "moneyOrderView")
    MoneyOrderResponse moneyOrderView(@CloudFunctionParam("queryViewDTO") QueryViewDTO param) 
        throws InvocationTargetException, IllegalAccessException;
}
```

#### 控制器接口定义示例
```java
@CloudService
public interface AccBalanceControllerInterface {
    
    @CloudFunction(apiUrl = "listAccBalance", functionId = "900102")
    ResponseData<PageInfo<HkAccBalanceVo>> listAccBalance(
        @CloudFunctionParam(value = "instCode") String instCode,
        @CloudFunctionParam(value = "acntCode") String acntCode,
        @CloudFunctionParam(value = "fundId") String fundId,
        @CloudFunctionParam(value = "pageNo") Integer pageNo,
        @CloudFunctionParam(value = "pageSize") Integer pageSize);
}
```

### RPC接口强制约束
- **接口类必须添加**：`@CloudService`
- **方法必须添加**：`@CloudFunction(functionId = "功能标识")`
- **参数必须添加**：`@CloudFunctionParam("参数名")`或`@CloudFunctionParam(value = "参数名")`
- **必须返回**：`ResponseData<T>`或其它自定义响应类型
- **功能标识必须唯一**：如`moneyOrderReq`、`detailsAccBalance`
- **接口类名建议**：Service接口以Service结尾，Controller接口以ControllerInterface结尾

## 第三部分：响应数据格式约束

### 统一响应格式
```java
@Data
public final class ResponseData<T> implements Serializable {
    
    @CloudFunctionParam("return_code")
    private Integer code;
    
    @CloudFunctionParam("biz_code")
    private Integer bizCode;
    
    @CloudFunctionParam("message")
    private String message;
    
    @CloudFunctionParam("data")
    private T data;
    
    // 成功响应
    public static ResponseData ok(final Object data) {
        final ResponseData<Object> responseData = new ResponseData<>();
        responseData.setCode(Status.SUCCESS.getCode());
        responseData.setMessage(Status.SUCCESS.getReason());
        responseData.setData(data);
        return responseData;
    }
    
    // 失败响应
    public static ResponseData fail(final Integer code, final String reason) {
        return new ResponseData(code, reason);
    }
}
```

### 响应数据强制约束
- **必须使用**：`ResponseData<T>`作为统一响应格式
- **成功响应使用**：`ResponseData.ok(data)`
- **失败响应使用**：`ResponseData.fail(code, message)`
- **状态码固定**：成功码`200`，错误码`500`等
- **错误消息使用中文描述**

## 第四部分：异常处理约束

### 业务异常示例
```java
// 参数校验异常
if (StringUtils.isBlank(param.getCustodianBankNo())) {
    throw new ServiceException(CCMResultCodeConstant.getMessage(
        CCMResultCodeConstant.Status.ERROR_MISS_ORDERPARAMS, "CUSTODIAN_BANK_NO[托管行代码]"));
}

// 统一异常处理示例
try {
    // 业务逻辑
    return ResponseData.ok(result);
} catch (ServiceException ex) {
    return ResponseData.fail(500, ex.getError() != null ? 
        ex.getError().getErrorCode() : null, ex.getMessage());
} catch (SQLException ex) {
    return ResponseData.fail(500, "数据库SQL执行异常");
} catch (IbatisException ex) {
    return ResponseData.fail(500, "数据库SQL操作异常");
} catch (Exception ex) {
    return ResponseData.fail(500, ex.getMessage());
}
```

### 错误码定义示例
```java
public enum Status implements StatusType {
    SUCCESS(200, "成功"),
    ERROR_MISS_ORDERPARAMS(20002, "划款请求失败，参数{%s}不能为空"),
    ERROR_UUID_EXIST(20005, "UUID不存在"),
    ERROR_HKMAIN_EXIST(20006, "该{%s}对应的划款记录不存在"),
    ERROR_TRANSFER_BEAN(20029, "转化BEAN类型失败");
}
```

### 异常处理强制约束
- **必须使用**：`ServiceException`抛出业务异常
- **必须使用**：`CCMResultCodeConstant.Status`枚举定义错误码
- **必须分类处理异常**：`ServiceException`、`SQLException`、`IbatisException`等
- **必须记录异常日志**：`log.error("异常描述", exception)`
- **必须返回用户友好的错误信息**：避免技术细节泄露

## 第五部分：参数校验约束

### 参数校验示例
```java
public ResponseData<String> moneyOrderReq(@RequestBody MoneyOrderStandDTO param) {
    // 必填参数校验
    if (StringUtils.isBlank(param.getCustodianBankNo())) {
        throw new ServiceException(CCMResultCodeConstant.getMessage(
            CCMResultCodeConstant.Status.ERROR_MISS_ORDERPARAMS, "CUSTODIAN_BANK_NO[托管行代码]"));
    }
    
    // 批量参数校验
    if (CollectionUtils.isEmpty(param.getSubHkmain())) {
        throw new ServiceException(CCMResultCodeConstant.getMessage(
            CCMResultCodeConstant.Status.ERROR_MISS_ORDERPARAMS, "List<SubHkmain>[子参数集合]"));
    }
    
    // 数据校验处理
    if (StringUtils.isBlank(param.getFundName())) {
        param.setFundName(param.getFundCode());
    }
}
```

### 参数校验强制约束
- **POST请求必须使用**：`@RequestBody`接收JSON参数
- **GET请求必须使用**：`@RequestParam`接收参数
- **必须进行非空校验**：使用`StringUtils.isBlank()`检查字符串参数
- **必须进行集合校验**：使用`CollectionUtils.isEmpty()`检查集合参数
- **必须提供明确的错误提示**：包含参数名称和要求描述

## 第六部分：数据映射约束

### 对象映射示例
```java
@Autowired
private DozerBeanMapper dozerBeanMapper;

public ResponseData<String> processRequest(@RequestBody MoneyOrderStandDTO standDTO) {
    // DTO转换
    MoneyOrderReqFindDTO findDTO = new MoneyOrderReqFindDTO();
    dozerBeanMapper.map(standDTO, findDTO);
    
    // 特殊字段处理
    Map<String, Object> paramMap = getOtherParam(standDTO);
    findDTO.setOtherParam(JSON.toJSON(paramMap).toString());
    
    return ResponseData.ok(service.process(findDTO));
}
```

### 数据映射强制约束
- **必须使用**：`DozerBeanMapper`进行对象映射
- **必须处理特殊字段**：不能直接映射的字段需单独处理
- **必须进行JSON序列化**：复杂对象使用`JSON.toJSON()`转换
- **必须处理空值**：映射前后检查关键字段是否为空

## 强制检查清单

### 控制层接口检查清单
- [ ] 类名以Controller结尾
- [ ] 添加`@RestController`注解
- [ ] 添加`@RequestMapping(value = "/capitalchannelmanager")`类级路径映射
- [ ] 添加`@Slf4j`日志注解
- [ ] URL路径使用功能名称命名
- [ ] POST请求使用`@RequestBody`，GET请求使用`@RequestParam`
- [ ] 返回`ResponseData<T>`统一格式
- [ ] 添加完整的异常处理机制
- [ ] 记录请求参数和处理结果日志
- [ ] 实现相应的Service接口

### RPC接口检查清单
- [ ] 接口类添加`@CloudService`注解
- [ ] 接口类名以Service或ControllerInterface结尾
- [ ] 方法添加`@CloudFunction(functionId = "功能标识")`注解
- [ ] 参数添加`@CloudFunctionParam("参数名")`注解
- [ ] 方法返回`ResponseData<T>`或其它响应类型
- [ ] 功能标识唯一且有意义
- [ ] 添加适当的JavaDoc文档注释

### 异常处理检查清单
- [ ] 使用ServiceException抛出业务异常
- [ ] 使用CCMResultCodeConstant.Status定义错误码
- [ ] 分类处理不同类型异常
- [ ] 记录完整异常堆栈信息
- [ ] 提供用户友好的错误信息
- [ ] 避免敏感信息泄露

### 参数校验检查清单
- [ ] 使用StringUtils.isBlank()检查字符串参数
- [ ] 使用CollectionUtils.isEmpty()检查集合参数
- [ ] 提供明确的参数错误提示
- [ ] 包含参数名称和中文描述
- [ ] 处理参数默认值设置

### 数据映射检查清单
- [ ] 使用DozerBeanMapper进行对象映射
- [ ] 单独处理无法直接映射的特殊字段
- [ ] 使用JSON.toJSON()处理复杂对象序列化
- [ ] 检查映射前后关键字段完整性
- [ ] 处理映射过程中的空值情况

## 附录：常用工具类和方法

### 字符串工具类
```java
// 字符串非空校验
StringUtils.isBlank(str)
StringUtils.isNotBlank(str)

// 集合非空校验  
CollectionUtils.isEmpty(collection)
CollectionUtils.isNotEmpty(collection)
```

### JSON工具类
```java
// 对象转JSON
JSON.toJSON(object).toString()

// JSON转对象
JSON.parseObject(jsonString, TargetClass.class)
```

### 异常工具类
```java
// 抛出业务异常
throw new ServiceException(CCMResultCodeConstant.getMessage(
    CCMResultCodeConstant.Status.ERROR_CODE, "参数描述"));

// 获取错误信息
CCMResultCodeConstant.getMessage(Status.ERROR_CODE, params...)
```

### 日志记录
```java
// 信息日志
log.info("[功能描述] 参数信息");

// 错误日志
log.error("错误描述", exception);
```