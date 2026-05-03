# Skill: Plan to Slices

## Purpose

将已澄清的需求或规格拆解为小而可执行、可验证、可审计、可回滚的任务切片。

本 skill 的目标是避免把一个复杂需求一次性交给编程智能体，导致大范围误改、返工和技术债。

---

## When to Use

当出现以下情况时使用：

- 用户要求“拆任务”“分阶段实现”“给执行计划”。
- Spec / PRD 已经形成，需要转成开发任务。
- 需求涉及多个模块。
- 任务超过单个智能体一次安全执行范围。
- 需求同时涉及前端、后端、数据库、权限、存储、测试、部署中的多个部分。
- 需要区分哪些任务可 AFK 执行，哪些需要 HITL 决策。

---

## Core Principle

优先 vertical slices，而不是按技术层横切。

不推荐：

```text
任务 1：先建数据库
任务 2：再写所有 API
任务 3：再写所有前端
任务 4：最后统一测试
```

推荐：

```text
Slice 1：完成一个最小端到端闭环
Slice 2：补充权限和异常路径
Slice 3：补充列表、筛选、分页
Slice 4：补充测试和文档
```

每个 slice 应尽量做到：

```text
小范围
可执行
可测试
可审计
可回滚
```

---

## Required Inputs

建议读取：

```text
.ai/templates/ISSUE_SLICE_TEMPLATE.md
.ai/templates/TASK_PACKAGE_TEMPLATE.md
.ai/project/AI_REPO_CONTEXT.md
.ai/project/AI_DOMAIN_CONTEXT.md
.ai/project/AI_PROJECT_MEMORY.md
```

如已有规格，读取：

```text
.ai/tasks/<current-task>/01-prd.md
.ai/tasks/<current-task>/02-rfc.md
```

---

## Workflow

### Step 1: Restate the Spec Goal

先确认要拆解的目标。

```markdown
## 1. 待拆解目标

本次要实现的是：...
```

---

### Step 2: Identify Impact Areas

列出涉及区域。

```markdown
## 2. 影响区域

| Area | Involved | Notes |
|---|---|---|
| Frontend | Yes / No | ... |
| Backend | Yes / No | ... |
| Database | Yes / No | ... |
| Permission | Yes / No | ... |
| Storage | Yes / No | ... |
| Tests | Yes / No | ... |
| Deployment | Yes / No | ... |
| Docs | Yes / No | ... |
```

如果涉及 4 类以上，默认应该拆成多 slice。

---

### Step 3: Identify Dependencies

```markdown
## 3. 依赖关系

| Dependency | Needed Before | Reason |
|---|---|---|
```

例如：

- 数据模型需先于 API。
- 权限规则需先于前端隐藏。
- 存储封装需先于下载入口。

---

### Step 4: Classify HITL vs AFK

```markdown
## 4. HITL / AFK 分类

| Decision / Task | HITL or AFK | Reason |
|---|---|---|
```

HITL：需要人类决策。

例如：

- 是否改变权限模型。
- 是否新增付费服务。
- 是否删除历史数据。
- 是否引入新基础设施。
- 是否接受破坏性变更。

AFK：智能体可以按明确任务独立执行。

例如：

- 查找代码路径。
- 新增局部接口。
- 补充测试。
- 更新文档。

---

### Step 5: Create Vertical Slices

每个 slice 应包含：

- Slice ID。
- 目标。
- 类型。
- HITL / AFK。
- 输入。
- 输出。
- 涉及模块。
- 验收标准。
- 风险。

格式：

```markdown
## 5. 任务切片

| Slice | Type | HITL/AFK | Goal | Acceptance Criteria | Risk |
|---|---|---|---|---|---|
| S0 | Investigation | AFK | ... | ... | Low |
```

---

### Step 6: Define Suggested Order

```markdown
## 6. 推荐执行顺序

1. S0 - ...
2. S1 - ...
3. S2 - ...
```

每一步说明为什么排在这里。

---

### Step 7: Identify Stop Points

定义每个阶段何时停下来让人类确认。

```markdown
## 7. 人类确认点

| Stop Point | Before Slice | Why |
|---|---|---|
```

---

### Step 8: Identify What Not to Combine

防止任务过大。

```markdown
## 8. 不应合并的任务

- 不要把 ... 和 ... 放在同一个执行 Prompt。
```

---

### Step 9: Recommend First Executable Slice

最后推荐下一步最适合交给编程智能体的 slice。

```markdown
## 9. 推荐第一个执行任务

推荐先执行：S...
理由：...
```

---

## Output Format

```markdown
# Plan to Slices Report

## 1. 待拆解目标

## 2. 影响区域

| Area | Involved | Notes |
|---|---|---|

## 3. 依赖关系

| Dependency | Needed Before | Reason |
|---|---|---|

## 4. HITL / AFK 分类

| Decision / Task | HITL or AFK | Reason |
|---|---|---|

## 5. 任务切片

| Slice | Type | HITL/AFK | Goal | Acceptance Criteria | Risk |
|---|---|---|---|---|---|

## 6. 推荐执行顺序

## 7. 人类确认点

## 8. 不应合并的任务

## 9. 推荐第一个执行任务
```

---

## Slice Types

推荐使用以下类型：

| Type | Meaning |
|---|---|
| Investigation | 只读探查，不改代码 |
| Spec | 规格补充 |
| Data | 数据模型 / migration |
| Backend | 后端逻辑 / API |
| Frontend | 前端页面 / 交互 |
| Permission | 权限和安全 |
| Storage | 文件 / 对象存储 |
| Test | 测试和验证 |
| Docs | 文档和记忆沉淀 |
| Review | 审计任务 |

---

## Task Size Guidelines

建议判断任务大小：

| Size | Signal | Action |
|---|---|---|
| S | 1-2 个文件，小改动 | 可直接执行 |
| M | 3-5 个文件，单一模块 | 可执行但需明确验收 |
| L | 6-8 个文件，多模块 | 建议拆分 |
| XL | 超过 8 个文件或涉及核心架构 | 必须拆分 |

---

## Quality Bar

好的任务切片应该：

- 每个 slice 目标单一。
- 每个 slice 有明确验收。
- 每个 slice 可以独立审计。
- 任务顺序合理。
- HITL / AFK 分类明确。
- 避免把未来规划塞进当前实现。

---

## Anti-patterns

禁止：

- 把一个大需求直接变成一个巨大 Prompt。
- 按数据库/API/前端横切导致中间长期不可用。
- 没有验收标准的任务。
- 没有区分人类决策和 AI 执行。
- 把探查任务和实现任务混在一起。
- 把重构和功能开发混在一起。

---

## Handoff

完成后通常交给：

- `execution-prompt-compiler`：为某个 slice 生成执行 Prompt。
- `spec-before-code`：如果拆解时发现规格不完整。
- `review-quality-gate`：执行后审计。
