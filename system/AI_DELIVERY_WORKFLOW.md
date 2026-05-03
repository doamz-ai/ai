# AI Delivery Workflow

本文件定义 AI Engineering Delivery OS 的标准工程交付生命周期。

它的目标是让 AI 编程从“用户一句话 → AI 直接改代码”升级为“上下文驱动、任务切片、增量实现、测试反馈、质量审计、长期沉淀”的工程交付流程。

---

## 1. Full Lifecycle

标准生命周期：

```text
0. Context
1. Define
2. Spec
3. Plan
4. Prompt
5. Build
6. Verify
7. Review
8. Ship
9. Memory
```

对应关系：

| 阶段 | 目标 | 主要产物 |
|---|---|---|
| 0. Context | 建立项目上下文 | Repo Context / Domain Context |
| 1. Define | 识别真实问题 | Problem Statement / Assumptions |
| 2. Spec | 形成规格 | PRD / RFC / Acceptance Criteria |
| 3. Plan | 拆任务 | Vertical Slices / HITL-AFK 分类 |
| 4. Prompt | 编译执行任务包 | Exec Prompt / Task Package |
| 5. Build | 增量实现 | Code Changes / Implementation Summary |
| 6. Verify | 测试验证 | Feedback Loop / Test Results |
| 7. Review | 质量审计 | Review Report / Verdict |
| 8. Ship | 交付总结 | Ship Report / Changelog |
| 9. Memory | 长期沉淀 | Project Memory / ADR / Domain Updates |

---

## 2. Stage 0: Context

### Purpose

让 AI 先理解项目，而不是凭空猜。

### Inputs

- README。
- docs。
- 目录结构。
- 依赖文件。
- 入口文件。
- 路由 / API。
- 业务 service。
- 数据模型。
- 前端页面。
- 权限逻辑。
- 测试和部署配置。

### Outputs

```text
.ai/project/AI_REPO_CONTEXT.md
.ai/project/AI_DOMAIN_CONTEXT.md
.ai/project/AI_CONTEXT_MAP.md
.ai/project/AI_PROJECT_MEMORY.md
```

### Quality Gate

进入下一阶段前应满足：

- 项目技术栈已识别。
- 核心业务流程已识别。
- 主要模块已识别。
- 领域术语已初步定义。
- 未确认点已标注。

### Failure Mode

如果没有上下文就进入 Build，容易导致：

- 重复造轮子。
- 破坏现有架构。
- 使用错误命名。
- 改错文件。
- 忽视权限和部署约束。

---

## 3. Stage 1: Define

### Purpose

把用户模糊想法转化为真实问题。

### Inputs

- 用户原始想法。
- 项目上下文。
- 领域术语。
- 当前业务流程。

### Actions

1. 重述表层想法。
2. 识别真实问题。
3. 判断需求成熟度。
4. 列出用户角色。
5. 列出业务价值。
6. 列出关键假设。
7. 列出初始 Not Doing。

### Outputs

- Problem Statement。
- User Story 草案。
- Assumption Ledger。
- Initial Not Doing。

### Quality Gate

进入 Spec 或 Plan 前应满足：

- 用户真正想解决的问题已明确。
- 关键假设已显式列出。
- 至少有初步成功标准。

---

## 4. Stage 2: Spec

### Purpose

把问题定义转化为可评审的规格。

### Inputs

- Problem Statement。
- Assumptions。
- User Story。
- Repo Evidence。
- 业务约束。

### Actions

1. 明确背景。
2. 明确目标。
3. 明确非目标。
4. 明确业务流程。
5. 明确数据要求。
6. 明确 API / interface 要求。
7. 明确前端 / 交互要求。
8. 明确权限与安全要求。
9. 明确测试和验收标准。
10. 明确开放问题。

### Outputs

- PRD。
- RFC。
- Audit Spec。
- Acceptance Criteria。

### Quality Gate

进入 Plan 前应满足：

- Goals 和 Non-goals 清晰。
- 验收标准可测试。
- 高风险点已显式列出。
- 未确认项不会阻塞任务拆解，或已标注为 HITL。

---

## 5. Stage 3: Plan

### Purpose

把规格拆成可执行、可验证、可回滚的任务切片。

### Inputs

- PRD / RFC。
- Acceptance Criteria。
- Repo Evidence。
- 依赖关系。

### Actions

1. 识别任务依赖。
2. 区分 HITL / AFK。
3. 优先 vertical slices。
4. 控制任务大小。
5. 为每个 slice 定义目标和验收。
6. 标注风险等级。
7. 标注执行顺序。

### HITL / AFK Definitions

```text
HITL = Human In The Loop，需要人类做业务、风险或不可逆决策。
AFK = Away From Keyboard，智能体可按明确任务独立执行。
```

### Outputs

- Issue Slice List。
- Execution Plan。
- Dependency Map。
- Risk Map。

### Quality Gate

进入 Prompt 阶段前应满足：

- 每个任务足够小。
- 每个任务有明确验收。
- HITL 和 AFK 已区分。
- 不存在隐藏的大范围重构。

---

## 6. Stage 4: Prompt

### Purpose

把任务切片编译成给编程智能体的高质量执行 Prompt。

### Inputs

- 单个任务切片。
- Repo Evidence。
- Goals。
- Non-goals。
- Constraints。
- Acceptance Criteria。

### Required Prompt Structure

```markdown
# Task

# Background

# Repo Evidence

# Goals

# Non-goals

# Files / Modules to Inspect

# Implementation Requirements

# Constraints

# Acceptance Criteria

# Required Final Response
```

### Outputs

- `exec-prompt.md`
- `TASK_PACKAGE`

### Quality Gate

进入 Build 前应满足：

- 编程智能体不需要猜目标。
- 编程智能体知道不能做什么。
- 文件或模块检查范围明确。
- 验收标准可测试。
- 完成后汇报格式明确。

---

## 7. Stage 5: Build

### Purpose

由编程智能体按任务包进行增量实现。

### Inputs

- `AI_AGENT_RULES.md`
- `exec-prompt.md`
- 相关代码文件。

### Actions

1. 阅读任务包。
2. 定位代码。
3. 检查已有实现。
4. 小步实现。
5. 避免无关重构。
6. 运行测试或记录无法运行原因。
7. 输出实现摘要。

### Outputs

- Code changes。
- Implementation Summary。
- Test Results。
- Known Risks。

### Quality Gate

进入 Verify 或 Review 前应满足：

- 代码可运行或已说明阻塞。
- 改动范围可解释。
- 没有明显违反 Non-goals。
- 有初步测试或验证说明。

---

## 8. Stage 6: Verify

### Purpose

用可重复反馈证明改动有效。

### Inputs

- Code changes。
- Acceptance Criteria。
- 测试框架。
- 运行环境。

### Actions

1. 验证正常路径。
2. 验证异常路径。
3. 验证权限路径。
4. 验证回归路径。
5. 记录测试命令和结果。
6. 如果无法测试，说明原因和替代验证路径。

### Outputs

- Feedback Loop。
- Test Report。
- Manual Verification。
- Missing Tests。

### Quality Gate

进入 Review 前应满足：

- 至少有一种明确 pass/fail 信号。
- 验收标准有对应验证方式。
- 未覆盖测试已说明原因。

---

## 9. Stage 7: Review

### Purpose

审计编程智能体的执行结果，判断是否可交付。

### Inputs

- 原任务包。
- Code diff。
- Implementation Summary。
- Test Results。
- Repo context。

### Review Axes

1. 需求符合度。
2. 正确性。
3. 架构一致性。
4. 安全与权限。
5. 数据与存储。
6. 性能与资源。
7. 测试证据。
8. 兼容性。
9. 可维护性。
10. 文档与记忆沉淀。

### Verdict

```text
PASS：可以交付。
NEEDS_FIX：需要修复后再交付。
REJECT：方向错误或风险过高，应回退或重做。
```

### Issue Severity

```text
Critical：必须修，不修不能合并。
Important：建议修，除非明确延期。
Optional：可选优化。
FYI：仅记录。
```

### Outputs

- Review Report。
- Verdict。
- Required Fixes。
- Fix Prompt。

### Quality Gate

进入 Ship 前必须：

- Verdict 为 PASS，或人类明确接受 Important 风险延期。
- Critical 问题已解决。

---

## 10. Stage 8: Ship

### Purpose

完成交付总结。

### Inputs

- Review Report。
- Final diff。
- Test Results。
- 用户确认。

### Actions

1. 总结本次完成内容。
2. 总结测试证据。
3. 总结风险。
4. 总结延期事项。
5. 判断是否需要更新项目文档。
6. 判断是否需要 ADR。
7. 生成交付报告。

### Outputs

- Ship Report。
- Changelog entry。
- Follow-up list。

### Quality Gate

进入 Memory 前应满足：

- 交付内容可追踪。
- 风险和延期事项已记录。
- 后续动作明确。

---

## 11. Stage 9: Memory

### Purpose

让项目从本次任务中学习。

### Inputs

- Ship Report。
- Review Report。
- 重要决策。
- 新术语。
- 技术债。

### Actions

判断是否需要更新：

```text
.ai/project/AI_PROJECT_MEMORY.md
.ai/project/AI_DOMAIN_CONTEXT.md
.ai/project/AI_CONTEXT_MAP.md
.ai/decisions/
.ai/changelog/
.ai/tasks/
.ai/reviews/
```

### What Should Be Remembered

应该沉淀：

- 长期有效的架构约定。
- 重要领域术语。
- 明确不做的事情。
- 被拒绝的重要方案和原因。
- 已延期技术债。
- 常见坑。
- 高风险模块。
- 未来触发条件。

不应该沉淀：

- 临时聊天内容。
- 已过期的中间讨论。
- 没有长期价值的过程细节。
- 重复信息。

### Outputs

- Project Memory update。
- Domain Context update。
- ADR。
- Changelog。

---

## 12. Workflow Shortcuts

不是所有任务都需要完整 0-9 阶段。

### Tiny Change

适用于轻微文案、注释、样式修正：

```text
Context → Prompt → Build → Verify → Review
```

### Bug Fix

```text
Context → Diagnose → Verify → Build → Verify → Review → Ship
```

### New Feature

```text
Context → Define → Spec → Plan → Prompt → Build → Verify → Review → Ship → Memory
```

### Architecture Refactor

```text
Context → Define → Spec → Plan → Prompt → Build by slices → Verify → Review → ADR → Memory
```

### Existing PR Review

```text
Context → Review → Fix Prompt → Verify → Ship
```

---

## 13. Anti-Patterns

禁止以下交付方式：

### 13.1 Prompt-and-pray

```text
用户说一句
→ AI 直接改一堆代码
→ 没有验收
→ 没有测试
→ 没有审计
```

### 13.2 Big bang rewrite

```text
一次性重写大量模块
→ 中途不可运行
→ 无法审计
→ 难以回滚
```

### 13.3 Hidden scope creep

```text
任务是 A
→ AI 顺手做 B、C、D
→ 用户难以判断风险
```

### 13.4 Test theater

```text
AI 声称测试通过
→ 没有命令
→ 没有输出
→ 没有覆盖验收标准
```

### 13.5 Memory pollution

```text
把所有讨论都塞进项目记忆
→ 后续 AI 读到大量噪音
```

---

## 14. Final Principle

AI 工程交付不是“让模型更会写代码”，而是让每一次代码改动都具备：

```text
清晰上下文
明确问题
可控范围
小步执行
可验证证据
独立审计
长期沉淀
```
