
【公共模块】存放提效相关工具，包含：大模型MCP、skill、小工具等

/  
├── 01-skills/                # Claude Code Skills（技能）  
├── 02-agents/                # Agent 配置、工作流、提示词  
├── 03-mcp/                   # MCP 服务、适配器、工具  
├── 04-prompts/               # 通用 Prompt 模板库  
├── 05-templates/             # 研发流程文档模板  
│   ├── 01-requirement/       # 需求规格说明书  
│   ├── 02-design/            # 概要设计 / 详细设计  
│   ├── 03-test/              # 自动化测试分析模板、自动化测试用例模版  

### 01-skills/
- 存放所有 Claude Code Skill 文件夹
- 每个技能一个子目录（直接从 .claude/skills 复制过来）

### 02-agents/
存放各种智能 Agent：
- 自定义 Agent 配置
- 多轮对话工作流
- 角色设定（测试助手、架构师、项目经理等）

### 03-mcp/
MCP 相关资产：
- MCP 适配器
- 服务配置
- 调用示例

### 04-prompts/
高质量通用 Prompt 库：
- 代码生成
- 代码审查
- 文档生成
- 数据处理
- 问题排查

### 05-templates/（文档模板全部放这里）
- 01-requirement：需求规格说明书模板
- 02-design：概要设计文档、详细设计文档
- 03-test：自动化测试分析模板、自动化测试用例模版
