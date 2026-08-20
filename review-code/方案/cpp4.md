# C++ 项目门控 4 技术选型

## 一、背景与目标

门控 4 负责接口、契约与数据兼容检查，拦截 API 签名变更、ABI 不兼容、返回值契约破坏、序列化协议非兼容变更，以及默认语义变化。

## 二、工具选型

| 维度 | 工具 | 说明 |
|---|---|---|
| **ABI 兼容性** | abidiff（libabigail 2.4+） | 对比 `.so`/`.a` 的符号表、类型大小、虚函数表 |
| **API/头文件兼容** | abi-compliance-checker / HeaderHunter | 检测头文件中函数签名、类布局、默认参数变化 |
| **序列化协议兼容** | buf breaking（Protobuf） | 对比 `.proto` 字段编号、类型、标签变更 |
| **契约测试** | Pact-C++ | 消费者驱动契约测试，跨模块接口校验 |
| **返回值契约** | `[[nodiscard]]` + clang-tidy | 编译器属性 + `bugprone-unchecked-optional-access` |
| **版本语义** | SemVer + cxx-abi 工具链 | 版本号与兼容性自动校验 |

## 三、ABI 兼容性检查流程

```text
基线版本（main 分支最新 release .so）
        ↓ abidiff 对比
当前 MR 构建产物 .so
        ↓
变更分类：
  - Compatible（符号新增）→ 通过
  - Incompatible（符号删除/签名变更/类型大小变化）→ 拦截，要求 bump SOVERSION
```

## 四、Protobuf 兼容性规则（buf breaking）

禁止的变更：
- 删除已有字段
- 修改字段编号（tag number）
- 修改字段类型（如 int32 → int64）
- 修改字段标签（required/optional/repeated 互转）
- 修改 service / rpc 方法签名

## 五、工具版本矩阵

| 门控 | 工具 | 推荐最低版本 | 输出格式 | 许可证 |
|---|---|---|---|---|
| 4 | abidiff (libabigail) | 2.4 | text / XML | Apache 2.0 |
| 4 | buf | 1.30 | JSON | Apache 2.0 |
| 4 | Pact-C++ | 最新稳定 | Pact JSON | MIT |

## 六、门禁阈值建议

### 6.1 分级拦截策略

| 等级 | 定义 | 处理方式 |
|---|---|---|
| **Blocker** | 编译失败、测试失败、ABI break、Critical 漏洞、安全 CVE | 立即拦截，禁止合入 |
| **Error** | clang-tidy error、cppcheck error、格式化不通过、覆盖率不达标 | 拦截，需修复或豁免 |
| **Warning** | 编译 warning（已升级为 error）、静态分析 warning | 趋势管控，新增即拦截 |
| **Info** | 建议性提示、代码风格偏好 | 不拦截，仅展示 |

### 6.2 门控 4 具体阈值

| 门控 | 拦截条件 | 豁免机制 |
|---|---|---|
| **4 接口契约** | abidiff 检测到 ABI break → 失败；buf breaking 非兼容变更 → 失败；Pact 契约不通过 → 失败 | ABI break 需同步 bump 主版本号并更新文档 |

## 七、CI 配置示例（GitLab CI 片段）

```yaml
stages:
  - compat

# ── 门控 4：接口契约与兼容 ──
compat:abi:
  stage: compat
  image: ubuntu:24.04
  before_script:
    - apt-get update && apt-get install -y abigail-tools
  script:
    - curl -o libbaseline.so $BASELINE_SO_URL
    - abidiff --no-added-syms libbaseline.so $BUILD_DIR/libtarget.so || exit 1

compat:proto:
  stage: compat
  image: bufbuild/buf:1.30
  script:
    - buf breaking proto/ --against ".git#branch=main,subdir=proto"

compat:pact:
  stage: compat
  script:
    - ./$BUILD_DIR/tests/pact_verifier --pact-dir=pacts/
```
