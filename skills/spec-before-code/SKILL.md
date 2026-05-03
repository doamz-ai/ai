# Skill: Spec Before Code

## Purpose

在写代码之前，把需求整理成可评审、可拆解、可验收的规格文档。

本 skill 的核心目标是防止 AI 在需求边界不清、成功标准不明、风险未识别的情况下直接进入实现。

---

## When to Use

当出现以下情况时使用：

- 用户要求整理 PRD / RFC / 技术方案。
- 需求涉及多个模块。
- 需求需要人类和编程智能体共同审计。
- 需求会影响数据库、权限、API、文件存储、部署或用户体验。
- 需求已经通过 `idea-to-clarity` 或 `grill-with-repo` 初步澄清。
- 用户准备把方案交给编程智能体执行前，需要先形成规格。

通常对应成熟度：

```text
L1: Directional Need
L2: Executable Task
L3: Existing Plan / Spec
```

---

## Core Principle

规格不是为了写长文档，而是为了降低实现歧义。

一个好的 spec 必须回答：

```text
为什么做？
为谁做？
做什么？
不做什么？
怎么判断做完？
会影响哪些系统边界？
风险是什么？
哪些问题仍待确认？
```

---

## Required Inputs

建议读取：

```text
.ai/project/AI_REPO_CONTEXT.md
.ai/project/AI_DOMAIN_CONTEXT.md
.ai/project/AI_PROJECT_MEMORY.md
.ai/templates/PRD_TEMPLATE.md
.ai/templates/RFC_TEMPLATE.md
```

如果涉及重大架构决策，读取：

```text
.ai/templates/ADR_TEMPLATE.md
```

如果已有澄清报告，读取：

```text
.ai/tasks/<current-task>/00-idea.md
.ai/tasks/<current-task>/01-clarity.md
```

---

## Workflow

### Step 1: Define Background

说明为什么需要这个需求。

```markdown
## 1. 背景

当前情况：...
问题来源：...
为什么现在要处理：...
```

---

### Step 2: Define Problem

区分表层问题和真实问题。

```markdown
## 2. 问题定义

表层问题：...
真实问题：...
```

---

### Step 3: Define Goals and Non-goals

目标和非目标必须同时出现。

```markdown
## 3. 目标

1. ...

## 4. 非目标

1. ...
```

Non-goals 应包含：

- 本次不实现的未来能力。
- 不做的重构。
- 不改变的旧逻辑。
- 不引入的依赖或基础设施。

---

### Step 4: Define User Stories

```markdown
## 5. 用户故事

作为【角色】，
当【场景】时，
我希望【动作】，
以便【价值】。
```

如有多个角色，分别列出。

---

### Step 5: Define Business Flow

用清晰步骤描述流程。

```markdown
## 6. 业务流程

```text
步骤 1
→ 步骤 2
→ 步骤 3
→ 完成
```
```

---

### Step 6: Define System Impact

按系统边界展开。

```markdown
## 7. 系统影响面

### 前端
- ...

### 后端
- ...

### 数据库 / 存储
- ...

### 权限 / 安全
- ...

### 测试
- ...

### 部署 / 配置
- ...
```

没有涉及的部分明确写 “不涉及”。

---

### Step 7: Define Data and State

如涉及数据，必须说明：

- 实体。
- 字段。
- 状态。
- 生命周期。
- 清理策略。
- 兼容性。

```markdown
## 8. 数据设计

| Entity | Field | Meaning | Notes |
|---|---|---|---|
```

---

### Step 8: Define Interface / API

如涉及接口，必须说明：

- API 名称。
- 请求参数。
- 返回结构。
- 错误处理。
- 权限要求。
- 兼容性影响。

---

### Step 9: Define Acceptance Criteria

验收标准必须可测试。

避免：

```text
体验更好
性能更高
逻辑更清晰
```

改成：

```text
当 X 时，系统应 Y。
当无权限用户访问 Z 时，应返回 403。
当导出失败时，应记录 error_message 并展示失败状态。
```

格式：

```markdown
## 9. 验收标准

1. 当【场景】时，系统应该【结果】。
2. 当【异常场景】时，系统应该【结果】。
```

---

### Step 10: Define Risks and Open Questions

```markdown
## 10. 风险

| 风险 | 影响 | 缓解方式 |
|---|---|---|

## 11. 开放问题

| 问题 | 为什么重要 | 下一步 |
|---|---|---|
```

---

### Step 11: Decide If ADR Is Needed

如果满足以下任一条件，建议创建 ADR：

- 决策难以逆转。
- 有多个合理方案且取舍明显。
- 未来维护者可能疑惑为什么这样做。
- 涉及技术栈、基础设施、权限模型、数据存储重大选择。

如果不需要 ADR，明确写：

```text
本次不需要 ADR，因为该决策是局部实现选择，影响范围有限。
```

---

## Output Format

```markdown
# Spec Before Code

## 1. 背景

## 2. 问题定义

## 3. 目标

## 4. 非目标

## 5. 用户故事

## 6. 业务流程

## 7. 系统影响面

### 前端
### 后端
### 数据库 / 存储
### 权限 / 安全
### 测试
### 部署 / 配置

## 8. 数据 / 状态 / 接口设计

## 9. 验收标准

## 10. 风险

## 11. 开放问题

## 12. 是否需要 ADR

## 13. 下一步建议
```

---

## Quality Bar

好的 spec 应该：

- 清楚说明为什么做。
- 目标和非目标都明确。
- 验收标准可测试。
- 不确定性被标注。
- 不夹带无关重构。
- 能直接进入任务拆解。
- 能让编程智能体理解边界。

---

## Anti-patterns

禁止：

- 只有功能描述，没有 Non-goals。
- 只有业务语言，没有工程影响面。
- 验收标准不可测试。
- 忽略权限、安全、失败路径。
- 把未来规划全部塞进本次规格。
- 为了显得完整，写大量无关内容。

---

## Handoff

完成后通常交给：

- `plan-to-slices`：拆成任务切片。
- `execution-prompt-compiler`：生成执行 Prompt。
- `architecture-deepening`：如果发现重大架构问题。
