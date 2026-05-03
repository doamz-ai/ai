# Skill: Execution Prompt Compiler

## Purpose

将已经澄清、规格化、拆分后的任务切片，编译成一段可以直接交给编程智能体执行的高质量 Prompt。

本 skill 的目标是降低编程智能体的理解歧义、执行偏差、无关改动和返工成本。

---

## When to Use

当出现以下情况时使用：

- 某个任务已经达到 L2：目标清晰，可执行。
- 已有 PRD / RFC / task slice，需要转成执行 Prompt。
- 用户要把任务交给 Opus / Codex / Claude Code / Cursor Agent 等编程智能体。
- 需要控制昂贵模型的 token 和试错成本。
- 需要把复杂讨论收敛成一段高密度执行指令。

---

## Core Principle

执行 Prompt 不是聊天总结，而是工程任务单。

它必须让编程智能体明确知道：

```text
做什么
为什么做
先看哪里
怎么做
不能做什么
怎么验收
完成后如何汇报
```

---

## Required Inputs

建议读取：

```text
.ai/system/AI_AGENT_RULES.md
.ai/templates/TASK_PACKAGE_TEMPLATE.md
.ai/project/AI_REPO_CONTEXT.md
.ai/project/AI_DOMAIN_CONTEXT.md
.ai/project/AI_PROJECT_MEMORY.md
```

如果已有任务材料，读取：

```text
.ai/tasks/<current-task>/01-prd.md
.ai/tasks/<current-task>/02-plan.md
.ai/tasks/<current-task>/03-slices.md
```

---

## Workflow

### Step 1: Confirm Task Readiness

先判断任务是否可执行。

```markdown
## 1. 任务可执行性检查

| Item | Status | Notes |
|---|---|---|
| Goal clear | Yes / No | ... |
| Non-goals clear | Yes / No | ... |
| Files to inspect known | Yes / No | ... |
| Acceptance criteria testable | Yes / No | ... |
| Major human decisions resolved | Yes / No | ... |
```

如果关键项为 No，不应生成最终执行 Prompt，应回到 Grill / Spec / Plan。

---

### Step 2: Compile Repo Evidence

列出编程智能体需要知道的仓库事实。

```markdown
## 2. Repo Evidence

### Confirmed
- ...

### To Verify Before Editing
- ...

### Assumptions
- ...
```

---

### Step 3: Define Task

任务必须一句话清晰。

```markdown
# Task

请基于当前 GitHub 仓库完成以下任务：...
```

---

### Step 4: Define Background

简明说明为什么做。

不要写长篇讨论。

```markdown
# Background

...
```

---

### Step 5: Define Goals and Non-goals

目标必须具体。

非目标必须显眼。

```markdown
# Goals

1. ...

# Non-goals

1. ...
```

---

### Step 6: Define Files / Modules to Inspect

如果已知路径，列路径。

如果未知，要求编程智能体先定位真实路径，不要新建重复模块。

```markdown
# Files / Modules to Inspect First

- `path/to/file`: reason
- 待定位：...
```

---

### Step 7: Define Implementation Requirements

按模块展开。

```markdown
# Implementation Requirements

## Backend
- ...

## Frontend
- ...

## Database / Storage
- ...

## Permission / Security
- ...

## Testing
- ...

## Documentation
- ...
```

没有涉及的部分写 “Not involved”。

---

### Step 8: Define Constraints

约束要比目标还清楚。

```markdown
# Constraints

- 不要 ...
- 必须 ...
```

必须包含：

- 不做无关重构。
- 不引入不必要依赖。
- 不改变无关 API。
- 不绕过权限。
- 不重复造轮子。
- 不把未来规划提前实现。

---

### Step 9: Define Acceptance Criteria

验收必须可测试。

```markdown
# Acceptance Criteria

1. 当 X 时，系统应该 Y。
2. 当异常 Z 时，系统应该 W。
3. 现有功能仍然正常。
```

---

### Step 10: Define Required Final Response

强制编程智能体执行后汇报。

```markdown
# Required Final Response

完成后请输出：

1. 修改文件列表。
2. 新增文件列表。
3. 删除文件列表。
4. 数据库 / migration 变化。
5. 环境变量变化。
6. 测试方式。
7. 测试结果。
8. 已知风险。
9. 未完成事项。
10. 延期技术债。
```

---

## Output Format

最终输出应是一段可直接复制的 Prompt：

```markdown
# Task

...

# Background

...

# Repo Evidence

## Confirmed
- ...

## To Verify Before Editing
- ...

## Assumptions
- ...

# Goals

1. ...

# Non-goals

1. ...

# Files / Modules to Inspect First

- ...

# Implementation Requirements

## Backend
- ...

## Frontend
- ...

## Database / Storage
- ...

## Permission / Security
- ...

## Testing
- ...

## Documentation
- ...

# Constraints

- ...

# Acceptance Criteria

1. ...

# Required Final Response

完成后请输出：
...
```

---

## Quality Bar

好的执行 Prompt 应该：

- 可以直接复制给编程智能体。
- 不需要编程智能体猜需求。
- 明确先检查哪些文件。
- 明确目标和非目标。
- 明确禁止事项。
- 明确验收标准。
- 明确完成后汇报格式。
- 尽量减少模型自由发挥空间。

---

## Anti-patterns

禁止：

- 把长篇讨论直接粘给编程智能体。
- 没有 Non-goals。
- 没有验收标准。
- 没有文件检查范围。
- 没有权限/测试要求。
- 同一个 Prompt 要求完成过多无关任务。
- 使用“顺便”“优化一下”“尽量完善”这类模糊指令。

---

## Handoff

完成后交给：

- 编程智能体进入 Build Mode。
- 执行后交给 `review-quality-gate` 审计。
- 如执行失败，交给 `diagnose-bug` 或生成 Fix Prompt。
