# Skill: Grill with Repo

## Purpose

对一个方向基本明确但边界不清的需求进行追问、挑刺、代码事实核对和场景压测。

本 skill 的目标不是为难用户，而是在进入规格或执行前，把隐含风险、缺失信息、边界条件和过度设计倾向暴露出来。

---

## When to Use

当出现以下情况时使用：

- 用户已有方向，但不确定是否合理。
- 需求涉及多个模块或角色。
- 需求可能影响权限、数据、存储、成本或架构。
- 用户要求“帮我挑刺”“从第一性原理审视”。
- 需求听起来简单，但可能有隐藏工程复杂度。
- 用户提出未来规划，需要区分当前做与未来做。

通常对应成熟度：

```text
L1: Directional Need
L3: Existing Plan / Spec
```

---

## Core Principle

能从仓库确认的问题，不要问用户。

应该先查：

- 当前是否已有类似功能。
- 当前代码路径在哪里。
- 当前数据模型是什么。
- 当前权限模型是什么。
- 当前接口和前端模式是什么。
- 当前测试和部署方式是什么。

只有以下问题才问用户：

- 业务取舍。
- 用户体验偏好。
- 风险接受度。
- 成本接受度。
- 不可逆架构决策。
- 权限和数据保留策略。

---

## Required Inputs

建议读取：

```text
.ai/project/AI_REPO_CONTEXT.md
.ai/project/AI_DOMAIN_CONTEXT.md
.ai/project/AI_PROJECT_MEMORY.md
.ai/references/ANTI_OVERENGINEERING_RULES.md
```

根据需求类型可选读取：

```text
.ai/references/SECURITY_CHECKLIST.md
.ai/references/API_INTERFACE_CHECKLIST.md
.ai/references/DATABASE_MIGRATION_CHECKLIST.md
.ai/references/FRONTEND_UX_CHECKLIST.md
.ai/references/PERFORMANCE_CHECKLIST.md
```

---

## Workflow

### Step 1: Identify What Must Be Verified in Repo

先列出需要从仓库确认的事实。

格式：

```markdown
## 1. 需要从仓库确认的事实

| 问题 | 为什么重要 | 如何确认 |
|---|---|---|
| ... | ... | 查看 ... |
```

---

### Step 2: Separate Known, Unknown, Assumed

把信息分层。

格式：

```markdown
## 2. 当前信息分层

### 已确认
- ...

### 待确认
- ...

### 基于假设
- ...
```

---

### Step 3: Pressure-test the Requirement

从以下维度压测。

#### Business Path

- 正常业务路径是什么？
- 用户为什么需要它？
- 谁会用？
- 不做会怎样？

#### Data Path

- 数据从哪里来？
- 存在哪里？
- 生命周期是什么？
- 是否需要迁移？
- 是否有清理策略？

#### Permission Path

- 谁能看？
- 谁能改？
- 谁不能访问？
- 后端如何校验？
- 是否存在越权风险？

#### Failure Path

- 失败怎么办？
- 是否可重试？
- 是否记录错误？
- 用户看到什么？

#### Scale Path

- 数据量大时怎么办？
- 是否需要分页、异步、对象存储、限流？

#### Compatibility Path

- 是否影响旧 API？
- 是否影响旧页面？
- 是否影响已有数据？

#### Future Path

- 哪些只是未来预留？
- 哪些不能现在做？
- 当前设计是否会阻塞未来？

---

### Step 4: Ask Up to 3 High-value Questions

只有必要时才问。

问题必须高价值，避免问代码能回答的问题。

格式：

```markdown
## 3. 需要你确认的关键问题

1. ...
2. ...
3. ...
```

如果无需问用户，写：

```text
当前可以基于已有信息继续推进，无需额外提问。
```

---

### Step 5: Identify Scope Creep Risk

指出过度设计风险。

格式：

```markdown
## 4. 范围膨胀风险

容易被误加进去但本次不应做的内容：

- ...
```

---

### Step 6: Recommend Scope Boundary

输出明确边界。

```markdown
## 5. 推荐范围边界

### 本次要做
- ...

### 本次不做
- ...

### 仅预留，不实现
- ...
```

---

### Step 7: Decide Next Step

根据结果判断进入哪个阶段。

```markdown
## 6. 下一步建议

建议进入：Spec Mode / Plan Mode / Prompt Compile Mode / Stop
理由：...
```

---

## Output Format

```markdown
# Grill with Repo Report

## 1. 需要从仓库确认的事实

| 问题 | 为什么重要 | 如何确认 |
|---|---|---|

## 2. 当前信息分层

### 已确认
- ...

### 待确认
- ...

### 基于假设
- ...

## 3. 场景压测

### Business Path
- ...

### Data Path
- ...

### Permission Path
- ...

### Failure Path
- ...

### Scale Path
- ...

### Compatibility Path
- ...

### Future Path
- ...

## 4. 需要你确认的关键问题

1. ...

## 5. 范围膨胀风险

- ...

## 6. 推荐范围边界

### 本次要做
- ...

### 本次不做
- ...

### 仅预留，不实现
- ...

## 7. 下一步建议

...
```

---

## Quality Bar

输出必须做到：

- 先查代码事实，再问用户。
- 最多问 3 个高价值问题。
- 明确区分已确认、待确认、假设。
- 覆盖业务、数据、权限、失败、规模、兼容、未来路径。
- 明确范围边界和 Not Doing。
- 能指出过度设计风险。

---

## Anti-patterns

禁止：

- 问一堆代码可以回答的问题。
- 用户提出未来能力，就建议现在全做。
- 只夸方案，不挑风险。
- 没有权限和失败路径分析。
- 没有范围边界。
- 把追问变成审问，阻碍推进。

---

## Handoff

完成后通常交给：

- `spec-before-code`：生成 PRD/RFC。
- `plan-to-slices`：拆任务。
- `execution-prompt-compiler`：生成执行 Prompt。
