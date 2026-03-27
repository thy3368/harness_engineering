---
description: "AI Coding Rules - API设计规范"
globs: *.md,*.java
alwaysApply: false
version: 1.0.0
author: liangzp35600
created: 2025-9-16
lastUpdated: 2025-9-16
---

# API强制约束规则

## 第一部分：控制层接口约束（Web API）

### 控制器类约束
- **类名必须以Action结尾**：如`TransferInputAction`、`CommonAction`
- **必须添加**：`@Controller`或`@RestController`
- **必须添加**：`@RequestMapping(value = "/模块路径/")`
- **必须添加**：`@Api(value = "模块描述", tags = {"标签"})`
- **建议添加**：`@Slf4j`

### 控制层接口示例

#### 标准POST接口示例
```java
@Controller
@RequestMapping(value = "/cashsettle/input/")
@Api(value = "资金结算", tags = {"资金结算录入"})
@Slf4j
public class TransferInputAction {
    
    @RequestMapping(value = "splitTransfer.json", method = RequestMethod.POST)
    @ApiOperation(value = "指令拆分")
    @RequiresPermissions("copTransferSplit")
    @ResponseBody
    public ServerResponse<String> splitTransfer(@Valid @RequestBody SplitTransferRequest request) {
        try {
            // 业务逻辑处理
            transferService.splitTransfer(request);
            return ServerResponse.ok("拆分成功");
        } catch (BusinessException e) {
            return new ServerResponse<>(e);
        }
    }
}
```

#### 标准GET查询接口示例
```java
@Controller
@RequestMapping(value = "/common/")
@Api(value = "通用功能", tags = {"通用功能维护"})
@Slf4j
public class CommonAction {
    
    @RequestMapping(value = "fundList.json", method = RequestMethod.GET)
    @ApiOperation(value = "查询基金列表")
    @RequiresPermissions("copCommonQuery")
    @ResponseBody
    public ServerResponse<List<FundInfo>> getFundList(
            @RequestParam(required = false) String fundCode,
            @RequestParam(defaultValue = "1") Integer pageNum,
            @RequestParam(defaultValue = "20") Integer pageSize) {
        
        List<FundInfo> result = fundService.queryFundList(fundCode, pageNum, pageSize);
        return ServerResponse.ok(result);
    }
}
```

### 控制层强制约束
- **URL路径必须以.json结尾**
- **POST请求必须使用**：`@RequestBody`接收JSON参数
- **GET请求必须使用**：`@RequestParam`接收参数  
- **必须启用参数校验**：`@Valid @RequestBody`
- **业务接口必须添加权限控制**：`@RequiresPermissions("权限码")`
- **必须返回**：`ServerResponse<T>`统一格式
- **Controller必须添加**：`@ResponseBody`（RestController除外）

## 第二部分：RPC接口约束（对外T2服务）

### T2 RPC接口示例

#### 标准T2接口定义
```java
@CloudService
public interface CopWebService {
    
    /**
     * TCMP指令下达接口
     */
    @CloudFunction(functionId = "5100252", desc = "下达指令")
    T2Response addTcmpCommand(@CloudFunctionParam("transferInfo") List<TcmpCommand> transferInfo);
    
    /**
     * TCMP指令撤销接口  
     */
    @CloudFunction(functionId = "5100253", desc = "撤销指令")
    T2Response deleteTcmpCommand(@CloudFunctionParam("transferInfo") List<TcmpCancelCommand> cancelCommands);
    
    /**
     * O32指令下达接口
     */
    @CloudFunction(functionId = "5100072", desc = "O32指令下达")
    T2Response addRemoteCommand(@CloudFunctionParam("transferInfo") RemoteTransferDTO transferInfo);
}
```

#### 外部系统推送接口示例
```java
@CloudService
public interface OuterSystemPushService {
    
    @CloudFunction(functionId = "9626", desc = "外部系统推送托管组合代码映射")
    T2Response pushCusComCodeMap(@CloudFunctionParam("OpType") String OpType,
                               @CloudFunctionParam("SysType") String SysType,
                               @CloudFunctionParam("FundLevel") String FundLevel,
                               @CloudFunctionParam("FundCode") String FundCode,
                               @CloudFunctionParam("AssetCode") String AssetCode,
                               @CloudFunctionParam("BankComCode") String BankComCode,
                               @CloudFunctionParam("BankComName") String BankComName,
                               @CloudFunctionParam("CustoDianNo") String CustoDianNo);
}
```

### RPC接口强制约束
- **接口类必须添加**：`@CloudService`
- **方法必须添加**：`@CloudFunction(functionId = "功能码", desc = "功能描述")`
- **参数必须添加**：`@CloudFunctionParam("参数名")`
- **必须返回**：`T2Response`或其子类
- **功能码必须唯一**：通常为7位数字
- **接口类名必须以Service结尾**

## 第三部分：HTTP外部调用约束

### HTTP客户端使用示例
```java
@Service
public class DataCenterServiceImpl {
    
    RestTemplate restTemplate = RestTemplateUtil.getInstance("utf-8");
    
    public String callExternalApi(String requestData) {
        try {
            HttpHeaders headers = new HttpHeaders();
            headers.setContentType(MediaType.APPLICATION_JSON_UTF8);
            
            HttpEntity<String> request = new HttpEntity<>(requestData, headers);
            ResponseEntity<String> response = restTemplate.postForEntity(
                externalApiUrl, request, String.class);
            
            if (response.getStatusCode().is2xxSuccessful()) {
                return response.getBody();
            } else {
                throw new BusinessException("外部接口调用失败");
            }
        } catch (Exception e) {
            log.error("调用外部接口异常：", e);
            throw new BusinessException("外部接口调用异常");
        }
    }
}
```

### HTTP调用强制约束
- **必须使用配置好的RestTemplate**：`RestTemplateUtil.getInstance("utf-8")`
- **必须设置Content-Type**：`MediaType.APPLICATION_JSON_UTF8`
- **必须添加异常处理**：捕获所有调用异常并转换为BusinessException
- **必须记录异常日志**：`log.error("异常信息", exception)`

## 第四部分：异常处理约束

### 业务异常示例
```java
// 业务异常抛出示例
if (transferInfo == null) {
    throw new BusinessException(ResponseCode.PARAM_ERROR, "指令信息不能为空");
}

// 异常转换示例
try {
    externalService.callApi();
} catch (Exception e) {
    log.error("外部接口调用失败", e);
    throw new BusinessException(ResponseCode.FAIL, "外部接口调用异常");
}
```

### 异常处理强制约束
- **必须使用**：`BusinessException(ResponseCode, message)`
- **必须使用**：`ResponseCode`枚举定义错误码
- **成功码固定**：`"0"`
- **错误消息使用中文描述**
- **必须记录异常堆栈**：`log.error("异常描述", exception)`

## 第五部分：参数校验约束

### 参数校验示例
```java
public class TransferRequest {
    @NotBlank(message = "指令ID不能为空")
    @Size(max = 32, message = "指令ID长度不能超过32位")
    private String transferId;
    
    @NotNull(message = "金额不能为空")
    @DecimalMin(value = "0.01", message = "金额必须大于0")
    private BigDecimal amount;
    
    @MessageCheck(label = "业务类型", required = true, allowedValues = {"1", "2", "3"})
    private String businessType;
}

// Controller中使用校验
@RequestMapping(value = "submit.json", method = RequestMethod.POST)
public ServerResponse<String> submit(@Valid @RequestBody TransferRequest request) {
    // 业务处理
}
```

### 参数校验强制约束
- **POST请求必须使用**：`@RequestBody`接收JSON
- **GET请求必须使用**：`@RequestParam`接收参数
- **必须启用校验**：`@Valid @RequestBody`
- **必须使用标准校验注解**：`@NotNull`、`@NotBlank`、`@Size`等
- **可使用自定义校验**：`@MessageCheck`（特殊场景）

## 强制检查清单

### 控制层接口检查清单
- [ ] 类名以Action结尾
- [ ] 添加`@Controller`或`@RestController`
- [ ] 添加`@RequestMapping`类级路径映射
- [ ] 添加`@Api`和`@ApiOperation`文档注解
- [ ] URL路径以.json结尾
- [ ] 业务方法添加`@RequiresPermissions`权限控制
- [ ] 返回`ServerResponse<T>`统一格式
- [ ] POST请求使用`@RequestBody`，GET请求使用`@RequestParam`
- [ ] 启用参数校验`@Valid @RequestBody`
- [ ] Controller方法添加`@ResponseBody`（RestController除外）

### RPC接口检查清单
- [ ] 接口类添加`@CloudService`注解
- [ ] 接口类名以Service结尾
- [ ] 方法添加`@CloudFunction(functionId, desc)`注解
- [ ] 参数添加`@CloudFunctionParam("参数名")`注解
- [ ] 方法返回`T2Response`或其子类
- [ ] 功能码唯一且为7位数字

### HTTP外部调用检查清单
- [ ] 使用配置好的RestTemplate实例
- [ ] 设置正确的Content-Type
- [ ] 添加完整异常处理机制
- [ ] 将外部异常转换为BusinessException
- [ ] 记录调用异常日志

### 异常处理检查清单
- [ ] 使用BusinessException抛出业务异常
- [ ] 使用ResponseCode枚举定义错误码
- [ ] 记录完整异常堆栈信息
- [ ] 提供用户友好的错误信息
- [ ] 避免敏感信息泄露
