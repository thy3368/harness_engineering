---
description: "AI Coding Rules - 工程模块规范"
globs: *.md,*.java
alwaysApply: false
version: 1.0.0
author: 架构办
created: 2025-9-19
lastUpdated: 2025-9-19
---

## 工程模块规范

### 根模块结构

公共模块
```
├── COMMONS
└── └── cop-parent                      # 父工程
```

业务模块
```
├── COP
│   ├── RUN                             # 运行相关
│   │   ├── bin                         # bin目录
│   │   ├── deployPack                  # 部署包相关
│   │   ├── 工具    		            # 对接O45数据库脚本
│   ├── SOURCES                         # 源码相关
│   │   │   ├── app    		            # 移动审批前端
│   │   │   ├── plugin                  # 各类插件
│   │   │   │   ├── acf-gateway    		# ACF网关应用
│   │   │   │   ├── airs-ocr            # OCR服务，以SVN工程为准
│   │   │   │   ├── ccPlugin            # 适配CC2.0插件
│   │   │   │   ├── filePlugin          # 
│   │   │   │   ├── insPlugin           # 适配非标1.0插件
│   │   │   │   ├── copl.0Plugin        # 适配copl.0插件
│   │   │   │   ├── cop1.0Plugin2       # 适配copl.0插件
│   │   │   │   ├── hongcun             # 
│   │   │   │   ├── newtranPlugin       # 信创转换机
│   │   │   ├── service                 # 服务
│   │   │   │   ├── fax-gateway    		# 传真网关应用
│   │   │   │   ├── mail-gateway        # 邮件网关应用
│   │   │   │   ├── cbsch-gateway       # 结算网关应用，已废弃
│   │   │   ├── vue                     # 前端应用
│   │   │   │   ├── cop-app             # 前端
│   │   │   │   ├── cop-frame    		# 前端外框
│   │   │   │   ├── cop-h5    		    # 前端H5
│   │   │   ├── web                     # 核心服务
│   │   │   │   │   ├── cop-web    		# 核心服务
│   │   │   │   │   │   ├── cop-api     # api接口
│   │   │   │   │   │   ├── cop-server  # 核心逻辑
│   │   │   │   │   │   ├── cop-gateway # O32中间件
│   │   │   ├── work                    # 转换机
│   │   │   │   ├── transFramework      # C#转换机
│   │   │   ├── workflow                # 工作流
│   │   │   │   ├── cop-workflow        # 工作流（COP二开）
│   │   │   ├── 升级脚本                 # 升级脚本
│   │   │   │   ├── mysql    		    # mysql数据库脚本
│   │   │   │   ├── oracle    		    # oracle数据库脚本
│   │   │   │   ├── obmysql    		    # obmysql数据库脚本
│   │   │   │   ├── oboracle    		# oboracle数据库脚本
└── └── └── └── └── 对接045    		    # 对接O45数据库脚本
```

### 模块依赖关系

#### 工程依赖关系
```
graph TB
    PARENT[cop-parent] --> API[cop-api]
    PARENT --> SERVER[cop-server]
    PARENT --> GATEWAY[cop-gateway]
    API --> SERVER
    API --> GATEWAY
    API --> NEWTRAN[newtranPlugin]
    
    FAX_PARENT[fax-gateway-parent] --> FAX_API[fax-gateway-api]
    FAX_PARENT --> FAX_START[fax-gateway-start]
    FAX_API --> FAX_START
    
    MAIL_PARENT[mail-gateway-parent] --> MAIL_API[mail-api]
    MAIL_PARENT --> MAIL_SERVER[mail-server]
    MAIL_API --> MAIL_SERVER
    
    style PARENT fill:#e3f2fd,stroke:#0d47a1
    style API fill:#e1f5fe,stroke:#01579b
    style SERVER fill:#f3e5f5,stroke:#4a148c
    style GATEWAY fill:#e8f5e8,stroke:#1b5e20
    style NEWTRAN fill:#fff3e0,stroke:#e65100
    style FAX_PARENT fill:#fce4ec,stroke:#ad1457
    style FAX_API fill:#f8bbd9,stroke:#ad1457
    style FAX_START fill:#f48fb1,stroke:#ad1457
    style MAIL_PARENT fill:#f1f8e9,stroke:#33691e
    style MAIL_API fill:#c8e6c9,stroke:#33691e
    style MAIL_SERVER fill:#a5d6a7,stroke:#33691e
```

#### 分层依赖关系
```
graph LR
    CONTROLLER[Controller] --> SERVICE[Service]
    SERVICE --> DAO[DAO/Mapper]
    SERVICE --> THIRDPARTY[ThirdParty]
    SERVICE --> MQ[MQ/Kafka]
    DAO --> DBCLASS[DbClass/PO]
    
    style CONTROLLER fill:#ffebee,stroke:#c62828
    style SERVICE fill:#e8f5e8,stroke:#2e7d32
    style DAO fill:#fff3e0,stroke:#ef6c00
    style THIRDPARTY fill:#e3f2fd,stroke:#1565c0
    style MQ fill:#f3e5f5,stroke:#7b1fa2
    style DBCLASS fill:#fce4ec,stroke:#ad1457
```

## cop-web 核心业务模块

### 包结构描述

```
com.hundsun.cop/
├── CopStarter.java                  # 主启动类
├── annotation/                      # 自定义注解
├── api/                             # API接口层
├── ar/                              # 应收应付模块
├── bo/                              # 业务对象
├── common/                          # 通用工具类
├── config/                          # 配置类
│   ├── DataSourceConfig.java        # 数据源配置
│   ├── MqConfig.java               # 消息队列配置
│   ├── RedisConfig.java            # Redis配置
│   ├── TaskConfig.java             # 定时任务配置
│   └── WebConfig.java              # Web配置
├── constant/                        # 常量定义
├── controller/                      # 控制器层
│   ├── AccountController.java       # 账户管理控制器
│   ├── InstructionController.java   # 指令管理控制器
│   ├── MonitorController.java       # 监控控制器
│   ├── ReportController.java        # 报表控制器
│   ├── SettlementController.java    # 结算控制器
│   ├── SystemController.java        # 系统管理控制器
│   └── ...                          # 其他控制器
├── convert/                         # 对象转换器
├── dao/                             # 数据访问层
│   ├── AccountDao.java              # 账户数据访问
│   ├── InstructionDao.java          # 指令数据访问
│   ├── SettlementDao.java           # 结算数据访问
│   ├── SystemDao.java               # 系统数据访问
│   └── ...                          # 其他数据访问对象
├── dbclass/                         # 数据库实体类
│   ├── CopTAccount.java             # 账户表实体
│   ├── CopTInstruction.java         # 指令表实体
│   ├── CopTSettlement.java          # 结算表实体
│   ├── CopTOperator.java            # 操作员表实体
│   └── ...                          # 其他数据库实体类
├── dto/                             # 数据传输对象
│   ├── request/                     # 请求DTO
│   ├── response/                    # 响应DTO
│   └── internal/                    # 内部传输DTO
├── event/                           # 事件处理
├── exception/                       # 异常处理
│   ├── GlobalExceptionHandler.java  # 全局异常处理器
│   ├── BusinessException.java       # 业务异常
│   └── SystemException.java         # 系统异常
├── filter/                          # 过滤器
├── inittask/                        # 初始化任务
├── kafka/                           # Kafka消息处理
├── listener/                        # 监听器
├── model/                           # 数据模型
├── monitor/                         # 监控组件
├── mq/                              # 消息队列处理
│   ├── producer/                    # 消息生产者
│   └── consumer/                    # 消息消费者
├── po/                              # 持久化对象
├── sequence/                        # 序列号生成器
├── service/                         # 业务服务层
│   ├── AccountService.java          # 账户服务接口
│   ├── InstructionService.java      # 指令服务接口
│   ├── SettlementService.java       # 结算服务接口
│   ├── SystemService.java           # 系统服务接口
│   ├── ...                          # 其他服务接口
│   └── impl/                        # 服务实现
│       ├── AccountServiceImpl.java      # 账户服务实现
│       ├── InstructionServiceImpl.java  # 指令服务实现
│       ├── SettlementServiceImpl.java   # 结算服务实现
│       ├── SystemServiceImpl.java       # 系统服务实现
│       └── ...                          # 其他服务实现
├── task/                             # 定时任务
├── thirdparty/                       # 第三方集成
│   ├── ccm/                         # CCM支付网关集成
│   ├── ois/                         # 场外系统集成
│   └── workflow/                    # 工作流集成
├── util/                            # 工具类
│   ├── DateUtils.java               # 日期工具类
│   ├── FileUtils.java               # 文件工具类
│   ├── JsonUtils.java               # JSON工具类
│   └── ValidationUtils.java         # 验证工具类
├── webservice/                      # Web服务
├── websocket/                       # WebSocket处理
└── workflow/                        # 工作流处理
```

### 子模块结构

#### cop-api API接口模块
```
com.hundsun.cop.api/
├── dto/                             # API数据传输对象
│   ├── AccountDto.java              # 账户DTO
│   ├── InstructionDto.java          # 指令DTO
│   ├── SettlementDto.java           # 结算DTO
│   └── ...                          # 其他DTO对象
└── service/                         # API服务接口
    ├── AccountApiService.java       # 账户API服务
    ├── InstructionApiService.java   # 指令API服务
    ├── SettlementApiService.java    # 结算API服务
    └── ...                          # 其他API服务接口
```

#### cop-gateway O32中间件模块
```
com.hundsun.cop.gateway/
├── CopGatewayStarter.java           # 网关启动类
├── config/                          # 网关配置
├── handler/                         # 处理器
└── service/                         # 网关服务
```

### 部署配置文件

```
deploy/
├── deploy.xml                   # 部署配置文件
├── scripts/                     # 部署脚本目录
│   └── cop_gateway/             # cop-gateway脚本
│       ├── install.sh           # 安装脚本
│       ├── afterInstall.sh      # 安装后处理脚本
│       ├── run_server.sh        # 启动脚本
│       ├── stop_server.sh       # 停止脚本
│       ├── validateStart.sh     # 启动状态检测脚本
│       ├── validateStop.sh      # 停止状态检测脚本
│       └── ...                  # 其他运维脚本
├── template/                    # 配置模板目录
│   ├── application.properties   # 应用配置模板
│   ├── password.properties      # 密码配置模板
│   ├── log4j2.xml              # 日志配置模板
│   ├── startup.sh              # 启动脚本模板
│   ├── shutdown.sh             # 停止脚本模板
│   └── getDump.sh              # 故障转储脚本模板
└── sqls/                       # SQL脚本目录
    └── ...                     # 数据库脚本
```

### 资源配置文件(位于src/main/resources)

```
resources/
├── application.properties           # 主配置文件
├── middleware.properties           # 中间件配置
├── log4j2.xml                      # 日志配置
├── mapper/                         # MyBatis映射文件
│   ├── AccountMapper.xml           # 账户映射
│   ├── InstructionMapper.xml       # 指令映射
│   ├── SettlementMapper.xml        # 结算映射
│   └── ...                         # 其他映射文件
├── META-INF/                       # 元数据配置
├── assemble/                       # 组装配置
├── chinese/                        # 中文资源
├── errorFormat/                    # 错误格式配置
├── lib/                            # 依赖库
├── pdf/                            # PDF模板
└── sqlTemplate/                    # SQL模板
```

## newtranPlugin 信创转换机插件

### 包结构描述

```
com.hundsun.cop.newtran/
├── ServerStarter.java               # 插件启动类
├── api/                             # API接口
├── bo/                              # 业务对象
│   ├── OperatorBo.java             # 操作员业务对象
│   └── NewtranTaskInfoBo.java      # 转换任务信息对象
├── dao/                             # 数据访问层
│   ├── OpDao.java                  # 操作员数据访问
│   ├── ISysParamDao.java           # 系统参数访问
│   └── IBasicDataDao.java          # 基础数据访问
├── dbclass/                        # 数据库实体类
│   └── SysParam.java               # 系统参数实体
├── dto/                            # 数据传输对象
│   ├── TaskConfigModelDto.java     # 任务配置模型DTO
│   ├── TransferFileInfoDto.java    # 转换文件信息DTO
│   └── ReportInfoDto.java          # 报告信息DTO
├── service/                        # 业务服务层
│   ├── CopNewtranService.java      # COP转换服务接口
│   ├── TransferTaskService.java    # 转换任务服务接口
│   ├── BasicDataService.java       # 基础数据服务接口
│   ├── ...                         # 其他服务接口
│   └── impl/                       # 服务实现
│       ├── CopNewtranServiceImpl.java     # COP转换服务实现
│       ├── TransferTaskServiceImpl.java   # 转换任务服务实现
│       ├── BasicDataServiceImpl.java      # 基础数据服务实现
│       └── ...                     # 其他服务实现
└── util/                           # 工具类
    ├── ThreadPoolUtil.java         # 线程池工具类
    └── ...                         # 其他工具类
```

### 资源配置文件

```
resources/
├── application.properties          # 应用配置
├── log4j2.xml                     # 日志配置
├── mapper/                        # MyBatis映射文件
│   ├── OpDao.xml                  # 操作员映射
│   ├── SysParamMapper.xml         # 系统参数映射
│   ├── IBasicDataDao.xml          # 基础数据映射
│   ├── NewtranTaskInfoMapper.xml  # 转换任务信息映射
│   └── ...                        # 其他映射文件
└── assemble/                      # 组装配置
    └── assembly.xml               # 打包配置
```

## fax-gateway 传真网关服务

### 根模块结构

```
fax-gateway/
├── pom.xml                         # 父POM文件
├── fax-gateway-api/                # API接口模块
├── fax-gateway-common/             # 通用模块
├── fax-gateway-app/                # 应用模块
├── fax-gateway-service/            # 服务模块
├── fax-gateway-instruct/           # 指令处理模块
└── fax-gateway-start/              # 启动模块
```

### 包结构描述

#### fax-gateway-start 启动模块
```
com.hundsun.fax.start/
└── FixGateWayStart.java            # 传真网关启动类
```

#### fax-gateway-service 服务模块
```
com.hundsun.fax.service/
├── convert/                        # 转换器
│   └── FaxRecordConvert.java       # 传真记录转换器
├── entitys/                        # 实体类
│   └── base/                       # 基础实体
│       ├── BaseFaxResultEntity.java    # 基础传真结果实体
│       ├── EastFaxResultEntity.java    # 东方传真结果实体
│       └── FaxFileRecordEntity.java    # 传真文件记录实体
└── services/                       # 服务层
    ├── BaseFaxService.java         # 基础传真服务
    ├── ...                         # 其他服务接口
    └── impl/                       # 服务实现
        ├── EastFaxWork.java        # 东方传真工作实现
        └── ...                     # 其他服务实现
```

#### fax-gateway-instruct 指令模块
```
com.hundsun.fax.instruct/
├── constants/                      # 常量定义
│   └── DataSourceUseEnums.java     # 数据源使用枚举
├── po/                             # 持久化对象
│   ├── EastFaxResultPo.java        # 东方传真结果PO
│   ├── FaxFileRecordPo.java        # 传真文件记录PO
│   └── ...                         # 其他持久化对象
└── service/                        # 服务接口
    ├── EastFaxResultService.java   # 东方传真结果服务
    ├── FaxFileRecordService.java   # 传真文件记录服务
    └── ...                         # 其他服务接口
```

#### fax-gateway-common 通用模块
```
com.hundsun.fax.common/
├── constants/                      # 常量定义
│   ├── cons/                       # 常量类
│   │   ├── LogConstants.java       # 日志常量
│   │   └── ...                     # 其他常量类
│   └── enums/                      # 枚举类
│       ├── DateFormatEnums.java            # 日期格式枚举
│       ├── FaxSendProcessOriginStateEnums.java # 传真发送状态枚举
│       ├── FaxTypeSupportEnums.java        # 传真类型支持枚举
│       ├── FuncEnums.java                  # 功能枚举
│       └── ...                             # 其他枚举类
```

### 资源配置文件

```
resources/
├── application.properties          # 应用配置
├── log4j2.xml                     # 日志配置
├── META-INF/                      # 元数据配置
│   └── additional-spring-configuration-metadata.json
└── assemble/                      # 组装配置
    └── assembly.xml               # 打包配置
```

### 部署配置文件

```
deploy/
├── deploy.xml                      # 部署配置文件
├── scripts/                        # 部署脚本目录
│   └── faxgateway/                 # 传真网关脚本
│       ├── install.sh              # 安装脚本
│       ├── afterInstall.sh         # 安装后处理脚本
│       ├── start.sh                # 启动脚本
│       ├── stop.sh                 # 停止脚本
│       ├── validateStart.sh        # 启动状态检测脚本
│       ├── validateStop.sh         # 停止状态检测脚本
│       └── ...                     # 其他运维脚本
├── template/                       # 配置模板目录
│   ├── application.properties      # 应用配置模板
│   ├── log4j2.xml                 # 日志配置模板
│   └── faxgateway/                # 传真网关配置模板
│       ├── start.sh               # 启动脚本模板
│       ├── stop.sh                # 停止脚本模板
│       └── ...                    # 其他配置模板
└── sqls/                          # SQL脚本目录
    └── ...                        # 数据库脚本
```

## mail-gateway 邮件网关服务

### 根模块结构

```
mail-gateway/
├── pom.xml                         # 父POM文件
├── mail-api/                       # API接口模块
└── mail-server/                    # 服务实现模块
```

### 包结构描述

#### mail-server 服务模块
```
com.hundsun.cop.mail/
├── MailGatewayStarter.java         # 邮件网关启动类
├── controller/                     # 控制器层
│   ├── MailController.java         # 邮件控制器
│   └── ...                         # 其他控制器
└── util/                          # 工具类
    ├── BizSecurity.java           # 业务安全工具类
    └── ...                        # 其他工具类
```

#### mail-api API模块
```
com.hundsun.cop.mail.api/
├── constant/                       # 常量定义
│   └── AuthModeEnum.java          # 认证模式枚举
├── entity/                        # 实体类
│   ├── AttachInfo.java            # 附件信息
│   ├── MailRes.java               # 邮件响应
│   └── ...                        # 其他实体类
└── service/                       # 服务接口
    ├── MailService.java           # 邮件服务接口
    ├── ...                        # 其他服务接口
    └── impl/                      # 服务实现
        ├── MailServiceImpl.java   # 邮件服务实现
        └── ...                    # 其他服务实现
```

### 资源配置文件

```
resources/
├── application.properties          # 应用配置
├── logback.xml                     # 日志配置(Logback)
└── assemble/                       # 组装配置
    └── assembly.xml                # 打包配置
```

### 部署配置文件

```
deploy/
├── deploy.xml                      # 部署配置文件
├── scripts/                        # 部署脚本目录
│   └── server/                     # 邮件服务器脚本
│       ├── install.sh              # 安装脚本
│       ├── afterInstall.sh         # 安装后处理脚本
│       ├── start.sh                # 启动脚本
│       ├── stop.sh                 # 停止脚本
│       ├── validateStart.sh        # 启动状态检测脚本
│       └── ...                     # 其他运维脚本
└── template/                       # 配置模板目录
    └── server/                     # 服务器配置模板
        ├── application.properties  # 应用配置模板
        ├── logback.xml            # 日志配置模板
        ├── start.sh               # 启动脚本模板
        ├── stop.sh                # 停止脚本模板
        └── ...                    # 其他配置模板
```
