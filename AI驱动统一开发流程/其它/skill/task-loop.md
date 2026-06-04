---
name: task-loop
description: 后台任务循环引擎 — 详见 skills/task-loop/SKILL.md
version: 0.1.0-draft
---

# task-loop

完整方案文档已移至项目级 `skills/task-loop/SKILL.md`。

## 快速参考

- **方案文档**：`skills/task-loop/SKILL.md`
- **daemon入口**：`skills/task-loop/daemon.mjs`（待实现）
- **HTTP API**：`http://127.0.0.1:4080`

## 使用方式

```bash
# 启动daemon
cd skills/task-loop && node daemon.mjs

# 在opencode中查询进度
curl -s http://127.0.0.1:4080/task-loop/status
```
