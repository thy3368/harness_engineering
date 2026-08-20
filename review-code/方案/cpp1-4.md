# C++ 项目门控 1-4 技术选型

## 一、背景与目标

在代码合入门控体系中，门控 1-4 属于**确定性规则检查**，其核心特征是规则明确、可机器判定、零语义模糊性。此类检查不应依赖 LLM/OCR，而应由编译工具链、静态分析器和契约校验工具完成，以保证毫秒级响应速度与 100% 可复现的判定结果。

本报告以 C++ 项目为对象，给出四门控的完整技术选型、工具版本矩阵、门禁阈值、CI 集成方案及落地路径。

---

## 二、总体架构

```
┌─────────────────────────────────────────────────────────────┐
│  门控 1  代码规范        → clang-format + clang-tidy + cpplint │
│  门控 2  语言/构建/测试  → GCC/Clang + CMake + GoogleTest + Sanitizer │
│  门控 3  静态质量与安全  → Clang SA + cppcheck + SonarQube + Infer │
│  门控 4  接口契约与兼容  → abidiff + buf breaking + Pact-C++ │
├─────────────────────────────────────────────────────────────┤
│  统一输出层：SARIF / JSON / JUnit XML → 效能平台聚合展示       │
└─────────────────────────────────────────────────────────────┘
```

**设计原则**：
- 确定性检查全部左移到 CI，本地 pre-commit 做第一道拦截
- 所有工具输出标准化格式（SARIF/JSON），统一汇入缺陷管理平台
- 门禁阈值分级：error 级零容忍，warning 级按趋势管控

---

## 三、门控 1：代码规范

### 3.1 目标
拦截模糊命名、编码约定违反、格式不一致、include 顺序混乱等问题。

### 3.2 工具选型

| 工具 | 职责 | 配置文件 |
|---|---|---|
| **clang-format** | 代码格式化（缩进、换行、括号、空格） | `.clang-format` |
| **clang-tidy** | 命名规范、现代 C++ 用法、include 顺序、可读性检查 | `.clang-tidy` |
| **cpplint** | Google C++ Style 合规检查（补充 clang-tidy 未覆盖项） | `CPPLINT.cfg` |
| **doxygen + clang-doc** | 公共 API 文档注释完整性检查 | Doxyfile |

### 3.3 关键规则示例

**clang-tidy 检查集**：
```
readability-identifier-naming       # 命名规范（类大驼峰、函数小驼峰、常量全大写）
readability-braces-around-statements # 条件/循环必须加花括号
readability-magic-numbers           # 禁止魔法数字
modernize-use-nullptr               # 用 nullptr 替代 NULL
modernize-use-auto                  # 合理使用 auto
modernize-use-override              # 虚函数加 override
llvm-include-order                  # include 排序
```

**clang-format 关键项**：
```yaml
BasedOnStyle: Google
IndentWidth: 4
ColumnLimit: 120
SortIncludes: true
BreakBeforeBraces: Attach
```

### 3.4 集成方式
- **本地**：pre-commit hook 运行 `clang-format --dry-run -Werror`，格式化不通过则拒绝提交
- **CI**：全量运行 `run-clang-tidy`，输出 SARIF；cpplint 输出文本报告
- **IDE**：CLion / VSCode 安装 clangd 插件，实时提示

---

## 四、门控 2：语言、构建与基础测试

### 4.1 目标
拦截类型误用、编译告警、构建失败、单元测试不通过、覆盖率不达标、未定义行为。

### 4.2 工具选型

| 维度 | 工具 | 说明 |
|---|---|---|
| **编译器** | GCC 13+ / Clang 17+ / MSVC 2022 | 多编译器矩阵编译，保证可移植性 |
| **构建系统** | CMake 3.25+ + Ninja | 统一构建配置 |
| **单元测试** | GoogleTest 1.14+ / Catch2 | 测试框架 + Mock（gmock） |
| **覆盖率** | gcovr 6.0+ / llvm-cov 17+ | 行覆盖率、分支覆盖率统计 |
| **运行时检查** | AddressSanitizer / UndefinedBehaviorSanitizer | 内存越界、未定义行为检测 |
| **内存泄漏** | LeakSanitizer（ASan 内置） | 运行时泄漏检测 |

### 4.3 编译选项基线

```cmake
# CMakeLists.txt 关键配置
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_COMPILE_WARNING_AS_ERROR ON)

add_compile_options(
  -Wall -Wextra -Wpedantic
  -Wshadow -Wconversion -Wsign-conversion
  -Wnon-virtual-dtor -Wold-style-cast
  -Wnull-dereference -Wdouble-promotion
)

# Sanitizer 构建类型
set(CMAKE_CXX_FLAGS_ASAN "-fsanitize=address,undefined -g -O1")
```

### 4.4 测试与覆盖率要求
- 单元测试必须随代码一同提交，新增代码行覆盖率 ≥ 80%
- 测试输出 JUnit XML，覆盖率输出 Cobertura XML
- CI 中分别跑 Release（正常）和 ASan（内存检查）两种构建

---

## 五、门控 3：静态质量与安全

### 5.1 目标
拦截可疑比较、恒真/恒假分支、空指针解引用、资源泄漏、异常调用、CWE 漏洞模式、第三方依赖 CVE。

### 5.2 工具选型

| 层级 | 工具 | 定位 | 速度 |
|---|---|---|---|
| **L1 快速扫描** | cppcheck 2.13+ | 无编译依赖，跨平台，规则覆盖广 | 快（分钟级） |
| **L2 路径敏感分析** | Clang Static Analyzer 17+ | 基于编译数据库，路径敏感，精度高 | 中 |
| **L3 增量深度分析** | Infer（Meta 开源） | 增量分析快，空指针/资源泄漏强 | 中 |
| **L4 企业级平台** | SonarQube 10.x（C/C++ Plugin） | 规则库全，质量门禁，长期趋势 | 慢（全量） |
| **L5 商业增强（可选）** | Coverity / PVS-Studio | 深度缺陷检测，CWE 映射全 | 慢 |
| **依赖安全** | OSV-Scanner / Conan audit | 第三方库 CVE 扫描 | 快 |

### 5.3 关键检测能力映射

| 问题类型 | 主力工具 | 规则/检查器示例 |
|---|---|---|
| 空指针解引用 | Clang SA / Infer | `core.NullDereference` |
| 资源泄漏 | Clang SA / cppcheck | `unix.Malloc` / `resourceLeak` |
| 恒真/恒假分支 | cppcheck / Clang SA | `stylistic` / `core.DivideZero` |
| 可疑比较 | cppcheck | `comparison` / `mismatchExpressionTypes` |
| 未初始化变量 | Clang SA | `core.uninitialized` |
| 数组越界 | Clang SA / ASan | `core.ArrayIndexOutOfBounds` |
| 整数溢出 | cppcheck / PVS-Studio | `integerOverflow` |
| 依赖 CVE | OSV-Scanner | 全量 CVE 库匹配 |

### 5.4 集成方式
- cppcheck 在 CI 中每次全量运行，`--enable=all --error-exitcode=1`
- Clang SA 使用 `scan-build` 包装编译，输出 HTML + SARIF
- SonarQube 每日夜间全量扫描（或 MR 增量扫描），作为长期质量门禁
- OSV-Scanner 在依赖变更时触发

---

## 六、门控 4：接口、契约与数据兼容

### 6.1 目标
拦截 API 签名变更、ABI 不兼容、返回值契约破坏、序列化协议非兼容变更、默认语义变化。

### 6.2 工具选型

| 维度 | 工具 | 说明 |
|---|---|---|
| **ABI 兼容性** | abidiff（libabigail 2.4+） | 对比 `.so`/`.a` 的符号表、类型大小、虚函数表 |
| **API/头文件兼容** | abi-compliance-checker / HeaderHunter | 检测头文件中函数签名、类布局、默认参数变化 |
| **序列化协议兼容** | buf breaking（Protobuf） | 对比 `.proto` 字段编号、类型、标签变更 |
| **契约测试** | Pact-C++ | 消费者驱动契约测试，跨模块接口校验 |
| **返回值契约** | `[[nodiscard]]` + clang-tidy | 编译器属性 + `bugprone-unchecked-optional-access` |
| **版本语义** | SemVer + cxx-abi 工具链 | 版本号与兼容性自动校验 |

### 6.3 ABI 兼容性检查流程

```
基线版本（main 分支最新 release .so）
        ↓ abidiff 对比
当前 MR 构建产物 .so
        ↓
变更分类：
  - Compatible（符号新增）→ 通过
  - Incompatible（符号删除/签名变更/类型大小变化）→ 拦截，要求 bump SOVERSION
```

### 6.4 Protobuf 兼容性规则（buf breaking）

禁止的变更：
- 删除已有字段
- 修改字段编号（tag number）
- 修改字段类型（如 int32 → int64）
- 修改字段标签（required/optional/repeated 互转）
- 修改 service / rpc 方法签名

---

## 七、工具版本矩阵

| 门控 | 工具 | 推荐最低版本 | 输出格式 | 许可证 |
|---|---|---|---|---|
| 1 | clang-format | LLVM 17 | plain / JSON | Apache 2.0 |
| 1 | clang-tidy | LLVM 17 | SARIF / JSON | Apache 2.0 |
| 1 | cpplint | 1.6.1 | plain text | BSD-3 |
| 2 | GCC | 13.2 | 编译日志 | GPL |
| 2 | Clang | 17.0 | 编译日志 | Apache 2.0 |
| 2 | CMake | 3.25 | - | BSD-3 |
| 2 | GoogleTest | 1.14 | JUnit XML | BSD-3 |
| 2 | gcovr | 6.0 | Cobertura XML | BSD-3 |
| 3 | Clang Static Analyzer | LLVM 17 | SARIF / HTML | Apache 2.0 |
| 3 | cppcheck | 2.13 | XML / SARIF | GPL-3 |
| 3 | Infer | 1.1 | JSON / SARIF | MIT |
| 3 | SonarQube | 10.x | 平台内 / Web API | LGPL（社区版） |
| 3 | OSV-Scanner | 1.4 | JSON / SARIF | Apache-2.0 |
| 4 | abidiff (libabigail) | 2.4 | text / XML | Apache 2.0 |
| 4 | buf | 1.30 | JSON | Apache 2.0 |
| 4 | Pact-C++ | 最新稳定 | Pact JSON | MIT |

---

## 八、门禁阈值建议

### 8.1 分级拦截策略

| 等级 | 定义 | 处理方式 |
|---|---|---|
| **Blocker** | 编译失败、测试失败、ABI break、Critical 漏洞、安全 CVE | 立即拦截，禁止合入 |
| **Error** | clang-tidy error、cppcheck error、格式化不通过、覆盖率不达标 | 拦截，需修复或豁免 |
| **Warning** | 编译 warning（已升级为 error）、静态分析 warning | 趋势管控，新增即拦截 |
| **Info** | 建议性提示、代码风格偏好 | 不拦截，仅展示 |

### 8.2 各门控具体阈值

| 门控 | 拦截条件 | 豁免机制 |
|---|---|---|
| **1 代码规范** | clang-format 有 diff → 失败；clang-tidy error ≥1 → 失败 | 单行 `NOLINT` 注释 + Reviewer 确认 |
| **2 语言构建** | 编译 error/warning ≥1 → 失败（-Werror）；单测通过率 <100% → 失败；行覆盖率 <70% → 失败 | 覆盖率豁免需标注原因并审批 |
| **3 静态质量** | Clang SA / cppcheck error ≥1 → 失败；Critical/High 漏洞 ≥1 → 失败；已知 CVE 未修复 → 失败 | SonarQube 标记 Won't Fix + 安全负责人审批 |
| **4 接口契约** | abidiff 检测到 ABI break → 失败；buf breaking 非兼容变更 → 失败；Pact 契约不通过 → 失败 | ABI break 需同步 bump 主版本号并更新文档 |

---

## 九、CI 配置示例（GitLab CI 完整版）

```yaml
variables:
  BUILD_DIR: build
  CC: gcc
  CXX: g++

stages:
  - lint
  - build
  - test
  - analyze
  - compat

# ── 门控 1：代码规范 ──
lint:format:
  stage: lint
  image: silkeh/clang:17
  script:
    - find src/ -name '*.cpp' -o -name '*.h' | xargs clang-format --dry-run --Werror

lint:tidy:
  stage: lint
  image: silkeh/clang:17
  script:
    - cmake -B $BUILD_DIR -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
    - run-clang-tidy -p $BUILD_DIR -header-filter=src/ -checks=-*,readability-*,modernize-*,bugprone-*,cppcoreguidelines-*
  artifacts:
    reports:
      codequality: clang-tidy-sarif.json

lint:cpplint:
  stage: lint
  image: python:3.11
  script:
    - pip install cpplint
    - cpplint --recursive --counting=detailed src/ || exit 1

# ── 门控 2：语言、构建与测试 ──
build:gcc:
  stage: build
  image: gcc:13
  script:
    - cmake -B $BUILD_DIR -G Ninja -DCMAKE_BUILD_TYPE=Release -DCMAKE_COMPILE_WARNING_AS_ERROR=ON
    - cmake --build $BUILD_DIR
  artifacts:
    paths: [$BUILD_DIR]

build:clang-asan:
  stage: build
  image: silkeh/clang:17
  script:
    - cmake -B $BUILD_DIR-asan -G Ninja -DCMAKE_BUILD_TYPE=Debug
      -DCMAKE_CXX_FLAGS="-fsanitize=address,undefined -fno-omit-frame-pointer"
    - cmake --build $BUILD_DIR-asan
  artifacts:
    paths: [$BUILD_DIR-asan]

test:unit:
  stage: test
  dependencies: [build:gcc]
  script:
    - ./$BUILD_DIR/tests/unit_tests --gtest_output=xml:junit.xml
  artifacts:
    reports:
      junit: junit.xml

test:coverage:
  stage: test
  image: gcc:13
  script:
    - cmake -B $BUILD_DIR-cov -DCMAKE_BUILD_TYPE=Debug -DCMAKE_CXX_FLAGS="--coverage"
    - cmake --build $BUILD_DIR-cov
    - ./$BUILD_DIR-cov/tests/unit_tests
    - gcovr -r . --xml-pretty -o coverage.xml --fail-under-line 70 --fail-under-branch 60
  artifacts:
    reports:
      coverage_report:
        coverage_format: cobertura
        path: coverage.xml

# ── 门控 3：静态质量与安全 ──
analyze:clang-sa:
  stage: analyze
  image: silkeh/clang:17
  script:
    - scan-build -o scan-report --status-bugs cmake --build $BUILD_DIR
  artifacts:
    paths: [scan-report]

analyze:cppcheck:
  stage: analyze
  image: nereoc/cppcheck:2.13
  script:
    - cppcheck --enable=all --inconclusive --error-exitcode=1
      --suppress=missingIncludeSystem --xml src/ 2> cppcheck.xml
  artifacts:
    reports:
      codequality: cppcheck.xml

analyze:sonar:
  stage: analyze
  image: sonarsource/sonar-scanner-cli:latest
  script:
    - sonar-scanner -Dsonar.projectKey=$CI_PROJECT_NAME
      -Dsonar.sources=src/ -Dsonar.cfamily.compile-commands=$BUILD_DIR/compile_commands.json
  allow_failure: true  # 夜间全量，MR 阶段仅告警

analyze:osv:
  stage: analyze
  image: ghcr.io/google/osv-scanner:latest
  script:
    - osv-scanner --lockfile=conan.lock --format=sarif > osv.sarif
  artifacts:
    reports:
      codequality: osv.sarif

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

---



## 十、与 OCR 的协作边界

| 门控 | 负责方 | OCR 角色 |
|---|---|---|
| 1-4 | 确定性工具链 | 不介入检查逻辑 |
| 5 Agentic CR | OCR | 语义审查主战场 |
| 1-4 结果增强 | OCR（可选） | 对 Sonar/cppcheck 告警做语义判断（如"可疑比较是否真导致业务 bug"），输出修复建议 |

**核心结论**：门控 1-4 是确定性工程的领地，工具链成熟、速度快、可复现；OCR 的不可替代价值在门控 5 的语义理解，以及对前四门控结果的语义增强，而非替代确定性检查。
