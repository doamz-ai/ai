# Skill: Architecture Deepening

## Purpose

分析模块边界、架构一致性、技术债和长期演进风险，帮助项目在不盲目重构的前提下变得更可维护。

本 skill 不鼓励大改，而是用于判断什么时候该治理架构、怎么分阶段治理、哪些技术债应记录而不是顺手修。

---

## When to Use

当出现以下情况时使用：

- 用户觉得某个模块越来越乱。
- 需求会反复触碰同一块代码。
- AI 多次在同一区域犯错。
- 代码重复、边界不清、测试困难。
- 某功能未来会成为平台能力或公共能力。
- 审计发现结构性技术债。
- 需要判断是否写 ADR。

---

## Core Principle

架构治理不是为了“优雅”，而是为了降低未来变更成本和错误率。

默认不进行大重构。

优先：

```text
识别边界
→ 记录技术债
→ 找到触发条件
→ 拆出安全切片
→ 小步治理
```

---

## Required Inputs

建议读取：

```text
.ai/project/AI_REPO_CONTEXT.md
.ai/project/AI_PROJECT_MEMORY.md
.ai/project/AI_DOMAIN_CONTEXT.md
.ai/references/ANTI_OVERENGINEERING_RULES.md
.ai/templates/ADR_TEMPLATE.md
```

如有具体 diff 或模块，读取相关代码和历史任务记录。

---

## Workflow

### Step 1: Define the Architecture Concern

```markdown
## 1. Architecture Concern

当前担忧：...
为什么现在出现：...
影响范围：...
```

---

### Step 2: Identify Module Boundaries

```markdown
## 2. Module Boundary Analysis

| Module | Responsibility | Current Boundary | Problem |
|---|---|---|---|
```

---

### Step 3: Identify Change Pressure

判断是否真的值得治理。

```markdown
## 3. Change Pressure

| Signal | Evidence | Severity |
|---|---|---|
| Repeated changes | ... | High / Medium / Low |
| Duplicate logic | ... | ... |
| Testing difficulty | ... | ... |
| Security risk | ... | ... |
| Performance risk | ... | ... |
```

---

### Step 4: Separate Refactor from Feature Work

```markdown
## 4. Refactor vs Feature

### Should not mix with current feature
- ...

### Can be included safely
- ...

### Should become separate task
- ...
```

---

### Step 5: Propose Evolution Options

```markdown
## 5. Options

### Option A: Do nothing now
- When appropriate: ...
- Risk: ...

### Option B: Local cleanup
- Scope: ...
- Risk: ...

### Option C: Phased refactor
- Phase 1: ...
- Phase 2: ...
- Phase 3: ...

### Option D: Architecture redesign
- Only if: ...
```

---

### Step 6: Recommend Minimal Safe Move

```markdown
## 6. Recommended Move

推荐：...
原因：...
本次不做：...
未来触发条件：...
```

---

### Step 7: Decide ADR Need

需要 ADR 的情况：

- 决策长期影响大。
- 有多个合理方案。
- 未来维护者会疑惑为什么这样做。
- 涉及基础设施、权限模型、数据存储、核心架构。

输出：

```markdown
## 7. ADR Decision

是否需要 ADR：Yes / No
原因：...
建议 ADR 标题：...
```

---

## Output Format

```markdown
# Architecture Deepening Report

## 1. Architecture Concern

## 2. Module Boundary Analysis

| Module | Responsibility | Current Boundary | Problem |
|---|---|---|---|

## 3. Change Pressure

| Signal | Evidence | Severity |
|---|---|---|

## 4. Refactor vs Feature

## 5. Options

## 6. Recommended Move

## 7. Deferred Technical Debt

| Debt | Impact | Revisit Trigger | Priority |
|---|---|---|---|

## 8. ADR Decision

## 9. Suggested Task Slices
```

---

## Quality Bar

好的架构分析应该：

- 基于真实代码压力，而不是审美偏好。
- 不默认建议大重构。
- 能区分本次功能和长期治理。
- 给出阶段化方案。
- 明确技术债和触发条件。
- 判断是否需要 ADR。

---

## Anti-patterns

禁止：

- 为了“优雅”建议大范围重写。
- 把重构夹进功能任务。
- 没有证据就说架构差。
- 不给迁移路径。
- 不说明风险。
- 不记录被延期的技术债。

---

## Handoff

完成后通常交给：

- `plan-to-slices`：拆架构治理任务。
- `spec-before-code`：形成 RFC。
- `execution-prompt-compiler`：生成局部重构 Prompt。
- `ship-and-record`：沉淀架构规则或 ADR。
