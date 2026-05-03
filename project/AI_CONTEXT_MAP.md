# AI Context Map

本文件定义当前项目中不同任务场景应该加载哪些上下文文件。

它的目标是避免两种问题：

1. 上下文不足：AI 缺少关键信息，开始脑补。
2. 上下文过载：AI 一次读太多无关内容，注意力分散。

AI 在处理任务前，应根据任务类型选择最小必要上下文。

---

## 1. Context Loading Principle

### 1.1 Progressive Disclosure

不要默认读取所有文件。

优先按需加载：

```text
系统规则
→ 项目上下文
→ 相关 skill
→ 相关 template
→ 相关 checklist
→ 相关源码
→ 相关任务记录
```

### 1.2 Smallest Sufficient Context

选择足以完成当前阶段的最小上下文。

例如：

- 澄清想法时，不需要读取所有测试 checklist。
- 审计 diff 时，必须读取 review template 和 security/testing checklist。
- 编程执行时，必须读取 agent rules 和任务包。

### 1.3 Evidence Priority

上下文优先级：

```text
当前仓库真实代码
→ 当前项目 AI_REPO_CONTEXT
→ 当前项目 AI_DOMAIN_CONTEXT
→ 当前任务包
→ 已合并决策记录
→ 历史项目记忆
→ 通用系统规则
→ 模型常识
```

模型常识不能覆盖项目事实。

---

## 2. Core Context Files

| File | Purpose | Load When |
|---|---|---|
| `.ai/START_HERE.md` | 系统入口说明 | 第一次进入项目，或不确定如何开始 |
| `.ai/system/AI_MASTER_PROMPT.md` | 军师/调度器总规则 | 军师模型处理任何复杂任务 |
| `.ai/system/AI_AGENT_RULES.md` | 编程智能体执行规则 | 任何代码修改前 |
| `.ai/system/AI_OPERATING_MODES.md` | 工作模式定义 | 判断当前该进入哪个模式 |
| `.ai/system/AI_DELIVERY_WORKFLOW.md` | 完整交付生命周期 | 规划复杂任务或设计流程时 |
| `.ai/project/AI_REPO_CONTEXT.md` | 项目事实地图 | 几乎所有项目相关任务 |
| `.ai/project/AI_DOMAIN_CONTEXT.md` | 领域语言和术语 | 涉及业务概念、命名、用户沟通时 |
| `.ai/project/AI_PROJECT_MEMORY.md` | 长期项目记忆 | 需要了解历史决策、技术债、长期约定时 |

---

## 3. Scenario-based Context Loading

### 3.1 New Project Initialization

当项目刚安装 AI Engineering Delivery OS 时，读取：

```text
.ai/START_HERE.md
.ai/system/AI_MASTER_PROMPT.md
.ai/system/AI_DELIVERY_WORKFLOW.md
.ai/project/AI_REPO_CONTEXT.md
.ai/project/AI_DOMAIN_CONTEXT.md
.ai/project/AI_CONTEXT_MAP.md
.ai/project/AI_PROJECT_MEMORY.md
```

目标：

- 扫描仓库。
- 生成项目画像。
- 生成领域词典。
- 标注未知点。

不要读取：

- 所有 skill。
- 所有 references。
- 所有 templates。

---

### 3.2 User Has a Raw Idea

用户说：

```text
我有一个想法……
我感觉这里是不是应该……
未来能不能……
```

读取：

```text
.ai/system/AI_MASTER_PROMPT.md
.ai/system/AI_OPERATING_MODES.md
.ai/project/AI_REPO_CONTEXT.md
.ai/project/AI_DOMAIN_CONTEXT.md
.ai/skills/idea-to-clarity/SKILL.md
```

如果涉及现有代码影响，再读取：

```text
.ai/skills/grill-with-repo/SKILL.md
```

输出：

- 需求成熟度。
- 真实问题。
- 假设。
- Not Doing。
- 是否需要继续进入 Spec / Plan。

---

### 3.3 Need to Grill / Challenge a Requirement

读取：

```text
.ai/system/AI_MASTER_PROMPT.md
.ai/project/AI_REPO_CONTEXT.md
.ai/project/AI_DOMAIN_CONTEXT.md
.ai/skills/grill-with-repo/SKILL.md
```

可选读取：

```text
.ai/references/ANTI_OVERENGINEERING_RULES.md
.ai/references/SECURITY_CHECKLIST.md
```

适用场景：

- 用户想法边界不清。
- 需求可能有安全/权限风险。
- 需求可能过度设计。
- 用户要求“挑刺”。

---

### 3.4 Need PRD / RFC / Spec

读取：

```text
.ai/system/AI_DELIVERY_WORKFLOW.md
.ai/project/AI_REPO_CONTEXT.md
.ai/project/AI_DOMAIN_CONTEXT.md
.ai/skills/spec-before-code/SKILL.md
.ai/templates/PRD_TEMPLATE.md
.ai/templates/RFC_TEMPLATE.md
```

如果涉及重大架构决策，额外读取：

```text
.ai/templates/ADR_TEMPLATE.md
.ai/project/AI_PROJECT_MEMORY.md
```

---

### 3.5 Need Task Breakdown

读取：

```text
.ai/skills/plan-to-slices/SKILL.md
.ai/templates/ISSUE_SLICE_TEMPLATE.md
.ai/templates/TASK_PACKAGE_TEMPLATE.md
.ai/project/AI_REPO_CONTEXT.md
```

输出：

- Vertical slices。
- HITL / AFK 分类。
- 依赖顺序。
- 每个 slice 验收标准。

---

### 3.6 Need Coding Agent Prompt

读取：

```text
.ai/system/AI_AGENT_RULES.md
.ai/skills/execution-prompt-compiler/SKILL.md
.ai/templates/TASK_PACKAGE_TEMPLATE.md
.ai/project/AI_REPO_CONTEXT.md
.ai/project/AI_DOMAIN_CONTEXT.md
```

如果任务涉及特定领域，读取相关任务文档：

```text
.ai/tasks/<task-name>/
```

输出：

- 可直接复制给编程智能体的执行 Prompt。

---

### 3.7 Coding Agent Execution

编程智能体必须读取：

```text
.ai/START_HERE.md
.ai/system/AI_AGENT_RULES.md
.ai/project/AI_REPO_CONTEXT.md
.ai/project/AI_DOMAIN_CONTEXT.md
.ai/tasks/<current-task>/04-exec-prompt.md
```

如果涉及数据库，额外读取：

```text
.ai/references/DATABASE_MIGRATION_CHECKLIST.md
```

如果涉及 API，额外读取：

```text
.ai/references/API_INTERFACE_CHECKLIST.md
```

如果涉及前端，额外读取：

```text
.ai/references/FRONTEND_UX_CHECKLIST.md
```

如果涉及安全，额外读取：

```text
.ai/references/SECURITY_CHECKLIST.md
```

---

### 3.8 Need Tests / Verification

读取：

```text
.ai/skills/tdd-feedback-loop/SKILL.md
.ai/templates/FEEDBACK_LOOP_TEMPLATE.md
.ai/references/TESTING_CHECKLIST.md
.ai/project/AI_REPO_CONTEXT.md
```

输出：

- 测试策略。
- 自动测试路径。
- 手动验证路径。
- pass/fail 信号。

---

### 3.9 Bug / Error / Failed Test

读取：

```text
.ai/skills/diagnose-bug/SKILL.md
.ai/templates/FEEDBACK_LOOP_TEMPLATE.md
.ai/project/AI_REPO_CONTEXT.md
```

如涉及安全或权限：

```text
.ai/references/SECURITY_CHECKLIST.md
```

输出：

- 复现路径。
- 最小问题场景。
- 假设。
- 证据。
- 修复计划。
- regression test 建议。

---

### 3.10 Review Diff / PR / Implementation Summary

读取：

```text
.ai/skills/review-quality-gate/SKILL.md
.ai/templates/REVIEW_REPORT_TEMPLATE.md
.ai/system/AI_AGENT_RULES.md
.ai/project/AI_REPO_CONTEXT.md
.ai/project/AI_DOMAIN_CONTEXT.md
```

根据改动类型额外读取：

```text
.ai/references/SECURITY_CHECKLIST.md
.ai/references/TESTING_CHECKLIST.md
.ai/references/PERFORMANCE_CHECKLIST.md
.ai/references/API_INTERFACE_CHECKLIST.md
.ai/references/DATABASE_MIGRATION_CHECKLIST.md
.ai/references/FRONTEND_UX_CHECKLIST.md
.ai/references/ANTI_OVERENGINEERING_RULES.md
```

输出：

```text
Verdict: PASS / NEEDS_FIX / REJECT
```

---

### 3.11 Architecture Deepening / Technical Debt

读取：

```text
.ai/skills/architecture-deepening/SKILL.md
.ai/project/AI_REPO_CONTEXT.md
.ai/project/AI_PROJECT_MEMORY.md
.ai/references/ANTI_OVERENGINEERING_RULES.md
```

如果涉及重大决策：

```text
.ai/templates/ADR_TEMPLATE.md
```

输出：

- 模块边界分析。
- 技术债分类。
- 重构触发条件。
- 不建议现在做的内容。
- ADR 建议。

---

### 3.12 Ship and Record

读取：

```text
.ai/skills/ship-and-record/SKILL.md
.ai/templates/SHIP_REPORT_TEMPLATE.md
.ai/project/AI_PROJECT_MEMORY.md
.ai/project/AI_DOMAIN_CONTEXT.md
.ai/templates/ADR_TEMPLATE.md
```

输出：

- Ship Report。
- Project Memory 更新建议。
- Domain Context 更新建议。
- ADR 建议。
- Changelog 条目。

---

## 4. Context by Task Type

| Task Type | Must Read | Optional Read |
|---|---|---|
| 新功能 | Repo Context, Domain Context, Spec, Plan, Task Template | API / DB / Security / UX checklists |
| Bug 修复 | Repo Context, Diagnose Skill, Feedback Loop | Testing / Security checklist |
| 前端改动 | Repo Context, Domain Context, Frontend UX Checklist | API Checklist |
| 后端 API | Repo Context, API Checklist, Security Checklist | Testing Checklist |
| 数据库改动 | Repo Context, DB Migration Checklist | Performance Checklist |
| 权限改动 | Repo Context, Security Checklist | Review Quality Gate |
| 文件/导出 | Repo Context, Security Checklist, Performance Checklist | Storage-related project notes |
| 架构重构 | Repo Context, Project Memory, Architecture Skill | ADR Template |
| PR 审计 | Review Skill, Review Template, Agent Rules | Relevant checklists |

---

## 5. Context Freshness Rules

### 5.1 When to refresh repo context

需要刷新 `AI_REPO_CONTEXT.md` 的情况：

- 大量文件结构变化。
- 新增核心模块。
- 删除旧模块。
- 数据库或权限模型变化。
- 部署方式变化。
- 项目技术栈变化。

### 5.2 When to refresh domain context

需要刷新 `AI_DOMAIN_CONTEXT.md` 的情况：

- 新增业务术语。
- 用户纠正术语含义。
- 旧术语废弃。
- 页面名称、功能名称、角色名称变化。

### 5.3 When to refresh project memory

需要刷新 `AI_PROJECT_MEMORY.md` 的情况：

- 完成重大任务。
- 形成长期架构约定。
- 产生延期技术债。
- 拒绝某个重要方案。
- 做出不可逆或难逆转决策。

---

## 6. Context Noise Control

不要把以下内容放入长期上下文：

- 一次性聊天过程。
- 临时错误信息。
- 已解决且无长期价值的小 bug。
- 重复的任务描述。
- 大段未总结的 diff。
- 过期计划。

长期上下文应该只保留：

```text
未来 AI 进入项目时仍然值得知道的信息。
```

---

## 7. Final Rule

每次处理任务前，先问：

```text
为了正确处理当前任务，最少需要哪些上下文？
```

然后只加载这些上下文。
