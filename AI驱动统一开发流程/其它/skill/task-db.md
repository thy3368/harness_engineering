# task-db CLI使用手册

任务队列管理工具，用于跟踪文档生成和目录探查的进度。

## 路径

- **二进制**：`~/agent/tools/bin/task-db`
- 数据库通过 `--db <path>` 指定

## 命令

### 通用

| 命令 | 说明 |
|------|------|
| `task-db init --db <path>` | 建表（幂等） |
| `task-db progress [--module xxx] --db <path>` | 按模块聚合进度 |

### doc阶段

| 命令 | 说明 |
|------|------|
| `task-db doc-add --input docs.json --db <path>` | 批量添加doc记录 |
| `task-db doc-claim --limit N --module xxx --batch-id xxx --db <path>` | 认领N条pending→running |
| `task-db doc-complete --module xxx --source-file xxx --status done --db <path>` | 单条更新状态 |
| `task-db doc-batch-complete --input results.json --db <path>` | 批量更新状态（需写文件） |

### plan阶段

| 命令 | 说明 |
|------|------|
| `task-db plan-add --input plans.json --db <path>` | 批量添加plan记录 |
| `task-db plan-claim --db <path>` | 认领1条pending→running |
| `task-db plan-complete --id N --db <path>` | 标记plan为done |

### 维护

| 命令 | 说明 |
|------|------|
| `task-db reset-stale --db <path>` | 重置所有running为pending |

## 输入格式

### doc-add
```json
[{"source_type":"LF","domain":"equity","module":"xxx","source_file":"lf_xxx","source_path":"src/.../lf_xxx.uftfunction","output_path":"design/.../","publisher":"opencode"}]
```
- source_type：lf_开头→LF，ls_开头→LS
- 必须写JSON文件再用--input传入，不支持stdin

### plan-add
```json
[{"domain":"equity","module":"xxx","task_desc":"子目录探查","scope":"src/.../子目录/","publisher":"opencode"}]
```

## 递归目录探索场景

子agent收到一个plan后，只做3步：

1. **统计文件数**：`find scope目录 -name "*.uftfunction" -o -name "*.uftservice"` 统计含所有子目录的文件总数
2. **判断并执行**：
   - 文件数 ≤ 30：doc-add为所有文件创建doc_tasks → plan-complete
   - 文件数 > 30 且有子目录：为每个直接子目录plan-add创建子plan → plan-complete
   - 文件数 > 30 但无子目录（扁平大目录）：doc-add → plan-complete
3. **结束**

主session循环：claim 5~6条 → 并行spawn子agent → 等完成 → 再claim

## 注意事项

- **唯一键是(module, source_file)**，doc-claim和doc-complete必须带--module
- **doc-batch-complete不支持stdin**，必须用--input指定文件路径
