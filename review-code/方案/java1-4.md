# Java 项目门控 1-4 技术选型

## 一、背景与目标

在代码合入门控体系中，门控 1-4 属于**确定性规则检查**，其核心特征是规则明确、可机器判定、零语义模糊性。此类检查不应依赖 LLM/OCR，而应由 JDK 编译工具链、Maven 插件、测试框架、静态分析器、安全扫描器和契约校验工具完成，以保证响应速度、可复现性和可追溯性。

本报告以 **Spring Boot + Maven + JDK 21 LTS** 项目为对象，给出四个门控的完整技术选型、工具版本矩阵、门禁阈值、CI 集成方案及落地路径。

---

## 二、总体架构

```
┌─────────────────────────────────────────────────────────────┐
│  门控 1  代码规范        → Spotless + Checkstyle + PMD + Error Prone │
│  门控 2  语言/构建/测试  → javac + Maven Enforcer + JUnit 5 + JaCoCo + Testcontainers │
│  门控 3  静态质量与安全  → SpotBugs + FindSecBugs + SonarQube + OWASP Dependency-Check │
│  门控 4  接口契约与兼容  → Revapi/jApiCmp + Pact JVM + OpenAPI Diff + protobuf breaking │
├─────────────────────────────────────────────────────────────┤
│  统一输出层：SARIF / XML / JSON / JUnit XML → 效能平台聚合展示 │
└─────────────────────────────────────────────────────────────┘
```

**设计原则**：
- 确定性检查全部左移到 CI，本地 pre-commit 或 Maven Wrapper 做第一道拦截
- 所有工具输出标准化格式（XML/JSON/SARIF/JUnit XML），统一汇入缺陷管理平台
- 门禁阈值分级：error 级零容忍，warning 级按新增量和趋势管控
- Maven 构建以 `./mvnw verify` 为主入口，避免本地 Maven/JDK 版本漂移

---

## 三、门控 1：代码规范

### 3.1 目标

拦截格式不一致、命名与编码约定违反、重复或复杂代码、异常日志不规范、注释与公共 API 文档缺失等问题。

### 3.2 工具选型

| 工具 | 职责 | 配置文件 |
|---|---|---|
| **Spotless** | 代码格式化、import 顺序、版权头检查 | `pom.xml` / `spotless.xml` |
| **Checkstyle** | 命名、缩进、Javadoc、类与方法结构规范 | `checkstyle.xml` / `suppressions.xml` |
| **PMD** | 复杂度、重复逻辑、坏味道、异常与日志规范 | `pmd-ruleset.xml` |
| **Error Prone** | javac 编译期缺陷规则补充，拦截高置信度误用 | `maven-compiler-plugin` |

### 3.3 关键规则示例

**Checkstyle 检查集**：
```
TreeWalker
  TypeName / MethodName / MemberName      # 类、方法、字段命名规范
  AvoidStarImport                         # 禁止星号 import
  NeedBraces                              # 条件/循环必须加花括号
  MissingJavadocType                      # 公共类型必须有 Javadoc
  LineLength                              # 单行长度限制
  FinalClass / HideUtilityClassConstructor # 工具类与不可继承类约束
```

**PMD 规则集**：
```
category/java/bestpractices.xml
category/java/codestyle.xml
category/java/design.xml/CyclomaticComplexity
category/java/errorprone.xml
category/java/performance.xml
```

**Spotless 关键项**：
```xml
<plugin>
  <groupId>com.diffplug.spotless</groupId>
  <artifactId>spotless-maven-plugin</artifactId>
  <configuration>
    <java>
      <googleJavaFormat>
        <version>1.22.0</version>
      </googleJavaFormat>
      <removeUnusedImports />
      <importOrder />
    </java>
  </configuration>
</plugin>
```

### 3.4 集成方式

- **本地**：pre-commit hook 或 IDE 保存时运行 `./mvnw spotless:apply`
- **CI**：运行 `./mvnw spotless:check checkstyle:check pmd:check`
- **IDE**：IntelliJ IDEA 配置 Checkstyle 插件，统一启用 Maven Wrapper 和 JDK 21
- **豁免**：只允许通过 `suppressions.xml` 或带工单号的局部注解豁免，禁止大面积关闭规则

---

## 四、门控 2：语言、构建与基础测试

### 4.1 目标

拦截 JDK 版本不一致、编译失败、编译期高置信度错误、依赖版本漂移、单元测试失败、集成测试失败、覆盖率不达标和 Spring 上下文启动失败。

### 4.2 工具选型

| 维度 | 工具 | 说明 |
|---|---|---|
| **语言版本** | JDK 21 LTS + `javac --release 21` | 固定语言级别和目标字节码版本 |
| **构建系统** | Maven 3.9+ + Maven Wrapper | 统一构建入口，便于 CI 和本地一致 |
| **版本约束** | Maven Enforcer | 约束 JDK、Maven、依赖收敛、禁止快照依赖 |
| **单元测试** | JUnit 5 + Mockito | 业务逻辑和边界条件测试 |
| **覆盖率** | JaCoCo | 行覆盖率、分支覆盖率、增量覆盖率统计 |
| **集成测试** | Failsafe + Testcontainers | 数据库、MQ、Redis、外部依赖容器化验证 |
| **Spring 测试** | Spring Boot Test | 配置绑定、上下文启动、Profile 校验 |

### 4.3 Maven 构建基线

```xml
<properties>
  <java.version>21</java.version>
  <maven.compiler.release>21</maven.compiler.release>
  <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
</properties>

<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-enforcer-plugin</artifactId>
  <executions>
    <execution>
      <goals>
        <goal>enforce</goal>
      </goals>
      <configuration>
        <rules>
          <requireJavaVersion>
            <version>[21,22)</version>
          </requireJavaVersion>
          <requireMavenVersion>
            <version>[3.9,)</version>
          </requireMavenVersion>
          <dependencyConvergence />
          <banDuplicatePomDependencyVersions />
          <requireReleaseDeps />
        </rules>
      </configuration>
    </execution>
  </executions>
</plugin>
```

### 4.4 测试与覆盖率要求

- 单元测试必须随代码一同提交，新增业务代码行覆盖率建议 ≥ 80%
- 全量项目行覆盖率建议 ≥ 70%，分支覆盖率建议 ≥ 60%
- `maven-surefire-plugin` 输出 JUnit XML，`jacoco-maven-plugin` 输出 XML/HTML
- 外部依赖相关逻辑必须通过 Testcontainers 或 MockServer 做可复现集成测试
- Spring Boot 配置类、自动装配和关键 Profile 必须至少有上下文启动测试

---

## 五、门控 3：静态质量与安全

### 5.1 目标

拦截空指针风险、资源泄漏、错误异常处理、线程安全问题、SQL 注入、路径穿越、反序列化风险、日志敏感信息泄露、依赖 CVE 和许可证风险。

### 5.2 工具选型

| 层级 | 工具 | 定位 | 速度 |
|---|---|---|---|
| **L1 快速扫描** | SpotBugs 4.8+ | 字节码级缺陷扫描，覆盖空指针、资源泄漏、并发误用 | 快 |
| **L2 安全规则** | FindSecBugs | SpotBugs 安全插件，覆盖常见 Web 安全漏洞模式 | 快 |
| **L3 企业级平台** | SonarQube 10.x | 质量门禁、重复率、复杂度、安全热点、长期趋势 | 中 |
| **L4 依赖安全** | OWASP Dependency-Check | 基于 NVD/CPE 的第三方依赖 CVE 扫描 | 中 |
| **L5 开源漏洞补充** | OSV-Scanner / Snyk（可选） | 补充 Maven 生态漏洞和供应链风险 | 快 |
| **许可证合规** | License Maven Plugin | 输出依赖许可证清单，拦截不允许许可证 | 快 |

### 5.3 关键检测能力映射

| 问题类型 | 主力工具 | 规则/检查器示例 |
|---|---|---|
| 空指针解引用 | SpotBugs / SonarQube | `NP_NULL_ON_SOME_PATH` |
| 资源未关闭 | SpotBugs / SonarQube | `OS_OPEN_STREAM` |
| 错误字符串比较 | SpotBugs / PMD | `ES_COMPARING_STRINGS_WITH_EQ` |
| 线程安全问题 | SpotBugs | `IS2_INCONSISTENT_SYNC` |
| SQL 注入 | FindSecBugs / SonarQube | `SQL_INJECTION_*` |
| 路径穿越 | FindSecBugs | `PATH_TRAVERSAL_IN` |
| 反序列化风险 | FindSecBugs | `OBJECT_DESERIALIZATION` |
| 日志敏感信息 | SonarQube / 自定义规则 | password/token/idcard 关键字扫描 |
| 依赖 CVE | OWASP Dependency-Check / OSV-Scanner | CVSS / GHSA / CVE 匹配 |

### 5.4 集成方式

- SpotBugs 在 CI 中每次全量运行，`Effort=max`、`Threshold=Low`，输出 XML/SARIF
- FindSecBugs 作为 SpotBugs 插件随 `spotbugs:check` 运行
- SonarQube 在 MR 阶段跑增量扫描，夜间跑主干全量扫描
- OWASP Dependency-Check 在依赖文件变更时强制运行，主干每日刷新漏洞库
- 高危漏洞允许临时豁免时必须记录 CVE、影响范围、到期时间和安全负责人审批

---

## 六、门控 4：接口、契约与数据兼容

### 6.1 目标

拦截 Java 公共 API 签名破坏、Spring HTTP API 契约变化、消费者契约不兼容、序列化协议非兼容变更、数据库迁移脚本破坏性变更和默认语义变化。

### 6.2 工具选型

| 维度 | 工具 | 说明 |
|---|---|---|
| **Java API 兼容** | Revapi / jApiCmp | 对比 jar 的 public/protected API，检测类、方法、字段、泛型签名变化 |
| **HTTP 契约兼容** | OpenAPI Diff | 对比 OpenAPI 规范，拦截路径、方法、参数、响应 schema 的破坏性变更 |
| **契约测试** | Pact JVM | 消费者驱动契约测试，跨服务接口校验 |
| **序列化协议兼容** | buf breaking / protobuf-maven-plugin | 对 `.proto` 字段编号、类型、标签和 service 方法做兼容性检查 |
| **数据库变更** | Liquibase / Flyway Validate | 校验迁移脚本顺序、checksum、禁止修改已发布 migration |
| **版本语义** | SemVer + Maven Versions Plugin | 版本号与 API 兼容性结果联动 |

### 6.3 Java API 兼容性检查流程

```
基线版本（main 分支最新 release jar）
        ↓ Revapi / jApiCmp 对比
当前 MR 构建产物 jar
        ↓
变更分类：
  - Compatible（新增 public API、非破坏性注解补充）→ 通过
  - Potentially Breaking（方法签名、泛型、异常声明、可见性变化）→ 需要确认
  - Breaking（删除类/方法/字段、修改返回类型、收窄可见性）→ 拦截，要求调整或提升主版本号
```

### 6.4 OpenAPI / Protobuf 兼容性规则

**OpenAPI Diff 禁止的变更**：
- 删除已有 path 或 HTTP method
- 删除必需请求参数、修改参数类型或位置
- 将可选字段改为必填字段
- 删除响应字段或修改响应字段类型
- 删除已有响应码或改变错误语义

**Protobuf breaking 禁止的变更**：
- 删除已有字段但未保留 `reserved` 编号和名称
- 修改字段编号（tag number）
- 修改字段类型或 repeated/optional 语义
- 复用已删除字段编号
- 修改 service / rpc 方法签名

---

## 七、工具版本矩阵

| 门控 | 工具 | 推荐最低版本 | 输出格式 | 许可证 |
|---|---|---|---|---|
| 1 | Spotless Maven Plugin | 2.43 | plain / XML | Apache-2.0 |
| 1 | google-java-format | 1.22 | plain | Apache-2.0 |
| 1 | Checkstyle | 10.17 | XML / plain | LGPL-2.1 |
| 1 | PMD | 7.3 | XML / HTML / SARIF | BSD-4 |
| 1 | Error Prone | 2.28 | 编译日志 | Apache-2.0 |
| 2 | JDK | 21 LTS | 编译日志 | GPL-2.0 with CPE |
| 2 | Maven | 3.9 | 构建日志 | Apache-2.0 |
| 2 | Maven Enforcer Plugin | 3.5 | plain | Apache-2.0 |
| 2 | JUnit Jupiter | 5.10 | JUnit XML | EPL-2.0 |
| 2 | Mockito | 5.12 | JUnit XML | MIT |
| 2 | JaCoCo | 0.8.12 | XML / HTML | EPL-2.0 |
| 2 | Testcontainers | 1.20 | JUnit XML | MIT |
| 3 | SpotBugs | 4.8 | XML / SARIF | LGPL-2.1 |
| 3 | FindSecBugs | 1.13 | XML / SARIF | LGPL-3.0 |
| 3 | SonarQube | 10.x | 平台内 / Web API | LGPL（社区版） |
| 3 | OWASP Dependency-Check | 10.x | JSON / XML / HTML / SARIF | Apache-2.0 |
| 3 | OSV-Scanner | 1.8 | JSON / SARIF | Apache-2.0 |
| 4 | Revapi | 0.15+ | JSON / plain | Apache-2.0 |
| 4 | jApiCmp | 0.23+ | XML / HTML | Apache-2.0 |
| 4 | Pact JVM | 4.6+ | Pact JSON / JUnit XML | Apache-2.0 |
| 4 | OpenAPI Diff | 2.1+ | JSON / HTML / Markdown | Apache-2.0 |
| 4 | buf | 1.30+ | JSON | Apache-2.0 |
| 4 | Liquibase / Flyway | 4.x / 10.x | plain / JSON | Apache-2.0 |

---

## 八、门禁阈值建议

### 8.1 分级拦截策略

| 等级 | 定义 | 处理方式 |
|---|---|---|
| **Blocker** | 编译失败、测试失败、API break、契约不兼容、Critical 漏洞、安全高危 CVE | 立即拦截，禁止合入 |
| **Error** | 格式化不通过、Checkstyle/PMD error、SpotBugs 高置信缺陷、覆盖率不达标 | 拦截，需修复或豁免 |
| **Warning** | 静态分析 warning、复杂度升高、重复率升高、非高危依赖漏洞 | 趋势管控，新增即拦截或限期修复 |
| **Info** | 建议性提示、代码风格偏好、低风险重构建议 | 不拦截，仅展示 |

### 8.2 各门控具体阈值

| 门控 | 拦截条件 | 豁免机制 |
|---|---|---|
| **1 代码规范** | Spotless 有 diff → 失败；Checkstyle/PMD violation ≥1 → 失败 | `suppressions.xml` 或局部注解 + Reviewer 确认 |
| **2 语言构建** | 编译失败 → 失败；单测通过率 <100% → 失败；行覆盖率 <70% 或新增行覆盖率 <80% → 失败 | 覆盖率豁免需标注原因并审批 |
| **3 静态质量** | SpotBugs High ≥1 → 失败；FindSecBugs 高危 ≥1 → 失败；Critical/High CVE ≥1 → 失败 | SonarQube 标记 Won't Fix + 安全负责人审批 |
| **4 接口契约** | Revapi/jApiCmp 检测到 breaking change → 失败；OpenAPI Diff breaking → 失败；Pact 契约不通过 → 失败；protobuf breaking → 失败 | breaking change 需提升主版本号并更新迁移文档 |

---

## 九、CI 配置示例（GitLab CI 完整版）

```yaml
variables:
  MAVEN_OPTS: "-Dmaven.repo.local=.m2/repository"
  MAVEN_CLI_OPTS: "-B -U --no-transfer-progress"
  JAVA_TOOL_OPTIONS: "-Dfile.encoding=UTF-8"

stages:
  - lint
  - build
  - test
  - analyze
  - compat

cache:
  paths:
    - .m2/repository

# ── 门控 1：代码规范 ──
lint:format:
  stage: lint
  image: maven:3.9-eclipse-temurin-21
  script:
    - ./mvnw $MAVEN_CLI_OPTS spotless:check

lint:style:
  stage: lint
  image: maven:3.9-eclipse-temurin-21
  script:
    - ./mvnw $MAVEN_CLI_OPTS checkstyle:check pmd:check
  artifacts:
    when: always
    paths:
      - target/checkstyle-result.xml
      - target/pmd.xml

# ── 门控 2：语言、构建与测试 ──
build:compile:
  stage: build
  image: maven:3.9-eclipse-temurin-21
  script:
    - ./mvnw $MAVEN_CLI_OPTS enforcer:enforce clean compile
  artifacts:
    paths:
      - target/

test:unit:
  stage: test
  image: maven:3.9-eclipse-temurin-21
  script:
    - ./mvnw $MAVEN_CLI_OPTS test
  artifacts:
    when: always
    reports:
      junit:
        - target/surefire-reports/*.xml

test:coverage:
  stage: test
  image: maven:3.9-eclipse-temurin-21
  script:
    - ./mvnw $MAVEN_CLI_OPTS verify jacoco:report jacoco:check
  artifacts:
    when: always
    reports:
      junit:
        - target/surefire-reports/*.xml
        - target/failsafe-reports/*.xml
      coverage_report:
        coverage_format: jacoco
        path: target/site/jacoco/jacoco.xml
    paths:
      - target/site/jacoco/

# ── 门控 3：静态质量与安全 ──
analyze:spotbugs:
  stage: analyze
  image: maven:3.9-eclipse-temurin-21
  script:
    - ./mvnw $MAVEN_CLI_OPTS spotbugs:check
  artifacts:
    when: always
    paths:
      - target/spotbugsXml.xml

analyze:dependency:
  stage: analyze
  image: maven:3.9-eclipse-temurin-21
  script:
    - ./mvnw $MAVEN_CLI_OPTS org.owasp:dependency-check-maven:check
  artifacts:
    when: always
    paths:
      - target/dependency-check-report.html
      - target/dependency-check-report.json

analyze:sonar:
  stage: analyze
  image: maven:3.9-eclipse-temurin-21
  script:
    - ./mvnw $MAVEN_CLI_OPTS sonar:sonar
      -Dsonar.projectKey=$CI_PROJECT_NAME
      -Dsonar.coverage.jacoco.xmlReportPaths=target/site/jacoco/jacoco.xml
  allow_failure: true  # MR 阶段可只告警，主干和夜间流水线应强门禁

# ── 门控 4：接口契约与兼容 ──
compat:api:
  stage: compat
  image: maven:3.9-eclipse-temurin-21
  script:
    - ./mvnw $MAVEN_CLI_OPTS -Drevapi.oldArtifacts=$BASELINE_GAV revapi:check

compat:openapi:
  stage: compat
  image: openapitools/openapi-diff:latest
  script:
    - openapi-diff $BASELINE_OPENAPI target/generated/openapi.json --fail-on-incompatible

compat:pact:
  stage: compat
  image: maven:3.9-eclipse-temurin-21
  script:
    - ./mvnw $MAVEN_CLI_OPTS pact:verify

compat:proto:
  stage: compat
  image: bufbuild/buf:1.30
  script:
    - buf breaking proto/ --against ".git#branch=main,subdir=proto"
```

---

## 十、与 OCR 的协作边界

| 门控 | 负责方 | OCR 角色 |
|---|---|---|
| 1-4 | 确定性工具链 | 不介入检查逻辑 |
| 5 Agentic CR | OCR | 语义审查主战场 |
| 1-4 结果增强 | OCR（可选） | 对 SonarQube、SpotBugs、Dependency-Check 告警做语义判断，输出修复建议 |

**核心结论**：门控 1-4 是确定性工程的领地，Java 生态已有成熟的 Maven 插件、静态分析器、安全扫描器和契约校验工具，可以快速、稳定、可复现地完成拦截；OCR 的不可替代价值在门控 5 的语义理解，以及对前四门控结果的语义增强，而非替代确定性检查。
