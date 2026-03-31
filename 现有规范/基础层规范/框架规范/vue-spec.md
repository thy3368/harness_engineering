# Vue 框架规范

## 概述

本规范用于指导 Vue 项目开发，统一代码风格和最佳实践。

## 技术栈

| 技术 | 版本 | 说明 |
|------|------|------|
| Vue | ^3.4 | 推荐使用 Composition API |
| TypeScript | ^5.0 | 强类型支持 |
| Vite | ^5.0 | 构建工具 |
| Pinia | ^2.1 | 状态管理 |
| Vue Router | ^4.2 | 路由管理 |

## 项目结构

```
src/
├── assets/           # 静态资源
├── components/       # 公共组件
│   └── Basic/        # 基础组件
├── composables/      # 组合式函数
├── layouts/          # 布局组件
├── router/           # 路由配置
├── services/         # API 服务
├── stores/           # Pinia 状态管理
├── types/            # TypeScript 类型定义
├── utils/            # 工具函数
└── views/            # 页面组件
```

## 组件规范

### 组件命名

| 规则 | 说明 | 示例 |
|------|------|------|
| 组件文件名 | 使用 PascalCase | `UserProfile.vue` |
| 基础组件 | 添加前缀 `Base` | `BaseButton.vue` |
| 业务组件 | 使用业务前缀 | `OrderList.vue` |
| 组件属性 | 使用 camelCase | `userName` |

### 组件结构

```vue
<script setup lang="ts">
// 1. 导入
import { ref, computed } from 'vue'
import type { PropType } from 'vue'

// 2. 类型定义
interface Props {
  title: string
  data?: Item[]
}

// 3. Props 定义
const props = withDefaults(defineProps<Props>(), {
  data: () => []
})

// 4. Emits 定义
const emit = defineEmits<{
  (e: 'update', value: string): void
  (e: 'delete', id: number): void
}>()

// 5. 响应式数据
const count = ref(0)

// 6. 计算属性
const doubled = computed(() => count.value * 2)

// 7. 方法
function handleClick() {
  emit('update', 'new value')
}
</script>

<template>
  <div class="component-name">
    <!-- 模板内容 -->
  </div>
</template>

<style scoped>
.component-name {
  /* 组件样式 */
}
</style>
```

### Props 定义

| 规则 | 说明 |
|------|------|
| 类型必须 | 使用 TypeScript 类型定义，禁止使用 `any` |
| 默认值 | 使用 `withDefaults` 提供默认值 |
| 必填标记 | 必填属性不提供默认值 |
| 验证函数 | 复杂验证使用 validator |

```typescript
// ✅ 正确
const props = defineProps<{
  title: string
  count?: number
  status: 'pending' | 'success' | 'error'
}>()

// ❌ 错误
const props = defineProps({
  title: String,
  count: Number
})
```

## 状态管理

### Store 命名

| 规则 | 说明 |
|------|------|
| 命名方式 | 使用 `useXxxStore` 格式 |
| 文件命名 | `xxx.ts` 格式 |
| 模块管理 | 按业务模块划分 |

### Store 结构

```typescript
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useUserStore = defineStore('user', () => {
  // 状态
  const userInfo = ref<UserInfo | null>(null)
  const loading = ref(false)

  // 计算属性
  const isLoggedIn = computed(() => !!userInfo.value)

  // Actions
  async function fetchUserInfo() {
    loading.value = true
    try {
      const data = await getUserInfo()
      userInfo.value = data
    } finally {
      loading.value = false
    }
  }

  function logout() {
    userInfo.value = null
  }

  return {
    userInfo,
    loading,
    isLoggedIn,
    fetchUserInfo,
    logout
  }
})
```

## 路由规范

### 路由配置

```typescript
const routes = [
  {
    path: '/user',
    name: 'User',
    component: () => import('@/views/UserLayout.vue'),
    children: [
      {
        path: 'profile',
        name: 'UserProfile',
        component: () => import('@/views/UserProfile.vue'),
        meta: { title: '个人中心' }
      }
    ]
  }
]
```

### 路由守卫

| 守卫 | 说明 |
|------|------|
| beforeEach | 权限验证、登录跳转 |
| beforeResolve | 导航确认 |
| afterEach | 页面统计 |

## API 服务

### 请求封装

```typescript
// services/request.ts
import axios from 'axios'

const request = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
  timeout: 10000
})

// 请求拦截
request.interceptors.request.use(
  (config) => {
    const token = useUserStore().token
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error) => Promise.reject(error)
)

// 响应拦截
request.interceptors.response.use(
  (response) => response.data,
  (error) => {
    const { response } = error
    if (response?.status === 401) {
      // 处理未授权
    }
    return Promise.reject(error)
  }
)

export default request
```

### API 模块化

```typescript
// services/user.ts
import request from './request'
import type { UserInfo } from '@/types/user'

export function getUserInfo(): Promise<UserInfo> {
  return request.get('/user/info')
}

export function updateUser(data: Partial<UserInfo>): Promise<void> {
  return request.put('/user/update', data)
}
```

## 样式规范

### CSS 命名

| 规则 | 说明 |
|------|------|
| 命名方式 | 使用 BEM 或模块化 CSS |
| 作用域 | 必须使用 `scoped` |
| 预处理器 | 推荐使用 SCSS |

```vue
<template>
  <div class="user-card">
    <div class="user-card__avatar"></div>
    <div class="user-card__info">
      <span class="user-card__name"></span>
    </div>
  </div>
</template>

<style scoped>
.user-card {
  &__avatar {
    width: 48px;
    height: 48px;
  }
  
  &__info {
    margin-top: 8px;
  }
  
  &__name {
    font-weight: 500;
  }
}
</style>
```

### 全局样式

| 规则 | 说明 |
|------|------|
| 变量 | 在 `variables.scss` 定义全局变量 |
| 重置 | 在 `reset.scss` 定义基础重置样式 |
| 字体 | 使用系统字体或预定义字体栈 |

## 性能优化

### 组件优化

| 优化点 | 说明 |
|--------|------|
| 路由懒加载 | 使用 `() => import()` 动态导入 |
| 组件懒加载 | 使用 `defineAsyncComponent` |
| v-show | 频繁切换使用 v-show |
| v-memo | 列表渲染使用 v-memo |

### 响应式数据

| 规则 | 说明 |
|------|------|
| 深层响应 | 谨慎使用 `reactive`，优先使用 `ref` |
| 浅层响应 | 大列表使用 `shallowRef` |
| 计算缓存 | 复杂计算使用 `computed` |

## 最佳实践

### Do's

| 规则 | 说明 |
|------|------|
| 使用 TypeScript | 始终使用类型定义 |
| 使用 Composition API | 推荐使用 `<script setup>` |
| 组件拆分 | 保持组件职责单一 |
| 注释复杂逻辑 | 添加必要的代码注释 |

### Don'ts

| 规则 | 说明 |
|------|------|
| 直接修改 props | 使用 emit 通知父组件 |
| 使用 any | 使用具体的类型定义 |
| 魔法数字 | 使用常量替代 |
| 全局状态滥用 | 合理使用 Pinia |

## 相关文档

- [Vue 官方文档](https://vuejs.org/)
- [Vue TypeScript 指南](https://vuejs.org/guide/typescript/overview.html)
- [Pinia 文档](https://pinia.vuejs.org/)
- [Vue Router 文档](https://router.vuejs.org/)
