# Skill: Idea to Clarity

## Purpose

将用户模糊、不成熟、跳跃的想法，转化为清晰的问题定义、初步目标、关键假设和 Not Doing 清单。

本 skill 不负责写代码，也不负责直接生成最终执行 Prompt。它负责完成从“灵感”到“可讨论需求”的第一步转译。

---

## When to Use

当用户输入类似以下内容时使用：

- “我有个想法……”
- “这里是不是应该加个功能？”
- “未来能不能做成……”
- “我感觉这个流程不太对。”
- “这个功能是不是可以和另一个功能合并？”
- “我还没想清楚，你帮我判断下。”

对应需求成熟度通常是：

```text
L0: Raw Idea
L1: Directional Need
```

---

## Core Principle

不要急着把想法变成任务。

先回答：

```text
这个想法背后的真实问题是什么？
```

用户说出的通常是表象，AI 需要识别：

- 真实业务痛点。
- 用户角色。
- 当前流程缺口。
- 数据或权限边界。
- 成功标准。
- 约束条件。
- 当前不应该做的事情。

---

## Required Inputs

最低输入：

- 用户原始想法。

建议读取：

```text
.ai/system/AI_MASTER_PROMPT.md
.ai/system/AI_OPERATING_MODES.md
.ai/project/AI_REPO_CONTEXT.md
.ai/project/AI_DOMAIN_CONTEXT.md
.ai/project/AI_PROJECT_MEMORY.md
```

如果项目上下文为空，可以先基于用户想法做通用分析，并标注：

```text
当前缺少项目上下文，以下为基于假设的初步澄清。
```

---

## Workflow

### Step 1: Restate the Surface Idea

先用简洁语言复述用户表层想法。

格式：

```markdown
## 1. 表层想法

你现在提出的是：...
```

---

### Step 2: Identify the Real Problem

从第一性原理识别真实问题。

思考方向：

- 用户真正想减少什么成本？
- 想提升什么效率？
- 想降低什么风险？
- 想增强什么可控性？
- 当前流程的断点在哪里？
- 是产品问题、工程问题、数据问题、权限问题、体验问题，还是运营问题？

格式：

```markdown
## 2. 真实问题识别

表面上是：...
本质上是：...
```

---

### Step 3: Classify the Need

判断需求类型，可多选但要标主类型。

可选类型：

- Feature：新增功能。
- Workflow：流程优化。
- Data：数据治理。
- Permission：权限模型。
- UX：前端体验。
- Integration：外部系统集成。
- Architecture：架构治理。
- Operation：运维/部署。
- Quality：测试/稳定性。
- Future-facing：未来能力预留。

格式：

```markdown
## 3. 需求类型

主类型：...
辅助类型：...
理由：...
```

---

### Step 4: Define the User and Job-to-be-Done

用 JTBD 方式描述需求。

格式：

```markdown
## 4. 用户与 JTBD

作为【用户角色】，
当【场景/触发条件】时，
我希望【完成某个动作】，
以便【获得某个业务价值】。
```

如果用户角色不明确，标注为待确认。

---

### Step 5: List Assumptions

把所有假设显式列出。

格式：

```markdown
## 5. 关键假设

| 假设 | 影响 | 如何验证 |
|---|---|---|
| ... | ... | ... |
```

规则：

- 不要把假设写成事实。
- 能从代码验证的，写“查仓库验证”。
- 需要用户判断的，写“问用户确认”。

---

### Step 6: Identify Success Criteria

定义初步成功标准。

格式：

```markdown
## 6. 初步成功标准

如果这个想法成立，至少应满足：

1. ...
2. ...
3. ...
```

成功标准应尽量可验证，避免空话。

---

### Step 7: Draft Not Doing List

提前控制范围。

格式：

```markdown
## 7. 初步 Not Doing

本阶段暂不应该做：

1. ...
2. ...
3. ...

原因：...
```

Not Doing 特别重要，用来防止 AI 后续过度实现。

---

### Step 8: Decide Next Mode

根据清晰度判断下一步。

可选：

| Next Mode | When |
|---|---|
| Grill Mode | 边界不清，需要追问/挑刺 |
| Spec Mode | 需求已较清晰，需要 PRD/RFC |
| Plan Mode | 目标明确，需要拆任务 |
| Prompt Compile Mode | 已可执行，需要生成编程智能体 Prompt |
| Stop | 想法暂不值得做 |

格式：

```markdown
## 8. 下一步建议

建议进入：...
理由：...
```

---

## Output Format

```markdown
# Idea to Clarity Report

## 1. 表层想法

...

## 2. 真实问题识别

...

## 3. 需求类型

...

## 4. 用户与 JTBD

...

## 5. 关键假设

| 假设 | 影响 | 如何验证 |
|---|---|---|

## 6. 初步成功标准

1. ...

## 7. 初步 Not Doing

1. ...

## 8. 风险与不确定性

- ...

## 9. 下一步建议

建议进入：...
```

---

## Quality Bar

输出必须做到：

- 不直接写代码。
- 不直接下最终结论。
- 不把假设当事实。
- 能区分表层想法和真实问题。
- 能明确用户角色和业务价值。
- 能产出 Not Doing。
- 能判断下一步该进入哪个模式。

---

## Anti-patterns

禁止：

- 用户说一句想法，直接输出大段代码方案。
- 把未来规划全部当成当前要做。
- 只复述用户原话，没有提炼真实问题。
- 没有假设清单。
- 没有 Not Doing。
- 一上来就要求用户回答大量问题。

---

## Handoff

完成本 skill 后，通常交给：

- `grill-with-repo`：继续追问和压测。
- `spec-before-code`：形成 PRD/RFC。
- `plan-to-slices`：拆成任务。
- `execution-prompt-compiler`：当任务已非常清晰时生成执行 Prompt。
