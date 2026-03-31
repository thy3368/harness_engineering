---
description: "AI Coding Rules - C++ 单元测试规范"
globs: "*.cpp,*.hpp,*.cc"
alwaysApply: false
version: 1.0.1
author: 架构办
created: 2025-11-3
lastUpdated: 2025-11-3
---

# C++ 单元测试规范

## 概述

本规范为 C++ 项目单元测试的标准规范，规定了测试框架选择、测试结构、测试编写等方面的要求。

## 测试框架要求

### 推荐框架

| 框架 | 说明 | 特点 |
|------|------|------|
| **Google Test (gtest)** | Google 开源测试框架 | 功能强大，支持 Mock，广泛使用 |
| **Catch2** | 现代 C++ 测试框架 | 头文件-only，语法简洁，性能优秀 |
| **doctest** | 轻量级测试框架 | 头文件-only，与代码共存 |

### 技术栈

| 组件 | 说明 |
|------|------|
| 测试框架 | Google Test 1.12+ 或 Catch2 3.x |
| Mock 框架 | Google Mock (gmock) 或 Trompeloeil |
| 内存检测 | Valgrind / AddressSanitizer |

### 依赖配置

#### Google Test (CMake)

```cmake
# FetchContent 方式
include(FetchContent)
FetchContent_Declare(
    googletest
    GIT_REPOSITORY https://github.com/google/googletest.git
    GIT_TAG release-1.12.1
)
FetchContent_MakeAvailable(googletest)

enable_testing()
add_executable(tests test_main.cpp ${TEST_SOURCES})
target_link_libraries(tests gtest gmock)
add_test(NAME tests COMMAND tests)
```

#### Catch2 (CMake)

```cmake
FetchContent_Declare(
    catch2
    GIT_REPOSITORY https://github.com/catchorg/Catch2.git
    GIT_TAG v3.4.0
)
FetchContent_MakeAvailable(catch2)

target_link_libraries(tests Catch2::Catch2WithMain)
```

## 测试目录结构

### 标准目录

| 目录 | 说明 |
|------|------|
| `tests/` | 测试代码根目录 |
| `tests/unit/` | 单元测试 |
| `tests/integration/` | 集成测试 |
| `tests/fixtures/` | 测试固件 |
| `tests/mocks/` | Mock 对象 |

### 目录示例

```
project/
├── src/
│   ├── user_service.cpp
│   └── user_service.h
├── tests/
│   ├── unit/
│   │   ├── user_service_test.cpp
│   │   ├── user_service_test.h
│   │   └── mocks/
│   │       └── mock_user_repository.h
│   ├── integration/
│   │   └── user_service_integration_test.cpp
│   └── fixtures/
│       └── test_data.h
└── CMakeLists.txt
```

## 测试类命名规范

### 命名规则

| 类型 | 规则 | 示例 |
|------|------|------|
| 测试类 | `[被测类名]Test` | `UserServiceTest` |
| 测试 fixture | `[被测类名]Fixture` | `UserServiceFixture` |
| Mock 类 | `Mock[被测类名]` | `MockUserRepository` |
| 参数化测试 | `[被测类名]ParamTest` | `UserServiceParamTest` |

### 测试方法命名

| 规则 | 说明 |
|------|------|
| **强制** | 使用 `TEST` 或 `TEST_F` 宏定义 |
| **强制** | 方法名描述测试场景 |
| **推荐** | 使用 `test[场景][expected]` 格式 |

### 方法命名示例

```cpp
// Google Test
TEST(UserServiceTest, Save_WithValidUser_ReturnsSuccess) {}
TEST(UserServiceTest, Save_WithNullUser_ThrowsException) {}
TEST(UserServiceTest, FindById_UserExists_ReturnsUser) {}
TEST_F(UserServiceFixture, Save_WithTransaction_CommitsSuccessfully) {}

// Catch2
TEST_CASE("UserService: Save with valid user returns success") {}
TEST_CASE("UserService: Save with null user throws exception") {}
TEST_CASE_METHOD(UserServiceFixture, "UserService: Find by id", "[user]") {}
```

## Google Test 规范

### 基本测试

```cpp
#include <gtest/gtest.h>

// 基本测试
TEST(TestSuiteName, TestName) {
    // Arrange
    int expected = 42;
    
    // Act
    int actual = calculate();
    
    // Assert
    EXPECT_EQ(expected, actual);
}
```

### Test Fixture

```cpp
class UserServiceTest : public ::testing::Test {
protected:
    void SetUp() override {
        // 初始化
        userService = std::make_unique<UserService>(mockRepo);
    }
    
    void TearDown() override {
        // 清理
        userService.reset();
    }
    
    std::unique_ptr<UserService> userService;
    std::shared_ptr<MockUserRepository> mockRepo;
};

TEST_F(UserServiceTest, Save_WithValidUser_ReturnsSuccess) {
    // Given
    User user("testuser", "test@example.com");
    EXPECT_CALL(*mockRepo, save(_)).WillOnce(Return(true));
    
    // When
    bool result = userService->save(user);
    
    // Then
    EXPECT_TRUE(result);
}
```

### 参数化测试

```cpp
class IsPrimeTest : public ::testing::TestWithParam<int> {};

INSTANTIATE_TEST_SUITE_P(PrimeValues, IsPrimeTest,
    ::testing::Values(2, 3, 5, 7, 11, 13, 17, 19, 23, 29));

TEST_P(IsPrimeTest, ReturnsTrueForPrimeNumbers) {
    EXPECT_TRUE(IsPrime(GetParam()));
}
```

### 异常测试

```cpp
TEST(UserServiceTest, Save_WithNullUser_ThrowsException) {
    EXPECT_THROW(
        userService->save(nullptr),
        std::invalid_argument
    );
}

TEST(UserServiceTest, Save_WithInvalidEmail_ThrowsException) {
    EXPECT_THROW(
        userService->save(User("user", "invalid-email")),
        std::invalid_argument
    );
}
```

## Catch2 规范

### 基本测试

```cpp
#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>

TEST_CASE("Calculator: addition", "[calculator]") {
    Calculator calc;
    REQUIRE(calc.add(2, 3) == 5);
}

TEST_CASE("Calculator: division by zero throws", "[calculator]") {
    Calculator calc;
    REQUIRE_THROWS_AS(calc.divide(1, 0), std::invalid_argument);
}
```

### Section 语法

```cpp
TEST_CASE("Vector operations") {
    std::vector<int> vec = {1, 2, 3};
    
    SECTION("push_back increases size") {
        vec.push_back(4);
        REQUIRE(vec.size() == 4);
    }
    
    SECTION("empty vector is empty") {
        std::vector<int> empty;
        REQUIRE(empty.empty());
    }
}
```

### Fixture

```cpp
struct UserServiceFixture {
    std::unique_ptr<UserService> service;
    std::shared_ptr<MockUserRepository> repo;
    
    UserServiceFixture() {
        repo = std::make_shared<MockUserRepository>();
        service = std::make_unique<UserService>(repo);
    }
};

TEST_CASE_METHOD(UserServiceFixture, "UserService: save valid user", "[user]") {
    User user("test", "test@example.com");
    REQUIRE(service->save(user) == true);
}
```

## Mock 使用规范

### Google Mock 基本使用

```cpp
#include <gmock/gmock.h>
#include <gtest/gtest.h>

class MockUserRepository : public UserRepository {
public:
    MOCK_METHOD(bool, save, (const User& user), (override));
    MOCK_METHOD(std::optional<User>, findById, (int id), (override));
    MOCK_METHOD(bool, remove, (int id), (override));
};

TEST(UserServiceTest, Save_CallsRepository) {
    // Arrange
    MockUserRepository mockRepo;
    UserService service(&mockRepo);
    User user("test", "test@example.com");
    
    EXPECT_CALL(mockRepo, save(_)).WillOnce(Return(true));
    
    // Act
    bool result = service.save(user);
    
    // Assert
    EXPECT_TRUE(result);
}
```

### Mock 行为设置

```cpp
// 返回值
EXPECT_CALL(mock, method(_)).WillOnce(Return(value));
EXPECT_CALL(mock, method(_)).WillRepeatedly(Return(value));

// 抛出异常
EXPECT_CALL(mock, method(_)).WillOnce(Throw(std::runtime_error("error")));

// 调用函数
EXPECT_CALL(mock, process(_)).WillOnce Invoke([](const User& u) {
    // 处理逻辑
});

// 参数匹配
EXPECT_CALL(mock, save(An<const User&>())).WillOnce(Return(true));
EXPECT_CALL(mock, findById(Gt(0))).WillOnce(Return(User()));
```

## 断言规范

### Google Test 断言

| 断言 | 说明 |
|------|------|
| `EXPECT_EQ(a, b)` | 相等 |
| `EXPECT_NE(a, b)` | 不等 |
| `EXPECT_TRUE(a)` | 真 |
| `EXPECT_FALSE(a)` | 假 |
| `EXPECT_STREQ(a, b)` | 字符串相等 |
| `EXPECT_FLOAT_EQ(a, b)` | 浮点数近似相等 |
| `EXPECT_DOUBLE_EQ(a, b)` | 双精度浮点数近似相等 |
| `EXPECT_THROW(code, exception_type)` | 抛出异常 |
| `EXPECT_ANY_THROW(code)` | 抛出任何异常 |
| `EXPECT_NO_THROW(code)` | 不抛出异常 |

### Catch2 断言

| 断言 | 说明 |
|------|------|
| `REQUIRE(expr)` | 致命断言（失败终止测试） |
| `CHECK(expr)` | 非致命断言（失败继续） |
| `REQUIRE_EQ(a, b)` | 相等 |
| `REQUIRE_NE(a, b)` | 不等 |
| `REQUIRE_THROWS(code)` | 抛出异常 |
| `REQUIRE_THROWS_AS(code, type)` | 抛出特定类型异常 |
| `REQUIRE_FALSE(expr)` | 表达式为假 |

### 断言示例

```cpp
// 基本断言
EXPECT_EQ(user.getId(), 1);
EXPECT_STREQ(user.getName(), "test");
EXPECT_TRUE(user.isActive());

// 浮点数断言
EXPECT_DOUBLE_EQ(calculate(), 3.14159);

// 集合断言
ASSERT_FALSE(users.empty());
ASSERT_EQ(users.size(), 3);

// 智能指针断言
ASSERT_THAT(pointers, ElementsAre(Pointee(1), Pointee(2)));
```

## 测试数据管理

### 测试固件

```cpp
struct TestData {
    static User createValidUser() {
        return User(1, "testuser", "test@example.com");
    }
    
    static User createUserWithNullEmail() {
        return User(1, "testuser", "");
    }
    
    static std::vector<User> createUserList(int count) {
        std::vector<User> users;
        for (int i = 0; i < count; ++i) {
            users.emplace_back(i, "user" + std::to_string(i), "user" + std::to_string(i) + "@test.com");
        }
        return users;
    }
};
```

### 数据原则

| 规则 | 说明 |
|------|------|
| **强制** | 测试数据与生产数据隔离 |
| **强制** | 每个测试独立准备数据 |
| **强制** | 测试后清理资源 |
| **推荐** | 使用 RAII 管理资源 |

## 测试分类

### 单元测试

| 规则 | 说明 |
|------|------|
| **强制** | 测试单个类或函数 |
| **强制** | 使用 Mock 隔离依赖 |
| **强制** | 快速执行 |
| **强制** | 无外部依赖 |

### 集成测试

| 规则 | 说明 |
|------|------|
| **强制** | 测试多个组件交互 |
| **强制** | 使用真实数据库（测试环境） |
| **强制** | 测试前后清理数据 |

### 内存测试

```cpp
// 使用 AddressSanitizer
// CMake: -fsanitize=address -g

TEST(MemoryTest, NoMemoryLeaks) {
    // 分配内存
    auto* ptr = new char[100];
    
    // 使用...
    
    // 释放（测试结束自动检测）
    delete[] ptr;
}
```

## 性能测试

### 时间限制

```cpp
TEST_P(PerformanceTest, BatchOperation_CompletesInTime) {
    std::vector<int> data = generateData(10000);
    
    auto start = std::chrono::high_resolution_clock::now();
    processor.batchProcess(data);
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(
        std::chrono::high_resolution_clock::now() - start
    );
    
    EXPECT_LT(duration.count(), 5000);  // 5秒内完成
}
```

### 基准测试

```cpp
// Google Benchmark
#include <benchmark/benchmark.h>

static void BM_SortVector(benchmark::State& state) {
    std::vector<int> data = generateRandomData(state.range(0));
    for (auto _ : state) {
        std::sort(data.begin(), data.end());
    }
}
BENCHMARK(BM_SortVector)->Range(1 << 10, 1 << 20);
BENCHMARK_MAIN();
```

## 禁止行为

| 规则 | 说明 |
|------|------|
| **禁止** | 在测试中使用生产环境数据 |
| **禁止** | 在测试中进行真实的网络通信 |
| **禁止** | 在测试中操作生产数据库 |
| **禁止** | 编写没有断言的测试 |
| **禁止** | 测试之间相互依赖 |
| **禁止** | 忽略测试失败 |
| **禁止** | 使用 `new` 后不配对 `delete` |
| **禁止** | 在测试中硬编码路径 |
| **禁止** | 测试中包含耗时操作 |

## CI/CD 集成

### CMake 配置

```cmake
# 启用测试
enable_testing()

# 添加测试
add_test(NAME unit_tests COMMAND tests)

# 生成测试报告
add_custom_command(TARGET tests POST_BUILD
    COMMAND ${CMAKE_CTEST_COMMAND} --output-on-failure
)
```

### GitLab CI 示例

```yaml
test:
  script:
    - mkdir build && cd build
    - cmake .. -DCMAKE_CXX_FLAGS="-Wall -Wextra"
    - make
    - ctest --output-on-failure --junit-xml=report.xml
  artifacts:
    reports:
      junit: report.xml
```

## 版本历史

| 版本 | 日期 | 修改内容 | 作者 |
|------|------|----------|------|
| 1.0.1 | 2025-11-3 | 初始版本，参考 AAA/GWT/Clean Architecture | 架构办 |

---

> 更多通用规范请参阅：[单元测试通用规范](./unit-test-spec.md)
