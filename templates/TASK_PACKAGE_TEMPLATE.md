# Task Package Template

本模板用于生成可直接交给编程智能体执行的工程任务包。

---

# Task

请基于当前 GitHub 仓库完成以下工程任务：

```text
[一句话任务描述]
```

---

# Background

## Business Context

```text
[为什么要做这个任务，它解决什么业务问题]
```

## Engineering Context

```text
[当前系统现状、相关模块、已有约束]
```

---

# Requirement Maturity

- Level: L0 / L1 / L2 / L3 / L4
- Reason:

```text
[为什么当前任务已经适合或不适合执行]
```

---

# Repo Evidence

## Confirmed

| Fact | Evidence |
|---|---|
| [已确认事实] | [文件/模块/代码路径] |

## To Verify Before Editing

| Item | Why It Matters | Suggested Location |
|---|---|---|
| [待确认项] | [原因] | [路径/搜索关键词] |

## Assumptions

| Assumption | Impact If Wrong | How to Validate |
|---|---|---|
| [假设] | [影响] | [验证方式] |

---

# Goals

本次必须完成：

1. [目标 1]
2. [目标 2]
3. [目标 3]

---

# Non-goals

本次明确不做：

1. [非目标 1]
2. [非目标 2]
3. [非目标 3]

---

# Scope

## In Scope

- [本次范围内]

## Out of Scope

- [本次范围外]

## Reserved for Future

- [仅预留，不实现]

---

# Files / Modules to Inspect First

| Path / Module | Reason |
|---|---|
| `[path]` | [为什么要先看这里] |
| 待定位：[关键词] | [如果路径未知，先搜索定位，不要新建重复模块] |

---

# Implementation Requirements

## Backend

- [后端要求]

## Frontend

- [前端要求]

## Database / Storage

- [数据库或存储要求]

## Permission / Security

- [权限和安全要求]

## Testing

- [测试要求]

## Documentation

- [文档要求]

---

# Constraints

请严格遵守：

1. 不要做无关重构。
2. 不要修改与任务无关的文件。
3. 不要引入不必要的新依赖。
4. 不要重复创建仓库中已有能力。
5. 不要绕过现有权限和架构边界。
6. 不要改变旧 API 返回结构，除非本任务明确要求。
7. 不要把未来规划提前完整实现。
8. 不要把临时方案写死为长期架构。

---

# Acceptance Criteria

完成后必须满足：

1. 当 [场景 A] 时，系统应该 [结果 A]。
2. 当 [异常场景 B] 时，系统应该 [结果 B]。
3. 当 [权限场景 C] 时，系统应该 [结果 C]。
4. 现有相关功能仍然正常。
5. 提供测试或手动验证说明。

---

# Required Final Response From Coding Agent

完成后请输出：

```markdown
# Implementation Summary

## Modified Files
- `path`: reason

## Added Files
- `path`: reason

## Deleted Files
- `path`: reason

## Database / Migration Changes
- None / ...

## Environment Variable Changes
- None / ...

## Tests Run
- Command: ...
- Result: ...

## Manual Verification
- ...

## Known Risks
- ...

## Deferred Technical Debt
- ...

## Follow-up Suggestions
- ...
```
