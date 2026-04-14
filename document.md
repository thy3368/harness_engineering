## 封面
| Unnamed: 0 | Unnamed: 1 |
| --- | --- |
| NaN | NaN |
| NaN | NaN |
| NaN | NaN |
| NaN | NaN |
| NaN | NaN |
| NaN | NaN |
| NaN | 低码工具 |
| NaN | NaN |
| NaN | 业务功能树 |
| NaN | NaN |
| NaN | NaN |
| NaN | NaN |
| NaN | NaN |
| NaN | NaN |
| NaN | <技术平台总部-低码PDT> |
| NaN | NaN |
| NaN | 2024 年 6 月 |
| NaN | NaN |
| NaN | 说明：业务功能树作为产品需求规格清单，是产品规划、研发的依据，后续需持续进行更新，每个RP-TR5做交付件检查。 |

## 版本页
| Unnamed: 0 | 文档修改记录 | Unnamed: 2 | Unnamed: 3 | Unnamed: 4 | Unnamed: 5 | Unnamed: 6 |
| --- | --- | --- | --- | --- | --- | --- |
| NaN | 版本 | 修订人 | 参编人 | 修订说明 | 修订日期 | NaN |
| NaN | 1.0 | 张云纯 | NaN | 第一版 | 20240425 | NaN |
| NaN | 1.1 | 韦旭阳 | NaN | 基于新版本和L0图进行调整 | 20240614 | NaN |
| NaN | 1.2 | 斯炘 | NaN | 针对产品特性范围，对HSDDML语言域进行微调 | 20240621 | NaN |
| NaN | 1.3 | 严跃杰 | NaN | HSDDML语言 中的前后端引擎进行删减。设计实现模块，不需要在产品业务功能树中呈现。 | 20240628 | NaN |
| NaN | 1.4 | 斯炘 | 严跃杰、唐红尧、张亮、韦旭阳、韩喆、马欢乐 | 1、移除HSDDML部分\n2、DFX部分补充完成\n3、新增：业务运行引擎（控制台）业务功能（更新到语言版本1.10）\n4、物料资产按照通用要求表格新增分组\n5、IDE设计器按照对标livebos改版后的功能重新编写 | 20240721 | NaN |
| NaN | 1.5 | 斯炘 | 韦旭阳、夏亚静 | 基于TSE的建议，参照GB/T25000.10-2016、ISO9241-110标准，制定DFX需求规格中设计器易用性要求 | 20240724 | NaN |
| NaN | 1.6 | 斯炘 | NaN | 依据域L0级图一致性要求，追加应用管理sheet，待完善 | 20240731 | NaN |
| NaN | 1.7 | 斯炘 | 唐红尧 | 一级域依据L0业务架构图进行调整 | 20240808 | NaN |
| NaN | 1.8 | 斯炘 | 夏亚静、唐红尧 | 依据L0级图中的开发域、打包调试域设定进行业务功能树调整 | 20240814 | NaN |
| NaN | 1.9 | 斯炘 | NaN | 应用管理域一处笔误修改 | 20240816 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | …… | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | 说 明 | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | 本文档中所包含的信息属于商业机密信息，如无恒生电子股份有限公司的书面许可，任何人都无权复制或利用。 | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | 文档评审意见 | NaN | NaN | NaN | NaN | NaN |
| NaN | 评审日期 | 评审人 | 评审意见 | NaN | 状态 | 责任人 |
| NaN | 0712 | 严跃杰 | HSDDML语言规格按设计器生成的初始语言规格描述，即基本要跟设计器表达结构保持一致，不要分前后端。 | NaN | 待修改 | 斯炘 |
| NaN | 0712 | 严跃杰 | 1、IDE设计器规格要跟设计器业务功能树完全一致，并且要体现叶子节点的配置项\n2、应用运行引擎的内容移入应用运行引擎规格的sheet页面 | NaN | 待修改 | 马欢乐 |
| NaN | 0712 | 严跃杰 | 应用运行引擎待补充，需要体现应用运行引擎控制台的业务功能树 | NaN | 待修改 | 斯炘 |
| NaN | 0712 | 严跃杰 | 物料资产中心规格要跟物料资产中心的业务功能树完全一致 | NaN | 待修改 | 韩喆 |
| NaN | 0712 | 严跃杰 | 物料资产开发规范和工具 要补充开发规范文档 | NaN | 待修改 | 韩喆 |
| NaN | 0712 | 严跃杰 | DFX需求要贴上来 | NaN | 待修改 | 张亮 |

## 开发域
| 业务领域(一级) | 价值流（二级）（一级菜单） | 活动（三级）（二级菜单） | 任务（四级）（大纲树菜单项） | 子任务（五级）（大纲上资源操作） | 步骤（六级）（资源信息查看和操作） | 子步骤（七级）（Tab和抽屉） | 关键字段 | 语言 | 描述 | 业务规则 | 接口 | 实体 | DFX | 必填 | 备注(是否多选，前置依赖，限制要求 等) | 低码开发人员 | 资产管理运营人员 | 专业开发人员 | 语言版本 | 发布版本 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IDE设计器 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | NaN | NaN |
| NaN | 设计器设置 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | NaN | NaN |
| NaN | NaN | 正版管理（设计器） | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | license管理 | NaN | NaN | NaN | NaN | NaN | 设计器版本的合法性管理 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | license检查 | NaN | NaN | NaN | NaN | 校验license是否有效，有效才可以使用设计器 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | license查看 | NaN | NaN | NaN | NaN | 查看license的证书和有效期 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | license激活 | NaN | NaN | NaN | NaN | 离线激活license | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | 用户管理 | NaN | NaN | NaN | NaN | NaN | NaN | 目前暂不涉及 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | 暂未实现 | 暂未实现 |
| NaN | NaN | NaN | 用户账号管理 | NaN | NaN | NaN | NaN | NaN | 目前暂不涉及 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | 暂未实现 | 暂未实现 |
| NaN | NaN | NaN | 用户登录管理 | NaN | NaN | NaN | NaN | NaN | 目前暂不涉及 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | 暂未实现 | 暂未实现 |
| NaN | NaN | NaN | 用户会话管理 | NaN | NaN | NaN | NaN | NaN | 目前暂不涉及 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | 暂未实现 | 暂未实现 |
| NaN | NaN | NaN | 用户日志管理 | NaN | NaN | NaN | NaN | NaN | 目前暂不涉及 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | 暂未实现 | 暂未实现 |
| NaN | NaN | 权限管理 | NaN | NaN | NaN | NaN | NaN | NaN | 目前暂不涉及 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | 暂未实现 | 暂未实现 |
| NaN | NaN | NaN | 角色授权管理 | NaN | NaN | NaN | NaN | NaN | 目前暂不涉及 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | 暂未实现 | 暂未实现 |
| NaN | NaN | NaN | 资源许可管理 | NaN | NaN | NaN | NaN | NaN | 目前暂不涉及 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | 暂未实现 | 暂未实现 |
| NaN | NaN | NaN | 设计器功能许可管理 | NaN | NaN | NaN | NaN | NaN | 目前暂不涉及 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | 暂未实现 | 暂未实现 |
| NaN | NaN | NaN | 权限申请 | NaN | NaN | NaN | NaN | NaN | 目前暂不涉及 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | 暂未实现 | 暂未实现 |
| NaN | NaN | 版本管理 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | 默认设计器版本 | NaN | NaN | NaN | NaN | NaN | 打开旧版本设计器开发的应用工程时，设计器使用当前应用工程atom.config.js文件中配置的设计器版本，\n\n如果没有配置则使用语言版本默认的设计器版本 | NaN | /materialManage/engineManager/getEngineListDesigner | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | 升级设计器版本 | NaN | NaN | NaN | NaN | NaN | 允许用户主动切换版本，在设计器版本切换过程中需要进行风险提示，并执行升级脚本 | NaN | /materialManage/engineManager/getEngineListDesigner | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | 应用创建 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | 创建一个应用工程用于应用开发 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | 新建工程 | NaN | NaN | NaN | NaN | NaN | NaN | 初始化一个可以运行的demo工程 | 可被权限管控（可操作或不可操作） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | 打开本地工程 | NaN | NaN | NaN | NaN | NaN | NaN | 打开本地已有工程 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.9 | V202401.00 |
| NaN | NaN | 导入增量交付包 | NaN | NaN | NaN | NaN | NaN | NaN | 导入增量交付包，升级已有功能 | 可被权限管控（可操作或不可操作） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | 开发配置 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | 基础配置 | NaN | NaN | NaN | NaN | NaN | {\n "hddmlVersion": "1.9",\n "distPath": "Hc2Build",\n "sourcePath": "Hc2Res",\n "config": {\n "designer": {\n "base": {\n "repoEnvironment": "http://10.20.162.92:10099",\n "hepServerUrl": "http://hep.hundsun.com",\n "servieCode": "mkm,csmf",\n "productCode": "CP-S001398-1.0",\n "useHepPluginGetData": false,\n "localPreviewPort": "12347",\n "plugins": {},\n "useRepoServer": true,\n "useHep": true\n },\n "preview": {\n "urlPrefix": "/hc2page",\n "isHistoryMode": false,\n "frameLayout": "/frame-layout-local",\n "previewEnvironment": "http://10.20.36.203:8088",\n "subSystemApiHome": "/g/hswealth.csm/v",\n "useDefaultBackEngine": false\n },\n "hooks": {\n "postCodeGenerate": "Hc2GenCode/merge\_code.js",\n "handleProxy": "function (req, res, proxy) {\r\n if (req.url.indexOf(\"/g/hswealth.csm/v\") > -1) {\r\n req.url = req.url.replace(\"/g/hswealth.csm/v\", \"/g/hswealth.csm/v\");\r\n proxy.web(req, res, {\r\n target: \"http://10.20.29.168:8088\",\r\n changeOrigin: true,\r\n headers: { Cookie: `token=e9c187e9-9f74-48c3-a25a-6a9d805114c9;operator\_code=admin` },\r\n });\r\n return true;\r\n }\r\n }"\n },\n "export": {\n "mysql": {\n "sqlExportType": [\n "oracle"\n ]\n }\n }\n },\n "translator": {\n "translator\_generatecode": {\n "server": {\n "system-name": "CRM5.0",\n "module-name": "客户管理微服务(csmf)",\n "package": "com.hundsun.hswealth.csmf.biz.atom"\n },\n "\_tmp": {}\n }\n }\n },\n "dependencies": {\n "designerPlugins": {},\n "artifacts": {\n "backendEngine": "1.7.0-release",\n "frontendEngine": "1.7.0-release",\n "combineTool": "1.7.2-0521test",\n "codeGenerator": "1.7.2-0521test",\n "designer": "1.9.0"\n }\n }\n} | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | 资产中心配置 | NaN | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 是否使用资产中心服务(useRepoServer) | NaN | 是否使用资产中心服务：是、否 | 可被权限管控（只读或可编辑） | NaN | NaN | 默认值：是 | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 资产中心的服务地址(repoEnvironment) | NaN | 物料资产中心的服务器地址，http://开头 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 资产中心的AccessKey(repoEnvironmentAccessKey) | NaN | 用于资产中心请求数据时，对访问用户进行鉴权 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | HEP配置 | NaN | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | hep服务地址(hepServerUrl) | NaN | 请求HEP数据时，HEP的访问地址，http://开头 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 产品编号(productCode) | NaN | 工程对应的HEP产品编号，一个工程只能配置一个产品绑定 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | hep微服务编号(servieCode) | NaN | 产品所对应的所有微服务；设计器在设计时取HEP数据以产品/微服务为单位读取数据，一个工程只能配置多个微服务绑定 | 可被权限管控（只读或可编辑） | /g/external/v/external/microservice/getList | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 是否启用从hep插件读取数据(useHepPluginGetData) | NaN | 是否启用从hep插件读取数据：是、否。\n是只能读取本地插件提供的数据；否则设计时在线读取HEP元数据 | 可被权限管控（只读或可编辑） | NaN | NaN | 默认值：否 | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | 出码配置 | NaN | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 是否出码模式(outputType) | NaN | 是否出码模式：是、否 | 可被权限管控（只读或可编辑） | NaN | NaN | 否 | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 出码引擎版本号(codeGenerator) | NaN | 出码引擎版本号 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 出码回调路径(postCodeGenerate) | NaN | 出码回调路径 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 系统名称(systemName) | NaN | 系统名称 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 模块名称(moduleName) | NaN | 模块名称 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 包路径(package) | NaN | 包路径 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 预览联调远程地址(previewEnvironment) | NaN | 预览联调远程地址 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 预览联调远程系统上外框架的访问路径(frameLayout) | NaN | 预览联调远程系统上外框架的访问路径 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 预览联调子系统前缀(urlPrefix) | NaN | 预览联调子系统前缀 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 预览联调远程系统上外框架的路由模式是否为history(isHistoryMode) | NaN | 预览联调远程系统上外框架的路由模式是否为history：是、否 | 可被权限管控（只读或可编辑） | NaN | NaN | 是 | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | 设计器插件配置 | NaN | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 设计器插件(designerPlugins) | NaN | 设计器插件 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 设计器插件配置(plugins) | NaN | 设计器插件配置 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | 资源前缀配置 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 数据表(table) | NaN | 新增数据表，ID前缀配置 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 实体(businessComponent) | NaN | 新增实体，ID前缀配置 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 对象(businessObject) | NaN | 新增对象，ID前缀配置 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 页面(page) | NaN | 新增页面，ID前缀配置 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 逻辑(businessService) | NaN | 新增逻辑，ID前缀配置 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 模块(module) | NaN | 新增模块，ID前缀配置 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 字典(pickList) | NaN | 新增字典，ID前缀配置 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 插件(plugin) | NaN | 新增插件，ID前缀配置 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 数据源(dataSource) | NaN | 新增数据源，ID前缀配置 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 工作流(workflow) | NaN | 新增工作流，ID前缀配置 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | 环境配置 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | 环境配置 | NaN | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | 新增环境信息 | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 标识(id) | NaN | 运行环境的标识，唯一 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 名称(name) | NaN | 运行环境的名称 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 地址(address) | NaN | 运行环境的访问地址，http://开头 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 用户名(userName) | NaN | 运行环境的用户名 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 密码(password) | NaN | 运行环境的密码 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 服务端参数(serverConfig) | NaN | 运行环境部署需要用到的服务端参数 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 前端参数(clientConfig) | NaN | 运行环境部署需要用到的前端参数 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | 验证环境联通性 | NaN | NaN | NaN | NaN | 验证运行环境是否可以联通 | 可被权限管控（只读或可编辑） | /manager-app/hcreator/manager/manage/ping | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | 删除环境信息 | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | 编辑环境信息 | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | 环境配置项 | NaN | NaN | NaN | NaN | NaN | 运行环境部署需要用到的服务端和前端全局参数，如果环境配置中没有配置参数值则以全局参数为准 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | 新增服务端参数 | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 参数名(key) | NaN | 参数名 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 参数值(defaultValue) | NaN | 参数值 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 描述(desc) | NaN | 描述 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | 删除服务端参数 | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | 编辑服务端参数 | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | 新增前端参数 | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 参数名(key) | NaN | 参数名 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 参数值(defaultValue) | NaN | 参数值 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 描述(desc) | NaN | 描述 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | 删除前端参数 | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | 编辑前端参数 | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | SQL导出配置 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | mysql配置 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | mysql引擎(engine) | NaN | mysql引擎：InnoDB、MylSAM | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 编码格式(encode) | NaN | 编码格式：utf8mb4、utf8mb3 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 校对规则(checkRule) | NaN | 校对格式包含4个选项 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | oracle配置 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | 应用定义 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | 基本信息 | NaN | NaN | NaN | NaN | NaN | <application id="application\_standard" title="CRM低码应用" version="1.0.0" desc="客户管理 csmf" hddmlVersion="1.8">\n <abac>\n </abac>\n</application> | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | 新增基本信息 | NaN | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 应用(id) | NaN | 仅支持英文、数字、下划线，长度<=32 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 应用标题(title) | NaN | 应用标题，不支持<>&"'，长度<=100 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 应用版本号(version) | NaN | 长度<=20，只能输入数字和"."，首位不能输入"." | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 描述(desc) | NaN | 描述，长度<=300 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | 参数 | NaN | NaN | NaN | NaN | NaN | <parameters id="parameters">\n <parameter key="test1" value="1">\n </parameter>\n <parameter key="test2" value="2">\n </parameter>\n</parameters> | NaN | 可被权限管控（只读或可编辑） | hep接口：/g/external/v/external/generate/list | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | 新增参数 | NaN | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 参数(key) | NaN | 参数名称，仅支持英文、数字、"\_"、"."、"$"，长度<=30 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 参数类型(parameterType) | NaN | 参数类型，数据来源应用定义-数据类型-物理类型 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | NaN | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 参数值(value) | NaN | 参数值，长度<=100 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 名称(name) | NaN | 参数名称，不支持<>&"'，长度<=100 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 描述(desc) | NaN | 描述，长度<=300 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 绑定插件(repo) | NaN | 下拉选择，数据来源于应用定义-插件 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | 同步参数 | NaN | NaN | NaN | NaN | NaN | 配置了hep信息，可以从hep同步 | 可被权限管控（只读或可编辑） | g/external/v/external/generate/list | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | 删除参数 | NaN | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | 编辑参数 | NaN | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | 查询参数 | NaN | NaN | NaN | NaN | NaN | 1、通过参数名称、描述查询参数\n2、显示参数名称、参数值、描述，不分页 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | 触发器 | NaN | NaN | NaN | NaN | NaN | <applicationEventTriggers>\n <applicationEventTrigger id="trigger\_shhirv3c29" eventType="BUSINESS\_COMPONENT\_CREATE\_EVENT" eventStage="BEFORE" order="99" desc="新增时设置创建日期，更新日期，创建人，更新人">\n <businessScript language="JAVASCRIPT"></businessScript>\n <businessServiceRef>DataChangeInsertStandardSysFieldTrigger</businessServiceRef>\n </applicationEventTrigger>\n <applicationEventTrigger id="trigger\_8cj1nu82edn" eventType="BUSINESS\_COMPONENT\_UPDATE\_EVENT" eventStage="BEFORE" order="99" desc="修改时设置更新改日期，更新人">\n <businessScript language="JAVASCRIPT"></businessScript>\n <businessServiceRef>DataChangeUpdateStandardSysFieldTrigger</businessServiceRef>\n </applicationEventTrigger>\n</applicationEventTriggers> | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | 新增触发器 | NaN | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 类型(eventType) | NaN | 应用触发器类型，选择项包含12种事件 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 时机(eventStage) | NaN | 事件时机，选择项有“之前”和“之后” | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 优先级(order) | NaN | 非零整数，相同事件类型，序号小先执行，仅支持>=0的整数 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 描述(desc) | NaN | 描述，长度<=300 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 绑定类型(handlerType) | NaN | 绑定类型，选项包括绑定逻辑、绑定插件、绑定业务脚本 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 绑定的逻辑(businessServiceRef) | NaN | 下拉选择，数据来源于开发设计-模块-逻辑 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | 删除触发器 | NaN | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | 编辑触发器 | NaN | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | 查询触发器 | NaN | NaN | NaN | NaN | NaN | 1、通过类型、时机、绑定逻辑、描述查询触发器\n2、显示类型、时机、优先级、绑定逻辑、描述，不分页 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | 内置协议 | NaN | NaN | NaN | NaN | NaN | <responseAdaptor id="responseAdaptor">\n <spreadEnabled>true</spreadEnabled>\n <errorCodeField source="code" transfer="1">\n </errorCodeField>\n <errorMessageField source="message" transfer="2">\n </errorMessageField>\n</responseAdaptor> | NaN | 可被权限管控（只读或可编辑） | hep接口：/g/external/v/external/microservice/getList | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | 内置协议配置 | NaN | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 协议项(title) | NaN | 预置响应错误码字段、响应错误消息字段 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 参数值(source) | NaN | 预置code、message | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 转换字段(transfer) | NaN | 转换字段，比如code转换为errnum、message转换为errmessage | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | 平铺接口 | NaN | NaN | NaN | NaN | NaN | 平铺接口开关打开后，入栈适配器会对对象、逻辑和字典额外暴露带资源类型、资源id（可选）和资源方法名的URL，格式为如下两种之一：\n\n/hcreator2/v2/invoke/资源类型/资源id/资源方法名\n/hcreator2/v2/invoke/资源类型/资源批量方法名 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | 开放接口 | NaN | NaN | NaN | NaN | NaN | <openApi>\n <![CDATA[{"openApis":[{"protocols":[{"name":"T3","functionId":"mkm.deleteVisitrecordAtomInner","apiUrl":"deleteVisitrecordAtomInner"},{"name":"HTTP","path":"deleteVisitrecordAtomInner","method":"POST"}],"inputs":{"pageSize":"","pageNum":"","commonParams":[{"name":"mac\_address","label":"mac地址","required":"false","dataType":"String","defaultValue":"\" \""},{"name":"operator\_code","label":"操作员代码","required":"false","dataType":"String","defaultValue":"\" \""},{"name":"tenant\_id","label":"租户号","required":"false","dataType":"String","defaultValue":"\" \""},{"name":"op\_station","label":"站点地址","required":"false","dataType":"String","defaultValue":"\" \""},{"name":"op\_org\_id","label":"操作员所属组织","required":"false","dataType":"String","defaultValue":"\" \""},{"name":"user\_token","label":"访问令牌","required":"false","dataType":"String","defaultValue":"\" \""}],"sortFields":[],"boParams":[{"name":"visitrecord\_id","label":"服务记录编号","bcRef":"mkmVisitrecord","bcFieldName":"ROW\_ID","required":"true","defaultValue":"","children":[],"dataType":"String","isCollection":"false","operator":"EQUALS"}]},"outputs":{"code":"error\_no","message":"error\_info","total":"","pageSize":"","pageNum":"","boParams":[],"commonParams":[{"name":"error\_no","label":"错误号","dataType":"Int","defaultValue":"0"},{"name":"error\_info","label":"错误信息","dataType":"String","defaultValue":""}]},"id":"deleteVisitrecordAtomInner","name":"删除服务记录","apiType":"DELETE","apiCategory":"inner","fieldFormatBsRef":"","boId":"mkmVisitrecord","desc":""},{"protocols":[{"name":"HTTP","path":"getVisitrecordAtomInner","method":"POST"},{"name":"T3","functionId":"mkm.getVisitrecordAtomInner","apiUrl":"getVisitrecordAtomInner"}],"inputs":{"pageSize":"page\_size","pageNum":"page\_no","commonParams":[{"name":"mac\_address","label":"mac地址","required":"false","dataType":"String","defaultValue":"\" \""},{"name":"operator\_code","label":"操作员代码","required":"false","dataType":"String","defaultValue":"\" \""},{"name":"tenant\_id","label":"租户号","required":"false","dataType":"String","defaultValue":"\" \""},{"name":"op\_station","label":"站点地址","required":"false","dataType":"String","defaultValue":"\" \""},{"name":"op\_org\_id","label":"操作员所属组织","required":"false","dataType":"String","defaultValue":"\" \""},{"name":"user\_token","label":"访问令牌","required":"false","dataType":"String","defaultValue":"\" \""},{"name":"page\_no","label":"页码","dataType":"Int","defaultValue":"1","required":"false"},{"name":"page\_size","label":"每页数量","dataType":"Int","defaultValue":"20","required":"false"},{"name":"restrictResOwnershipCodes","label":"限定数据权限所有者","dataType":"String","defaultValue":"","required":"false"},{"name":"restrictViewCodesOfResOwnership","label":"限定数据权限所有者视角","dataType":"String","defaultValue":"","required":"false"}],"boParams":[{"name":"owner\_id\_array","label":"所有人id数组","dataType":"String","bcRef":"mkmVisitrecord","bcFieldName":"","required":"false","isCollection":"true","operator":"CONTAINS","defaultValue":"","searchSpec":"CREATE\_USER in {} or participater\_codes in {}","children":[]},{"name":"chn\_code\_root","label":"渠道编号（下钻）","dataType":"String","bcRef":"mkmVisitrecord","bcFieldName":"chn\_code","required":"false","isCollection":"false","operator":"RLIKE","defaultValue":"","children":[]},{"name":"creator\_array","label":"创建人数组","dataType":"String","bcRef":"mkmVisitrecord","bcFieldName":"CREATE\_USER","required":"false","isCollection":"true","operator":"CONTAINS","defaultValue":"","children":[]},{"label":"客户联系人数组","bcRef":"mkmVisitrecord","name":"customer\_contact\_id\_array","dataType":"String","children":[],"bcFieldName":"customer\_contact\_ids","required":"false","operator":"CONTAINS","isCollection":"true"},{"label":"渠道联系人数组","bcRef":"mkmVisitrecord","name":"channel\_contact\_id\_array","dataType":"String","children":[],"bcFieldName":"channel\_contact\_ids","required":"false","operator":"CONTAINS","isCollection":"true"},{"name":"visitrecord\_id\_array","label":"服务记录编号数组","dataType":"String","bcRef":"mkmVisitrecord","bcFieldName":"ROW\_ID","required":"false","isCollection":"true","operator":"CONTAINS","defaultValue":"","children":[]},{"name":"daily\_id","label":"日报id","bcRef":"mkmVisitrecord","bcFieldName":"daily\_id","required":"false","defaultValue":"","children":[],"dataType":"String","operator":"CONTAINS","isCollection":"true"},{"name":"week\_id","label":"周报id","bcRef":"mkmVisitrecord","bcFieldName":"week\_id","required":"false","defaultValue":"","children":[],"dataType":"String","operator":"CONTAINS","isCollection":"true"},{"name":"creator","label":"创建人","bcRef":"mkmVisitrecord","bcFieldName":"CREATE\_USER","required":"false","defaultValue":"","children":[],"dataType":"String","operator":"EQUALS","isCollection":"false"},{"name":"daily\_status","label":"提交状态","bcRef":"mkmVisitrecord","bcFieldName":"daily\_status","required":"false","defaultValue":"","dataType":"String","children":[],"operator":"EQUALS","isCollection":"false"},{"name":"client\_id\_array","label":"客户编号","dataType":"String","bcRef":"mkmVisitrecord","bcFieldName":"client\_id","required":"false","isCollection":"true","operator":"CONTAINS","defaultValue":"","children":[]},{"name":"chn\_code\_array","label":"渠道编号","dataType":"String","bcRef":"mkmVisitrecord","bcFieldName":"chn\_code","required":"false","isCollection":"true","operator":"CONTAINS","defaultValue":"","children":[]},{"name":"end\_visit\_date","label":"服务日期结束","dataType":"BigInt","bcRef":"mkmVisitrecord","bcFieldName":"visit\_date","required":"false","isCollection":"false","operator":"LESS\_THAN\_OR\_EQUAL\_TO","defaultValue":"","children":[]},{"name":"visitrecord\_id","label":"服务记录编号","bcRef":"mkmVisitrecord","bcFieldName":"ROW\_ID","required":"false","defaultValue":"","children":[],"dataType":"String","operator":"EQUALS","isCollection":"false"},{"name":"start\_visit\_date","label":"服务日期开始","bcRef":"mkmVisitrecord","bcFieldName":"visit\_date","required":"false","defaultValue":"","children":[],"dataType":"BigInt","operator":"GREATER\_THAN\_OR\_EQUAL\_TO","isCollection":"false"},{"name":"visit\_object\_type","label":"服务对象类型","bcRef":"mkmVisitrecord","bcFieldName":"visit\_object\_type","required":"false","defaultValue":"","children":[],"dataType":"String","operator":"EQUALS","isCollection":"false"},{"name":"visit\_type","label":"服务方式","bcRef":"mkmVisitrecord","bcFieldName":"visit\_type","required":"false","defaultValue":"","children":[],"dataType":"String","operator":"EQUALS","isCollection":"false"},{"name":"visit\_title","label":"服务主题","bcRef":"mkmVisitrecord","bcFieldName":"visit\_title","required":"false","defaultValue":"","children":[],"dataType":"String","operator":"EQUALS","isCollection":"false"}],"sortFields":[{"bcId":"mkmVisitrecord","fieldName":"visit\_date","asc":"false"}]},"outputs":{"code":"error\_no","message":"error\_info","total":"total","pageSize":"","pageNum":"current\_page","commonParams":[{"name":"error\_no","label":"错误号","dataType":"Int","defaultValue":"0"},{"name":"error\_info","label":"错误信息","dataType":"String","defaultValue":""},{"name":"total","label":"总记录数","dataType":"Int","defaultValue":""},{"name":"current\_page","label":"当前页码","dataType":"Int","defaultValue":""}],"boParams":[{"name":"rows","label":"数据","dataType":"Map","bcRef":"mkmVisitrecord","bcFieldName":"","isCollection":"true","isPicklist":"false","children":[{"name":"dept\_name","label":"部门名称","dataType":"String","bcRef":"mkmVisitrecord","bcFieldName":"org\_id","isCollection":"false","isPicklist":"true","children":[]},{"name":"creator\_name","label":"创建人名称","dataType":"String","bcRef":"mkmVisitrecord","bcFieldName":"CREATE\_USER","isCollection":"false","isPicklist":"true","children":[]},{"name":"participater\_code\_names","label":"同行人员名称","dataType":"String","bcRef":"mkmVisitrecord","bcFieldName":"participater\_codes","isCollection":"true","isPicklist":"true","children":[]},{"name":"product\_codes\_name","label":"产品名称","dataType":"String","bcRef":"mkmVisitrecord","bcFieldName":"product\_codes","isCollection":"true","isPicklist":"true","children":[]},{"name":"channel\_contact\_names","label":"渠道联系人名称","dataType":"String","bcRef":"mkmVisitrecord","bcFieldName":"channel\_contact\_ids","isCollection":"true","isPicklist":"true","children":[]},{"name":"customer\_contact\_names","label":"客户联系人名称","dataType":"String","bcRef":"mkmVisitrecord","bcFieldName":"customer\_contact\_ids","isCollection":"true","isPicklist":"true","children":[]},{"name":"chn\_names","label":"渠道名称","dataType":"String","bcRef":"mkmVisitrecord","bcFieldName":"chn\_code","isCollection":"true","isPicklist":"true","children":[]},{"name":"client\_names","label":"客户名称","dataType":"String","bcRef":"mkmVisitrecord","bcFieldName":"client\_id","isCollection":"true","isPicklist":"true","children":[]},{"name":"daily\_status\_name","label":"提交状态名称","dataType":"String","bcRef":"mkmVisitrecord","bcFieldName":"daily\_status","isCollection":"false","isPicklist":"true","children":[]},{"name":"visit\_title\_name","label":"服务主题名称","dataType":"String","bcRef":"mkmVisitrecord","bcFieldName":"visit\_title","isCollection":"false","isPicklist":"true","children":[]},{"name":"visit\_type\_name","label":"服务方式名称","dataType":"String","bcRef":"mkmVisitrecord","bcFieldName":"visit\_type","isCollection":"false","isPicklist":"true","children":[]},{"name":"visit\_object\_type\_name","label":"服务对象类型名称","dataType":"String","bcRef":"mkmVisitrecord","bcFieldName":"visit\_object\_type","isCollection":"false","isPicklist":"true","children":[]},{"name":"visitrecord\_id","label":"服务记录编号","bcRef":"mkmVisitrecord","bcFieldName":"ROW\_ID","required":"true","defaultValue":"","children":[],"dataType":"String","isCollection":"false","isPicklist":"false"},{"name":"visit\_date","label":"服务日期","bcRef":"mkmVisitrecord","bcFieldName":"visit\_date","required":"false","defaultValue":"","children":[],"dataType":"BigInt","isCollection":"false","isPicklist":"false"},{"name":"visit\_object\_type","label":"服务对象类型","bcRef":"mkmVisitrecord","bcFieldName":"visit\_object\_type","required":"true","defaultValue":"","children":[],"dataType":"String","isCollection":"false","isPicklist":"false"},{"name":"visit\_type","label":"服务方式","bcRef":"mkmVisitrecord","bcFieldName":"visit\_type","required":"false","defaultValue":"","children":[],"dataType":"String","isCollection":"false","isPicklist":"false"},{"name":"visit\_title","label":"服务主题","bcRef":"mkmVisitrecord","bcFieldName":"visit\_title","required":"false","defaultValue":"","children":[],"dataType":"String","isCollection":"false","isPicklist":"false"},{"name":"visit\_start\_date\_time","label":"服务开始时间","bcRef":"mkmVisitrecord","bcFieldName":"visit\_start\_date\_time","required":"false","defaultValue":"","children":[],"dataType":"BigInt","isCollection":"false","isPicklist":"false"},{"name":"visit\_end\_date\_time","label":"服务结束时间","bcRef":"mkmVisitrecord","bcFieldName":"visit\_end\_date\_time","required":"false","defaultValue":"","children":[],"dataType":"BigInt","isCollection":"false","isPicklist":"false"},{"name":"visit\_time","label":"服务时长","bcRef":"mkmVisitrecord","bcFieldName":"visit\_time","required":"true","defaultValue":"","children":[],"dataType":"BigInt","isCollection":"false","isPicklist":"false"},{"name":"address","label":"地址","bcRef":"mkmVisitrecord","bcFieldName":"address","required":"false","defaultValue":"","children":[],"dataType":"String","isCollection":"false","isPicklist":"false"},{"name":"visit\_content","label":"服务内容","bcRef":"mkmVisitrecord","bcFieldName":"visit\_content","required":"false","defaultValue":"","children":[],"dataType":"String","isCollection":"false","isPicklist":"false"},{"name":"daily\_status","label":"提交状态","bcRef":"mkmVisitrecord","bcFieldName":"daily\_status","required":"false","defaultValue":"","children":[],"dataType":"String","isCollection":"false","isPicklist":"false"},{"name":"creator","label":"创建人","bcRef":"mkmVisitrecord","bcFieldName":"CREATE\_USER","required":"false","defaultValue":"","children":[],"dataType":"String","isCollection":"false","isPicklist":"false"},{"name":"create\_date\_time","label":"创建日期时间","bcRef":"mkmVisitrecord","bcFieldName":"CREATE\_TIME","required":"true","defaultValue":"","children":[],"dataType":"BigInt","isCollection":"false","isPicklist":"false"},{"name":"update\_date\_time","label":"更新日期时间","bcRef":"mkmVisitrecord","bcFieldName":"UPDATE\_TIME","required":"true","defaultValue":"","children":[],"dataType":"BigInt","isCollection":"false","isPicklist":"false"},{"name":"other\_participater\_name","label":"同行人员（录入）","bcRef":"mkmVisitrecord","bcFieldName":"other\_participater\_name","required":"false","defaultValue":"","children":[],"dataType":"String","isCollection":"false","isPicklist":"false"},{"name":"org\_id","label":"组织编号","bcRef":"mkmVisitrecord","bcFieldName":"org\_id","required":"false","defaultValue":"","children":[],"dataType":"String","isCollection":"false","isPicklist":"false"},{"name":"follow\_act\_remark","label":"后续服务计划","bcRef":"mkmVisitrecord","bcFieldName":"follow\_act\_remark","required":"false","defaultValue":"","children":[],"dataType":"String","isCollection":"false","isPicklist":"false"},{"name":"daily\_id","label":"日报id","bcRef":"mkmVisitrecord","bcFieldName":"daily\_id","required":"false","defaultValue":"","children":[],"dataType":"String","isCollection":"false","isPicklist":"false"},{"name":"week\_id","label":"周报id","bcRef":"mkmVisitrecord","bcFieldName":"week\_id","required":"false","defaultValue":"","children":[],"dataType":"String","isCollection":"false","isPicklist":"false"},{"name":"broker\_position\_id","label":"打卡编号","bcRef":"mkmVisitrecord","bcFieldName":"broker\_position\_id","required":"false","defaultValue":"","children":[],"dataType":"String","isCollection":"false","isPicklist":"false"},{"name":"memo","label":"备注","bcRef":"mkmVisitrecord","bcFieldName":"memo","required":"false","defaultValue":"","children":[],"dataType":"String","isCollection":"false","isPicklist":"false"},{"label":"客户","bcRef":"mkmVisitrecord","name":"client\_id","dataType":"String","children":[],"bcFieldName":"client\_id","isCollection":"true","isPicklist":"false"},{"label":"客户联系人","bcRef":"mkmVisitrecord","name":"customer\_contact\_ids","dataType":"String","children":[],"bcFieldName":"customer\_contact\_ids","isCollection":"true","isPicklist":"false"},{"label":"渠道","bcRef":"mkmVisitrecord","name":"chn\_code","dataType":"String","children":[],"bcFieldName":"chn\_code","isCollection":"true","isPicklist":"false"},{"label":"渠道联系人","bcRef":"mkmVisitrecord","name":"channel\_contact\_ids","dataType":"String","children":[],"bcFieldName":"channel\_contact\_ids","isCollection":"true","isPicklist":"false"},{"label":"产品","bcRef":"mkmVisitrecord","name":"product\_codes","dataType":"String","children":[],"bcFieldName":"product\_codes","isCollection":"true","isPicklist":"false"},{"label":"同行人员","bcRef":"mkmVisitrecord","name":"participater\_codes","dataType":"String","children":[],"bcFieldName":"participater\_codes","isCollection":"true","isPicklist":"false"}]}]},"id":"getVisitrecordAtomInner","name":"查询服务记录","apiType":"QUERY\_PAGE","apiCategory":"inner","fieldFormatBsRef":"OpenApiTriggerImpl","boId":"mkmVisitrecord","desc":""},{"protocols":[{"name":"HTTP","path":"postVisitrecordAtomInner","method":"POST"},{"name":"T3","functionId":"mkm.postVisitrecordAtomInner","apiUrl":"postVisitrecordAtomInner"}],"inputs":{"pageSize":"","pageNum":"","commonParams":[{"name":"mac\_address","label":"mac地址","required":"false","dataType":"String","defaultValue":"\" \""},{"name":"operator\_code","label":"操作员代码","required":"false","dataType":"String","defaultValue":"\" \""},{"name":"tenant\_id","label":"租户号","required":"false","dataType":"String","defaultValue":"\" \""},{"name":"op\_station","label":"站点地址","required":"false","dataType":"String","defaultValue":"\" \""},{"name":"op\_org\_id","label":"操作员所属组织","required":"false","dataType":"String","defaultValue":"\" \""},{"name":"user\_token","label":"访问令牌","required":"false","dataType":"String","defaultValue":"\" \""}],"boParams":[{"name":"visitrecord","label":"服务记录","dataType":"Map","bcRef":"mkmVisitrecord","bcFieldName":"","required":"false","isCollection":"false","operator":"","defaultValue":"","children":[{"name":"visit\_date","label":"服务日期","bcRef":"mkmVisitrecord","bcFieldName":"visit\_date","required":"false","defaultValue":"","children":[],"dataType":"BigInt","isCollection":"false"},{"name":"visit\_object\_type","label":"服务对象类型","bcRef":"mkmVisitrecord","bcFieldName":"visit\_object\_type","required":"false","defaultValue":"","children":[],"dataType":"String","isCollection":"false"},{"name":"visit\_type","label":"服务方式","bcRef":"mkmVisitrecord","bcFieldName":"visit\_type","required":"false","defaultValue":"","children":[],"dataType":"String","isCollection":"false"},{"name":"visit\_title","label":"服务主题","bcRef":"mkmVisitrecord","bcFieldName":"visit\_title","required":"false","defaultValue":"","children":[],"dataType":"String","isCollection":"false"},{"name":"visit\_start\_date\_time","label":"服务开始时间","bcRef":"mkmVisitrecord","bcFieldName":"visit\_start\_date\_time","required":"false","defaultValue":"","children":[],"dataType":"BigInt","isCollection":"false"},{"name":"visit\_end\_date\_time","label":"服务结束时间","bcRef":"mkmVisitrecord","bcFieldName":"visit\_end\_date\_time","required":"false","defaultValue":"","children":[],"dataType":"BigInt","isCollection":"false"},{"name":"visit\_time","label":"服务时长","bcRef":"mkmVisitrecord","bcFieldName":"visit\_time","required":"false","defaultValue":"","children":[],"dataType":"BigInt","isCollection":"false"},{"name":"address","label":"地址","bcRef":"mkmVisitrecord","bcFieldName":"address","required":"false","defaultValue":"","children":[],"dataType":"String","isCollection":"false"},{"name":"visit\_content","label":"服务内容","bcRef":"mkmVisitrecord","bcFieldName":"visit\_content","required":"false","defaultValue":"","children":[],"dataType":"String","isCollection":"false"},{"name":"daily\_status","label":"提交状态","bcRef":"mkmVisitrecord","bcFieldName":"daily\_status","required":"false","defaultValue":"","children":[],"dataType":"String","isCollection":"false"},{"name":"other\_participater\_name","label":"同行人员（录入）","bcRef":"mkmVisitrecord","bcFieldName":"other\_participater\_name","required":"false","defaultValue":"","children":[],"dataType":"String","isCollection":"false"},{"name":"org\_id","label":"组织编号","bcRef":"mkmVisitrecord","bcFieldName":"org\_id","required":"false","defaultValue":"","children":[],"dataType":"String","isCollection":"false"},{"name":"follow\_act\_remark","label":"后续服务计划","bcRef":"mkmVisitrecord","bcFieldName":"follow\_act\_remark","required":"false","defaultValue":"","children":[],"dataType":"String","isCollection":"false"},{"name":"daily\_id","label":"日报id","bcRef":"mkmVisitrecord","bcFieldName":"daily\_id","required":"false","defaultValue":"","children":[],"dataType":"String","isCollection":"false"},{"name":"week\_id","label":"周报id","bcRef":"mkmVisitrecord","bcFieldName":"week\_id","required":"false","defaultValue":"","children":[],"dataType":"String","isCollection":"false"},{"name":"broker\_position\_id","label":"打卡编号","bcRef":"mkmVisitrecord","bcFieldName":"broker\_position\_id","required":"false","defaultValue":"","children":[],"dataType":"String","isCollection":"false"},{"name":"memo","label":"备注","bcRef":"mkmVisitrecord","bcFieldName":"memo","required":"false","defaultValue":"","children":[],"dataType":"String","isCollection":"false"},{"label":"客户","bcRef":"mkmVisitrecord","name":"client\_id","dataType":"String","children":[],"bcFieldName":"client\_id","required":"false","isCollection":"true"},{"label":"客户联系人","bcRef":"mkmVisitrecord","name":"customer\_contact\_ids","dataType":"String","children":[],"bcFieldName":"customer\_contact\_ids","required":"false","isCollection":"true"},{"label":"渠道","bcRef":"mkmVisitrecord","name":"chn\_code","dataType":"String","children":[],"bcFieldName":"chn\_code","required":"false","isCollection":"true"},{"label":"渠道联系人","bcRef":"mkmVisitrecord","name":"channel\_contact\_ids","dataType":"String","children":[],"bcFieldName":"channel\_contact\_ids","required":"false","isCollection":"true"},{"label":"产品","bcRef":"mkmVisitrecord","name":"product\_codes","dataType":"String","children":[],"bcFieldName":"product\_codes","required":"false","isCollection":"true"},{"label":"同行人员","bcRef":"mkmVisitrecord","name":"participater\_codes","dataType":"String","children":[],"bcFieldName":"participater\_codes","required":"false","isCollection":"true"}]}],"sortFields":[]},"outputs":{"code":"error\_no","message":"error\_info","total":"","pageSize":"","pageNum":"","commonParams":[{"name":"error\_no","label":"错误号","dataType":"Int","defaultValue":"0"},{"name":"error\_info","label":"错误信息","dataType":"String","defaultValue":""}],"boParams":[{"name":"visitrecord\_id","label":"服务记录编号","bcRef":"mkmVisitrecord","bcFieldName":"ROW\_ID","children":[],"dataType":"String","isCollection":"false"}]},"id":"postVisitrecordAtomInner","name":"新增服务记录","apiType":"INSERT","apiCategory":"inner","fieldFormatBsRef":"OpenApiTriggerImpl","boId":"mkmVisitrecord","desc":""},{"protocols":[{"name":"HTTP","path":"putVisitrecordAtomInner","method":"POST"},{"name":"T3","functionId":"mkm.putVisitrecordAtomInner","apiUrl":"putVisitrecordAtomInner"}],"inputs":{"pageSize":"","pageNum":"","commonParams":[{"name":"mac\_address","label":"mac地址","required":"false","dataType":"String","defaultValue":"\" \""},{"name":"operator\_code","label":"操作员代码","required":"false","dataType":"String","defaultValue":"\" \""},{"name":"tenant\_id","label":"租户号","required":"false","dataType":"String","defaultValue":"\" \""},{"name":"op\_station","label":"站点地址","required":"false","dataType":"String","defaultValue":"\" \""},{"name":"op\_org\_id","label":"操作员所属组织","required":"false","dataType":"String","defaultValue":"\" \""},{"name":"user\_token","label":"访问令牌","required":"false","dataType":"String","defaultValue":"\" \""}],"boParams":[{"name":"visitrecord","label":"服务记录","dataType":"Map","bcRef":"mkmVisitrecord","bcFieldName":"","required":"false","isCollection":"false","operator":"","defaultValue":"","children":[{"name":"visitrecord\_id","label":"服务记录编号","bcRef":"mkmVisitrecord","bcFieldName":"ROW\_ID","required":"true","defaultValue":"","children":[],"dataType":"String","operator":"EQUALS","isCollection":"false"},{"name":"visit\_date","label":"服务日期","bcRef":"mkmVisitrecord","bcFieldName":"visit\_date","required":"false","defaultValue":"","children":[],"dataType":"BigInt","isCollection":"false"},{"name":"visit\_object\_type","label":"服务对象类型","bcRef":"mkmVisitrecord","bcFieldName":"visit\_object\_type","required":"false","defaultValue":"","children":[],"dataType":"String","isCollection":"false"},{"name":"visit\_type","label":"服务方式","bcRef":"mkmVisitrecord","bcFieldName":"visit\_type","required":"false","defaultValue":"","children":[],"dataType":"String","isCollection":"false"},{"name":"visit\_title","label":"服务主题","bcRef":"mkmVisitrecord","bcFieldName":"visit\_title","required":"false","defaultValue":"","children":[],"dataType":"String","isCollection":"false"},{"name":"visit\_start\_date\_time","label":"服务开始时间","bcRef":"mkmVisitrecord","bcFieldName":"visit\_start\_date\_time","required":"false","defaultValue":"","children":[],"dataType":"BigInt","isCollection":"false"},{"name":"visit\_end\_date\_time","label":"服务结束时间","bcRef":"mkmVisitrecord","bcFieldName":"visit\_end\_date\_time","required":"false","defaultValue":"","children":[],"dataType":"BigInt","isCollection":"false"},{"name":"visit\_time","label":"服务时长","bcRef":"mkmVisitrecord","bcFieldName":"visit\_time","required":"false","defaultValue":"","children":[],"dataType":"BigInt","isCollection":"false"},{"name":"address","label":"地址","bcRef":"mkmVisitrecord","bcFieldName":"address","required":"false","defaultValue":"","children":[],"dataType":"String","isCollection":"false"},{"name":"visit\_content","label":"服务内容","bcRef":"mkmVisitrecord","bcFieldName":"visit\_content","required":"false","defaultValue":"","children":[],"dataType":"String","isCollection":"false"},{"name":"daily\_status","label":"提交状态","bcRef":"mkmVisitrecord","bcFieldName":"daily\_status","required":"false","defaultValue":"","children":[],"dataType":"String","isCollection":"false"},{"name":"other\_participater\_name","label":"同行人员（录入）","bcRef":"mkmVisitrecord","bcFieldName":"other\_participater\_name","required":"false","defaultValue":"","children":[],"dataType":"String","isCollection":"false"},{"name":"org\_id","label":"组织编号","bcRef":"mkmVisitrecord","bcFieldName":"org\_id","required":"false","defaultValue":"","children":[],"dataType":"String","isCollection":"false"},{"name":"follow\_act\_remark","label":"后续服务计划","bcRef":"mkmVisitrecord","bcFieldName":"follow\_act\_remark","required":"false","defaultValue":"","children":[],"dataType":"String","isCollection":"false"},{"name":"daily\_id","label":"日报id","bcRef":"mkmVisitrecord","bcFieldName":"daily\_id","required":"false","defaultValue":"","children":[],"dataType":"String","isCollection":"false"},{"name":"week\_id","label":"周报id","bcRef":"mkmVisitrecord","bcFieldName":"week\_id","required":"false","defaultValue":"","children":[],"dataType":"String","isCollection":"false"},{"name":"broker\_position\_id","label":"打卡编号","bcRef":"mkmVisitrecord","bcFieldName":"broker\_position\_id","required":"false","defaultValue":"","children":[],"dataType":"String","isCollection":"false"},{"name":"memo","label":"备注","bcRef":"mkmVisitrecord","bcFieldName":"memo","required":"false","defaultValue":"","children":[],"dataType":"String","isCollection":"false"},{"label":"客户","bcRef":"mkmVisitrecord","name":"client\_id","dataType":"String","children":[],"bcFieldName":"client\_id","required":"false","isCollection":"true"},{"label":"客户联系人","bcRef":"mkmVisitrecord","name":"customer\_contact\_ids","dataType":"String","children":[],"bcFieldName":"customer\_contact\_ids","required":"false","isCollection":"true"},{"label":"渠道","bcRef":"mkmVisitrecord","name":"chn\_code","dataType":"String","children":[],"bcFieldName":"chn\_code","required":"false","isCollection":"true"},{"label":"渠道联系人","bcRef":"mkmVisitrecord","name":"channel\_contact\_ids","dataType":"String","children":[],"bcFieldName":"channel\_contact\_ids","required":"false","isCollection":"true"},{"label":"产品","bcRef":"mkmVisitrecord","name":"product\_codes","dataType":"String","children":[],"bcFieldName":"product\_codes","required":"false","isCollection":"true"},{"label":"同行人员","bcRef":"mkmVisitrecord","name":"participater\_codes","dataType":"String","children":[],"bcFieldName":"participater\_codes","required":"false","isCollection":"true"}]}],"sortFields":[]},"outputs":{"code":"error\_no","message":"error\_info","total":"","pageSize":"","pageNum":"","commonParams":[{"name":"error\_no","label":"错误号","dataType":"Int","defaultValue":"0"},{"name":"error\_info","label":"错误信息","dataType":"String","defaultValue":""}],"boParams":[]},"id":"putVisitrecordAtomInner","name":"修改服务记录","apiType":"UPDATE","apiCategory":"inner","fieldFormatBsRef":"OpenApiTriggerImpl","boId":"mkmVisitrecord","desc":""}]}]]>\n</openApi> | NaN | 可被权限管控（只读或可编辑） | hep接口：/g/external/v/external/interface/publicParameter | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | 新增接口 | NaN | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | api编码(id) | NaN | api编码，唯一，仅支持英文、数字、下划线，长度<=30 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 中文名称(name) | NaN | 中文名称，不支持<>&"'，长度<=100 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | api类型(apiType) | NaN | api的类型，有8种 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 接口分类(apiCategory) | NaN | 接口的分类，有4种 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 绑定对象(boId) | NaN | 下拉选择，数据来源于开发设计-模块-对象 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 协议类型(protocols.name) | NaN | 协议类型：HTTP、T3 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 方法(protocols.method) | NaN | 协议类型：HTTP，方法：GET、POST | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 路径(protocols.path) | NaN | 协议类型：HTTP显示该字段 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 功能号(protocols.functionId) | NaN | 协议类型：T3显示该字段 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | api路由(protocols.apiUrl) | NaN | 协议类型：T3显示该字段 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 绑定类型(handlerType) | NaN | 绑定类型，选项包括绑定逻辑、绑定插件 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 描述(desc) | NaN | 开放接口的描述 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 入参 | NaN | 填写入参，包括常规参数、字段参数、排序字段 ，字段参数支持从实体导入 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 出参 | NaN | 填写出参，包括常规参数、输出编码、输出提示、字段参数，字段参数支持从实体导入 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | 删除接口 | NaN | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | 编辑接口 | NaN | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | 查询接口 | NaN | NaN | NaN | NaN | NaN | 1、通过中文名称、功能号、绑定对象、模块名称、api类型、接口分类查询\n2、显示中文名称、功能号、绑定对象、模块名称、api类型、接口分类，分页 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | 导出接口 | NaN | NaN | NaN | NaN | NaN | 可以选择接口，导出接口文档 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | 配置微服务 | NaN | NaN | NaN | NaN | NaN | 开放接口入参的常规参数会从选择的微服务中请求 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | 国际化 | NaN | NaN | NaN | NaN | NaN | {\n "localePath": "./i18n\_data",\n "locales": [\n "zh-HK",\n "zh-TW",\n "en-US",\n "en-GB",\n "zh-CN"\n ],\n "defaultLocale": "zh-TW",\n "globalLocaleGetter": "function(){ \nreturn localStorage.getItem('locale')\n }",\n "globalLocaleSetter": "function(lang){\nlocalStorage.setItem('locale', lang) \n}"\n} | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | 新增基本信息 | NaN | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 语言包(localePath) | NaN | 下拉选择，默认是i18n\_data | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 语言类型(locales) | NaN | 语料包中，用户需要开启的国际化语言集合。下拉选择，可以多选，包含10种语言 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 默认语言(defaultLocale) | NaN | 从选择的语言类型中选择一种语言作为默认语言，当用户未指定语言的时候使用该字段的值 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 从全局环境中获取语言(globalLocaleGetter) | NaN | 从外部环境中获取用户设置的locale信息。\n\n如：用户在外框中切换了locale，hui外框会将locale信息写入到localStorage的locale字段中，不同版本、不同项目的外框写入的位置可能不同，相对应的getter方法也不同。 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 设置全局环境的语言(globalLocaleSetter) | NaN | 设置外部环境的locale信息 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | 语料管理 | NaN | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | 新增语料 | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 国际化资源key(key) | NaN | 全局不能重复；配置语料明细；key必须要以page.\pickList.\frontEnd.\backEnd.\组件包名.组件名.开头 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 中文(zh-CN) | NaN | 根据选择的语言类型 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | 删除语料 | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | 编辑语料 | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | 查询语料 | NaN | NaN | NaN | NaN | 1、通过关键字查询语料\n2、显示key、语言，分页 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | 导入语料 | NaN | NaN | NaN | NaN | 为了方便工作中的语料翻译工作，可导出csv文件，并在工作中传递 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | 导出语料 | NaN | NaN | NaN | NaN | 为了方便工作中的语料翻译工作，可导出csv文件，并在工作中传递 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | 导出模板 | NaN | NaN | NaN | NaN | 为了方便工作中的语料翻译工作，可导出csv文件，并在工作中传递 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | 从项目中提取 | NaN | NaN | NaN | NaN | 提取资源文件并绑定国际化 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | 标准字段 | NaN | NaN | NaN | NaN | NaN | <standardField id="standardField">\n <field name="uuid\_arr" title="uuid列表" dataType="HsChar100" desc=""></field>\n <field name="user\_id" title="用户编码" dataType="HsChar64" desc=""></field>\n <field name="user\_name" title="用户名称" dataType="HsChar100" desc=""></field>\n</standardField> | NaN | 可被权限管控（只读或可编辑） | 调用HEP接口:/g/external/v/external/standfield/getPage\n/g/external/v/external/dataType/getPage\n/g/external/v/external/standfield/getPage\n/g/external/v/external/microservice/getList\n/g/external/v/external/interface/detail.json | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | 导入标准字段 | NaN | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | 下载模板 | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 字段名(name) | NaN | 字段名 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 字段中文名(title) | NaN | 字段中文名 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 类型(dataType) | NaN | 类型 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 描述(desc) | NaN | 描述 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | 导入 | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | 同步标准字段 | NaN | NaN | NaN | NaN | NaN | 配置了hep信息，可以从hep同步 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | 删除标准字段 | NaN | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | 编辑标准字段 | NaN | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | 查询标准字段 | NaN | NaN | NaN | NaN | NaN | 1、通过字段名、字段中文名、类型、描述查询标准字段\n2、显示字段名、字段中文名、类型、描述，分页 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | 数据类型 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | hep接口：/g/external/v/external/businessType/getPage\n/g/external/v/external/dataType/getPage | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | 字段类型 | NaN | NaN | NaN | NaN | <fieldTypes>\n <name>fieldTypes</name>\n <fieldType name="Int" label="整数" physicalType="Int" scale="" precision="" validatorRef="" defaultComponent=""/>\n <fieldType name="BigInt" label="长整数" physicalType="BigInt" scale="" precision="" validatorRef="" defaultComponent=""/>\n <fieldType name="Bool" label="布尔" physicalType="Bool" scale="" precision="" validatorRef="" defaultComponent=""/>\n <fieldType name="Decimal" label="浮点数" physicalType="Decimal" scale="14" precision="6" validatorRef="" defaultComponent=""/>\n <fieldType name="Date" label="日期" physicalType="Date" scale="" precision="" validatorRef="" defaultComponent=""/>\n <fieldType name="DateTime" label="日期时间" physicalType="DateTime" scale="" precision="" validatorRef="" defaultComponent=""/>\n <fieldType name="Time" label="时间" physicalType="Time" scale="" precision="" validatorRef="" defaultComponent=""/>\n <fieldType name="Clob" label="长文本" physicalType="Clob" scale="" precision="" validatorRef="" defaultComponent=""/>\n <fieldType name="String" label="文本" physicalType="String" scale="" precision="" validatorRef="" defaultComponent=""/>\n <fieldType name="Map" label="Map" physicalType="Map" scale="" precision="" validatorRef="" defaultComponent=""/>\n <fieldType name="List" label="列表" physicalType="List" scale="" precision="" validatorRef="" defaultComponent=""/>\n <fieldType name="PrimaryKey" label="主键" physicalType="Object" scale="" precision="" validatorRef="" defaultComponent=""/>\n</fieldTypes> | 用于描述实体中的字段类型 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | 新增字段类型 | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | 同步字段类型 | NaN | NaN | NaN | NaN | 配置了hep信息，可以从hep同步 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | 删除字段类型 | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | 编辑字段类型 | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | 查询字段类型 | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | 物理类型 | NaN | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | 新增字段类型 | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | 删除字段类型 | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | 编辑字段类型 | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | 查询字段类型 | NaN | NaN | NaN | <physicalTypes>\n <name>physicalTypes</name>\n <physicalType name="TinyInt" label="TinyInt" javaType="Integer" javaScriptType="Number" validatorRef="">\n <databaseType database="DB\_MYSQL" type="tinyint"/>\n <databaseType database="DB\_ORACLE" type="number(3,0)"/>\n </physicalType>\n <physicalType name="SmallInt" label="SmallInt" javaType="Integer" javaScriptType="Number" validatorRef="">\n <databaseType database="DB\_MYSQL" type="smallint"/>\n <databaseType database="DB\_ORACLE" type="number(5,0)"/>\n </physicalType>\n <physicalType name="MediumInt" label="MediumInt" javaType="Integer" javaScriptType="Number" validatorRef="">\n <databaseType database="DB\_MYSQL" type="mediumint"/>\n <databaseType database="DB\_ORACLE" type="number(7,0)"/>\n </physicalType>\n <physicalType name="Int" label="整数" javaType="Integer" javaScriptType="Number" validatorRef="">\n <databaseType database="DB\_MYSQL" type="int"/>\n <databaseType database="DB\_ORACLE" type="number(10,0)"/>\n </physicalType>\n <physicalType name="BigInt" label="长整数" javaType="Long" javaScriptType="Number" validatorRef="">\n <databaseType database="DB\_MYSQL" type="bigint"/>\n <databaseType database="DB\_ORACLE" type="number(18,0)"/>\n </physicalType>\n <physicalType name="Double" label="双精度数" javaType="Double" javaScriptType="Number" validatorRef="">\n <databaseType database="DB\_MYSQL" type="decimal($L,$P)"/>\n <databaseType database="DB\_ORACLE" type="number($L,$P)"/>\n </physicalType>\n <physicalType name="LongDouble" label="高双精度数" javaType="BigDecimal" javaScriptType="Number" validatorRef="">\n <databaseType database="DB\_MYSQL" type="decimal($L,$P)"/>\n <databaseType database="DB\_ORACLE" type="number($L,$P)"/>\n </physicalType>\n <physicalType name="Bool" label="布尔" javaType="Boolean" javaScriptType="Boolean" validatorRef="">\n <databaseType database="DB\_MYSQL" type="tinyint"/>\n <databaseType database="DB\_ORACLE" type="number(1,0)"/>\n </physicalType>\n <physicalType name="Char" label="字符" javaType="Char" javaScriptType="String" validatorRef="">\n <databaseType database="DB\_MYSQL" type="char($L)"/>\n <databaseType database="DB\_ORACLE" type="char"/>\n </physicalType>\n <physicalType name="Decimal" label="精确数字" javaType="BigDecimal" javaScriptType="Number" validatorRef="">\n <databaseType database="DB\_MYSQL" type="decimal($L,$P)"/>\n <databaseType database="DB\_ORACLE" type="number($L,$P)"/>\n </physicalType>\n <physicalType name="Date" label="日期" javaType="Integer" javaScriptType="Number" validatorRef="">\n <databaseType database="DB\_MYSQL" type="int"/>\n <databaseType database="DB\_ORACLE" type="number(8,0)"/>\n </physicalType>\n <physicalType name="DateTime" label="日期时间" javaType="Long" javaScriptType="Number" validatorRef="">\n <databaseType database="DB\_MYSQL" type="bigint"/>\n <databaseType database="DB\_ORACLE" type="number(18,0)"/>\n </physicalType>\n <physicalType name="Time" label="时间" javaType="Integer" javaScriptType="Number" validatorRef="">\n <databaseType database="DB\_MYSQL" type="int"/>\n <databaseType database="DB\_ORACLE" type="number(8,0)"/>\n </physicalType>\n <physicalType name="Clob" label="长文本" javaType="String" javaScriptType="String" validatorRef="">\n <databaseType database="DB\_MYSQL" type="longtext"/>\n <databaseType database="DB\_ORACLE" type="clob"/>\n </physicalType>\n <physicalType name="String" label="文本" javaType="String" javaScriptType="String" validatorRef="">\n <databaseType database="DB\_MYSQL" type="varchar($L)"/>\n <databaseType database="DB\_ORACLE" type="varchar2($L)"/>\n </physicalType>\n <physicalType name="Map" label="Map" javaType="Map" javaScriptType="Object" validatorRef="">\n <databaseType database="DB\_MYSQL" type="json"/>\n <databaseType database="DB\_ORACLE" type="clob"/>\n </physicalType>\n <physicalType name="List" label="列表" javaType="List" javaScriptType="Array" validatorRef="">\n <databaseType database="DB\_MYSQL" type="json"/>\n <databaseType database="DB\_ORACLE" type="clob"/>\n </physicalType>\n <physicalType name="Object" label="Object" javaType="Object" javaScriptType="Any" validatorRef="">\n <databaseType database="DB\_MYSQL" type="json"/>\n <databaseType database="DB\_ORACLE" type="clob"/>\n </physicalType>\n</physicalTypes> | 用于描述数据表中的列类型 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | 字典 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | hep接口：/g/external/v/external/stdDict/subDictList | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | 字典管理 | NaN | NaN | NaN | NaN | <pickList id="picklist\_visiting\_addr" title="访问地点">\n <name>访问地点</name>\n <comments>访问地点</comments>\n <staticDict>true</staticDict>\n <lovType>visiting\_addr</lovType>\n <typeValues>\n <typeValue>1</typeValue>\n <typeValue>2</typeValue>\n <typeValue>3</typeValue>\n </typeValues>\n</pickList> | NaN | 可被权限管控（只读或可编辑） | 调用HEP接口\n\ngetDict\ngetSubDict | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | 新增字典 | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 名称(title) | NaN | 名称，不支持<>&"'，长度<=100 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | ID(id) | NaN | ID，唯一，仅支持英文、数字、下划线，长度<=30 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | 设计字典 | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 字典名称(name) | NaN | 字典名称，仅支持英文、数字、"\_"、"."、"$"，长度<=30，支持从hep选择 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 描述(comments) | NaN | 描述，长度<=300 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 字典类型(staticDict) | NaN | 字典类型，可以选择静态字典或业务模型动态字典 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 字典项标识(lovType) | NaN | "静态字典"分类下，字典项标识，长度<=30，只能输入数字、英文字母、下划线 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 字典值明细(listOfValueItem) | NaN | "静态字典"分类下，字典值明细，长度<=30，只能输入数字、字母、下划线 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 绑定的实体(businessComponentRef) | NaN | 字典类型：业务模型动态字典，数据来源应用定义-模块-实体 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 字典值对应字段(valueField) | NaN | 字典类型：业务模型动态字典，数据来源绑定的实体字段 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 字典显示字段(nameField) | NaN | 字典类型：业务模型动态字典，数据来源绑定的实体字段 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | 删除字典 | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | 编辑字典 | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | 查询字典 | NaN | NaN | NaN | NaN | 通过名称和ID查询字典 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | 查看字典查询方法 | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | 字典项管理 | NaN | NaN | NaN | NaN | <listOfValues id="mkm\_lov">\n<name >mkm\_lov</name>\n<listOfValue >\n<type >visiting\_addr</type>\n<listOfValueItem >\n<typeName >华宝基金</typeName>\n<typeValue >1</typeValue>\n</listOfValueItem>\n<listOfValueItem >\n<typeName >兴业证券</typeName>\n<typeValue >2</typeValue>\n</listOfValueItem>\n<listOfValueItem >\n<typeName >中邮保险</typeName>\n<typeValue >3</typeValue>\n</listOfValueItem>\n</listOfValue>\n</listOfValues> | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | 基本信息 | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 字典值(name) | NaN | 字典值，只能输入数字、英文字母、下划线，长度<=30 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 描述(desc) | NaN | 描述，长度<=300 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | 字典值列表 | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | 新增字典项 | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 字典值标识(type) | NaN | 字典值标识 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 字典值明细(listOfValueItem) | NaN | 字典值明细，包括名称(typeName)和值(typeValue)，可以移动字典值形成多级字典 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | 删除字典项 | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | 编辑字典项 | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | 查询字典项 | NaN | NaN | NaN | 1、通过关键字查询字典标识\n2、显示字典标识，不分页 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | 插件 | NaN | NaN | NaN | NaN | NaN | <plugins id="id\_generator">\n <!-- 插件lib包 -->\n <libCoordinate>com.hundsun.hcreator2.office.plugin:id-generator:1.7.0</libCoordinate>\n <!-- UUID -->\n <plugin id="uuid" type="OutboundAdapter.IdGenerator" inter="com.hundsun.atom2.domain.plugin.idgenerator.IdGenerator" impl="com.hundsun.hcreator2.office.plugin.IdGeneratorUuid" vendor="ATOM"/>\n <!-- 雪花算法 -->\n <plugin id="snow\_flake" type="OutboundAdapter.IdGenerator" inter="com.hundsun.atom2.domain.plugin.idgenerator.IdGenerator" impl="com.hundsun.hcreator2.office.plugin.IdGeneratorSnowFlake" vendor="ATOM"/>\n <!-- Pg自增 -->\n <plugin id="auto\_number\_pg" type="OutboundAdapter.IdGenerator" inter="com.hundsun.atom2.domain.plugin.idgenerator.IdGenerator" impl="com.hundsun.hcreator2.office.plugin.IdGeneratorAutoNumberPg" vendor="ATOM"/>\n <!-- Oracle时序 -->\n <plugin id="oracle\_seq" type="OutboundAdapter.IdGenerator" inter="com.hundsun.atom2.domain.plugin.idgenerator.IdGenerator" impl="com.hundsun.hcreator2.office.plugin.IdGeneratorSequence" vendor="ATOM"/>\n</plugins> | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | 查看插件 | NaN | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | 编辑插件 | NaN | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | 菜单 | NaN | NaN | NaN | NaN | NaN | <menus>\n <menu id="application\_standard" title="CRM低码应用" icon="" index="0" visible="true" type="" ref="" param="" extInfo="application\_standard" origin="LOCAL">\n <menu id="application\_standard\_common" title="低码应用通用菜单" icon="" index="1" visible="true" type="" ref="" param="" extInfo="application\_standard\_common" origin="LOCAL">\n </menu>\n </menu>\n <menu id="crm" extInfo="c202c63d-19d2-4398-a281-fdaf0631634f" title="客户营销" icon="" index="" visible="true" type="" ref="" param="" origin="HEP">\n <menu id="mkm" title="营销管理" icon="" index="10" visible="true" type="" ref="" param="" extInfo="08a3076f-8977-4210-9ec4-1a7fa78c889c" origin="HEP">\n <menu id="dailyworkManage" title="日志管理" icon="" index="10" visible="true" type="" ref="" param="" extInfo="2c646c86-596e-49fe-ab7c-3911a2f99956" origin="HEP">\n <menu id="mkmVisitrecordCustomerList" title="客户服务记录" icon="" index="11" visible="true" type="PAGE" ref="mkmVisitrecordCustomerList" param="" extInfo="76894efa-228b-4427-a64a-d01b53b4bec3" origin="HEP" moduleRef="mkmVisitrecord">\n <menu id="mkmSubVisitrecordCustomerList" title="下属服务记录" icon="" index="20" visible="true" type="" ref="" param="" extInfo="10d7e5af-aa40-4968-a1cb-f888ea269cfc" origin="HEP">\n </menu>\n <menu id="mkmMyVisitrecordCustomerList" title="我的服务记录" icon="" index="10" visible="true" type="" ref="" param="" extInfo="39a21239-16fd-4adb-87fe-42b9eacab025" origin="HEP">\n </menu>\n </menu>\n <menu id="mkmVisitrecordChannelList" title="渠道服务记录" icon="" index="12" visible="true" type="PAGE" ref="mkmVisitrecordChannelList" param="" extInfo="87896d83-c899-44c7-995e-6895f2dd0eee" origin="HEP" moduleRef="mkmVisitrecord">\n <menu id="mkmSubVisitrecordChannelList" title="下属服务记录" icon="" index="20" visible="true" type="" ref="" param="" extInfo="debb0b4d-d320-4891-b6a0-3e2aabae63fd" origin="HEP">\n </menu>\n <menu id="mkmMyVisitrecordChannelList" title="我的服务记录" icon="" index="10" visible="true" type="" ref="" param="" extInfo="136d6b9c-3048-4fc4-9f73-97cb9858dbd2" origin="HEP">\n </menu>\n </menu>\n </menu>\n <menu id="kpiobjectscore" title="绩效评分" icon="" index="" visible="true" type="" ref="" param="" extInfo="ddfc2837-f592-4925-a1b2-caf82389188d" origin="HEP">\n <menu id="kpiobjectscoredataList" title="项目绩效评分数据" icon="" index="" visible="true" type="" ref="" param="" extInfo="8a4a5a37-fad6-4496-877a-45064df1b66f" origin="HEP">\n </menu>\n <menu id="kpiobjectscoreruleList" title="项目绩效评分规则" icon="" index="" visible="true" type="PAGE" ref="kpiobjectscoreruleList" param="" extInfo="d9a71084-b9c1-4ab8-9c2d-7ab6fdece6fd" origin="HEP" moduleRef="kpiobjectscorerule">\n </menu>\n </menu>\n <menu id="sell" title="销售分析" icon="" index="" visible="true" type="" ref="" param="" extInfo="e49df859-8818-4028-987b-9d7c47c87c82" origin="HEP">\n <menu id="invest" title="投顾数据维护" icon="" index="10" visible="true" type="PAGE" ref="mkmInvestInfoList" param="" extInfo="baf47142-d513-4c2f-b8ba-acc9f7b605fe" origin="HEP" moduleRef="invest">\n </menu>\n </menu>\n </menu>\n <menu id="csmfund" title="客户管理" icon="" index="" visible="true" type="" ref="" param="" extInfo="61439441-3be0-46e3-88be-870b1c1172ad" origin="HEP">\n <menu id="accoqueryfund" title="账户查询" icon="" index="" visible="true" type="" ref="" param="" extInfo="3a34ef00-e0fb-4e14-a9bd-5d75f91be748" origin="HEP">\n <menu id="fundcustorgList" title="机构账户" icon="" index="" visible="true" type="" ref="" param="" extInfo="880c4fad-f873-4b9e-b6b9-6f50c1bca917" origin="HEP">\n </menu>\n <menu id="fundCustomerList" title="产品账户" icon="" index="" visible="true" type="PAGE" ref="mkm\_card\_info\_list" param="" extInfo="d4c09ffe-2bf5-4377-bba3-1a450291abc5" origin="HEP" moduleRef="mkm\_card\_info">\n </menu>\n </menu>\n <menu id="custContactManage" title="联系人管理" icon="" index="" visible="true" type="" ref="" param="" extInfo="58c655dd-4757-4922-a4fa-99fc4c9a05d4" origin="HEP">\n <menu id="fundcustcontactList" title="客户联系人" icon="" index="" visible="true" type="PAGE" ref="fundcustcontactList" param="" extInfo="0bac0b41-cbfa-4e84-a5f0-aac0aed54b4b" origin="HEP" moduleRef="csmCustcontactInfo">\n </menu>\n </menu>\n <menu id="custqueryfund" title="客户查询" icon="" index="" visible="true" type="" ref="" param="" extInfo="a5078ad5-717e-4d86-ac76-1447702b32e5" origin="HEP">\n <menu id="custGroupList" title="机构客户" icon="" index="" visible="true" type="" ref="" param="" extInfo="411570f1-9e7b-40ed-ba97-e2c5778e6ff3" origin="HEP">\n <menu id="potentialcustgroupList" title="潜在机构客户" icon="" index="" visible="true" type="" ref="" param="" extInfo="367dc93a-f8eb-4a31-8807-f621cf98a6cd" origin="HEP">\n </menu>\n </menu>\n </menu>\n </menu>\n <menu id="chm" title="渠道管理" icon="" index="" visible="true" type="" ref="" param="" extInfo="af1d5879-d54e-4fb8-82f8-82cfb0912843" origin="HEP">\n <menu id="chnContactManage" title="联系人管理" icon="" index="39" visible="true" type="" ref="" param="" extInfo="ab570f07-38d6-4bea-876c-ae9be4c0f824" origin="HEP">\n <menu id="contactfundList" title="渠道联系人" icon="" index="13" visible="true" type="PAGE" ref="contactfundList" param="" extInfo="af3377b9-2e6a-4874-9c59-847cc9180154" origin="HEP" moduleRef="chmChannelContract">\n </menu>\n </menu>\n </menu>\n </menu>\n</menus> | NaN | 可被权限管控（只读或可编辑） | hep接口：/g/external/v/external/menu/list | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | 新增菜单 | NaN | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 菜单编号 | NaN | 菜单编号，唯一，仅支持英文、数字、下划线，长度<=200 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 菜单名称 | NaN | 菜单名称，不支持<>&"'，长度<=128 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 是否显示 | NaN | 是否显示，选项包括是、否 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 上级菜单 | NaN | 下拉选择，数据来源菜单 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 绑定页面 | NaN | 下拉选择，数据来源开发设计-模块-页面 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | 同步菜单 | NaN | NaN | NaN | NaN | NaN | 配置了hep信息，可以从hep同步 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | 删除菜单 | NaN | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | 编辑菜单 | NaN | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | 查询菜单 | NaN | NaN | NaN | NaN | NaN | 1、通过菜单名称、菜单编号、绑定页面查询菜单\n2、显示菜单名称、菜单编号、绑定页面，不分页 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | 复制地址 | NaN | NaN | NaN | NaN | NaN | 复制菜单的地址，用于跳转指定页面等场景 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | 功能权限 | NaN | NaN | NaN | NaN | NaN | <functions>\n <function code="25sj3c5" name="表格查询组件" menuRef="hwsDynTpl\_visitFundRecordListNew" pageRef="visitor\_record\_list" index="0" origin="LOCAL">\n </function>\n</functions> | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | 同步功能权限 | NaN | NaN | NaN | NaN | NaN | 菜单绑定页面后，可以从页面上自动收集功能权限并建立关系 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 操作功能名称(name) | NaN | 功能权限的名称 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 操作功能编码(code) | NaN | 功能权限的编码 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | 查询功能权限 | NaN | NaN | NaN | NaN | NaN | 1、通过操作功能名称、操作功能编码查询功能权限\n2、显示操作功能名称、操作功能编码，不分页 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | 角色 | NaN | NaN | NaN | NaN | NaN | <roles>\n <role name="213" id="123" index="1">\n <permission menuRef="tgy3nrjipr\_common" functionRef="tgy3nrjipr\_necessary" type="OPERATION">\n </permission>\n <permission menuRef="tgy3nrjipr\_common" functionRef="tgy3nrjipr\_necessary" type="AUTHORIZATION">\n </permission>\n <permission menuRef="tgy3nrjipr\_common" functionRef="tgy3nrjipr\_generic\_api" type="OPERATION">\n </permission>\n <permission menuRef="tgy3nrjipr\_common" functionRef="tgy3nrjipr\_generic\_api" type="AUTHORIZATION">\n </permission>\n <permission menuRef="tgy3nrjipr\_common" functionRef="tgy3nrjipr\_workflow" type="OPERATION">\n </permission>\n <permission menuRef="tgy3nrjipr\_common" functionRef="tgy3nrjipr\_workflow" type="AUTHORIZATION">\n </permission>\n <permission menuRef="hwsDynTpl\_visitFundRecordListNew" functionRef="25sj3c5" type="OPERATION">\n </permission>\n <permission menuRef="hwsDynTpl\_visitFundRecordListNew" functionRef="25sj3c5" type="AUTHORIZATION">\n </permission>\n </role>\n</roles> | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | 新增角色 | NaN | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 角色名称(name) | NaN | 角色名称，不支持< > & " '，长度<=32 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 角色编号(id) | NaN | 仅支持英文、数字、下划线，长度不超过32 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | 分配权限 | NaN | NaN | NaN | NaN | NaN | 分配角色可以操作或授权的菜单功能 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | 删除角色 | NaN | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | 编辑角色 | NaN | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | 查询角色 | NaN | NaN | NaN | NaN | NaN | 1、通过角色名称、角色编码查询角色\n2、显示角色名称、角色编码，不分页 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | 数据源 | NaN | NaN | NaN | NaN | NaN | <dataSource xmlns="http://hundsun.com/hddml1.0" id="datasource"> \n <name>${datasource.name}</name> \n <url>${datasource.url}</url> \n <userName>${datasource.userName}</userName> \n <password>${datasource.password}</password> \n <dataSourceType>${datasource.dataSourceType}</dataSourceType> \n</dataSource> | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | 新增数据源 | NaN | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 名称(title) | NaN | 名称，不支持<>&"'，长度<=100 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | ID(id) | NaN | ID，唯一，仅支持英文、数字、下划线，长度<=30 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | 设计数据源 | NaN | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 数据源名称(name) | NaN | 数据源名称 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 数据源连接(url) | NaN | 数据源连接 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 用户名(userName) | NaN | 数据源用户名称 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 密码(password) | NaN | 数据源密码 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 数据源类型(dataSourceType) | NaN | 数据源类型：支持MySQL、oracle、lightDB | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 绑定数据源插件(plugin) | NaN | 绑定数据源插件，用户自定义数据源 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | 删除数据源 | NaN | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | 编辑数据源 | NaN | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | 查询数据源 | NaN | NaN | NaN | NaN | NaN | 通过名称和ID查询数据源 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | 流程监听配置 | NaN | NaN | NaN | NaN | NaN | <workflowListeners>\n <workflowListener id="fea347dd4b7340899c6acb34c7c05cf5" desc="">\n <eventName>节点兼任务创建</eventName>\n <eventClassName>org.jbpm.pvm.internal.history.events.TaskActivityStart</eventClassName>\n <invokeType>cloud</invokeType>\n <invokePath>{hcreator\_workflow\_callback\_service\_path}</invokePath>\n <invokeParameters>\n <invokeParameter name="methodPath" value="{&quot;type&quot;:&quot;bo&quot;,&quot;id&quot;:&quot;bo\_visitor\_record&quot;,&quot;method&quot;:&quot;delete&quot;}">\n </invokeParameter>\n </invokeParameters>\n <listenerScope>1</listenerScope>\n <processKey>wf\_visitor\_record\_process</processKey>\n <invokeConnectType>sync</invokeConnectType>\n <eventPressType>1</eventPressType>\n </workflowListener>\n</workflowListeners> | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.9 | V202401.00 |
| NaN | NaN | NaN | 新增监听配置 | NaN | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.9 | V202401.00 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 监听类型(eventClassName) | NaN | 下拉选择，有53种选项 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.9 | V202401.00 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 监听范围(listenerScope) | NaN | 监听范围：应用、流程 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.9 | V202401.00 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 调用方式(invokeConnectType) | NaN | 调用方式：同步、异步 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.9 | V202401.00 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 选择服务(methodPath) | NaN | 下拉选择，数据来源开发设计-模块-对象-方法 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.9 | V202401.00 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 参数配置(invokeParameters) | NaN | 参数配置，包括参数和值 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.9 | V202401.00 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 事件处理机制(eventPressType) | NaN | 事件处理机制：即时处理、最终处理 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.9 | V202401.00 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 描述(desc) | NaN | 描述，长度<=300 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.9 | V202401.00 |
| NaN | NaN | NaN | 删除监听配置 | NaN | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.9 | V202401.00 |
| NaN | NaN | NaN | 编辑监听配置 | NaN | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.9 | V202401.00 |
| NaN | NaN | NaN | 查询监听配置 | NaN | NaN | NaN | NaN | NaN | 1、通过监听类型和流程编码查询监听器\n2、显示监听类型、监听范围、流程编码、调用类型、事件处理机制、描述，不分页 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.9 | V202401.00 |
| NaN | NaN | 连接器 | NaN | NaN | NaN | NaN | NaN | [{"id":"test","url":"http://123","method":"get","isCors":false,"headers":[{"key":"a","value":"1"},{"key":"b","value":"2"}],"description":"123","type":"custom","title":"测试","timeout":0,"params":[{"name":"","type":"","default":"","required":false,"children":[]}],"return":[{"name":"","type":"","default":"","required":false,"children":[]}]}] | NaN | 可被权限管控（只读或可编辑） | hep接口：/g/external/v/external/dataType/getPage\n/g/external/v/external/microservice/getList\n/g/external/v/external/interface/getPage\n/g/external/v/external/interface/detail.json\n资产中心接口：/materialManage/connectorManager/getConnectorContentDesigner | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | 新增连接器 | NaN | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | ID(id) | NaN | ID，唯一，仅支持英文、数字、下划线，长度<=30 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 中文名(title) | NaN | 中文名，不支持<>&"'，长度<=100 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 描述(description) | NaN | 描述，长度<=300 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 类型(type) | NaN | 类型，选项包括http、t3 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 版本号(version) | NaN | 版本号，长度限制<=20 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 请求地址前缀(urlPrefix) | NaN | 请求地址前缀，长度限制<=100 | 可被权限管控（只读或可编辑） | NaN | NaN | 关闭 | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 公共参数(headers) | NaN | 公共参数，类型为t3显示该字段 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 微服务gsv(gsv) | NaN | 微服务gsv，类型为http显示该字段，长度限制<=100 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | 导入连接器 | NaN | NaN | NaN | NaN | NaN | 从物料资产中心导入连接器 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | 删除连接器 | NaN | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | 编辑连接器 | NaN | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | 查询连接器 | NaN | NaN | NaN | NaN | NaN | 1、通过关键字查询连接器\n2、显示ID、中文名、描述、请求地址，不分页 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | 资产视图管理 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | 组件包 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | 查询组件包 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | 查看组件包详情 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | 查询组件 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | 查看组件详情 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 使用说明 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 元数据 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | 依赖组件包 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | 删除组件包 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | 本地导入 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | 线上获取 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | 工具函数包 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | 查询工具函数包 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | 查看工具函数包详情 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | 查询工具函数 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | 查看工具函数详情 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 使用说明 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 元数据 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | 删除工具函数包 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | 本地导入 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | 线上获取 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | 低代码组件包 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | 查询低代码组件包 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | 查看低代码组件包详情 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | 查询低代码组件 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | 查看低代码组件详情 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 使用说明 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 元数据 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | 依赖组件包 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | 依赖工具函数包 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | 依赖低代码组件包 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | 删除低代码组件包 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | 本地导入 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | 线上获取 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | 逻辑库 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | 查询逻辑库 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | 查看逻辑库详情 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | 删除逻辑库 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | 本地导入 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | 线上获取 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | 后端插件包 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | 查询后端插件包 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | 查看后端插件包详情 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | 删除后端插件包 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | 本地导入 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | 线上获取 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | 开发设计 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | NaN | NaN |
| NaN | NaN | 目录管理 | NaN | NaN | NaN | NaN | NaN | <catalog id="application\_visitor\_record" title="访客记录"></catalog> | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | 新建目录 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 名称(title) | NaN | 名称，不支持<>&"'，长度<=100 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | ID(id) | NaN | ID，唯一，仅支持英文、数字、下划线，长度<=30 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 所属目录 | NaN | 所属目录 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | 删除目录 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | 编辑目录 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | 查询目录 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | 移动目录 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.9 | V202401.00 |
| NaN | NaN | 模块管理 | NaN | NaN | NaN | NaN | NaN | <module id="application\_visitor\_record" title="访客记录"></module> | NaN | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | 新增模块 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 名称(title) | NaN | 名称，不支持<>&"'，长度<=100 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | ID(id) | NaN | ID，唯一，仅支持英文、数字、下划线，长度<=30 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 所属目录 | NaN | 所属目录 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | 删除模块 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | 编辑模块 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | 查询模块 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | 移动模块 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.9 | V202401.00 |
| NaN | NaN | 公共模块开发 | NaN | NaN | NaN | NaN | NaN | NaN | 目前暂不涉及 | 可被权限管控（只读或可编辑） | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | 暂未实现 | 暂未实现 |
| NaN | NaN | NaN | 公共表 | NaN | NaN | NaN | NaN | NaN | 目前暂不涉及 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | 暂未实现 | 暂未实现 |
| NaN | NaN | NaN | 公共实体 | NaN | NaN | NaN | NaN | NaN | 目前暂不涉及 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | 暂未实现 | 暂未实现 |
| NaN | NaN | NaN | 公共对象 | NaN | NaN | NaN | NaN | NaN | 目前暂不涉及 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | 暂未实现 | 暂未实现 |
| NaN | NaN | NaN | 公共逻辑 | NaN | NaN | NaN | NaN | NaN | 目前暂不涉及 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | 暂未实现 | 暂未实现 |
| NaN | NaN | NaN | 公共页面 | NaN | NaN | NaN | NaN | NaN | 目前暂不涉及 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | 暂未实现 | 暂未实现 |
| NaN | NaN | 业务模块开发 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | 暂未实现 | 暂未实现 |
| NaN | NaN | NaN | 数据表 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | hep接口：/g/external/v/external/microservice/getList\n/g/external/v/external/table/getPag | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | 数据表 | NaN | NaN | NaN | <table xmlns="" id="mkm\_dailywork\_relation" desc="" title="日常工作关系表">\n <name>mkm\_dailywork\_relation</name>\n <tableType>intersection</tableType>\n <alias>\n </alias>\n <label>日常工作关系表</label>\n <columns>\n <column name="serial\_no" label="流水序号" comments="" physicalType="BigInt" primaryKey="true" nullable="false" scale="0" precision="20" generator="table\_generator\_tydpteneh4">\n </column>\n <column name="obj\_id" label="对象编号" physicalType="String" primaryKey="false" nullable="false" length="256">\n </column>\n <column name="obj\_type" label="对象类型" physicalType="String" primaryKey="false" nullable="false" length="32">\n </column>\n <column name="relation\_type" label="关联类型" physicalType="String" primaryKey="false" nullable="false" length="20">\n </column>\n <column name="relation\_code" label="关联方编码" physicalType="String" primaryKey="false" nullable="false" length="100">\n </column>\n <column name="cooperation\_status" label="协作状态" physicalType="String" primaryKey="false" nullable="true" length="2">\n </column>\n <column name="remark" label="备注" physicalType="String" primaryKey="false" nullable="true" length="4000">\n </column>\n <column name="deal\_date\_time" label="处理时间" physicalType="DateTime" primaryKey="false" nullable="true">\n </column>\n </columns>\n <indexes>\n <index>\n <indexName>pk\_relation</indexName>\n <indexColumn>\n <columnName>serial\_no</columnName>\n <sortOrder>asc</sortOrder>\n </indexColumn>\n <comments>\n </comments>\n <unique>true</unique>\n </index>\n <index>\n <indexName>uk\_dailwork\_relation</indexName>\n <indexColumn>\n <columnName>obj\_id</columnName>\n <sortOrder>asc</sortOrder>\n </indexColumn>\n <indexColumn>\n <columnName>obj\_type</columnName>\n <sortOrder>asc</sortOrder>\n </indexColumn>\n <indexColumn>\n <columnName>relation\_type</columnName>\n <sortOrder>asc</sortOrder>\n </indexColumn>\n <indexColumn>\n <columnName>relation\_code</columnName>\n <sortOrder>asc</sortOrder>\n </indexColumn>\n <comments>\n </comments>\n <unique>true</unique>\n </index>\n </indexes>\n <dataSourceRef>hs\_mkm</dataSourceRef>\n <status>true</status>\n</table> | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | 新建数据表 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 名称(title) | NaN | 名称，不支持<>&"'，长度<=100 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | ID(id) | NaN | ID，唯一，仅支持英文、数字、下划线，长度<=30 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | 复制数据表 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | 删除数据表 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | 新增引用 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | 删除引用 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | SQL导入 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | 设计数据表 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 基本信息 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | ID(id) | NaN | ID，唯一，仅支持英文、数字、下划线，长度<=30 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 表名(name) | NaN | 表名，长度<=100 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 中文名(label) | NaN | 中文名，长度<=200 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 表别名(alias) | NaN | 表别名，长度<=100 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 表类型(tableType) | NaN | 表类型：数据表、扩展表、中间表 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 数据源(dataSourceRef) | NaN | 下拉选择，数据来源应用定义-数据源 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 描述(desc) | NaN | 描述，长度<=300 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 新增列 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 列名(name) | NaN | 列名，只能输入数字、英文字母、下划线，长度<=30 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 列类型(physicalType) | NaN | 列类型，数据来源应用定义-数据类型-物理类型 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 数字有效长度(precision) | NaN | 列类型：数字型，仅支持最大5位数字，且首位不能为0 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 精度(scale) | NaN | 列类型：数字型，仅支持最大5位数字，且首位不能为0 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 字符长度(length) | NaN | 列类型：数字型，仅支持最大5位数字，且首位不能为0 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 列的中文名(label) | NaN | 列的中文名，长度<=30 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 是否可为空(nullable) | NaN | 是否可为空：是、否 | NaN | NaN | NaN | 否 | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 是否主键(primaryKey) | NaN | 是否主键：是、否 | NaN | NaN | NaN | 否 | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 绑定插件(generator) | NaN | 是否主键：是，数据来源应用定义-插件 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 参数(userProperty) | NaN | 是否主键：是，添加参数名、参数值 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 字段备注(comments) | NaN | 字段备注，长度<=300 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 删除列 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 编辑列 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询列 | NaN | NaN | 1、通过关键字查询列\n2、显示列名、中文名、列类型、是否为主键、是否可为空、字符长度、数字有效长度、精度、备注，不分页 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 新增索引 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 索引名称(indexName) | NaN | 索引名称，只能输入数字、英文字母、下划线，长度<=30 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 索引配置(indexColumn) | NaN | 添加排序规则，包括列字段，排序方式 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 是否是唯一索引(unique) | NaN | 是否是唯一索引：是、否 | NaN | NaN | NaN | 否 | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 是否是唯一查询条件(queryUniqueKey) | NaN | 是否是唯一查询条件：是、否 | NaN | NaN | NaN | 否 | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 索引描述(comments) | NaN | 索引描述，长度<=300 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 删除索引 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 编辑索引 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询索引 | NaN | NaN | 1、通过关键字查询索引\n2、显示索引名称、索引描述、是否是唯一索引、是否是唯一查询条件，不分页 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | SQL数据集 | NaN | NaN | NaN | <table desc="" title="12213321">\n <name>test</name>\n <tableType>dataSet</tableType>\n <alias>\n </alias>\n <label>12213321</label>\n <columns>\n <column name="course\_id" physicalType="String" label="" nullable="true" primaryKey="false" comments="">\n </column>\n <column name="assistant\_id" physicalType="String" label="" nullable="true" primaryKey="false" comments="">\n </column>\n </columns>\n <dataSourceRef>datasource</dataSourceRef>\n <status>true</status>\n <userProperties>\n <userProperty name="dataSetSql" valueType="CDATA">\n <cdataValue><![CDATA[select \* from COURSE\_ASS\_REL]]></cdataValue>\n </userProperty>\n <userProperty name="sqlParams" valueType="CDATA">\n <cdataValue><![CDATA[{"params":[{"name":"test","label":"测试","physicalType":"Double","defaultValue":"1"}]}]]></cdataValue>\n </userProperty>\n </userProperties>\n</table> | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | 新建SQL数据集 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 名称(title) | NaN | 名称，不支持<>&"'，长度<=100 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | ID(id) | NaN | ID，唯一，仅支持英文、数字、下划线，长度<=30 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | 复制SQL数据集 | NaN | NaN | NaN | 复制SQL数据集 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | 删除SQL数据集 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | 新增引用 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | 删除引用 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | 设计SQL数据集 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 基本信息 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | ID(id) | NaN | ID，唯一，仅支持英文、数字、下划线，长度<=30 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 表名(name) | NaN | 表名，长度<=100 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 中文名(label) | NaN | 中文名，长度<=200 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 表别名(alias) | NaN | 表别名，长度<=100 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 表类型(tableType) | NaN | 表类型：数据表、扩展表、中间表 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 数据源(dataSourceRef) | NaN | 下拉选择，数据来源应用定义-数据源 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 描述(desc) | NaN | 描述，长度<=300 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | SQL数据集 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 编辑列 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 列名(name) | NaN | SQL数据集生成，只读 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 列类型(physicalType) | NaN | 列类型，数据来源应用定义-数据类型-物理类型 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 数字有效长度(precision) | NaN | 列类型：数字型，仅支持最大5位数字，且首位不能为0 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 精度(scale) | NaN | 列类型：数字型，仅支持最大5位数字，且首位不能为0 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 字符长度(length) | NaN | 列类型：数字型，仅支持最大5位数字，且首位不能为0 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 列的中文名(label) | NaN | 列的中文名，长度<=30 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 是否可为空(nullable) | NaN | 是否可为空：是、否 | NaN | NaN | NaN | 否 | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 字段备注(comments) | NaN | 字段备注，长度<=300 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询列 | NaN | NaN | 1、通过关键字查询列\n2、显示列名、中文名、列类型、是否可为空、字符长度、数字有效长度、精度、备注，不分页 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 新增SQL参数 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 参数名(name) | NaN | 参数名，仅支持英文、数字、下划线，长度<=30 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 中文名(label) | NaN | 中文名，长度<=30 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 参数类型(physicalType) | NaN | 参数类型，数据来源应用定义-数据类型-物理类型 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 默认值(defaultValue) | NaN | 默认值，长度<=100 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 删除SQL参数 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 编辑SQL参数 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询SQL参数 | NaN | NaN | 1、通过关键字查询SQL参数\n2、显示参数名、中文名、参数类型、默认值，不分页 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | 实体 | NaN | NaN | NaN | NaN | <businessComponent xmlns="" id="chmChannelContactInfo" insRepoBusinessService="GeneralT3MethodBusinessService" insRepoType="API" title="渠道联系人" desc="">\n <name>渠道联系人</name>\n <field name="chn\_conp\_serial\_no" internalType="column" column="chn\_conp\_serial\_no" fieldType="String" length="19" required="true" pickListRef="" label="联系人编号" comments="" primaryKey="true" calculated="false">\n </field>\n <field name="chn\_conp\_name" internalType="column" column="chn\_conp\_name" fieldType="String" length="64" required="false" pickListRef="" label="联系人姓名" comments="" calculated="false">\n </field>\n <field name="mobile" internalType="column" column="mobile" fieldType="String" length="32" required="false" pickListRef="" label="手机号码" comments="" calculated="false">\n </field>\n <field name="chn\_code" internalType="column" column="chn\_code" fieldType="String" length="64" required="true" pickListRef="chmChannelInfoPickList" label="渠道代码" comments="" calculated="false">\n </field>\n <field name="wechat\_id" internalType="column" column="wechat\_id" fieldType="String" length="64" required="false" pickListRef="" label="微信账号" comments="" calculated="false">\n </field>\n <field name="chn\_conp\_duty" internalType="column" column="chn\_conp\_duty" fieldType="String" length="35" required="false" pickListRef="" label="渠道联系人职务" comments="" calculated="false">\n </field>\n <field name="telephone" internalType="column" column="telephone" fieldType="String" length="64" required="false" pickListRef="" label="联系电话" comments="" calculated="false">\n </field>\n <field name="email" internalType="column" column="email" fieldType="String" length="64" required="false" pickListRef="" label="电子邮箱" comments="" calculated="false">\n </field>\n <field name="birthday2" internalType="column" column="birthday2" fieldType="Date" length="64" required="false" pickListRef="" label="出生日期2" comments="" calculated="false">\n </field>\n <field name="sex" internalType="column" column="sex" fieldType="String" length="64" required="false" pickListRef="" label="性别" comments="" calculated="false">\n </field>\n <field name="age\_range" internalType="column" column="age\_range" fieldType="String" length="64" required="false" pickListRef="" label="年龄区间" comments="" calculated="false">\n </field>\n <field name="chn\_conp\_dept\_name" internalType="column" column="chn\_conp\_dept\_name" fieldType="String" length="200" required="false" pickListRef="" label="部门名称" comments="" calculated="false">\n </field>\n <field name="chn\_conp\_status" internalType="chn\_conp\_status" column="relation\_status" fieldType="String" length="64" required="false" pickListRef="" label="联系人状态" comments="" calculated="false">\n </field>\n <field name="resume" internalType="column" column="resume" fieldType="String" length="2000" required="false" pickListRef="" label="履历" comments="" calculated="false">\n </field>\n <field name="hobby" internalType="column" column="hobby" fieldType="String" length="255" required="false" pickListRef="" label="兴趣爱好" comments="" calculated="false">\n </field>\n <field name="remark" internalType="column" column="remark" fieldType="String" length="4000" required="false" pickListRef="" label="备注" comments="" calculated="false">\n </field>\n <field name="contact\_type" internalType="column" column="contact\_type" fieldType="String" length="64" required="false" pickListRef="" label="经办人类型" comments="" calculated="false">\n </field>\n <permission enabled="false">\n <userProperties>\n </userProperties>\n </permission>\n <method>\n <name>QUERY\_OBJECT\_LIST</name>\n <fullClass>com.hundsun.atom.infrastructure.pluginImpl.method.BusinessComponentQuery</fullClass>\n <userProperties>\n <userProperty name="apiConfig" value="{&apos;functionId&apos;:&apos;chm.getChannelFundContactInner&apos;,&apos;service&apos;:&apos;hswealth.chm&apos;,&apos;interfaceName&apos;:&apos;com.hundsun.hswealth.chmf.pub.service.InnerChmfService&apos;,&apos;version&apos;:&apos;v&apos;,&apos;group&apos;:&apos;g&apos;}">\n </userProperty>\n <userProperty name="paramsMapping" value="{&apos;chn\_conp\_serial\_no&apos;:{&apos;to&apos;:&apos;chn\_conp\_serial\_nos&apos;,&apos;action&apos;:&apos;toString&apos;}}">\n </userProperty>\n </userProperties>\n </method>\n <method>\n <name>CREATE\_OBJECT</name>\n <fullClass>com.hundsun.atom.infrastructure.pluginImpl.method.BusinessComponentQuery</fullClass>\n <userProperties>\n <userProperty name="apiConfig" value="{&apos;functionId&apos;:&apos;chm.postChannelFundContactInner&apos;,&apos;service&apos;:&apos;hswealth.chm&apos;,&apos;interfaceName&apos;:&apos;com.hundsun.hswealth.chmf.pub.service.InnerChmfService&apos;,&apos;version&apos;:&apos;v&apos;,&apos;group&apos;:&apos;g&apos;}">\n </userProperty>\n <userProperty name="paramsStructure" value="{&apos;isTree&apos;: {&apos;treeKey&apos;:&apos;channelcontact&apos;}}">\n </userProperty>\n </userProperties>\n </method>\n</businessComponent> | NaN | NaN | hep接口：/g/external/v/external/microservice/getList\n/g/external/v/external/table/getPag\n/g/external/v/external/interface/detail.json\n/g/external/v/external/interface/getPage | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | 实体 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | 新建实体 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 名称(title) | NaN | 名称，不支持<>&"'，长度<=100 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | ID(id) | NaN | ID，唯一，仅支持英文、数字、下划线，长度<=30 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | 复制实体 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | 删除实体 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | 新增引用 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | 删除引用 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | 设计实体 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 基本信息 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | ID(id) | NaN | ID，唯一，仅支持英文、数字、下划线，长度<=30 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 实体名称(name) | NaN | 实体名称，不支持<>&"'，长度<=100 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 创建类型(insRepoType) | NaN | 创建类型：绑定表、绑定逻辑、绑定插件 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 绑定表(table) | NaN | 创建类型：绑定表、绑定插件，数据来源同模块的数据表，支持从hep或sql导入 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 绑定逻辑(insRepoBusinessService) | NaN | 创建类型：绑定逻辑，数据来源同模块的逻辑 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 绑定插件(bcInsRepo) | NaN | 创建类型：绑定插件，数据来源应用定义-插件 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 是否权限控制(permission) | NaN | 是否权限控制：是、否 | NaN | NaN | NaN | 否 | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 用户参数(userProperty) | NaN | 是否权限控制：是，添加用户参数包括参数、值类型、值、表达式 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 描述(desc) | NaN | 描述，长度<=300 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 新增字段 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 分类(internalType) | NaN | 分类：绑定基表列、JOIN、计算字段 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 系统字段(systemField) | NaN | 分类：绑定基表列，包括4个选项 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 引用的表(tableRef) | NaN | 分类：JOIN，数据来源于同模块下数据表 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 绑定列(column) | NaN | 1、分类：绑定基表列，数据来源于同模块下数据表的列\n2、分类：JOIN，数据来源于引用的表 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 引用表的主键(targetColumn) | NaN | 分类：JOIN，数据来源于引用表的主键，自动填写 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 当前实体外键字段(sourceField) | NaN | 分类：JOIN，数据来源于当前实体的列 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 计算表达式(businessScript) | NaN | 分类：计算字段，编写表达式 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 字段名(name) | NaN | 字段名，数据来源于应用定义-标准字段 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 字段类型(fieldType) | NaN | 字段类型，数据来源于应用定义-数据类型-字段类型 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 长度(length) | NaN | 长度，仅支持最大5位数字，且首位不能为0 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 是否必填(required) | NaN | 分类：绑定基表列、JION，选项包括是、否 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 主键(primaryKey) | NaN | 分类：绑定基表列、JION，选项包括是、否 | NaN | NaN | NaN | 否 | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 默认值(defaultValue) | NaN | 分类：绑定基表列、JION，创建数据时，该字段按照填写的默认值入库 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 绑定字典(pickListRef) | NaN | 分类：绑定基表列、JION，数据来源于应用定义-字典 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 绑定字典(conditionalPickListRef) | NaN | 分类：计算字段，编写表达式 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 字段校验规则(fieldValidationRule) | NaN | 分类：绑定基表列、JION，添加的校验规则来源于物料资产中心的校验函数库 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 显示名称(label) | NaN | 显示名称，长度<=30 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 备注(comments) | NaN | 描述，长度<=300 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 从基表批量导入 | NaN | NaN | 从绑定的数据表选择列批量导入字段 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 从接口导入 | NaN | NaN | 从hep选择接口字段批量导入字段 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 排序字段 | NaN | NaN | 实体数据返回时的排序规则，配置包括排序字段、排序方式 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 默认查询条件 | NaN | NaN | 实体数据默认的查询条件，编写表达式 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 删除字段 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 编辑字段 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询字段 | NaN | NaN | 1、通过关键字查询字段\n2、显示字段名称、显示名称、字段类型、绑定列、是否必填、主键、默认值、字段校验规则、绑定字典、备注，不分页 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 新增多值字段 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 字段名(name) | NaN | 字段名，只能输入数字、英文字母、下划线，长度<=30 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 显示名称(label) | NaN | 显示名称，不支持<>&"'，长度<=100 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 描述(comments) | NaN | 描述，长度<=300 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 目标实体(destinationBusComp) | NaN | 目标实体，数据来源于同模块下实体 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 绑定的关联关系(destinationLink) | NaN | 在对象里面设置实体关系后自动填写 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 绑定字典(pickListRef) | NaN | 绑定字典，数据来源于应用定义-字典 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 删除多值字段 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 编辑多值字段 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询多值字段 | NaN | NaN | 1、通过关键字查询多值字段\n2、显示字段名、目标实体、绑定的关联关系，不分页 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 新增校验规则 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 规则名称(name) | NaN | 规则名称，只能输入数字、英文字母、下划线，长度<=30 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 校验失败提示(errorMessage) | NaN | 校验失败提示，长度<=300 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 表达式(businessScript) | NaN | 编写表达式 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 删除校验规则 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 编辑校验规则 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询校验规则 | NaN | NaN | 1、通过关键字查询校验规则\n2、显示规则名称、校验失败提示、表达式，不分页 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 新增接口与方法 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 方法名(name) | NaN | 方法名，只能输入数字、英文字母、下划线，长度<=30 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 完整类名(fullClass) | NaN | 完整类名，长度<=300 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 参数(userProperty) | NaN | 填加参数，包括参数、值类型、值、表达式 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 删除接口与方法 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 编辑接口与方法 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询接口与方法 | NaN | NaN | 1、通过关键字查询接口与方法\n2、显示方法名、完整类名，不分页 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 新增领域方法 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 方法名(name) | NaN | 方法名，只能输入数字、英文字母、下划线，长度<=30 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 描述(desc) | NaN | 描述，长度<=300 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 绑定的逻辑(businessServiceRef) | NaN | 绑定的逻辑，数据来源于当前模块-逻辑 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 删除领域方法 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 编辑领域方法 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询领域方法 | NaN | NaN | 1、通过关键字查询领域方法\n2、显示方法名、描述、绑定的逻辑，不分页 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | 子实体 | NaN | NaN | NaN | NaN | 子实体继承于实体\n1.子实体创建的规则：\na.一个实体支持创建多个子实体\nb.子实体不能创建子实体\nc.子实体只能在父实体所在的模块创建\nd.子实体创建后可以跨模块使用\ne.引用的实体不能创建子实体\n2.子实体修改的范围：\na.字段：长度、是否必填、绑定字典、显示名称、备注、默认值、排序字段、serchspec\nb.实体：绑定的逻辑、权限控制、描述\nc.多值字段：绑定字典\nd.接口与方法：只能修改参数的值和表达式、新增参数\ne.领域方法：描述、绑定的逻辑\nf.子实体新增的范围：字段、多值字段、校验规则、接口与方法、领域方法\n3.子实体相关功能:\na.实体相关下拉框列表中可选择到所有正确范围内的实体\nb.实体多值字段：目标实体不支持父子互相绑定（即不能将 父子实体 进行多值字段的 target 和 source 进行绑定）\nc.link 不支持父子互相绑定（即不能将 父子实体 进行 link）\nd.页面中绑定实体字段：能够绑定父实体以及子实体所有字段 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | 新建子实体 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | 复制子实体 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | 删除子实体 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | 新增引用 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | 删除引用 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | 设计子实体 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | 创建对象 | NaN | NaN | NaN | NaN | 基于实体快速创建对象 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | 对象 | NaN | NaN | NaN | NaN | <businessObject id="chmChannelContactInfo" title="渠道联系人">\n <name>渠道联系人</name>\n <primaryBusinessComponentRef>chmChannelContactInfo</primaryBusinessComponentRef>\n <description>\n </description>\n <businessObjectComponent businessComponentRef="chmChannelInfoTranslate">\n <linkRef>chmChannelContactInfo\_chmChannelInfoTranslate</linkRef>\n </businessObjectComponent>\n</businessObject> | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | 新建对象 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 名称(title) | NaN | 名称，不支持<>&"'，长度<=100 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | ID(id) | NaN | ID，唯一，仅支持英文、数字、下划线，长度<=30 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | 复制对象 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | 删除对象 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | 新增引用 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | 删除引用 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | 设计对象 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | 基本信息 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | ID(id) | NaN | ID，唯一，仅支持英文、数字、下划线，长度<=30 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 对象名称(name) | NaN | 对象名称 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 绑定实体(primaryBusinessComponentRef) | NaN | 绑定实体，数据来源于当前模块-实体 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 描述(desc) | NaN | 描述，长度<=300 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | 模型设计 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 新增实体 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | ID(id) | NaN | ID，唯一，仅支持英文、数字、下划线，长度<=30 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 名称(title) | NaN | 名称，不支持<>&"'，长度<=100 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 绑定表(table) | NaN | 绑定表，数据来源于当前模块-数据表，支持从hep同步或sql导入 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询实体 | NaN | NaN | 通过关键字查询实体 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 新增实体关系 | NaN | <link id="chmChannelContactInfo\_chmChannelInfoTranslate">\n <interTable>\n </interTable>\n <cascadeDelete>NONE</cascadeDelete>\n <searchSpec>\n </searchSpec>\n <sourceField>chn\_code</sourceField>\n <destinationField>chn\_code</destinationField>\n <interParentColumn>\n </interParentColumn>\n <interChildColumn>\n </interChildColumn>\n <parentBusinessComponentRef>chmChannelContactInfo</parentBusinessComponentRef>\n <childBusinessComponentRef>chmChannelInfoTranslate</childBusinessComponentRef>\n</link> | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 唯一标识(id) | NaN | 自动生成 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 关联类型(cascadeDelete) | NaN | 关联类型：查找关系和主子关系 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 关联方式(isTable) | NaN | 关联方式：普通关联和中间表关联 | NaN | NaN | NaN | 普通关联 | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 中间表(interTable) | NaN | 关联方式：中间表关联，数据来源于当面模块-数据表 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 父级实体(parentBusinessComponentRef) | NaN | 自动填写 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 父级实体对应的字段(sourceField) | NaN | 父实体关联字段（若为中间表场景，无需配置） | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 子级实体(childBusinessComponentRef) | NaN | 自动填写 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 子级实体对应的字段(destinationField) | NaN | 子实体关联字段（若为中间表场景，无需配置） | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 删除实体关系 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 编辑实体关系 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | 触发器 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 新增触发器 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 名称(name) | NaN | 名称，仅支持英文字母、数字、'\_'、中文、长度<=100 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 描述(desc) | NaN | 描述，长度<=300 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 事件类型(eventType) | NaN | 事件类型，包括6个选项 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 事件触发时机(eventStage) | NaN | 事件触发时机：之前、之后 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 业务脚本(businessScript) | NaN | 业务脚本，编写表达式 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 绑定的逻辑(businessServiceRef) | NaN | 绑定的逻辑，数据来源于当前模块-逻辑 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 删除触发器 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 编辑触发器 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询触发器 | NaN | NaN | 1、通过关键字查询触发器\n2、显示名称、事件类型、描述，不分页 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | 方法 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查看方法 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 方法名(name) | NaN | 对象内置方法 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 入参(parameters) | NaN | 对象内置方法的入参 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 出参(return) | NaN | 对象内置方法的出参 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | 对象生成页面 | NaN | NaN | NaN | NaN | 选择页面原型、对象，配置页面原型属性后快速生成页面 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | 选择页面原型 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | 选择对象 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | 配置页面原型属性 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | 创建流程 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.9 | V202401.00 |
| NaN | NaN | NaN | NaN | NaN | 填写流程名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.9 | V202401.00 |
| NaN | NaN | NaN | NaN | NaN | 填写流程编码 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.9 | V202401.00 |
| NaN | NaN | NaN | NaN | NaN | 填写流程模板 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.9 | V202401.00 |
| NaN | NaN | NaN | 逻辑 | NaN | NaN | NaN | NaN | <?xml version="1.0" encoding="UTF-8"?>\n<businessService id="mkmVisitrecordCreateTrigger" name="服务记录新增触发器" type="LIB" title="服务记录新增触发器">\n <fullClass>com.hundsun.hswealth.mkm.biz.dailywork.hcreator2.business.MkmVisitrecordCreateTrigger</fullClass>\n <businessServiceMethod name="triggerEvent" externalUse="false" desc="">\n <arg name="inputs" type="INPUT"></arg>\n </businessServiceMethod>\n</businessService> | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | 新建逻辑 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 名称(title) | NaN | 名称，不支持<>&"'，长度<=100 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | ID(id) | NaN | ID，唯一，仅支持英文、数字、下划线，长度<=30 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | 导入逻辑 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | 本地文件导入 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | 物料资产中心导入 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | 复制逻辑 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | 删除逻辑 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | 新增引用 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | 删除引用 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | 设计逻辑 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | 基本信息 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | ID(id) | NaN | ID，不支持<>&"'，长度<=100 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 名称(name) | NaN | 名称，不支持< > & " '，长度<=100 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 描述(desc) | NaN | 描述，长度<=300 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 参数(userProperty) | NaN | 填加参数，包括参数、值类型、值、表达式 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | 方法 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 新增方法 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 名称(name) | NaN | 名称，不支持< > & " '，长度<=100 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 是否外部使用(externalUse) | NaN | 是否外部使用：是、否 | NaN | NaN | NaN | 否 | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 添加参数(arg) | NaN | 添加参数，包括名称、类型、数据类型、默认值 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 添加表达式(\_script) | NaN | 编写逻辑方法表达式 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 删除方法 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 编辑方法 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询方法 | NaN | NaN | 1、通过关键字查询方法\n2、显示名称、是否外部使用，不分页 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | 页面 | NaN | NaN | NaN | NaN | {\n "version": "1.0.0",\n "componentsMap": [\n {\n "package": "hddml-components",\n "version": "2.7.1-beta.1",\n "exportName": "HddmlSelectTable",\n "main": "",\n "destructuring": true,\n "subName": "",\n "devStack": "vue2",\n "componentName": "HddmlSelectTable"\n },\n {\n "package": "hddml-components",\n "version": "2.7.1-beta.1",\n "exportName": "HddmlFormItem",\n "main": "",\n "destructuring": true,\n "subName": "",\n "devStack": "vue2",\n "componentName": "HddmlFormItem"\n },\n {\n "package": "hddml-components",\n "version": "2.7.1-beta.1",\n "exportName": "HddmlFieldPanel",\n "main": "",\n "destructuring": true,\n "subName": "",\n "devStack": "vue2",\n "componentName": "HddmlFieldPanel"\n },\n {\n "package": "hddml-components",\n "version": "2.7.1-beta.1",\n "exportName": "HddmlDatePicker",\n "main": "",\n "destructuring": true,\n "subName": "",\n "devStack": "vue2",\n "componentName": "HddmlDatePicker"\n },\n {\n "package": "hddml-components",\n "version": "2.7.1-beta.1",\n "exportName": "HddmlSelect",\n "main": "",\n "destructuring": true,\n "subName": "",\n "devStack": "vue2",\n "componentName": "HddmlSelect"\n },\n {\n "package": "hddml-components",\n "version": "2.7.1-beta.1",\n "exportName": "HddmlButton",\n "main": "",\n "destructuring": true,\n "subName": "",\n "devStack": "vue2",\n "componentName": "HddmlButton"\n },\n {\n "package": "hddml-components",\n "version": "2.7.1-beta.1",\n "exportName": "HddmlInput",\n "main": "",\n "destructuring": true,\n "subName": "",\n "devStack": "vue2",\n "componentName": "HddmlInput"\n },\n {\n "package": "hddml-components",\n "version": "2.7.1-beta.1",\n "exportName": "HddmlTimePicker",\n "main": "",\n "destructuring": true,\n "subName": "",\n "devStack": "vue2",\n "componentName": "HddmlTimePicker"\n },\n {\n "package": "hddml-components",\n "version": "2.7.1-beta.1",\n "exportName": "HddmlContainerCell",\n "main": "",\n "destructuring": true,\n "subName": "",\n "devStack": "vue2",\n "componentName": "HddmlContainerCell"\n },\n {\n "package": "hddml-components",\n "version": "2.7.1-beta.1",\n "exportName": "HddmlText",\n "main": "",\n "destructuring": true,\n "subName": "",\n "devStack": "vue2",\n "componentName": "HddmlText"\n },\n {\n "package": "hddml-components",\n "version": "2.7.1-beta.1",\n "exportName": "HddmlContainer",\n "main": "",\n "destructuring": true,\n "subName": "",\n "devStack": "vue2",\n "componentName": "HddmlContainer"\n },\n {\n "package": "hddml-components",\n "version": "2.7.1-beta.1",\n "exportName": "HddmlTextArea",\n "main": "",\n "destructuring": true,\n "subName": "",\n "devStack": "vue2",\n "componentName": "HddmlTextArea"\n },\n {\n "package": "hddml-components",\n "version": "2.7.1-beta.1",\n "exportName": "HddmlUploadDetailApplet",\n "main": "",\n "destructuring": true,\n "subName": "",\n "devStack": "vue2",\n "componentName": "HddmlUploadDetailApplet"\n },\n {\n "package": "hddml-components",\n "version": "2.7.1-beta.1",\n "exportName": "HddmlForm",\n "main": "",\n "destructuring": true,\n "subName": "",\n "devStack": "vue2",\n "componentName": "HddmlForm"\n },\n {\n "package": "hddml-components",\n "version": "2.7.1-beta.1",\n "exportName": "UpDownContainer",\n "main": "",\n "destructuring": true,\n "subName": "",\n "devStack": "vue2",\n "componentName": "UpDownContainer"\n },\n {\n "devMode": "lowCode",\n "componentName": "Page"\n }\n ],\n "componentsTree": [\n {\n "componentName": "Page",\n "id": "root",\n "props": {},\n "fileName": "/",\n "dataSource": {\n "list": [\n {\n "type": "businessObject",\n "resourceId": "mkmVisitrecord",\n "isInit": false,\n "isShowDefaultTip": false,\n "id": "mkmVisitrecord"\n },\n {\n "type": "pickList",\n "resourceId": "chmChannelInfoPickList",\n "id": "chmChannelInfoPickList"\n },\n {\n "type": "pickList",\n "resourceId": "chmChannelContactInfoPickList",\n "id": "chmChannelContactInfoPickList"\n },\n {\n "type": "pickList",\n "resourceId": "serviceTypeEnum",\n "id": "serviceTypeEnum"\n },\n {\n "type": "pickList",\n "resourceId": "serviceTopicEnum",\n "id": "serviceTopicEnum"\n },\n {\n "type": "pickList",\n "resourceId": "chmProductInfoPickList",\n "id": "chmProductInfoPickList"\n },\n {\n "type": "pickList",\n "resourceId": "tsysUserPickList",\n "id": "tsysUserPickList"\n },\n {\n "type": "businessObject",\n "resourceId": "chmChannelInfo",\n "isInit": false,\n "isShowDefaultTip": true,\n "id": "chmChannelInfo"\n },\n {\n "type": "businessObject",\n "resourceId": "chmChannelContactInfo",\n "isInit": false,\n "isShowDefaultTip": true,\n "id": "chmChannelContactInfo"\n },\n {\n "type": "businessObject",\n "resourceId": "tsysUser",\n "isInit": false,\n "isShowDefaultTip": true,\n "id": "tsysUser"\n },\n {\n "type": "businessObject",\n "resourceId": "chmProductInfo",\n "isInit": false,\n "isShowDefaultTip": true,\n "id": "chmProductInfo"\n },\n {\n "type": "fetch",\n "isInit": false,\n "isShowDefaultTip": false,\n "options": {\n "params": {\n "keys": "user\_name"\n },\n "method": "POST",\n "isCors": true,\n "timeout": 5000,\n "headers": {\n "Content-Type": "application/json;charset=UTF-8"\n },\n "uri": "/g/hswealth.mkm/v/hcreator2/v1/parameter/getValues"\n },\n "id": "parameter"\n },\n {\n "type": "businessObject",\n "resourceId": "ppsFileStorage",\n "isInit": false,\n "isShowDefaultTip": true,\n "id": "ppsFileStorage"\n },\n {\n "type": "fetch",\n "isInit": false,\n "isShowDefaultTip": false,\n "options": {\n "params": {\n "param\_code": "44006"\n },\n "method": "POST",\n "isCors": true,\n "timeout": 5000,\n "headers": {\n "Content-Type": "application/json;charset=UTF-8"\n },\n "uri": "/g/hswealth.oms/v/getParameterByCode"\n },\n "id": "visitDateRestriction"\n },\n {\n "type": "businessObject",\n "resourceId": "mkmBrokerPosition",\n "isInit": false,\n "isShowDefaultTip": true,\n "id": "mkmBrokerPosition"\n },\n {\n "type": "businessObject",\n "resourceId": "chmChannelNet",\n "isInit": false,\n "isShowDefaultTip": true,\n "id": "chmChannelNet"\n },\n {\n "type": "pickList",\n "resourceId": "mkmProjectPickList",\n "id": "mkmProjectPickList"\n },\n {\n "type": "businessObject",\n "resourceId": "mkmProject",\n "isInit": false,\n "isShowDefaultTip": true,\n "id": "mkmProject"\n }\n ]\n },\n "css": "",\n "originCode": "class LowcodeComponent extends Component {\n state = {\n // url参数\n urlParams: {},\n // 页面参数\n formOptions: {\n boName: 'mkmVisitrecord',\n bcName: 'mkmVisitrecord',\n pageId: '',\n formRefId: 'form-d09b0267',\n foldTitle: '渠道信息'\n },\n // 页面参数\n propParams: {\n visitDate: null,\n beginDate: null,\n endDate: null,\n needDraftFlag: true,\n source: null,\n dailyId: null,\n weeklyId: null,\n commitType: null,\n rowId: null\n },\n // 系统参数\n parameter: null,\n //下拉表格详情回显值\n pickList: {\n chn\_code: null,\n net\_codes: null,\n channel\_contact\_ids: null,\n participater\_codes: null,\n product\_codes: null,\n project\_no: null,\n broker\_position\_id: null\n },\n // 服务日期可选范围限制（N天）\n visitDateRestriction: 30,\n // 按钮loading\n loadingFlag: false,\n // 是否展示按钮区\n showBtnArea: true,\n hightBetArea: '48px',\n // 选中的渠道名称\n selectedChnName: '',\n // 是否实地拜访\n fieldVisitFlag: true,\n // 打卡地址是否必填\n requireBrokerPositionId: true,\n // 未关联打卡原因是否必填\n requireMemo: true,\n // 渠道联系人searchSpec\n channelContactSearchSpec: '',\n // 打卡地址searchSpec\n brokerPositionSearchSpec: '',\n // 额外展示的打卡地址id（关联查询用）\n existsBrokerPositionId: '',\n //是否禁用联系人\n disabledContact: true,\n //是否禁用服务日期\n disabledVisitDate: false,\n // 是否保留打卡地址\n keepBrokerPositionId: false,\n // 是否展示表单（重置表单用）\n showForm: true,\n rules: {\n idKind: [],\n idKindDefault: [{\n \"type\": \"maxLen\",\n \"content\": 64,\n \"errorMsg\": \"长度最大为64\"\n }]\n },\n 'mkmVisitrecord\_mkmVisitrecord': {\n model: {\n 'visit\_date': undefined,\n 'visit\_type': undefined,\n 'copy\_broker\_position\_id': undefined,\n 'net\_code': undefined,\n 'channel\_contact\_ids': undefined,\n 'participater\_codes': undefined,\n 'other\_participater\_name': undefined,\n 'visit\_title': undefined,\n 'project\_no': undefined,\n 'visit\_time\_range': undefined,\n 'address': undefined,\n 'memo': undefined,\n 'product\_codes': undefined,\n 'visit\_content': undefined,\n 'follow\_act\_remark': undefined\n },\n pickList: {\n 'visit\_date': undefined,\n 'visit\_type': undefined,\n 'copy\_broker\_position\_id': undefined,\n 'net\_code': undefined,\n 'channel\_contact\_ids': undefined,\n 'participater\_codes': undefined,\n 'other\_participater\_name': undefined,\n 'visit\_title': undefined,\n 'project\_no': undefined,\n 'visit\_time\_range': undefined,\n 'address': undefined,\n 'memo': undefined,\n 'product\_codes': undefined,\n 'visit\_content': undefined,\n 'follow\_act\_remark': undefined\n }\n }\n };\n componentDidMount() {\n this.init();\n console.log('did mountV2');\n }\n componentWillUnmount() {\n console.log('will unmount');\n }\n\n /\*\*\n \* 初始化\n \*/\n init() {\n console.log('初始化');\n if (this?.$attrs?.params) {\n this.initPropsInf(this.$attrs.params);\n }\n this.initBizUtils();\n\n // 初始化参数：是否实地拜访\n this.state.fieldVisitFlag = this.state.urlParams?.visitType === 'field';\n\n // 初始化参数：支持填写的服务日期范围\n this.dataSourceMap['visitDateRestriction'].load({\n data: {}\n }).then(res => {\n console.log(\"获取OMS参数:::\", res);\n if (res.param\_value) {\n this.state.visitDateRestriction = parseInt(res.param\_value);\n }\n }).catch(error => {\n console.error(\"调用获取OMS参数接口异常:::\", error);\n });\n console.log('this.state :::', this.state);\n }\n\n /\*\*\n \* 关闭\n \*/\n onClose() {\n console.log('关闭');\n this.bizUtils.backPage({\n reload: false\n });\n // this.initPropsInf({\n // visitDate: '20240404',\n // beginDate: '20240402',\n // endDate: '20240406',\n // source: 'weekly',\n // // dailyId: '',\n // // weeklyId: '',\n // commitType: 'CREATE\_OBJECT',\n // // rowId: '3'\n // });\n // this.submitInf({ dailyStatus:'1'});\n }\n\n /\*\*\n \* 提交\n \*/\n onSubmit(event, ext) {\n console.log('触发保存:::', ext);\n this.state.loadingFlag = true;\n let refId = this.state.formOptions.formRefId;\n const dailyStatus = ext.daily\_status;\n if (dailyStatus == '0') {\n return new Promise(resolve => {\n this.beforeDoSubmit(dailyStatus);\n this.bizUtils.onSubmit({\n successCloseFlag: ext?.successCloseFlag\n }).then(result => {\n this.state.loadingFlag = false;\n resolve(result);\n });\n });\n } else {\n return new Promise(resolve => {\n this.$refs[refId]['\_data'].validate(valid => {\n // true=校验失败，false=校验成功\n if (!valid) {\n this.$hMessage.error('校验失败，请确认后再提交！');\n this.state.loadingFlag = false;\n resolve({\n success: false\n });\n } else {\n this.beforeDoSubmit(dailyStatus);\n this.bizUtils.onSubmit({\n successCloseFlag: ext?.successCloseFlag\n }).then(result => {\n this.state.loadingFlag = false;\n resolve(result);\n });\n }\n });\n });\n }\n }\n\n /\*\*\n \* 新增表单，页面初始化回调\n \*/\n initCallback() {\n console.log('initCallback');\n\n // 服务日期默认值：当天\n let formattedCurrentDate = this.$utils[\"hddml-utils\"].dayjs(new Date()).format('YYYY-MM-DD');\n // 日期默认走当前日期，或前置页面指定\n if (this.state.propParams.visitDate) {\n this.state.mkmVisitrecord\_mkmVisitrecord.model.visit\_date = this.$utils[\"hddml-utils\"].dayjs(this.state.propParams.visitDate, 'YYYYMMDD').toDate().getTime();\n } else {\n this.state.mkmVisitrecord\_mkmVisitrecord.model.visit\_date = new Date(formattedCurrentDate).getTime();\n }\n // 服务方式默认值：实地拜访\n this.state.mkmVisitrecord\_mkmVisitrecord.model.visit\_type = '1';\n // 时长默认值：0\n this.state.mkmVisitrecord\_mkmVisitrecord.model.visit\_time = 0;\n // 服务对象类型默认值：渠道\n this.state.mkmVisitrecord\_mkmVisitrecord.model.visit\_object\_type = '4206';\n // 更新打卡地址查询条件\n this.updateBrokerPositionSearchSpec(this.state.mkmVisitrecord\_mkmVisitrecord.model.visit\_date);\n this.addEditInit();\n }\n\n /\*\*\n \* 修改表单，页面初始化回调\n \*/\n queryCallback() {\n console.log('queryCallback');\n // 控制草稿按钮是否展示\n if (this.state.mkmVisitrecord\_mkmVisitrecord.model.daily\_status && this.state.mkmVisitrecord\_mkmVisitrecord.model.daily\_status === '1') {\n this.state.propParams.needDraftFlag = false;\n }\n // 时长的时间区间\n if (this.state.mkmVisitrecord\_mkmVisitrecord.model.visit\_start\_date\_time === 0 && this.state.mkmVisitrecord\_mkmVisitrecord.model.visit\_end\_date\_time === 0) {\n this.state.mkmVisitrecord\_mkmVisitrecord.model.visit\_time\_range = [];\n } else {\n this.state.mkmVisitrecord\_mkmVisitrecord.model.visit\_time\_range = [this.$utils[\"hddml-utils\"].dayjs(this.state.mkmVisitrecord\_mkmVisitrecord.model.visit\_start\_date\_time).format('HH:mm'), this.$utils[\"hddml-utils\"].dayjs(this.state.mkmVisitrecord\_mkmVisitrecord.model.visit\_end\_date\_time).format('HH:mm')];\n }\n // 渠道\n if (this.state.mkmVisitrecord\_mkmVisitrecord.model.chn\_code && this.state.mkmVisitrecord\_mkmVisitrecord.model.chn\_code.length > 0) {\n this.state.mkmVisitrecord\_mkmVisitrecord.model.chn\_code\_str = this.state.mkmVisitrecord\_mkmVisitrecord.model.chn\_code[0];\n this.state.disabledContact = false;\n } else {\n this.state.disabledContact = true;\n }\n this.state.selectedChnName = this.state.mkmVisitrecord\_mkmVisitrecord.model.pickList?.chn\_code?.[0];\n // 下拉表格回显\n this.state.pickList.chn\_code = this.state.mkmVisitrecord\_mkmVisitrecord.model.pickList?.chn\_code?.[0];\n this.state.pickList.net\_codes = this.state.mkmVisitrecord\_mkmVisitrecord.model.pickList?.net\_codes;\n this.state.pickList.channel\_contact\_ids = this.state.mkmVisitrecord\_mkmVisitrecord.model.pickList?.channel\_contact\_ids;\n this.state.pickList.participater\_codes = this.state.mkmVisitrecord\_mkmVisitrecord.model.pickList?.participater\_codes;\n this.state.pickList.product\_codes = this.state.mkmVisitrecord\_mkmVisitrecord.model.pickList?.product\_codes;\n this.state.pickList.project\_no = this.state.mkmVisitrecord\_mkmVisitrecord.model.pickList?.project\_no;\n this.state.pickList.broker\_position\_id = this.state.mkmVisitrecord\_mkmVisitrecord.model.pickList?.broker\_position\_id;\n // 查询附件信息\n let bizKey = 'mkm\_visitrecord';\n let bizValue = this.state.mkmVisitrecord\_mkmVisitrecord.model.ROW\_ID;\n this.state.mkmVisitrecord\_ppsFileStorage.$query.RELATION\_BIZ\_VALUE = bizValue;\n this.state.mkmVisitrecord\_ppsFileStorage.$query.RELATION\_BIZ\_KEY = bizKey;\n this.dataSourceCustomMap['ppsFileStorage'].query({\n \"bo\": 'ppsFileStorage',\n \"bc\": 'ppsFileStorage',\n \"mainBc\": 'ppsFileStorage'\n }, {\n \"RELATION\_BIZ\_VALUE\": bizValue,\n \"RELATION\_BIZ\_KEY\": bizKey\n }).then(\_data => {\n // 附件赋值\n if (\_data.success && \_data?.data?.response[0]?.result?.data.length > 0) {\n console.log(\"附件展示\", \_data.success ? \_data.data.response[0].result.data[0].boData.bcData : []);\n this.state.mkmVisitrecord\_ppsFileStorage.$list = \_data.success ? \_data.data.response[0].result.data?.map(item => item?.boData?.bcData) : [];\n console.log('this.state.mkmVisitrecord\_ppsFileStorage.$list', this.state.mkmVisitrecord\_ppsFileStorage.$list);\n }\n });\n // 打卡地址\n if (this.state.mkmVisitrecord\_mkmVisitrecord.model.broker\_position\_id) {\n this.state.mkmVisitrecord\_mkmVisitrecord.model.copy\_broker\_position\_id = this.state.mkmVisitrecord\_mkmVisitrecord.model.broker\_position\_id;\n console.log('copy\_broker\_position\_id赋值:::', this.state.mkmVisitrecord\_mkmVisitrecord.model.copy\_broker\_position\_id, this.state.mkmVisitrecord\_mkmVisitrecord.model.broker\_position\_id);\n this.state.existsBrokerPositionId = this.state.mkmVisitrecord\_mkmVisitrecord.model.broker\_position\_id;\n }\n this.state.keepBrokerPositionId = true;\n // 更新打卡地址查询条件\n this.updateBrokerPositionSearchSpec(this.state.mkmVisitrecord\_mkmVisitrecord.model.visit\_date);\n this.addEditInit();\n }\n\n /\*\*\n \* 新建和修改页面通用初始化\n \*/\n addEditInit() {\n // 修改和通过日报页面新增的情况下，服务日期不可改\n if (this.state.propParams.rowId || this.state.propParams.source === 'daily' && this.state.propParams.visitDate) {\n this.state.disabledVisitDate = true;\n }\n }\n\n /\*\*\n \* 提交前处理数据\n \*/\n beforeDoSubmit(dailyStatue) {\n // 服务开始时间 - 结束时间\n if (this.state.mkmVisitrecord\_mkmVisitrecord.model.visit\_time\_range && this.state.mkmVisitrecord\_mkmVisitrecord.model.visit\_time\_range.length > 0) {\n this.state.mkmVisitrecord\_mkmVisitrecord.model.visit\_start\_date\_time = this.getTimestamp(this.state.mkmVisitrecord\_mkmVisitrecord.model.visit\_date, this.state.mkmVisitrecord\_mkmVisitrecord.model.visit\_time\_range[0]);\n this.state.mkmVisitrecord\_mkmVisitrecord.model.visit\_end\_date\_time = this.getTimestamp(this.state.mkmVisitrecord\_mkmVisitrecord.model.visit\_date, this.state.mkmVisitrecord\_mkmVisitrecord.model.visit\_time\_range[1]);\n } else {\n this.state.mkmVisitrecord\_mkmVisitrecord.model.visit\_start\_date\_time = 0;\n this.state.mkmVisitrecord\_mkmVisitrecord.model.visit\_end\_date\_time = 0;\n }\n // 提交状态\n this.state.mkmVisitrecord\_mkmVisitrecord.model.daily\_status = dailyStatue;\n // 关联日报id\n if (this.state.propParams.dailyId) {\n this.state.mkmVisitrecord\_mkmVisitrecord.model.daily\_id = this.state.propParams.dailyId;\n }\n // 关联周报id\n if (this.state.propParams.weeklyId) {\n this.state.mkmVisitrecord\_mkmVisitrecord.model.week\_id = this.state.propParams.weeklyId;\n }\n // 打卡地址id\n if (this.state.mkmVisitrecord\_mkmVisitrecord.model.copy\_broker\_position\_id) {\n this.state.mkmVisitrecord\_mkmVisitrecord.model.broker\_position\_id = this.state.mkmVisitrecord\_mkmVisitrecord.model.copy\_broker\_position\_id;\n } else {\n this.state.mkmVisitrecord\_mkmVisitrecord.model.broker\_position\_id = ' ';\n }\n }\n\n // 更新打卡地址查询条件\n updateBrokerPositionSearchSpec(visitDate) {\n let createDateStr = this.$utils[\"hddml-utils\"].dayjs(visitDate).format('YYYYMMDD');\n this.state.brokerPositionSearchSpec = \"related\_flag = '0' and create\_date\_str = '\" + createDateStr + \"'\";\n if (this.state.existsBrokerPositionId !== '') {\n this.state.brokerPositionSearchSpec += \" and exists\_broker\_position\_id = '\" + this.state.existsBrokerPositionId + \"'\";\n }\n }\n\n /\*\*\n \* 事件：服务日期修改\n \*/\n onChangeVisitDate(value) {\n console.log('onChangeVisitDate():::', this.$utils[\"hddml-utils\"].dayjs(value).format('YYYY-MM-DD'));\n // 更新打卡地址查询条件\n this.updateBrokerPositionSearchSpec(value);\n console.log('brokerPositionSearchSpec:::', this.state.brokerPositionSearchSpec);\n // 清空打卡地址\n if (!this.state.keepBrokerPositionId && this.state.mkmVisitrecord\_mkmVisitrecord.model.copy\_broker\_position\_id && this.state.mkmVisitrecord\_mkmVisitrecord.model.copy\_broker\_position\_id !== '') {\n console.log('清空打卡地址:::', this.state.mkmVisitrecord\_mkmVisitrecord.model.copy\_broker\_position\_id, this.state.pickList.broker\_position\_id);\n this.state.mkmVisitrecord\_mkmVisitrecord.model.copy\_broker\_position\_id = '';\n delete this.state.pickList.broker\_position\_id;\n }\n console.log('keepBrokerPositionId:::', this.state.keepBrokerPositionId);\n this.state.keepBrokerPositionId = false;\n }\n\n /\*\*\n \* 事件：服务时间修改，重新计算时长\n \*/\n onChangeVisitTimeRange(value) {\n console.log('onChangeVisitTimeRange():::', value);\n if (value.length === 0) {\n this.state.mkmVisitrecord\_mkmVisitrecord.model.visit\_time = 0;\n } else {\n let beginTime = '2020-01-01 ' + value[0] + ':00';\n let endTime = '2020-01-01 ' + value[1] + ':00';\n this.state.mkmVisitrecord\_mkmVisitrecord.model.visit\_time = this.$utils[\"hddml-utils\"].dayjs(endTime).diff(beginTime, 'minutes');\n }\n console.log('时长（分钟）:::', this.state.mkmVisitrecord\_mkmVisitrecord.model.visit\_time);\n }\n\n /\*\*\n \* 事件：渠道联系人下拉框聚焦\n \*/\n onChnContactFocus() {\n console.log('onChnContactFocus():::');\n this.$refs['selecttable-63b82bee'].queryData({\n page: {\n current: 1,\n size: 5\n }\n });\n }\n\n /\*\*\n \* 事件：打卡地址下拉框聚焦\n \*/\n onBrokerPositionFocus() {\n console.log('onBrokerPositionFocus():::');\n this.$refs['selecttable-db02f6c5'].queryData({\n page: {\n current: 1,\n size: 5\n }\n });\n }\n\n /\*\*\n \* 获取时间戳\n \*/\n getTimestamp(date, formattedTime) {\n let formattedDate = this.$utils[\"hddml-utils\"].dayjs(date).format('YYYY-MM-DD');\n let formattedDatetime = formattedDate + \" \" + formattedTime + \":00\";\n return new Date(formattedDatetime).getTime();\n }\n\n /\*\*\n \* 事件：关联渠道变化\n \*/\n onChnCodeChange(value) {\n console.log('关联渠道变化:::', this.state.mkmVisitrecord\_mkmVisitrecord.model.chn\_code, value);\n if (this.state.mkmVisitrecord\_mkmVisitrecord.model.chn\_code && this.state.mkmVisitrecord\_mkmVisitrecord.model.chn\_code[0] !== value) {\n // 清空渠道联系人\n this.state.mkmVisitrecord\_mkmVisitrecord.model.channel\_contact\_ids = [];\n console.log('清空渠道联系人');\n }\n // 绑定数据\n if (value && value != '') {\n this.state.mkmVisitrecord\_mkmVisitrecord.model.chn\_code = [value];\n } else {\n this.state.mkmVisitrecord\_mkmVisitrecord.model.chn\_code = [];\n }\n // 渠道联系人查询条件\n if (value && value != '') {\n this.state.channelContactSearchSpec = \"chn\_code = '\" + value + \"'\";\n this.state.disabledContact = false;\n } else {\n this.state.channelContactSearchSpec = '';\n this.state.disabledContact = true;\n }\n console.log('渠道联系人查询条件:::', this.state.channelContactSearchSpec);\n console.log('表单数据:::', this.state.mkmVisitrecord\_mkmVisitrecord);\n }\n\n /\*\*\n \* 事件：关联打卡地址变化\n \*/\n onBrokerPositionIdChange(value) {\n console.log('onBrokerPositionIdChange():::', value);\n if (value && value.trim() !== '') {\n this.state.requireMemo = false;\n this.state.requireBrokerPositionId = true;\n this.state.mkmVisitrecord\_mkmVisitrecord.model.memo = '';\n } else {\n this.state.requireMemo = true;\n }\n }\n\n /\*\*\n \* 事件：新增渠道联系人\n \*/\n onAddChannelContact() {\n console.log('this.state.mkmVisitrecord\_mkmVisitrecord.model.chn\_code\_str:::', this.state.mkmVisitrecord\_mkmVisitrecord.model.chn\_code\_str);\n if (!this.state.mkmVisitrecord\_mkmVisitrecord.model.chn\_code\_str || this.state.mkmVisitrecord\_mkmVisitrecord.model.chn\_code\_str === '') {\n this.$hMessage.error('请先选择渠道');\n return;\n }\n let url = '/chm/contactfundForm';\n let tabName = '新增渠道联系人';\n let compId = 'contactfundForm';\n let params = {\n opType: 'add',\n chn\_code: this.state.mkmVisitrecord\_mkmVisitrecord.model.chn\_code\_str,\n chn\_name: this.state.selectedChnName\n };\n console.log('params:::', params);\n let uid = 'contact\_add';\n this.$tabs.addNewTab(compId + uid, url + uid, params, tabName, {}, true, 'hswealth-chm', compId, false, {\n comName: compId,\n id: compId + uid\n });\n }\n\n /\*\*\n \* 事件：服务方式改变\n \*/\n onVisitTypeChange(value) {\n console.log('onVisitTypeChange():::', value);\n if (value === '1') {\n // 实地拜访\n console.log('实地拜访');\n this.state.fieldVisitFlag = true;\n this.state.requireBrokerPositionId = !(this.state.mkmVisitrecord\_mkmVisitrecord.model.memo && this.state.mkmVisitrecord\_mkmVisitrecord.model.memo.trim() != '');\n this.state.requireMemo = !(this.state.mkmVisitrecord\_mkmVisitrecord.model.copy\_broker\_position\_id && this.state.mkmVisitrecord\_mkmVisitrecord.model.copy\_broker\_position\_id != '');\n this.state.mkmVisitrecord\_mkmVisitrecord.model.address = '';\n } else {\n // 非实地拜访\n console.log('非实地拜访');\n this.state.fieldVisitFlag = false;\n this.state.requireBrokerPositionId = false;\n this.state.requireMemo = false;\n if (this.state.mkmVisitrecord\_mkmVisitrecord.model.copy\_broker\_position\_id && this.state.mkmVisitrecord\_mkmVisitrecord.model.copy\_broker\_position\_id !== '') {\n console.log('清空打卡地址:::', this.state.mkmVisitrecord\_mkmVisitrecord.model.copy\_broker\_position\_id, this.state.pickList.broker\_position\_id);\n this.state.mkmVisitrecord\_mkmVisitrecord.model.copy\_broker\_position\_id = '';\n delete this.state.pickList.broker\_position\_id;\n }\n this.state.mkmVisitrecord\_mkmVisitrecord.model.memo = '';\n }\n }\n\n /\*\*\n \* 事件：未关联打卡原因改变\n \*/\n onMemoChange(value) {\n console.log('onMemoChange():::', value);\n if (value && value.trim() !== '') {\n this.state.requireBrokerPositionId = false;\n } else {\n this.state.requireBrokerPositionId = true;\n }\n console.debug('表单对象:::', this.state.mkmVisitrecord\_mkmVisitrecord);\n }\n\n /\*\*\n \* 选中关联渠道\n \* 点击选项时触发, 返回当前选项对应的整行数据(selection)以及选中/取消选中状态(selected)。多选模式下, 点击面板中的全选/全不选不会生效\n \*/\n onChnCodeSelected(selection, selected) {\n console.log('onChnCodeSelected():::', selection, selected);\n // 把渠道名称存起来，跳转新增渠道联系人页面时用\n this.state.selectedChnName = selection.chn\_name;\n }\n\n /\*\*\n \* 服务日期可选范围限制\n \*/\n disabledDate(date) {\n let dateStr = this.$utils[\"hddml-utils\"].dayjs(date).format('YYYYMMDD');\n if (this.state.propParams.beginDate && dateStr < this.state.propParams.beginDate) {\n // console.log('服务日期可选范围限制1:::', dateStr, this.state.propParams.beginDate);\n return true;\n }\n if (this.state.propParams.endDate && dateStr > this.state.propParams.endDate) {\n // console.log('服务日期可选范围限制2:::', dateStr, this.state.propParams.endDate);\n return true;\n }\n let beginTime = date;\n let endTime = new Date(this.$utils[\"hddml-utils\"].dayjs(new Date()).format('YYYY-MM-DD') + \" 00:00:00\");\n let daysDiff = this.$utils[\"hddml-utils\"].dayjs(endTime).diff(beginTime, 'days');\n // console.log('服务日期可选范围限制3:::', beginTime, endTime, daysDiff);\n return daysDiff > this.state.visitDateRestriction || daysDiff < 0;\n }\n\n /\*\*\n \* 更新附件\n \*/\n updateFile(val) {\n this.state.mkmVisitrecord\_ppsFileStorage.$list = val;\n }\n\n /\*\*\n \* 设置当前用户\n \*/\n setCurrentUser() {\n this.dataSourceMap['parameter'].load({\n data: {}\n }).then(res => {\n console.log(\"获取系统参数\", res);\n this.state.parameter = res.success ? res.data : {};\n }).catch(error => { });\n }\n\n /\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\n \* \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*外部调用的函数开放\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\n \* \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/\n /\*\*\n \* 初始化入参\n \*/\n initPropsInf({\n visitDate,\n beginDate,\n endDate,\n source,\n dailyId,\n weeklyId,\n commitType,\n rowId\n }) {\n this.state.propParams.visitDate = visitDate;\n this.state.propParams.beginDate = beginDate;\n this.state.propParams.endDate = endDate;\n this.state.propParams.needDraftFlag = false;\n this.state.propParams.source = source;\n this.state.propParams.dailyId = dailyId;\n this.state.propParams.weeklyId = weeklyId;\n this.state.propParams.commitType = commitType;\n this.state.propParams.rowId = rowId;\n // 隐藏按钮区\n if (source === 'daily' || source === 'weekly') {\n console.log('hideBtnArea');\n this.state.showBtnArea = false;\n this.state.hightBetArea = '0px';\n }\n }\n /\*\*\n \* 提交\n \*/\n submitInf({\n dailyStatus\n }) {\n let params = {\n daily\_status: dailyStatus\n };\n if (this.state.propParams.source === 'daily' || this.state.propParams.source === 'weekly') {\n params.successCloseFlag = 0;\n }\n return this.onSubmit(null, params);\n //true：提交（表单页面会有成功标识）\n //false：失败（表单页面会有错误弹框）\n }\n\n /\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\n \* \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*工具方法begin\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\n \* \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/\n initBizUtils() {\n this.bizUtils = {\n init: () => {\n const boName = this.state.formOptions.boName;\n const bcName = this.state.formOptions.bcName;\n const bobcName = `${boName}\_${bcName}`;\n this.state.windowObj = window?.proxy || window;\n const params = this.bizUtils.getQueryParams(location.href);\n this.state.urlParams = params;\n const rowId = params?.rowId || this.state.propParams.rowId;\n const commitType = params?.commitType || this.state.propParams.commitType;\n this.state.formOptions.pageId = JSON.parse(localStorage.getItem('bizStorage')).activeMenuItem.uuid;\n\n // 新增\n if (commitType === 'CREATE\_OBJECT') {\n if (this.initCallback) {\n this.initCallback();\n }\n }\n this.$set(this.state[bobcName]['model'], 'copy\_broker\_position\_id', '');\n // 修改，先做一次查询\n if (commitType === 'UPDATE\_OBJECT') {\n this.dataSourceCustomMap[boName].query({\n bo: boName,\n bc: bcName,\n mainBc: bcName\n }, {\n ROW\_ID: rowId\n }).then(data => {\n console.log(\"查询data\", data);\n const \_data = data.data.response[0].result.data[0].boData.bcData;\n \_data.copy\_broker\_position\_id = \_data.broker\_position\_id;\n this.$set(this.state[bobcName], 'model', \_data);\n this.$set(this.state[bobcName], 'pickList', data.data.response[0].result.data[0].boData.pickList);\n if (this.queryCallback) {\n this.queryCallback();\n }\n });\n }\n },\n /\*\*\n \* 表单提交（根据BO,BC提交）\n \* @param bcName BC名称\n \* @param boName BO名称（不传时，与BC一致）\n \*/\n onSubmit: ({\n successCloseFlag = 1\n }) => {\n const boName = this.state.formOptions.boName;\n const bcName = this.state.formOptions.bcName;\n const bobcName = `${boName}\_${bcName}`;\n const rowId = this.bizUtils.getQueryParams(location.href)?.rowId || this.state.propParams.rowId;\n const commitType = this.bizUtils.getQueryParams(location.href)?.commitType || this.state.propParams.commitType;\n let | NaN | NaN | 物料接口：/materialManage/designerPluginManager/getDesignerPluginPageDesigner\n/materialManage/lowcodePackageManager/getPackageListDesigner\n/materialManage/packageManager/getPackageListDesigner\n/materialManage/utilsPackageManager/getUtilsPackageListDesigner\n/materialManage/templateManager/getTemplateListDesignerV2\n/materialManage/templateManager/getTemplateContentDesigner\n/materialManage/templateManager/getTemplateListAndCategoryDesigner\n/materialManage/templateManager/saveTemplateDesignerV2\nhep接口：/g/external/v/external/microservice/getList\n/g/external/v/external/interface/detail.json\n/g/external/v/external/interface/getPage\n/g/external/v/external/menu/menusAndFunctions | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | 新建页面 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 名称(title) | NaN | 名称，不支持<>&"'，长度<=100 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | ID(id) | NaN | ID，唯一，仅支持英文、数字、下划线，长度<=30 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 模板 | NaN | 模板，选项包括页面模板、流程页面原型 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | NaN |
| NaN | NaN | NaN | NaN | 复制页面 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | 删除页面 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | 新增引用 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | 删除引用 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | 设计页面 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | 大纲树 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 过滤节点 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 隐藏节点 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 锁定节点 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 重命名节点 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 删除节点 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | 数据源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 新建连接器数据源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 类型 | NaN | 自动填充，支持从hep中选择接口快速填充 | NaN | NaN | NaN | 连接器 | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 数据源ID | NaN | 数据源ID | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 默认错误提示 | NaN | 默认错误提示 | NaN | NaN | NaN | 关闭 | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 请求地址 | NaN | 请求地址 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 请求参数 | NaN | 请求参数 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 请求方法 | NaN | 请求方法，包含6个选项 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 是否支持跨域 | NaN | 是否支持跨域 | NaN | NaN | NaN | 开启 | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 超时时长（毫秒） | NaN | 超时时长 | NaN | NaN | NaN | 5000 | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 请求头信息 | NaN | 请求头信息 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 添加数据处理函数 | NaN | 添加数据处理函数，包含4个选项 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 删除连接器数据源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 编辑连接器数据源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询连接器数据源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 新建对象数据源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 类型 | NaN | 自动填充 | NaN | NaN | NaN | 对象 | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 对象 | NaN | 对象，数据来源于当前模块-对象 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 数据源ID | NaN | 数据源ID | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 默认错误提示 | NaN | 默认错误提示 | NaN | NaN | NaN | 关闭 | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 删除对象数据源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 编辑对象数据源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询对象数据源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 新建字典数据源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 类型 | NaN | 自动填充 | NaN | NaN | NaN | 对象 | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 字典 | NaN | 字典，数据来源于应用定义-字典 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 数据源ID | NaN | 数据源ID | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 默认错误提示 | NaN | 默认错误提示 | NaN | NaN | NaN | 关闭 | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 删除字典数据源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 编辑字典数据源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询字典数据源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 新建逻辑数据源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 类型 | NaN | 自动填充 | NaN | NaN | NaN | 对象 | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 逻辑 | NaN | 逻辑，数据来源于当前模块-逻辑 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 数据源ID | NaN | 数据源ID | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 默认错误提示 | NaN | 默认错误提示 | NaN | NaN | NaN | 关闭 | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 删除建逻辑数据源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 编辑建逻辑数据源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询建逻辑数据源 | NaN | NaN | 通过数据源ID查询数据源 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | 组件库（官方组件、低代码组件、本地页面） | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询组件 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 拖拽组件做页面布局 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 组件属性配置 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 组件样式配置 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 组件事件配置 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 组件高级配置 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | 源码面板 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 编写JS | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | 编写CSS | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | 操作页面 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | 自适应 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | 撤销 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | 恢复 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | 重置 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | 另存为模板 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 存储方式 | NaN | 存储方式：新建、更新 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 需更新的模板 | NaN | 存储方式：更新，数据来源于物料资产中心 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 请输入模板名称 | NaN | 请输入模板名称 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 请输入模板描述 | NaN | 请输入模板描述 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 请选择模板示意图 | NaN | 请选择模板示意图 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | NaN | 保存 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.7 | V202303.07 |
| NaN | NaN | NaN | NaN | 对象生成页面 | NaN | NaN | NaN | NaN | 选择页面原型、对象，配置页面原型属性后快速生成页面 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | 选择页面原型 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | 选择对象 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | NaN | NaN | 配置页面原型属性 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | NaN | 流程 | NaN | NaN | NaN | NaN | <process xmlns='http://jbpm.org/4.4/jpdl' name='bo\_visitor\_record审批流程' key='wf\_visitor\_record\_process'>\n <start name='start' isProcessTemplate='false' g='15,66,48,48'>\n <transition name='to 人工 1' g=':-32,-5' to='人工 1'/>\n </start>\n <end name='end' isProcessTemplate='false' g='453,66,48,48' state='approved'/>\n <human wfCompanyId='BIZ' canNotice='false' canReassign='false' canCoordinate='false' message-notice='默认' enableRemind='false' g='93,65,90,50' id='task-4056bb2d-313d-42d8-9687-98292f8133de' name='人工 1'>\n <participants>[{&quot;name&quot;:&quot;默认表达式&quot;,&quot;code&quot;:&quot;#{starter}&quot;,&quot;typecode&quot;:&quot;script&quot;,&quot;typename&quot;:&quot;表达式&quot;,&quot;type&quot;:&quot;&quot;,&quot;\_index&quot;:0,&quot;\_rowKey&quot;:1}]</participants>\n <defaultNoticeSendUser>[]</defaultNoticeSendUser>\n <coordinateParticipants subtask-must-submit='false'>[]</coordinateParticipants>\n <extaction/>\n <form>[]</form>\n <transition wfCompanyId='BIZ' name='transition 1' g=':-48,-5' to='action 1'/>\n </human>\n <action wfCompanyId='BIZ' g='213,75,30,30' id='action-200dc3c7-0253-46b5-b0bc-6c93142e2d7e' text='动作 1' name='action 1'>\n <transition name='to 人工 2' g=':-32,-5' to='人工 2'/>\n </action>\n <human wfCompanyId='BIZ' canNotice='false' canReassign='false' canCoordinate='false' message-notice='默认' enableRemind='false' g='273,65,90,50' id='task-67552cb3-3801-4445-a255-97927cfd6287' name='人工 2'>\n <participants>[{&quot;name&quot;:&quot;默认表达式&quot;,&quot;code&quot;:&quot;#{starter}&quot;,&quot;typecode&quot;:&quot;script&quot;,&quot;typename&quot;:&quot;表达式&quot;,&quot;type&quot;:&quot;&quot;,&quot;\_index&quot;:1,&quot;\_rowKey&quot;:2}]</participants>\n <defaultNoticeSendUser>[]</defaultNoticeSendUser>\n <coordinateParticipants subtask-must-submit='false'>[]</coordinateParticipants>\n <extaction/>\n <form>[]</form>\n <transition wfCompanyId='BIZ' name='transition 2' g=':-48,-5' to='action 2'/>\n </human>\n <action wfCompanyId='BIZ' g='393,75,30,30' id='action-f015d4a0-f073-4b74-9f89-79c2210cbe57' text='动作 2' name='action 2'>\n <transition name='to end' g=':-24,-5' to='end'/>\n </action>\n</process>\n | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.9 | V202401.00 |
| NaN | NaN | NaN | NaN | 新建流程 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.9 | V202401.00 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 流程名称 | NaN | 流程名称，不支持<>&"'，长度<=100 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.9 | V202401.00 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 流程编码 | NaN | 流程编码，唯一，仅支持英文、数字、下划线，长度<=30 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.9 | V202401.00 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 关联表单 | NaN | 关联表单，数据来源于当前模块-表单页面 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.9 | V202401.00 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 流程描述 | NaN | 流程描述，长度<=300 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.9 | V202401.00 |
| NaN | NaN | NaN | NaN | 复制流程 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.9 | V202401.00 |
| NaN | NaN | NaN | NaN | 删除流程 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.9 | V202401.00 |
| NaN | NaN | NaN | NaN | 新增引用 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.9 | V202401.00 |
| NaN | NaN | NaN | NaN | 删除引用 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.9 | V202401.00 |
| NaN | NaN | NaN | NaN | 基于方法创建 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 流程设计 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.9 | V202401.00 |
| NaN | NaN | NaN | NaN | NaN | 基本信息 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.9 | V202401.00 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 流程名称 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.9 | V202401.00 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 流程编码 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.9 | V202401.00 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 关联表单 | NaN | 关联表单，数据来源于当前模块-表单页面 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.9 | V202401.00 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 流程模板 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 数据同步 | NaN | 数据同步，选项包括是、否 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 描述 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.9 | V202401.00 |
| NaN | NaN | NaN | NaN | NaN | 设计流程图 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.9 | V202401.00 |
| NaN | NaN | NaN | NaN | NaN | NaN | 添加节点 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.9 | V202401.00 |
| NaN | NaN | NaN | NaN | NaN | NaN | 编排节点 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.9 | V202401.00 |
| NaN | NaN | NaN | NaN | NaN | NaN | 配置节点 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.9 | V202401.00 |
| NaN | NaN | NaN | NaN | NaN | 操作流程图 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.9 | V202401.00 |
| NaN | NaN | NaN | NaN | NaN | NaN | 保存 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.9 | V202401.00 |
| NaN | NaN | NaN | NaN | NaN | NaN | 导入 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.9 | V202401.00 |
| NaN | NaN | NaN | NaN | NaN | NaN | 清空 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.9 | V202401.00 |
| NaN | NaN | NaN | NaN | NaN | NaN | 撤销 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.9 | V202401.00 |
| NaN | NaN | NaN | NaN | NaN | NaN | 恢复 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.9 | V202401.00 |
| NaN | NaN | NaN | NaN | NaN | NaN | 删除 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.9 | V202401.00 |
| NaN | NaN | NaN | NaN | NaN | NaN | 横向布局 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.9 | V202401.00 |
| NaN | NaN | NaN | NaN | NaN | NaN | 竖向布局 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.9 | V202401.00 |
| NaN | 低代码组件开发 | NaN | NaN | NaN | NaN | NaN | NaN | {\n "version": "1.0.0",\n "componentsMap": [\n {\n "package": "hddml-components",\n "version": "2.7.1-beta.1",\n "exportName": "HddmlSelectTable",\n "main": "",\n "destructuring": true,\n "subName": "",\n "devStack": "vue2",\n "componentName": "HddmlSelectTable"\n },\n {\n "devMode": "lowCode",\n "componentName": "Component"\n }\n ],\n "componentsTree": [\n {\n "componentName": "Component",\n "id": "root",\n "props": {\n "componentName": "crm\_lc\_agencySelector",\n "title": "销售商下拉框",\n "componentConfig": {\n "isFormItem": true\n },\n "componentId": "iobd90j"\n },\n "fileName": "/",\n "dataSource": {\n "list": [\n {\n "type": "businessObject",\n "resourceId": "chmAgencyInfo",\n "isInit": false,\n "isShowDefaultTip": true,\n "id": "chmAgencyInfo"\n }\n ]\n },\n "state": {},\n "css": "",\n "lifeCycles": {\n "componentDidMount": {\n "type": "JSFunction",\n "value": "function componentDidMount() {\n console.log('did mount');\n}",\n "source": "function componentDidMount() {\n console.log('did mount');\n}"\n },\n "componentWillUnmount": {\n "type": "JSFunction",\n "value": "function componentWillUnmount() {\n console.log('will unmount');\n}",\n "source": "function componentWillUnmount() {\n console.log('will unmount');\n}"\n }\n },\n "methods": {\n "changeAgency": {\n "type": "JSFunction",\n "value": "function changeAgency(value) {\n this.$emit('input', value);\n}",\n "source": "function changeAgency(value) {\n this.$emit('input', value);\n}"\n }\n },\n "originCode": "class LowcodeComponent extends Component {\n state = {\n }\n\n componentDidMount() {\n console.log('did mount');\n }\n componentWillUnmount() {\n console.log('will unmount');\n }\n \n changeAgency(value) {\n this.$emit('input', value);\n }\n}",\n "hidden": false,\n "title": "",\n "isLocked": false,\n "condition": true,\n "conditionGroup": "",\n "propTypes": [\n {\n "name": "multiple",\n "setValue": {\n "type": "JSFunction",\n "value": "function setValue(target, value) {\r\n return value;\r\n}\r\n"\n },\n "defaultValue": false,\n "title": "是否多选",\n "setter": "BoolSetter",\n "propType": "boolean"\n },\n {\n "name": "pageSize",\n "setValue": {\n "type": "JSFunction",\n "value": "function setValue(target, value) {\r\n return value;\r\n}\r\n"\n },\n "defaultValue": "",\n "title": "每页条数",\n "setter": "NumberSetter",\n "propType": "number"\n },\n {\n "name": "limit",\n "setValue": {\n "type": "JSFunction",\n "value": "function setValue(target, value) {\r\n return value;\r\n}\r\n"\n },\n "defaultValue": "",\n "title": "多选个数限制",\n "setter": "NumberSetter",\n "propType": "number"\n },\n {\n "name": "filterable",\n "setValue": {\n "type": "JSFunction",\n "value": "function setValue(target, value) {\r\n return value;\r\n}\r\n"\n },\n "defaultValue": false,\n "title": "是否支持模糊查询",\n "setter": "BoolSetter",\n "propType": "boolean"\n },\n {\n "name": "isCheckall",\n "setValue": {\n "type": "JSFunction",\n "value": "function setValue(target, value) {\r\n return value;\r\n}\r\n"\n },\n "defaultValue": false,\n "title": "显示全选、反选按钮",\n "setter": "BoolSetter",\n "propType": "boolean"\n },\n {\n "name": "v-model",\n "setValue": {\n "type": "JSFunction",\n "value": ""\n },\n "setter": "StringSetter",\n "propType": "string",\n "defaultValue": "",\n "title": "绑定值"\n },\n {\n "name": "displayValue",\n "setValue": {\n "type": "JSFunction",\n "value": "function setValue(target, value) {\r\n return value;\r\n}\r\n"\n },\n "title": "显示内容",\n "setter": "JsonSetter",\n "propType": "object",\n "defaultValue": {}\n },\n {\n "name": "model",\n "setValue": {\n "type": "JSFunction",\n "value": "function setValue(target, value) {\r\n return value;\r\n}\r\n"\n },\n "title": "显示模式",\n "setter": "StringSetter",\n "propType": "string",\n "defaultValue": "normal"\n }\n ],\n "children": [\n {\n "componentName": "HddmlSelectTable",\n "id": "node\_oclw5pe81e1",\n "props": {\n "dataSource": [\n {\n "id": "1",\n "name": "胡彦斌",\n "age": 32,\n "address": "西湖区湖底公园1号"\n },\n {\n "id": "2",\n "name": "王一博",\n "age": 28,\n "address": "滨江区网商路699号"\n }\n ],\n "columns": [\n {\n "title": "销售商编号",\n "dataIndex": "name",\n "key": "agency\_no",\n "align": "left"\n },\n {\n "title": "销售商名称",\n "dataIndex": "age",\n "key": "agency\_name",\n "align": "left"\n }\n ],\n "pagination": {\n "pageSize": {\n "type": "JSExpression",\n "value": "this.$props.pageSize"\n },\n "total": 15,\n "current": 1,\n "showTotal": true,\n "fastArrival": false\n },\n "\_\_isVModel": true,\n "loading": false,\n "autoPlacement": true,\n "format": [\n "agency\_name",\n "\_"\n ],\n "formatValue": "agency\_no",\n "disabled": false,\n "multiple": {\n "type": "JSExpression",\n "value": "this.$props.multiple"\n },\n "rowSelect": true,\n "limit": {\n "type": "JSExpression",\n "value": "this.$props.limit"\n },\n "isCheckall": {\n "type": "JSExpression",\n "value": "this.$props.isCheckall"\n },\n "filterable": {\n "type": "JSExpression",\n "value": "this.$props.filterable"\n },\n "remote": true,\n "showHeader": true,\n "showTitle": false,\n "transfer": false,\n "placeholder": "请选择",\n "dataSourceType": "BO\_INVOKE\_V2",\n "queryHandler": {\n "type": "JSFunction",\n "value": "function(){ return this.dataSourceCustomMap['chmAgencyInfo'].query.apply(this,[{\n \"bo\": \"chmAgencyInfo\",\n \"bc\": \"chmAgencyInfo\",\n \"mainBc\": \"chmAgencyInfo\"\n}].concat(Array.prototype.slice.call(arguments)))}"\n },\n "\_\_events": {\n "eventDataList": [\n {\n "type": "componentEvent",\n "name": "onChange",\n "relatedEventName": "changeAgency"\n }\n ],\n "eventList": [\n {\n "name": "onBlur",\n "template": "onBlur(){\n// 失去焦点时触发\nconsole.log('onBlur');}",\n "disabled": false\n },\n {\n "name": "onChange",\n "template": "onChange(value){\n// 选项发生变化时触发, 返回当前选项\nconsole.log('onChange', value);}",\n "disabled": true\n },\n {\n "name": "onSelectSelected",\n "template": "\n onSelectSelected(selection, selected){\n // 点击选项时触发, 返回当前选项对应的整行数据(selection)以及选中/取消选中状态(selected)。\n // 多选模式下, 点击面板中的全选/全不选不会生效\n console.log('onSelectSelected', selection, selected);\n }\n",\n "disabled": false\n },\n {\n "name": "onFocus",\n "template": "onFocus(){\n// 获取焦点时触发\nconsole.log('onFocus');}",\n "disabled": false\n },\n {\n "name": "onScroll",\n "template": "onScroll(value){\n// 滚动下拉框中滚动条触发, 返回滚动条到下拉框底部的距离\nconsole.log('onScroll', value);}",\n "disabled": false\n },\n {\n "name": "onPageChange",\n "template": "onPageChange(pageNum){\n// 页码改变的回调，返回改变后的页码\nconsole.log('onPageChange', pageNum);}",\n "disabled": false\n },\n {\n "name": "onPageSizeChange",\n "template": "onPageSizeChange(pageSize){\n// 切换每页条数时的回调，返回切换后的每页条数\nconsole.log('onPageSizeChange', pageSize);}",\n "disabled": false\n }\n ]\n },\n "onChange": {\n "type": "JSFunction",\n "value": "function(){return this.changeAgency.apply(this,Array.prototype.slice.call(arguments).concat([])) }"\n },\n "targetNode": "",\n "v-model": {\n "type": "JSExpression",\n "value": "this.$props.value"\n },\n "\_unsafe\_MixedSetter\_v-model\_select": "ExpressionSetter",\n "dropWidth": 300,\n "displayValue": {\n "type": "JSExpression",\n "value": "this.$props.displayValue"\n },\n "mode": {\n "type": "JSExpression",\n "value": "this.$props.model"\n },\n "ref": "hddmlselecttable-d6aa86d2"\n },\n "hidden": false,\n "title": "",\n "isLocked": false,\n "condition": true,\n "conditionGroup": "",\n "supportPermission": {\n "enable": false,\n "resourceTitle": "下拉表格"\n },\n "permissions": []\n }\n ]\n }\n ],\n "i18n": {},\n "meta": {}\n} | NaN | NaN | 物料接口：/materialManage/designerPluginManager/getDesignerPluginPageDesigner\n/materialManage/lowcodePackageManager/getPackageListDesigner\n/materialManage/packageManager/getPackageListDesigner\n/materialManage/utilsPackageManager/getUtilsPackageListDesigner\n/materialManage/templateManager/getTemplateListDesignerV2\n/materialManage/templateManager/getTemplateContentDesigner\n/materialManage/templateManager/getTemplateListAndCategoryDesigner\n\nhep接口：/g/external/v/external/microservice/getList\n/g/external/v/external/interface/detail.json\n/g/external/v/external/interface/getPage\n/g/external/v/external/menu/menusAndFunctions | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | 低代码组件包配置 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | ID(name) | NaN | 低代码组件包ID，不支持<>&"'，长度<=100 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 名称(title) | NaN | 低代码组件包名称，仅支持英文、数字、中划线，长度<=30 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 版本(version) | NaN | 低代码组件包版本，首位不能输入'.'，并仅包含数字和'.'，长度<=30 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 描述(description) | NaN | 低代码组件包描述，长度<=300 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | 低代码组件开发 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | 低代码组件 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | 新建低代码组件 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 名称(title) | NaN | 名称，不支持<>&"'，长度<=100 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | ID(id) | NaN | ID，唯一，仅支持英文、数字、下划线，长度<=30 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | 删除低代码组件 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | 设计低代码组件 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | 大纲树 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 过滤节点 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 隐藏节点 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 锁定节点 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 重命名节点 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 删除节点 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | 数据源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 新建连接器数据源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 删除连接器数据源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 编辑连接器数据源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询连接器数据源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 新建对象数据源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 删除对象数据源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 编辑对象数据源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询对象数据源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 新建字典数据源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 删除字典数据源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 编辑字典数据源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询字典数据源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 新建逻辑数据源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 删除建逻辑数据源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 编辑建逻辑数据源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询建逻辑数据源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | 组件库（官方组件） | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询组件 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 拖拽组件做页面布局 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 组件属性配置 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 组件样式配置 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 组件事件配置 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 组件高级配置 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | 低代码组件属性配置 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 组件名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 组件标题 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 是否是容器组件 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 是否是表单组件 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 属性定义 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | 源码面板 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 编写JS | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 编写CSS | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | 操作低代码组件 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | 自适应 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | 撤销 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | 恢复 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | 保存 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | 低代码组件测试 | NaN | NaN | NaN | NaN | NaN | {\n "version": "1.7",\n "componentsMap": [\n {\n "package": "crm-lc-components",\n "devMode": "lowCode",\n "componentName": "crm\_lc\_agencySelector"\n },\n {\n "devMode": "lowCode",\n "componentName": "Page"\n }\n ],\n "componentsTree": [\n {\n "componentName": "Page",\n "id": "root",\n "props": {},\n "fileName": "/",\n "dataSource": {\n "list": []\n },\n "state": {},\n "css": "",\n "lifeCycles": {\n "componentDidMount": {\n "type": "JSFunction",\n "value": "function componentDidMount() {\n console.log('did mount');\n}",\n "source": "function componentDidMount() {\n console.log('did mount');\n}"\n },\n "componentWillUnmount": {\n "type": "JSFunction",\n "value": "function componentWillUnmount() {\n console.log('will unmount');\n}",\n "source": "function componentWillUnmount() {\n console.log('will unmount');\n}"\n }\n },\n "methods": {\n "onChange": {\n "type": "JSFunction",\n "value": "function onChange(value) {}",\n "source": "function onChange(value) {}"\n }\n },\n "originCode": "class LowcodeComponent extends Component {\n state = {}\n componentDidMount() {\n console.log('did mount');\n }\n componentWillUnmount() {\n console.log('will unmount');\n }\n \n\n\tonChange(value){\n\t}\n}",\n "hidden": false,\n "title": "",\n "isLocked": false,\n "condition": true,\n "conditionGroup": "",\n "children": [\n {\n "componentName": "crm\_lc\_agencySelector",\n "id": "node\_oclw5pwl3k1",\n "props": {\n "multiple": true,\n "pageSize": 5,\n "limit": 10,\n "filterable": true,\n "isCheckall": true,\n "ref": "crm\_lc\_agencyselector-015578f4",\n "onChange": {\n "type": "JSFunction",\n "value": "function(){ return this.onChange.apply(this,Array.prototype.slice.call(arguments).concat([])) }"\n }\n },\n "hidden": false,\n "title": "",\n "isLocked": false,\n "condition": true,\n "conditionGroup": "",\n "loopArgs": [\n "",\n ""\n ]\n }\n ]\n }\n ],\n "i18n": {},\n "meta": {}\n} | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | 测试页面 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | 新建测试页面 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 名称(title) | NaN | 名称，不支持<>&"'，长度<=100 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | ID(id) | NaN | ID，唯一，仅支持英文、数字、下划线，长度<=30 | NaN | NaN | NaN | NaN | Y | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | 删除测试页面 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | 设计测试页面 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | 大纲树 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 过滤节点 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 隐藏节点 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 锁定节点 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 重命名节点 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 删除节点 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | 数据源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 新建连接器数据源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 删除连接器数据源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 编辑连接器数据源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询连接器数据源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 新建对象数据源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 删除对象数据源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 编辑对象数据源 | NaN | NaN | 通过数据源ID查询数据源 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询对象数据源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 新建字典数据源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 删除字典数据源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 编辑字典数据源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询字典数据源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 新建逻辑数据源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 删除建逻辑数据源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 编辑建逻辑数据源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询建逻辑数据源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | 组件库（官方组件、低代码组件） | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询组件 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 拖拽组件做页面布局 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 组件属性配置 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 组件样式配置 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 组件事件配置 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 组件高级配置 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | 源码面板 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 编写JS | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | NaN | 编写CSS | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | 操作测试页面 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | 自适应 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | 撤销 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | 恢复 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | 保存 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | NaN | NaN | NaN | NaN | 预览 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.10 | V202401.01 |
| NaN | 预览调试 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | NaN | NaN |
| NaN | NaN | 应用部署 | NaN | NaN | NaN | NaN | NaN | NaN | 配置运行环境后，才能选择运行环境进行部署 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.8 | V202303.08 |
| NaN | NaN | 出码预览 | NaN | NaN | NaN | NaN | NaN | NaN | 是否出码模式：是，才会显示 | NaN | NaN | NaN | NaN | NaN | NaN | Y | NaN | NaN | V1.9 | V202401.00 |

## 打包调试域
| 业务领域(一级) | 价值流（二级） | 活动（三级） | 子活动（四级） | 任务（四级） | 关键字段（五级） | 描述 | 接口 | 实体 | DFX | 必填 | 备注(是否多选，前置依赖，限制要求 等) | 语言版本 | 发布版本 | 低码开发人员 | 资产管理运营人员 | 专业开发人员 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 业务运行引擎（控制台） | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | 1.9 | V202401.00 | NaN | NaN | NaN |
| NaN | 应用调试部署 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | 1.9 | V202401.00 | NaN | NaN | NaN |
| NaN | NaN | 引擎地址管理 | NaN | NaN | NaN | NaN | /manager-app/hcreator/manager/configurer/configure | IpConfiguration | NaN | NaN | NaN | 1.9 | V202401.00 | NaN | NaN | NaN |
| NaN | NaN | NaN | 引擎地址配置 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | 1.9 | V202401.00 | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 操作员中心IP地址&端口号 | NaN | 形如：http://10.20.182.186:8088 | NaN | NaN | NaN | NaN | NaN | 1.9 | V202401.00 | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 工作流引擎IP地址&端口号 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | 1.9 | V202401.00 | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 业务模型引擎IP地址&端口号 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | 1.9 | V202401.00 | NaN | NaN | NaN |
| NaN | NaN | 应用交付包管理 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | 1.9 | V202401.00 | NaN | NaN | NaN |
| NaN | NaN | NaN | 应用交付包查询 | NaN | NaN | NaN | /manager-app/hcreator/manager/deployer/list | DeployPackage | NaN | NaN | NaN | 1.9 | V202401.00 | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | 应用交付包名称 | 自动获取应用ID | NaN | NaN | NaN | NaN | NaN | 1.9 | V202401.00 | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | 部署状态 | 部署成功/部署成功 | NaN | NaN | NaN | NaN | NaN | 1.9 | V202401.00 | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | 最近部署时间 | 对应用交付包执行部署的最近时间 | NaN | NaN | NaN | NaN | NaN | 1.9 | V202401.00 | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | 上传时间 | 上传应用交付包的时间 | NaN | NaN | NaN | NaN | NaN | 1.9 | V202401.00 | NaN | NaN | NaN |
| NaN | NaN | NaN | 全量包新增 | NaN | NaN | NaN | /manager-app/hcreator/manager/deployer/package/upload | DeployPackage | NaN | NaN | NaN | 1.9 | V202401.00 | NaN | NaN | NaN |
| NaN | NaN | NaN | 增量包新增 | NaN | NaN | NaN | /manager-app/hcreator/manager/deployer/package/upload | NaN | NaN | NaN | NaN | 1.9 | V202401.00 | NaN | NaN | NaN |
| NaN | NaN | NaN | 交付包管理 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | 1.9 | V202401.00 | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 参数配置 | NaN | 环境参数配置，从工程应用中获取全量环境参数 | /manager-app/hcreator/manager/deployer/configProperties | ConfigProperties | NaN | NaN | NaN | 1.9 | V202401.00 | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | 参数名 | 环境中需要用到的参数，不可修改 | NaN | NaN | NaN | NaN | NaN | 1.9 | V202401.00 | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | 描述 | 标识环境参数的用途 | NaN | NaN | NaN | NaN | NaN | 1.9 | V202401.00 | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | 参数值 | 当前环境参数的value值 | NaN | NaN | NaN | NaN | NaN | 1.9 | V202401.00 | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 部署 | NaN | 将交付包部署到当前环境对应的服务器中（由manager将应用交付包资源分发到对应引擎中） | /manager-app/hcreator/manager/deployer/package/deploy | DeployPackage | NaN | NaN | NaN | 1.9 | V202401.00 | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 下载 | NaN | 下载当前交付包 | /manager-app/hcreator/manager/deployer/download | DeployPackage | NaN | NaN | NaN | 1.9 | V202401.00 | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 删除 | NaN | NaN | /manager-app/hcreator/manager/deployer/delete | DeployPackage | NaN | NaN | NaN | 1.9 | V202401.00 | NaN | NaN | NaN |
| NaN | NaN | 日志监控 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | 1.1 | V202401.01 | NaN | NaN | NaN |
| NaN | NaN | NaN | 接口监控指标 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | 1.1 | V202401.01 | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 业务模型引擎接口监控 | NaN | 响应时间、请求频率、错误率 | NaN | NaN | NaN | NaN | NaN | 1.1 | V202401.01 | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 操作员中心接口监控 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | 1.1 | V202401.01 | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 工作流引擎接口监控 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | 1.1 | V202401.01 | NaN | NaN | NaN |
| NaN | NaN | NaN | 业务日志 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | 1.1 | V202401.01 | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 业务模型引擎业务日志 | NaN | 日志级别：INFO、ERROR、WARN、DEBUG；\n日志保存日期：十天\n日志格式：时间戳、日志级别、线程、接口、调用耗时、是否成功、错误码、出入参\n具体参考：实现方案 | NaN | NaN | NaN | NaN | NaN | 1.1 | V202401.01 | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 操作员中心业务日志 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | 1.1 | V202401.01 | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 工作流引擎业务日志 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | 1.1 | V202401.01 | NaN | NaN | NaN |
| NaN | 打包工具 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 导出sql脚本 | NaN | NaN | NaN | SQL导出配置后，才能全量导出sql脚本，包括mysql和oracle | NaN | NaN | NaN | NaN | NaN | 1.9 | V202401.00 | NaN | NaN | NaN |
| NaN | NaN | 导出全量交付包 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | 1.9 | V202401.00 | NaN | NaN | NaN |
| NaN | NaN | 导出增量交付包 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | 1.9 | V202303.08 | NaN | NaN | NaN |
| NaN | NaN | 出码 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | 1.9 | V202303.08 | NaN | NaN | NaN |
| NaN | 引擎部署 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 轻量化部署 | NaN | NaN | NaN | 适用于开发者本地或单机场景的引擎制品部署方案。低码提供用户手册。\nhttps://iknow.hs.net/portal/docView/home/114684 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 微服务部署 | NaN | NaN | NaN | 适用于恒生JRES体系的微服务场景引擎制品部署方案。低码提供用户手册。\nhttps://iknow.hs.net/portal/docView/home/114685 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 业务系统集成部署 | NaN | NaN | NaN | 低码开发部分业务模块，低码应用运行引擎不允许独立部署、需要跟业务产品运行框架集成部署时，低码提供定制化的集成部署解决方案。\nhttps://iknow.hs.net/portal/docView/home/114686 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | 用户权限系统（操作员中心） | NaN | NaN | NaN | NaN | 实现版本：OMC2.0-SEE.V202304.05.003 | NaN | NaN | NaN | NaN | NaN | 1.9 | V202401.00 | NaN | NaN | NaN |
| NaN | NaN | 用户设置 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 用户新增 | NaN | NaN | 对用户进行新增 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 用户管理 | NaN | NaN | 用户的删、改、查 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 用户角色分配 | NaN | NaN | 用户&角色进行绑定 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 离职交接 | NaN | NaN | 员工办理离职，将离职员工数据进行更新 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 角色设置 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 角色新增 | NaN | NaN | 对角色进行新增 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 角色管理 | NaN | NaN | 角色的删、改、查 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 组织机构设置 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 组织新增 | NaN | NaN | 对组织部门的新增 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 组织管理 | NaN | NaN | 组织部门的删、改、查 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 组织添加员工 | NaN | NaN | 建立组织和员工的绑定关系 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 菜单管理 | NaN | NaN | NaN | 对系统的菜单进行管理 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 菜单新增 | NaN | NaN | 对菜单的新增 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 菜单管理 | NaN | NaN | 菜单的删、改、查 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 修改菜单排序 | NaN | NaN | 调整菜单的排序（调整父子级） | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 导出SQL | NaN | NaN | 导出菜单对应的SQL数据 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 功能权限设置 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 资源权限管理 | NaN | NaN | 资源可以是一个完整的页面(菜单)，也可以是页面中的某个区域块,资源主要是用来管理页面里的功能等 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 操作功能管理 | NaN | NaN | 页面中的功能：如新增、修改、删除及可调用的API | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | 工作流系统 | NaN | NaN | NaN | NaN | 实现版本：WF1.2-wf12.V202304.05.001 | NaN | NaN | NaN | NaN | NaN | 1.9 | V202401.00 | NaN | NaN | NaN |
| NaN | NaN | 流程管理 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 新建流程 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 创建人工审批流程 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 创建模版流程 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 创建自动化流程 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 流程管理 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 流程管理 | NaN | 对流程进行删、改、查 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 流程发布 | NaN | 将流程进行发布 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 资源管理 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 表达式管理 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 表单管理 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 服务管理 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 分类管理 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 监听配置管理 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 监控管理 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 流程实例监控 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 任务监控 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 委托关系监控 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 外部服务异常监控 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 委托任务监控 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 缓存管理 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 配置项管理 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 通用数据监控 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 流程监控 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 催办监控 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 审计日志管理 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 查询用户参与过的节点 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 统计分析 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 每日处理实例数及趋势 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 实例周期耗时及趋势 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 流程处理情况 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 流程节点平均耗时统计 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 本日流程处理情况 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 任务处理 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 发起工作流 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 待办事项 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 已办流程 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 我发起的工作流 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 待阅事项 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 已阅事项 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 已阅流程 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 已阅任务 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 我分阅的任务 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 委托管理 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 我委托的任务 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 我分阅的流程 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 我的转办 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 代理任务 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |

## 资产管理域（1）
| 业务领域(一级) | 价值流（二级）（主菜单） | 活动（三级）二级菜单 | 任务（四级）主内容区 | 子任务（五级） | 步骤（六级） | 关键字段（七级） | 描述 | 接口 | 实体 | DFX | 必填 | 备注(是否多选，前置依赖，限制要求 等) | 低码开发人员 | 资产管理运营人员 | 专业开发人员 | 语言版本 | 发布版本 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 管理能力（物料资产中心） | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | 物料资产管理 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.08.000 |
| NaN | NaN | 物料资产看板 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.08.000 |
| NaN | NaN | NaN | 数据总览 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.08.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 接入产品总数 | 资产中心接入的产品总数 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.08.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 物料资产总数 | 资产中心接入的物料资产总数 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.08.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 组件包总数 | 资产中心接入的组件包总数 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.08.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 组件总数 | 资产中心接入的组件总数 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.08.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 模板总数 | 资产中心接入的模板总数 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.08.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 设计器插件总数 | 资产中心接入的设计器插件 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.08.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 后端插件 | 资产中心接入的后端插件 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.08.000 |
| NaN | NaN | NaN | 物料积累活跃图TOP3 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.08.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 支持呈现TOP3的物料积累趋势图 | 物料TOP3的物料积累趋势图 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.08.000 |
| NaN | NaN | NaN | 产品级资产总览 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.08.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 物料资产总数 | 当前产品下的物料资产总数 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.08.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 组件包总数 | 当前产品下的组件包总数 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.08.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 组件总数 | 当前产品下的组件总数 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.08.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 模板总数 | 当前产品下的模板总数 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.08.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 设计器插件总数 | 当前产品下的设计器插件总数 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.08.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 引擎插件 | 当前产品下的引擎插件 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.08.000 |
| NaN | NaN | 组件包管理 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | 查询组件包列表 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询-组件包名称 | 支持模糊查询组件包名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询-组件包版本 | 支持模糊查询组件包版本 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询-组件包编码 | 支持模糊查询组件包编码 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | 组件包列表 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 组件包编码 | 组件包编码 | NaN | NaN | NaN | 是 | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 组件包名称 | 组件包名称 | NaN | NaN | NaN | 是 | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 版本 | 组件包版本 | NaN | NaN | NaN | 否 | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 说明 | 组件包说明 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 所属产品 | 所属产品 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 上传方式 | 支持NPM上次 或者 手动上传 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 创建时间 | 创建时间 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 创建人 | 创建人 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | 查看组件包详情 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | 组件包详情 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 组件包图标 | 组件包图标 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 组件包名称 | 组件包名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 组件包版本 | 组件包版本 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 创建人 | 创建人 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 创建时间 | 创建时间 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 说明 | 组件包说明 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | 查询组件列表 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 组件图标 | 组件图标 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 组件ID | 组件ID | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 组件名称 | 组件名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | 查看组件详情 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | 组件说明 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 组件图片 | 组件图片 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 组件ID | 组件ID | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 组件说明 | 组件说明 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | 使用说明 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 使用说明 | 组件使用说明 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | 元数据说明 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | Json文件 | Json文件 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | 查询依赖组件包 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 组件包图标 | 组件包图标 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 组件包ID | 组件包ID | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 组件包名称 | 组件包名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 组件包版本 | 组件包版本 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 所属产品 | 所属产品 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | 设置组件包为默认 | NaN | NaN | NaN | 将组件包设为默认后，设计器侧在没有配置组件包的情况下，默认调默认组件包 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | 设置组件包为公开 | NaN | NaN | NaN | 将组件包设置为公开后，其它产品也可以进行访问 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | 上传组件包 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 手工上传 | 支持用户按照物料资产中心规格手动上传组件包 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | NPM包导入 | 支持NPM包导入组件包 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | 删除组件包版本 | NaN | NaN | NaN | 允许用户删除自身创建的组件包 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | 模板管理 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | 查询模板列表 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询-模板名称 | 支持模糊查询模板名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 类型 | 支持下拉选择模板类型（页面模板、代码模板） | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | 模板列表 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 模板名称 | 模板名称 | NaN | NaN | NaN | NaN | 是 | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 类型 | 类型 | NaN | NaN | NaN | NaN | 是 | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 图示 | 图示 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 所属产品 | 所属产品 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 上传方式 | 上传方式 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 创建时间 | 创建时间 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 创建人 | 创建人 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | 编辑模板 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | 编辑模板信息 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 模板名称 | 支持模板名称修改 | NaN | NaN | NaN | NaN | 是 | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 模板说明 | 模板说明 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | 上传模板图片 | NaN | NaN | NaN | 支持上传图片 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | 删除 | NaN | NaN | NaN | 资产管理员可以删除本产品下的模板 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | 设置模板为默认 | NaN | NaN | NaN | 将组件包设为默认后，设计器侧在没有配置组件包的情况下，默认调默认组件包 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | 设置模板为公开 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | 引擎包管理 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | 查询引擎包列表 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询-引擎包列表 | 支持模糊查询板本 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | 引擎包列表 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 引擎包名称 | 组件包版本 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 版本 | 组件包说明 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 备注 | 所属产品 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 所属产品 | 组件包上传方式 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 上传方式 | 创建时间 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 创建时间 | 创建人 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 创建人 | 创建人能够进行删除 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | 设置引擎包为默认 | NaN | NaN | NaN | 设计器如果没有绑定组件包的话，默认选择默认组件包 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | 上传引擎包 | NaN | NaN | NaN | 支持用户在物料资产中心上传组件包 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 选择引擎包进行上传 | 支持用户按照物料资产中心规格上传引擎包 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 选择HSDDML版本 | 选择HSDDML版本 | NaN | NaN | NaN | 是 | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 引擎包名称 | 引擎包名称 | NaN | NaN | NaN | 是 | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 版本 | 版本 | NaN | NaN | NaN | 是 | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 备注 | 备注 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | 删除引擎包版本 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | 支持引擎包上传人员删除引擎包版本 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | 工具函数包管理 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | 查询工具函数包列表 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询-工具函数包名称 | 支持模糊查询组件包名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询-工具函数包版本 | 支持模糊查询组件包版本 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询-工具函数包编码 | 支持模糊查询组件包编码 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | 工具函数包列表 | NaN | NaN | NaN | 上传方式 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 工具函数包编码 | 工具函数包编码 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 工具函数包名称 | 工具函数包名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 版本 | 版本 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 说明 | 说明 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 所属产品 | 所属产品 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 创建时间 | 创建时间 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 创建人 | 创建人 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 创建人 | 创建人能够进行删除 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | 查看工具函数包详情 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | 工具函数包详情 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 工具函数包图标 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 工具函数包名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 工具函数包版本 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 创建人 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 创建时间 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 说明 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | 查询工具函数包 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 工具函数包图标 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 工具函数包ID | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 工具函数包名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | 查看工具函数包详情 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | 工具函数包说明 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 工具函数包图片 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 工具函数包ID | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 工具函数包说明 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | 使用说明 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 使用说明 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | 元数据说明 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | Json文件 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | 查询依赖工具函数包 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 工具函数包图标 | 工具函数包图标 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 工具函数包ID | 工具函数包ID | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 工具函数包名称 | 工具函数包名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 工具函数包版本 | 工具函数包版本 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 所属产品 | 所属产品 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | 设置工具函数包为默认 | NaN | NaN | NaN | 设计器如果没有绑定工具函数包图标的话，默认选择默认组件包 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | 上传工具函数包 | NaN | NaN | NaN | 支持用户在物料资产中心上传组件包 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 手工上传 | 支持用户按照物料资产中心规格上传组件包 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | NPM包导入 | 支持NPM包导入组件包 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | 删除工具函数包版本 | NaN | NaN | NaN | 允许用户删除自身创建的工具函数包 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | 低代码组件包管理 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | 查询低代码组件包列表 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询-低代码组件包名称 | 支持模糊查询低代码组件包名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询-低代码组件包版本 | 支持模糊查询低代码组件包版本 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询-低代码组件包编码 | 支持模糊查询低代码组件包编码 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | 低代码组件包列表 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 低代码组件包编码 | 低代码组件包编码 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 低代码组件包名称 | 低代码组件包名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 版本 | 版本 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 说明 | 说明 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 所属产品 | 所属产品 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 上传方式 | 上传方式 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 创建时间 | 创建时间 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 创建人 | 创建人 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | 查看低代码组件包详情 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | 低代码组件包详情 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 低代码组件包图标 | 低代码组件包图标 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 低代码组件包名称 | 低代码组件包名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 低代码组件包版本 | 低代码组件包版本 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 创建人 | 创建人 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 创建时间 | 创建时间 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 说明 | 说明 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | 查询低代码组件列表 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 低代码组件图标 | 低代码组件图标 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 低代码组件ID | 低代码组件ID | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 低代码组件名称 | 低代码组件名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | 查看低代码组件详情 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | json文件 | json文件 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | 查询依赖组件包 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 组件包图标 | 组件包图标 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 组件包ID | 组件包ID | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 组件包名称 | 组件包名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 组件包版本 | 组件包版本 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 所属产品 | 所属产品 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | 查询依赖工具函数包 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 工具函数包图标 | 工具函数包图标 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 工具函数包ID | 工具函数包ID | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 工具函数包名称 | 工具函数包名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | 查询依赖低代码组件包 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 低代码组件包图标 | 低代码组件包图标 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 低代码组件包ID | 低代码组件包ID | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 低代码组件包名称 | 低代码组件包名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | 设置低代码组件包为默认 | NaN | NaN | NaN | 设计器如果没有绑定组件包的话，默认选择默认组件包 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | 上传低代码组件包 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 上传低代码组件包 | 支持用户按照物料资产中心规格上传组件包 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | NaN | 删除低代码组件包版本 | NaN | NaN | NaN | 允许用户删除自身创建的低代码组件包 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.06.000 |
| NaN | NaN | BS逻辑库管理 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | 查询BS逻辑库列表 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询-BS逻辑库名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询-BS逻辑库版本 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询-BS逻辑库编码 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | BS逻辑库列表 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | BS逻辑库编码 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | BS逻辑库名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 版本 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 说明 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 所属产品 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 创建时间 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 创建人 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | 查看BS逻辑库详情 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | BS逻辑库详情 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | BS逻辑库图标 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | BS逻辑库名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | BS逻辑库版本 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 创建人 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 创建时间 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 说明 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | BS逻辑库json文件 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | json文件 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | 设置BS逻辑库为默认 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | 上传BS逻辑库 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 手工上传BS逻辑库 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | NPM包导入 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | 删除BS逻辑库 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | 引擎插件管理 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | 查询引擎插件 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询-引擎插件名称 | 查询-引擎插件名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询-引擎插件版本 | 查询-引擎插件版本 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询-引擎插件编码 | 查询-引擎插件编码 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | 引擎插件列表 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 引擎插件编码 | 引擎插件编码 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 引擎插件名称 | 引擎插件名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 版本 | 版本 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 说明 | 说明 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 所属产品 | 所属产品 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 上传方式 | 上传方式 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 创建时间 | 创建时间 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 创建人 | 创建人 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | 查看引擎插件详情 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | 引擎插件详情 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 引擎插件图标 | 引擎插件图标 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 引擎插件名称 | 引擎插件名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 引擎插件版本 | 引擎插件版本 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 创建人 | 创建人 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 创建时间 | 创建时间 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 说明 | 说明 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | 引擎插件描述文件 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | json文件 | json文件 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | 设置引擎插件为默认 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | 上传引擎插件 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 手工上传 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | 删除引擎插件 | NaN | NaN | 删除引擎插件 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | 设计器插件管理 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | 查询设计器插件 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询-设计器插件名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询-设计器插件版本 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询-设计器插件编码 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | 设计器插件列表 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 设计器插件编码 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 设计器插件名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 版本 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 说明 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 所属产品 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 上传方式 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 创建时间 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 创建人 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | 查看设计器插件详情 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | 设计器插件详情 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 设计器插件图标 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 设计器插件名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 设计器插件版本 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 创建人 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 创建时间 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 说明 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | 设计器插件描述文件 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | json文件 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | 设置设计器插件为默认 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | 上传设计器插件 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | 上传设计器插件 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 手工上传 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | 查询设计器插件定义列表 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 根据关键字模糊搜索设计器插件中字段 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | 设置设计器插件定义的公开状态 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | 删除设计器插件版本 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | 查询设计器插件版本列表 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 根据设计器插件名称查询「引擎插件版本信息」中字段 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 根据版本查询「设计器插件信息」中字段 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | 将某版本设计器插件设置为默认版本 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | 查看某版本设计器插件的详情信息 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 设计器插件版本详情 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.00.000 |
| NaN | 权限管理 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | 用户管理 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | 查询用户 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | 查询-用户名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | 查询-用户账号 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | 查询-角色 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | 用户信息列表 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | 用户名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | 用户账号 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | 角色 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | 创建时间 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | 用户角色分配 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | 角色分配 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | 角色名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | 角色说明 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | 删除用户 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | 新增用户 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | 选择用户 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | 用户名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | 域账号 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | 角色管理 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | 查询角色 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | 查询-角色名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | 查询-用户编码 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | 角色信息列表 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | 角色名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | 角色编码 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | 说明 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | 角色类型 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | 创建时间 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | 创建人 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | 功能权限分配 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | 角色分配 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | 菜单名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | 功能编辑权限 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | 编辑角色 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | 角色名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | 角色编码 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | 说明 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | 新增角色 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | 角色名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | 角色编码 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | 说明 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | 删除角色 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 根据角色名称查询「角色」中字段 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 根据角色编码查询「角色」中字段 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | 功能权限分配 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 从菜单功能权限列表中勾选 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | 配置管理 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | 制品库管理 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | NPM仓库名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | Maven仓库名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | 系统设置 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | 产品管理 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202301.03.000 |
| NaN | NaN | NaN | 查询产品 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询-产品编号名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询-产品名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询-产品负责人 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | 产品列表 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 产品编码 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 产品名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 产品来源 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 产品简称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 产品负责人 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 创建人 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 创建时间 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | 新增产品 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | 从渠道新增 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 产品渠道 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 产品名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 产品简称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 产品编号 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 产品负责人 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | 自定义 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 产品名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 产品简称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 产品编号 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 产品负责人 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | 编辑产品 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 产品名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 产品简称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 产品编号 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 产品负责人 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | 字典管理 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | 查询字典 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询-字典值 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | 字典列表 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 字典类型 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 字典值 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 字典说明 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | 新增字典 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | 新增字典 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 字典类型 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 字典值 | NaN | NaN | 必填 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 说明 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | 删除字典 | NaN | NaN | 删除字典 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | 配置项管理 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | 查询配置管理 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询-配置项 | 支持模糊查询-配置项 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询-配置名称 | 支持模糊查询-配置名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | 配置管理列表 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 配置项 | 配置项 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 配置名称 | 配置名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 配置值 | 配置值 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 说明 | 说明 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | 编辑配置项 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 配置项 | 配置项 | NaN | 必填 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 配置名称 | 配置名称 | NaN | 必填 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 配置值 | 配置值 | NaN | 必填 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 说明 | 说明 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.00.000 |
| NaN | NaN | 物料接口管理 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.08.000 |
| NaN | NaN | NaN | 查询物料接口监控 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.08.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询接口URL | 查询接口URL | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.08.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询-使用产品 | 查询-使用产品 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.08.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 查询-调用时间区间 | 查询-调用时间区间 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.08.000 |
| NaN | NaN | NaN | 配置物料接口管理列表 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.08.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 接口URL | 接口URL | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.08.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 使用产品 | 使用产品 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.08.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 使用人 | 使用人 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.08.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 调用次数 | 调用次数 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.08.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 调用时间 | 调用时间 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.08.000 |
| NaN | NaN | 学习中心管理 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | Banner管理 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | Banner副标题 | Banner副标题 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | 手册素材管理 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | 新增手册素材 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 文档标题 | 文档标题 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 文档副标题 | 文档副标题 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 文档备注 | 文档备注 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 学习素材链接 | 学习素材链接 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 排序 | 排序 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | 素材列表 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 文档标题 | 文档标题 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 文档副标题 | 文档副标题 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 文档备注 | 文档备注 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 学习素材链接 | 学习素材链接 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 排序 | 排序 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | 编辑素材 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 文档标题 | 文档标题 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 文档副标题 | 文档副标题 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 文档备注 | 文档备注 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 学习素材链接 | 学习素材链接 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 排序 | 排序 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | 删除素材 | NaN | NaN | 支持删除素材 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | 视频素材管理 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | 新增手册素材 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 视频素材名称 | 视频素材名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 视频素材链接 | 视频素材链接 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 视频发布人 | 视频发布人 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 发布时间 | 发布时间 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 课程级别分类 | 课程级别分类 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 排序 | 排序 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | 素材列表 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 视频素材名称 | 视频素材名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 视频素材链接 | 视频素材链接 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 视频发布人 | 视频发布人 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 发布时间 | 发布时间 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 课程级别分类 | 课程级别分类 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 排序 | 排序 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | 编辑素材 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 视频素材名称 | 视频素材名称 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 视频素材链接 | 视频素材链接 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 视频发布人 | 视频发布人 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 发布时间 | 发布时间 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 课程级别分类 | 课程级别分类 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 排序 | 排序 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | 删除素材 | NaN | NaN | 支持素材的删除 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | 物料素材管理 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | 新增手册素材 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 版本号 | 版本号 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 下载链接 | 下载链接 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 依赖HSDDML | 依赖HSDDML | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 前端引擎版本 | 前端引擎版本 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 后端引擎版本 | 后端引擎版本 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 发布时间 | 发布时间 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 版本说明 | 版本说明 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | 素材列表 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 版本号 | 版本号 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 下载链接 | 下载链接 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 依赖HSDDML | 依赖HSDDML | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 前端引擎版本 | 前端引擎版本 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 后端引擎版本 | 后端引擎版本 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 发布时间 | 发布时间 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 版本说明 | 版本说明 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | 编辑素材 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 版本号 | 版本号 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 下载链接 | 下载链接 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 依赖HSDDML | 依赖HSDDML | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 前端引擎版本 | 前端引擎版本 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 后端引擎版本 | 后端引擎版本 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 发布时间 | 发布时间 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | NaN | NaN | 版本说明 | 版本说明 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | 删除素材 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | 设为最新版本 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |
| NaN | NaN | NaN | NaN | 设为稳定版本 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202303.03.000 |

## 资产管理域（2）
| 业务领域(一级) | 价值流（二级） | 活动（三级） | 任务（四级） | 关键字段（五级） | 描述 | 必填 | 备注(是否多选，前置依赖，限制要求 等) | 低码开发人员 | 资产管理运营人员 | 专业开发人员 | 语言版本 | 发布版本 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 资产物料&脚手架 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | 组件及组件二开 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 公司级组件 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 布局类 | NaN | https://192.168.84.41/head-develop/HCreator1.0/trunk/Documents/D5.Others/OBP2024/HCreator1.0-Release1.5/RP1.5 审计-三大基件/20240815布局类组件（导出）.xlsx | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 栅格布局 | 使用列在水平方向上拆分页面，以有组织的方式对元素进行布局 | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 容器类 | NaN | https://192.168.84.41/head-develop/HCreator1.0/trunk/Documents/D5.Others/OBP2024/HCreator1.0-Release1.5/RP1.5 审计-三大基件/20240815容器类组件（导出）.xlsx | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 容器 | 调整外层容器的布局方向和间距，可以控制内部组件元素的布局方向和间隙 | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 容器项 | 可调整组件所占区域的宽度 | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 折叠页 | 将内容区域折叠/展开。 | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 吸底按钮容器 | 底部可以添加多个按钮，支持编辑按钮文本和按钮类型 | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 表单容器 | 具有数据收集、校验和提交功能的表单，包含复选框、单选框、输入框、下拉选择框等元素。 | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 表单项 | 基于表单中组件元素页面效果、校验、标题等元素的集合 | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 页签容器 | 选项卡切换组件，常用于平级区域大块内容的的收纳和展现。 | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 上下布局容器 | 适用具有上下两层展示的场景 | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 展示类 | NaN | https://192.168.84.41/head-develop/HCreator1.0/trunk/Documents/D5.Others/OBP2024/HCreator1.0-Release1.5/RP1.5 审计-三大基件/20240815展示类组件（导出）.xlsx | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 图标 | Icon | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 按钮 | 基础表单组件，触发业务逻辑时使用。 | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 下拉按钮 | 展示一组折叠的下拉按钮 | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 低码文本组件 | 用于展示页面中的文本或标题的内容。 | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 分页组件 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 徽标组件 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 锚点组件 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 图片组件 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 步骤条 | 拆分某项流程的步骤，引导用户按流程完成任务。 | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 表格类 | NaN | https://192.168.84.41/head-develop/HCreator1.0/trunk/Documents/D5.Others/OBP2024/HCreator1.0-Release1.5/RP1.5 审计-三大基件/20240815表格类组件（导出）.xlsx | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 可编辑表格 | 表格单元格可编辑,可对列配置校验规则进行单个检验。 | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 表格 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 树形表格 | 主要用于展示大量结构化数据。支持排序、筛选、分页、自定义操作、导出csv等复杂功能 | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 表单类 | NaN | https://192.168.84.41/head-develop/HCreator1.0/trunk/Documents/D5.Others/OBP2024/HCreator1.0-Release1.5/RP1.5 审计-三大基件/20240815表单类组件（导出）.xlsx | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 级联框 | 从一组相关联的数据集合中进行选择，常用于省市区、公司级层、事务分类等。 | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 多选框 | 基本表单组件，用于一组可选项的多项选择或者单独用于标记切换某种状态。 | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 日期选择器 | 选择或输入日期，支持年、月、日期等类型，支持选择范围。 | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 日期范围 | 选择或输入日期，支持选择范围。 | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 时间选择器 | 选择或输入标准时间，支持选择范围。 | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 单行输入框 | 基本表单组件，支持 input 和 textarea，并在原生控件基础上进行了功能扩展，可以组合使用 | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 数字输入框 | 用于数字内容的输入。 | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 多行输入框 | 用于输入多行的文字内容。 | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 金额输入框 | 用于金额内容的输入。 | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 密码输入框 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 单选框 | 基本表单组件，用于一组可选项的单选或者单独用于切换到选中状态。 | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 下拉表格 | 以表格形式展示选项，用户可进行多选操作。 | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 下拉选择（单选、复选） | 以列表形式展示选项，用户可进行搜索和选择操作。 | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 下拉树（单选、多选） | 以树形式展示选项，用户可进行搜索和选择操作。 | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 开关 | 在开关状态/两种状态间切换时使用的开关选择器。 | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 滑块 | 滑动输入器，用于在数值区间/自定义区间内进行选择，支持连续或离散值。 | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 穿梭框 | 双栏穿梭选择框，常用于将多个项目从一边移动到另一边。 | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 评分 | 对事物进行快速的评级操作，或对评价进行展示。 | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 平铺标签 | 能够呈现平铺标签 | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 上传 | 文件选择上传和拖拽上传控件。 | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 富文本 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 反馈类 | NaN | https://192.168.84.41/head-develop/HCreator1.0/trunk/Documents/D5.Others/OBP2024/HCreator1.0-Release1.5/RP1.5 审计-三大基件/20240815反馈类组件（导出）.xlsx | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 弹出框提醒 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 弹出框 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 抽屉 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 图表类 | NaN | https://192.168.84.41/head-develop/HCreator1.0/trunk/Documents/D5.Others/OBP2024/HCreator1.0-Release1.5/RP1.5 审计-三大基件/20240815图表类组件（导出）.xlsx | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 柱状图 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 饼图 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 折线图 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 标题组件 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | Link链接 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 组件二开 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 组件扩展规范 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 二开扩展规范 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 组件二开脚手架 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 二开脚手架 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | 引擎插件及二开 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 公司级插件 | NaN | NaN | https:/192.168.84.41/head-develop/Hcreator1.0/trunk/Documents/D2.Designs/OBP2024/HCreator1.0-Release1.6/新架构版本/特性需求技术方案/特性需求技术方案-语言特性:服务端扩展点体系.doc | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 框架插件 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 用户Token解析插件 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 权限插件 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 系统参数仓储层插件 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 国际化仓储层插件 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 静态字典仓储层插件 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 数据库仓储层插件 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 业务插件 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | BO仓储层触发器(所有bo) | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | BO仓储层触发器(单个bo) | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | BC仓储层插件 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 数据源插件 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | ld生成器插件 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 应用服务触发器 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | 开放接口触发器 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | BC仓储层触发器(所有bc) | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 插件二开 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 插件扩展规范 | 插件扩展规范 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 插件脚手架 | 暂无 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 指令集 | 指令文档 | https://192.168.84.41/head-develop/HCreator1.0/trunk/Documents/D5.Others/OBP2024/HCreator1.0-Release1.5/RP1.5 审计-三大基件/20240815逻辑编排指令与节点规格（导出）.xlsx | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | 逻辑库及二开 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 公司级逻辑库 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 附件服务逻辑库 | 附件服务接口文档 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 工作流服务逻辑库 | 工作流BS逻辑库 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 小计合计逻辑库 | 小记合计接口文档 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 逻辑库二开 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 逻辑库扩展规范 | 逻辑库扩展规范 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 逻辑库脚手架 | 暂无 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 指令集 | 指令文档 | https://192.168.84.41/head-develop/HCreator1.0/trunk/Documents/D5.Others/OBP2024/HCreator1.0-Release1.5/RP1.5 审计-三大基件/20240815逻辑编排指令与节点规格（导出）.xlsx | NaN | NaN | NaN | NaN | NaN | NaN | NaN |

## 应用管理域
| 业务领域(一级) | 价值流（二级） | 活动（三级） | 子活动（四级） | 任务（四级） | 关键字段（五级） | 描述 | 接口 | 实体 | DFX | 必填 | 备注(是否多选，前置依赖，限制要求 等) | 语言版本 | 发布版本 | 低码开发人员 | 资产管理运营人员 | 专业开发人员 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 应用管理域 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | 业务元数据管理（待完善） | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | 引擎制品管理（待完善） | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | 依赖制品管理（待完善） | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | 应用交付包管理（待完善） | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |

## DFX
| 业务领域(一级) | 价值流（二级） | 活动（三级） | 任务（四级） | 关键字段（五级） | 描述 | 预定义 | 必填 | 强制性 | 备注(是否多选，前置依赖，限制要求 等) | 低码开发人员 | 资产管理运营人员 | 专业开发人员 | 版本 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 开发域(设计器) | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | 易安装性 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 设计器插件易安装 | NaN | <20min | 从0开始，安装、配置和demo应用发布到应用运行引擎时间（win10、mac14） | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.01 |
| NaN | NaN | 设计器插件易安装 | NaN | <10min | 从0开始，安装、配置和demo应用发布到应用运行引擎时间 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | 易操作性 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 合适任务 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 步骤合适 | NaN | 完成任务所需步骤只包括必要的步骤，省略不必要的步骤；用户完成一个任务的操作步骤原则最多三步 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 自动默认 | NaN | 如果一个任务所需的输入是典型的值，那就应该自动设为默认 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 避不相关 | NaN | 避免提供与用户成功完成任务不相关的信息 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 可控性 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 操作可控 | NaN | 交互应在用户控制之下，用户任何时候都可以决定放弃或者退回、退出；交互由用户根据自己的需求和特点进行调整 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 打断可控 | NaN | 如果对话被打断，用户应该有能力决定从何处重新开始--对话被打断之处，让用户自己决定是继续还是取消 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 记录可改 | NaN | 新增记录需要有相关的删除或取消或修改等编辑功能 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 用户期望 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 恢复现场 | NaN | 为适应用户的碎片化使用习惯，在各种切换和退出返回时，要能有恢复现场的能力 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 协助记忆 | NaN | 搜索栏有历史记录或输入框有自动联想功能，必要的时候可以记住账号，密码等信息 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 通用性强 | NaN | 1、基于用户的已有知识，交互系统应使用用户熟悉的词汇或行业通用词汇；基于用户已有的交互习惯进行设计\n2、控件不可使用时，置灰\n3、不可输入的输入框显示只读\n4、红色标\*的选项原则上必须为必选项 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 操作可见 | NaN | 用户在网页上的任何操作:单击、双击、长时间按下、滚动、滑动键盘操作，页面应即时给出反馈。“即时”是指，页面响应时间小于用户能忍受的等待时间。 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 状态可见 | NaN | 状态可见包含:按钮状态[颜色变化]、系统状志响应[读取中、加载中、下载中等]、进度条[状态、百分比]、其它提示信息等 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 响应快速 | NaN | 对话的响应和反应速度一般控制在2秒以内，如果反应时间与用户期待的时间差距较大，应告知用户，通过进度条或其他信息显示进度 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 自然真实 | NaN | 对话所展示的数据结构和组织表格应尽量以用户觉得自然的方式展示 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 功能一致性 | NaN | 1、相似任务的对话行为和外观应保持一致，以便用户在同一个产品中接受同一套规范或者逻辑，包括弹窗提示、弹窗风格、提示信息、系统提示状态提示、同类按钮形状、同类按钮颜色、同类按钮大小、同类按钮顺序、同类按钮位置、分页标识等\n2、输入限制提示与实际程序限制及错误提示要保持一致\n3、同类型的配置项的限制和错误提示要保持一致\n4、导航/菜单和对应功能页面的标题；弹窗入口文案和对应弹窗的title；要保持一致\n5、每页显示记录数量更改后界面尽量保持一致，不会出现界面不整洁情况 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 表现形式一致 | NaN | 1、界面缩放在80%~110%页面渲染一致，排版不错乱、字体无遮挡\n2、窗口切换、移动、改变大小时页面渲染一致，排版不错乱、字体无遮挡\n3、刷新后界面显示一致，排版不错乱、字体无遮挡\n4、不同的浏览器下页面渲染一致，排版不错乱、字体无遮挡 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 个性化 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 快捷可调 | NaN | 快捷操作可根据用户喜好做调整 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 页行可调 | NaN | 用户应该能够设置操作时间参数来匹配他/她的个人需求 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | 用户差错防御性 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 报错提示 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 明确错误 | NaN | 发生错误时允许用户纠正错误，明确错误提示：必填报错、非法和不合理的操作、字符限制长度限制报错等 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 提示易懂 | NaN | 报错提示为使用用户语言而不是开发者语言，贴近生活实际而不是学术概念 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 关键操作提示 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 关键操作提示 | NaN | 关键操作或数据删除等操作前是否有明确的提示，可能造成数据无法恢复的操作 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | 用户界面舒适性 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 信息获取 | NaN | NaN | 减少大篇幅连续的文字，图片>表格>文字，使用户能够快速方便的获取到关键信息或者操作入口 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 界面整洁 | NaN | NaN | 弹窗或界面排放整齐、不错乱、颜色覆盖全面、字体无遮挡 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 配色简洁 | NaN | NaN | 图片色彩与文字色彩原则上整体不超过5个颜色，检查界面的色彩搭配和对比度是否舒适，避免眼睛疲劳或视觉障碍。 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 导航简洁 | NaN | NaN | 导航简单易懂，不超过2层；标题命名贴合内容，不宜过于深奥复杂 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 操作高效 | NaN | NaN | 1、输入框中的文本支持拷贝、粘贴、剪切、转发、撤消等操作\n2、勾选框提供全选、取消全选等操作\n3、数据量大的下拉框提供搜索等操作 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 方便返回 | NaN | NaN | 弹窗或界面需要有方便快捷的返回方式\n选项少时多用勾选方式 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 选项排布 | NaN | NaN | 选项多时多用下拉列表框，界面空间较小时使用下拉框而不用选项框，需用户选择的列表越短越好，如果很长，应该适当分级显示 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 灵活性 | NaN | NaN | 1、页面数据暴涨出现较长列表时，要展示滚动条或进行分页保证页面显示完整的信息\n2、字段长度超出范围时，通过Hover展示完整信息或换行 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | 可辨识性(易理解性) | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 正确无误 | NaN | NaN | 没有错别字或笔误、乱码，JS等 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 含义清晰 | NaN | NaN | 所有用语(包括报错或提示信息等)足够通俗易懂且清晰明了 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 语言统一 | NaN | NaN | 同一含义的描述需要保持统一，不能全称、简称、中文、英文或英文缩写混用，或名称不一致 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 突出主次 | NaN | NaN | 重要信息突出展示，主次分明，重要的配置项、常用的下拉选项按照重要性、使用频率和逻辑顺序进行排列 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | 易学性 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 帮助到位 | NaN | NaN | 1、应提供适当的帮助信息(所有与用户有关的文档内容都应该详细、结构清晰、语言准确，便于理解和操作)\n2、目录或菜单选项划分有层次且容易找到，一般菜单不要超过三级；在必要时能够提供不同菜单项的使用说明 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 约束提示 | NaN | NaN | 1、输入或上传前提供友好的的限制说明或输入规则(输入格式)说明\n2、先后步骤的提示，操作步骤之间有依赖时，要进行先后依赖的提示，必要时展示向导功能 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 少学易用 | NaN | NaN | 1、让用户需要学的东西最少，只要输入最少量的信息，系统会按要求提供附加信息\n2、向导功能解释清楚、易懂，产品本身具有很好的引导性 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | 易访问性 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 易访问性 | NaN | NaN | 验证借助用户接口、帮助功能或用户文档集提供的手段，最终用户是否能够学习如何使用某一功能。 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | 兼容性 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 操作系统 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.01 |
| NaN | NaN | NaN | windows | 10+ | 设计器插件支持：支持windows10+ | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | Mac | 14+ | 设计器插件支持：支持和Mac14+ | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | 性能 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 最低设备要求 | NaN | NaN | 4核8G，50G硬盘 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.01 |
| NaN | NaN | 设计器加载应用交付包时间 | NaN | <10S | vscode+插件就绪后，设计器点击加载应用交付包后打开第一个资源编辑器时间（资源1000个以内：200个表，字段100+；160个实体；100个BO；100个BS；400个page；10个插件等）； | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.01 |
| NaN | NaN | 设计器打开第一个资源编辑器时间 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 资源编辑器 | <1S | 资源编辑器：200个节点1S内；（如field有200个） | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | page设计器 | <1S | page设计器：组件<=300个，渲染时间;(页面内每个类型的组件均分数量) | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 设计器操作响应速度 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 交互响应反馈时间 | <30ms | 交互响应反馈时间 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.01 |
| NaN | NaN | NaN | 页面浏览 | >25fps | 页面浏览fps | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.01 |
| NaN | NaN | 从IDE部署的时间 | NaN | <15S | 从IDE部署的时间，执行工程资源1000个以内（资源1000个以内：200个表，字段100+；160个实体；100个BO；100个BS；400个page；10个插件等）； | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | IDE内存占用 | NaN | <=1.5Ｇ | 内存要求（资源1000个以内：200个表，字段100+；160个实体；100个BO；100个BS；400个page；10个插件等）；； | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.01 |
| NaN | NaN | 出码的效率 | NaN | <5S | 资源数量<=1000个，出码时间（资源1000个以内：200个表，字段100+；160个实体；100个BO；100个BS；400个page；10个插件等）； | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | 安全性 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 设计器安全性 | NaN | NaN | license管理：资源许可管理、设计器功能许可管理等 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 资源文件的安全性 | NaN | NaN | 文件加密 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 资源敏感信息安全性 | NaN | NaN | 密码信息等加密 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| 应用管理域（应用运行引擎） | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | 易安装性 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 应用运行引擎-轻量化版本 | NaN | <20min | 安装部署和达到正常运行和可访问时间；\n系统要求：linux、mac、windows、虚拟机；\n全年目标：轻量化部署<10min | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.01 |
| NaN | NaN | 应用运行引擎-微服务版本 | NaN | <30min | 在jres框架安装完成的前提下应用运行引擎安装部署达到可访问的时间；\n系统要求：linux、centos、虚拟机； | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | 可靠性 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 应用运行引擎运行稳定性 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 轻量化 | 0.99 | 不中断服务（引擎正常运行，业务应用功能可正常访问且响应时间不受影响；排除人工操作和机器因素）\n【进程（主机）】- 【磁盘空间占用<=70%】\n【进程（主机）】-【CPU负载 <=CPU核数 \* 70%】\n【进程（主机）】- 【内存使用率<=70%】 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 微服务部署 | 0.9995 | 微服务部署情况下，不中断服务（引擎正常运行，业务应用功能可正常访问且响应时间不受影响；排除人工操作和机器因素）\n【进程（主机）】- 【磁盘空间占用<=70%】\n【进程（主机）】-【CPU负载 <=CPU核数 \* 70%】\n【进程（主机）】- 【内存使用率<=70%】 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | 安全性 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 能够通过安全性测试 | NaN | NaN | 通过公司安全性测试；\n详细参见链接：https://alidocs.dingtalk.com/i/nodes/G1DKw2zgV2RXpjejFMZeMpovVB5r9YAn?utm\_scene=team\_space | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.01 |
| NaN | 性能 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 最低设备要求 | NaN | NaN | 4核8G，50G硬盘 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 服务端BO接口响应效率 | NaN | NaN | 参考测试性能分析 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.01 |
| NaN | NaN | NaN | 查询 | TPS>50笔/s，\n调用时延小于1.5s | 单表、主子（一主三子）、主子孙等场景，\n铺底10W数据量的1000个字段查询，并发30； | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 新增 | TPS>50笔/s，\n调用时延小于2s | 单表、主子（一主三子）、主子孙等场景，\n铺底10W数据量的1000个字段查询，并发30； | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 修改 | TPS>50笔/s，\n调用时延小于2s | 单表、主子（一主三子）、主子孙等场景，\n铺底10W数据量的1000个字段查询，并发30； | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 删除 | TPS>50笔/s，\n调用时延小于2s | 单表、主子（一主三子）、主子孙等场景，\n铺底10W数据量的1000个字段查询，并发30； | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 业务运行引擎管理页面 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | 首屏 | <3S | 应用运行引擎的从输入url回车之后到用户可以操作 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.01 |
| NaN | NaN | NaN | 切换页面 | <1S | 切换页面到可以操作 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.01 |
| NaN | NaN | 前端页面渲染性能 | NaN | <1S | 首屏100个要素加载时间 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | V202401.01 |
| NaN | NaN | 前端页面渲染性能 | NaN | <2S | 首屏200个要素加载时间 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 前端页面渲染性能 | NaN | <3S | 首屏300个要素加载时间 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 运行引擎内存占用 | NaN | <=2G | 轻量化部署情况下，1000个资源（资源1000个以内：200个表，字段100+；160个实体；100个BO；100个BS；400个page；10个插件等）应用运行引擎内存 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| 资产管理域（物料资产中心） | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | 可靠性 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 资产中心可靠性 | NaN | 0.9995 | 不中断服务（PC端可正常访问，设计器可正常调用提供的接口，排除人工操作和机器因素）\n【进程（主机）】- 【磁盘空间占用<=70%】\n【进程（主机）】-【CPU负载 <=CPU核数 \* 70%】\n【进程（主机）】- 【内存使用率<=70%】 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | 性能 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 资产中心页面加载 | NaN | <1S | 加载时间 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 资产中心接口性能 | NaN | <200ms | 资产中心提供给设计器的对外接口响应时长 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
