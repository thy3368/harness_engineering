# 索引与元数据脚本手册

项目级索引/元数据基础设施，包含调用关系生成、数据结构文档生成、结构查询 CLI、调用链路分析工作空间管理，以及一键刷新。

## 一键刷新

```bash
bash scripts/refresh-all.sh
```

执行顺序和依赖链：

```
1. generate_layer_index.ts    → metadata/layer_relations/ (调用关系 CSV)
2. find_head_services.ts      → metadata/layer_relations/head_services.*
   top_ls_services.ts         → (屏幕输出 TOP LS 列表)
3. generate_structure_docs.ts → design2/data_structures/ (文档 + CSV)
4. structdb.py load --force   → design2/data_structures/metadata/struct.db (SQLite)
```

耗时约 30-60 秒。源码变更后运行即可全量刷新。

---

## 1 generate_layer_index.ts — 分层调用关系索引

### 用法

```bash
bun run scripts/generate_layer_index.ts
```

### 输出（metadata/layer_relations/）

| 文件 | 说明 |
|------|------|
| `layer_index_summary.md` | 分层概览 |
| `layer_LS_to_LF.csv` | LS → LF 调用关系 |
| `layer_LF_to_AS.csv` | LF → AS 调用关系 |
| `layer_LF_to_LF.csv` | LF → LF 调用关系 |
| `layer_AS_to_AF.csv` | AS → AF 调用关系 |
| `all_relations_forward.csv` | 全量正查 |
| `all_relations_reverse.csv` | 全量反查 |
| `reverse_AS_called_by.csv` | AS 被谁调用 |
| `reverse_LF_called_by.csv` | LF 被谁调用 |
| `head_services.csv` | 头部服务列表 |

CSV 列：`caller_name,caller_type,caller_file,callee_name,callee_type,callee_file`

---

## 2 generate_call_depth.ts — 调用深度路径追踪

### 用法

```bash
# 打印到屏幕
bun run scripts/generate_call_depth.ts <服务名1> [服务名2] ...

# 输出到文件
bun run scripts/generate_call_depth.ts -o <文件> <服务名1> ...
```

**前置**：需先运行 `generate_layer_index.ts`。

从指定服务出发追踪到 AS 层，输出调用树 + 完整路径 + 统计。

---

## 3 query_layer_calls.ts — 分层调用关系查询

### 用法

```bash
# 正查：该服务调用了谁
bun run scripts/query_layer_calls.ts <服务名> --forward

# 反查：该服务被谁调用
bun run scripts/query_layer_calls.ts <服务名> --reverse
```

**前置**：需先运行 `generate_layer_index.ts`。从 `metadata/layer_relations/` 读取 CSV。

---

## 4 generate_structure_docs.ts — 数据结构文档生成

### 用法

```bash
bun run scripts/generate_structure_docs.ts
```

### 输出

| 输出 | 说明 |
|------|------|
| `design2/data_structures/{域}/ST_*.md` | 39 份子模块文档（622 个结构） |
| `design2/data_structures/_index.md` | 全局索引 |
| `design2/data_structures/metadata/structure_fields.csv` | 13015 行，结构-字段映射 |
| `design2/data_structures/metadata/structure_index.csv` | 1457 行，索引定义 |
| `design2/data_structures/metadata/structure_refs.csv` | 621 行，引用关系 |

---

## 5 structdb.py — 数据结构查询 CLI

### 前置

```bash
python3 scripts/structdb.py load          # 首次构建
python3 scripts/structdb.py load --force  # 强制重建
```

### 命令速查

| 命令 | 用途 | 示例 |
|------|------|------|
| `struct <name>` | 结构详情（字段+索引+引用+服务） | `structdb.py struct uft_cstockinfo` |
| `field <name>` | 字段在哪些结构中使用 | `structdb.py field entrust_direction` |
| `field <name> --like` | 模糊搜索字段名 | `structdb.py field entrust --like` |
| `dict <id>` | 查字典枚举值 | `structdb.py dict 710032` |
| `dict <constant>` | 通过常量名查字典 | `structdb.py dict DICT_ENTDIR_BUY` |
| `dict <kw> --like` | 模糊搜索字典 | `structdb.py dict 行权方式 --like` |
| `dict-value <value> [dict]` | 反向查字典值含义 | `structdb.py dict-value 173 610403` |
| `dict-value <value>` | 在所有字典中查值 | `structdb.py dict-value 173` |
| `errorno <name\|no>` | 查询错误码 | `structdb.py errorno ERR_712222` |
| `errorno <kw> --like` | 模糊搜索错误码 | `structdb.py errorno 冻结 --like` |
| `refs <name>` | 结构引用关系和服务依赖 | `structdb.py refs uft_cfundinfo` |
| `index <name>` | 结构索引定义 | `structdb.py index uft_cstockinfo` |
| `search <kw>` | 全局模糊搜索 | `structdb.py search 期货 --scope struct` |
| `top [--limit N]` | TOP N 被引用最多的结构 | `structdb.py top --limit 10` |
| `stat` | 数据库统计 | `structdb.py stat` |

search 的 `--scope`：`struct` / `field` / `dict` / `errorno` / `all`（默认）

---

## 6 find_head_services.ts / top_ls_services.ts

| 脚本 | 用法 | 说明 |
|------|------|------|
| `find_head_services.ts` | `bun run scripts/find_head_services.ts` | 头部服务列表 → head_services.csv/md |
| `top_ls_services.ts` | `bun run scripts/top_ls_services.ts` | TOP LS 服务列表（屏幕输出） |

**前置**：均依赖 `generate_layer_index.ts` 生成的 `all_relations_forward.csv`。

---

## 7 as_af_mapping.py — 服务目录映射模块

根据服务名（中文前缀）和源码路径，映射到 `design2/` 下的目标文档目录。

### 核心 API

| 函数 | 输入 | 输出 | 用途 |
|------|------|------|------|
| `get_trace_chains_dir(name, src)` | 服务名+源码路径 | `03_equity_权益/secu_现货交易` | 链路文档目录（带中文） |
| `get_full_target_dir(name, src)` | 服务名+源码路径 | `03_equity/secu/xyhgrepurchase` | 服务文档目录（2级或3级） |
| `get_two_level_dir(name, src)` | 服务名+源码路径 | `03_equity/secu` | 2级目录 |
| `get_third_level_dir(name, src)` | 服务名+源码路径 | `xyhgrepurchase` | 3级子目录 |
| `map_service(name, src)` | 服务名+源码路径 | `[domain, subdir]` | 原始映射结果 |

### 映射数据文件（scripts/mapping/）

| 文件 | 条目数 | 用途 |
|------|--------|------|
| `prefix_to_dir.json` | 556 | 中文前缀 → [domain, subdir] |
| `atom_path_to_dir.json` | ~118 | 源码路径前缀 → {domain, subdir} |
| `prefix_third_level.json` | 467 | 2级目录+中文前缀 → 3级子目录 |
| `source_path_third_level.json` | — | 源码路径→3级目录映射规则（最长前缀匹配） |
| `dir_chinese_names.json` | 56 | 域/子目录代码 → 中文名 |
| `flat_dir_keywords.json` | 7 | 扁平目录的关键字分组规则 |

### 映射优先级

2级目录：
1. `prefix_to_dir.json`（中文前缀 → 2级目录）
2. `atom_path_to_dir.json`（源码路径 → 2级目录）

3级目录：
1. `prefix_third_level.json`（中文前缀 → 3级目录）
2. `source_path_third_level.json`（源码路径 → 3级目录，最长前缀匹配）
3. 源码路径 ≥5 段自动拆分
4. `flat_dir_keywords.json`（关键字 → 3级目录，现已支持3级目录路径如 `03_equity/equitypub/_other`）

### CLI 用法

```bash
# 单个映射
python3 scripts/as_af_mapping.py map "AS_期货业务公共_期货资金可用查询"

# 批量映射
python3 scripts/as_af_mapping.py batch engineering/call_depth/workspace/{LS名}/workspace.db

# 覆盖率检查
python3 scripts/as_af_mapping.py coverage

# 生成预览（0字节文件占位）
python3 scripts/as_af_mapping.py preview ~/working/design3_preview
```

---

## 8 call_depth_db.py — 调用链路分析工作空间管理

管理 SQLite 工作空间，用于调用链路文档和服务文档的生成调度。

完整命令参考见 [trace-chain-generation.md](../../.opencode/skill/trace-chain-generation.md) §12 CLI 工具参考，此处仅列出核心命令速查：

```bash
# 初始化工作空间（一条命令完成 init + parse + supplement）
python3 scripts/call_depth_db.py init "LS_xxx" --all

# 从 split_plan.json 注册拆分方案
python3 scripts/call_depth_db.py split [--force]

# 认领服务文档任务（返回 pending→running 的任务列表）
python3 scripts/call_depth_db.py doc-claim --limit 5 [--lf-branch X] [--json] -w <workspace>

# 标记服务文档完成
python3 scripts/call_depth_db.py doc-done --service-name "AS_xxx" -w <workspace>

# 释放 running→pending（崩溃恢复）
python3 scripts/call_depth_db.py doc-release -w <workspace>

# 重新计算 target_dir
python3 scripts/call_depth_db.py remap -w <workspace>

# 查看进度 / 验证完成
python3 scripts/call_depth_db.py progress -w <workspace>
python3 scripts/call_depth_db.py verify -w <workspace>
```

---

## 9 split_chain_docs.py — 链路文档拆分规划

按三层 LF 窗口算法规划调用链文档拆分，纯计算无副作用。

```bash
python3 scripts/split_chain_docs.py <workspace_dir>
# 输入: workspace/call_tree.md
# 输出: workspace/split_plan.json
```

算法：三层LF窗口 + 递归拆分 + 最小分支粒度（<3服务合并）+ LF去重。

---

## 10 目录拥挤分析与映射验证脚本（scripts/dir_split/）

| 脚本 | 用途 | 用法 |
|------|------|------|
| `analyze_crowding.py` | 目录拥挤分析（报告超限目录及贡献前缀/源码路径） | `python3 scripts/dir_split/analyze_crowding.py [--json] [--limit N]` |
| `generate_source_path_rules.py` | 源码路径规则候选生成 | `python3 scripts/dir_split/generate_source_path_rules.py [-o output.json]` |
| `verify_mapping.py` | 映射覆盖率和超限目录验证 | `python3 scripts/dir_split/verify_mapping.py` |

---

## 脚本依赖关系图

```
generate_layer_index.ts
  ├── find_head_services.ts      (依赖 forward CSV)
  ├── top_ls_services.ts         (依赖 forward CSV)
  ├── generate_call_depth.ts     (依赖 forward CSV)
  └── query_layer_calls.ts       (依赖 forward/reverse CSV)

generate_structure_docs.ts       (独立，读 src/uftstructure + src/metadata)
  └── structdb.py load           (依赖 structure_docs 生成的 3 个 CSV)

as_af_mapping.py                 (独立模块，读 mapping/*.json)
  └── call_depth_db.py init/supplement  (动态导入)

call_depth_db.py                 (读 CSV + workspace 文件)
  └── split_chain_docs.py        (读 call_tree.md → 输出 split_plan.json)
```

## 常见场景

| 场景 | 命令 |
|------|------|
| 源码变更后全量刷新 | `bash scripts/refresh-all.sh` |
| 查看 LS 调用链 | `bun run scripts/generate_call_depth.ts <LS名>` |
| 查某 AS 被谁调用 | 查看 `metadata/layer_relations/reverse_AS_called_by.csv` |
| 查结构字段和枚举 | `python3 scripts/structdb.py struct <结构名>` |
| 查字典可选值 | `python3 scripts/structdb.py dict <字典ID>` |
| 只刷新调用关系 | `bun run scripts/generate_layer_index.ts` |
| 只重建结构数据库 | `python3 scripts/structdb.py load --force` |
| 初始化链路分析工作空间 | `python3 scripts/call_depth_db.py init "LS_xxx" --all` |
| 查看链路分析进度 | `python3 scripts/call_depth_db.py progress` |
| 映射服务到目标目录 | `python3 scripts/as_af_mapping.py map "AS_xxx"` |
