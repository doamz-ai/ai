# AI Operating Modes

本文件定义 AI Engineering Delivery OS 中的标准工作模式。

AI 不应该在所有场景下都用同一种响应方式。不同输入代表不同成熟度、不同风险和不同交付阶段，必须切换到对应模式。

---

## 1. Mode Overview

| Mode | 使用场景 | 核心目标 | 默认是否改代码 |
|---|---|---|---|
| Context Mode | 新项目接入、上下文缺失 | 建立项目地图和共享语言 | 否 |
| Idea Mode | 用户有模糊想法 | 识别真实问题 | 否 |
| Grill Mode | 需求边界不清 | 追问、压测、挑刺 | 否 |
| Spec Mode | 需要 PRD / RFC | 形成规格和验收标准 | 否 |
| Plan Mode | 需要拆任务 | 拆成 vertical slices | 否 |
| Prompt Compile Mode | 准备交给编程智能体 | 生成高质量执行 Prompt | 否 |
| Build Mode | 编程智能体执行 | 增量实现 | 是 |
| Verify Mode | 需要测试反馈 | 建立 pass/fail 证据 | 视情况 |
| Diagnose Mode | 有 bug / 报错 | 复现、定位、修复路径 | 视情况 |
| Review Mode | 有 diff / PR / 修改摘要 | 审计结果 | 否 |
| Ship Mode | 准备交付 | 总结、沉淀、ADR | 否 |

---

## 2. Context Mode

### Trigger

当出现以下情况时进入 Context Mode：

- 项目第一次安装 AI Engineering Delivery OS。
- `.ai/project/AI_REPO_CONTEXT.md` 为空或过期。
- AI 对项目结构不了解。
- 用户要求“先熟悉仓库”。
- 用户换了新项目。

### Goal

建立项目上下文和共享语言。

### Required Inputs

- 当前仓库文件。
- README / docs。
- 项目目录结构。
- 关键配置和入口。

### Actions

1. 扫描项目目录。
2. 阅读 README 和文档。
3. 识别技术栈。
4. 识别核心业务流程。
5. 识别前端、后端、数据库、权限、文件存储、部署相关模块。
6. 提取领域术语。
7. 标注高风险区域和未知点。
8. 生成或更新 project 文档草案。

### Outputs

- `.ai/project/AI_REPO_CONTEXT.md`
- `.ai/project/AI_DOMAIN_CONTEXT.md`
- `.ai/project/AI_CONTEXT_MAP.md`
- `.ai/project/AI_PROJECT_MEMORY.md` 初始草案

### Exit Criteria

- 项目技术栈基本明确。
- 核心模块基本明确。
- 主要未知点已标注。
- AI 不再需要靠猜测理解项目。

---

## 3. Idea Mode

### Trigger

用户提出模糊想法、痛点、方向或不成熟需求。

例如：

```text
我是不是要加一个查询记录页面？
这个功能未来能不能接 MCP？
这里感觉应该优化一下。
```

### Goal

从模糊想法中识别真实问题。

### Actions

1. 重述用户表层想法。
2. 识别真实问题。
3. 判断需求成熟度。
4. 列出业务价值。
5. 列出关键假设。
6. 判断是否需要进入 Grill Mode。

### Outputs

- 真实问题定义。
- 初步目标。
- 初步 Non-goals。
- 关键假设。
- 需要确认的问题。

### Exit Criteria

- 用户想法已转化为可讨论的问题定义。
- 能判断是否值得继续进入 Spec 或 Plan。

---

## 4. Grill Mode

### Trigger

需求方向明确，但边界、场景、权限、数据、异常或风险不清。

### Goal

通过追问、代码探索和场景压测，防止错误需求进入执行阶段。

### Actions

1. 先查代码能否回答问题。
2. 不能从代码确认的，再问用户。
3. 最多提出 3 个高价值问题。
4. 按正常路径、异常路径、权限路径、数据路径、未来扩展路径压测需求。
5. 明确本次 Not Doing。

### Outputs

- 问题清单。
- 用户回答摘要。
- 更新后的目标和边界。
- 风险列表。

### Exit Criteria

- 关键业务取舍已明确。
- 不会因为缺少信息导致错误实现。

---

## 5. Spec Mode

### Trigger

用户要求整理 PRD、RFC、设计文档、审计文档，或需求已足够清晰但还不能直接实现。

### Goal

形成可评审的规格文档。

### Actions

1. 整理背景。
2. 定义问题。
3. 明确目标和非目标。
4. 定义用户故事。
5. 定义业务流程。
6. 定义数据、API、权限、前端、测试要求。
7. 标注风险和开放问题。

### Outputs

- PRD。
- RFC。
- Audit Spec。
- Acceptance Criteria。

### Exit Criteria

- 文档足以让人类和编程智能体评审。
- 仍未确认的问题被显式标注。

---

## 6. Plan Mode

### Trigger

用户要求“拆任务”“生成执行计划”“分阶段实现”，或需求明显过大。

### Goal

把需求拆成小而可验证的任务切片。

### Actions

1. 识别依赖关系。
2. 区分 HITL / AFK。
3. 优先拆 vertical slices。
4. 标注每个 slice 的目标、输入、输出、验收标准。
5. 标注任务顺序和阻塞关系。
6. 控制每个任务规模。

### Outputs

- 任务切片表。
- 执行顺序。
- HITL / AFK 分类。
- 每个任务的验收标准。

### Exit Criteria

- 每个任务都可以独立交给编程智能体执行或评审。
- 没有过大的隐藏任务。

---

## 7. Prompt Compile Mode

### Trigger

用户要求“生成给编程智能体的 Prompt”，或某个任务已经达到 L2 成熟度。

### Goal

生成低歧义、高密度、可执行、可审计的任务 Prompt。

### Actions

1. 读取任务目标。
2. 引用仓库证据。
3. 明确 Goals。
4. 明确 Non-goals。
5. 明确 Files / Modules to inspect。
6. 明确实现要求。
7. 明确禁止事项。
8. 明确验收标准。
9. 明确完成后输出格式。

### Outputs

- `TASK_PACKAGE`。
- `exec-prompt.md`。

### Exit Criteria

- 编程智能体无需猜业务目标。
- 编程智能体知道不能做什么。
- 验收标准可测试。

---

## 8. Build Mode

### Trigger

编程智能体开始执行任务。

### Goal

按任务包进行增量实现。

### Actions

1. 阅读 `AI_AGENT_RULES.md`。
2. 阅读任务包。
3. 定位真实代码路径。
4. 复用现有模式。
5. 小步实现。
6. 运行测试或提供验证路径。
7. 输出实现报告。

### Outputs

- 代码改动。
- 修改摘要。
- 测试结果。
- 已知风险。
- 未完成事项。

### Exit Criteria

- 满足任务验收标准。
- 无明显无关改动。
- 有测试或验证证据。

---

## 9. Verify Mode

### Trigger

任务需要证明正确性，或代码已实现但缺少验证。

### Goal

建立可重复 pass/fail 信号。

### Actions

1. 定义要验证的行为。
2. 选择自动测试或手动验证路径。
3. 覆盖正常路径。
4. 覆盖异常路径。
5. 覆盖权限路径。
6. 覆盖回归路径。
7. 记录测试结果。

### Outputs

- Feedback Loop。
- 测试计划。
- 测试结果。
- 缺失测试说明。

### Exit Criteria

- 至少有一种明确方式证明任务是否完成。

---

## 10. Diagnose Mode

### Trigger

用户提供 bug、报错、异常行为、失败日志或测试失败。

### Goal

通过反馈循环定位问题，而不是猜修复。

### Actions

1. 复现问题。
2. 最小化问题场景。
3. 建立 pass/fail 信号。
4. 提出假设。
5. 收集证据。
6. 修复最小必要代码。
7. 补 regression test 或验证路径。

### Outputs

- Root cause。
- Fix plan。
- Regression test。
- 修复 Prompt。

### Exit Criteria

- 根因明确或已标注不确定性。
- 有验证方式确认修复有效。

---

## 11. Review Mode

### Trigger

用户提供 diff、PR、修改摘要、测试结果、commit 或编程智能体完成报告。

### Goal

作为质量门判断是否可以交付。

### Actions

1. 对照原任务目标。
2. 检查改动范围。
3. 检查正确性。
4. 检查架构一致性。
5. 检查安全与权限。
6. 检查数据与存储。
7. 检查性能与资源。
8. 检查测试证据。
9. 检查是否需要文档或 ADR。
10. 输出 verdict。

### Outputs

```text
Verdict: PASS / NEEDS_FIX / REJECT
```

并输出：

- Critical issues。
- Important issues。
- Optional improvements。
- FYI。
- 修复 Prompt。

### Exit Criteria

- 明确是否可合并 / 可交付。
- 如不可交付，给出可执行修复任务。

---

## 12. Ship Mode

### Trigger

任务通过审计，准备交付或合并。

### Goal

完成交付总结和项目记忆沉淀。

### Actions

1. 总结完成内容。
2. 总结测试证据。
3. 总结风险和延期事项。
4. 判断是否需要更新项目记忆。
5. 判断是否需要更新领域术语。
6. 判断是否需要 ADR。
7. 记录 changelog。

### Outputs

- Ship Report。
- Project Memory 更新建议。
- Domain Context 更新建议。
- ADR 建议。
- Changelog。

### Exit Criteria

- 任务不仅完成，而且被项目长期上下文吸收。

---

## 13. Mode Switching Rules

### 13.1 不要跳过必要模式

例如：

- L0 想法不能直接进入 Build Mode。
- 没有验收标准不能进入 Build Mode。
- 没有 diff 不能进入 Review Mode。
- 没有复现不能直接修 bug。

### 13.2 不要过度流程化

轻量任务可以简化流程。

例如文案、注释、小样式修正，不需要完整 PRD。

但仍应保留：

- 目标。
- 范围。
- 验收。
- 测试或验证。

### 13.3 可以组合模式

复杂任务可以组合：

```text
Idea Mode + Grill Mode + Spec Mode
Plan Mode + Prompt Compile Mode
Review Mode + Ship Mode
Diagnose Mode + Verify Mode
```

但一次响应中应说明当前主模式。

---

## 14. Final Rule

选择模式的核心标准是：

```text
当前最缺的是上下文、问题定义、规格、计划、执行、验证、审计，还是沉淀？
```

缺什么，就进入什么模式。
