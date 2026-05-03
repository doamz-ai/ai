# Review Report Template

本模板用于审计编程智能体的执行结果、diff、PR 或修改摘要。

---

# Review Report: [Task / PR Name]

## 1. Verdict

```text
PASS / NEEDS_FIX / REJECT
```

### Verdict Reason

```text
[简要说明原因]
```

---

## 2. Original Task Summary

### Task

```text
[原任务]
```

### Goals

1. [目标 1]
2. [目标 2]

### Non-goals

1. [非目标 1]
2. [非目标 2]

---

## 3. Submitted Changes

### Modified Files

| File | Claimed Purpose | Review Notes |
|---|---|---|
| `[path]` | [用途] | [备注] |

### Added Files

| File | Purpose | Review Notes |
|---|---|---|
| `[path]` | [用途] | [备注] |

### Deleted Files

| File | Reason | Review Notes |
|---|---|---|
| `[path]` | [原因] | [备注] |

---

## 4. Goal Completion Check

| Goal | Status | Evidence | Notes |
|---|---|---|---|
| [目标] | Done / Partial / Missing | [证据] | [备注] |

---

## 5. Scope Check

| Check | Result | Notes |
|---|---|---|
| 是否有无关改动 | Yes / No | [备注] |
| 是否有过度重构 | Yes / No | [备注] |
| 是否改变无关 API | Yes / No | [备注] |
| 是否引入新依赖 | Yes / No | [备注] |
| 是否违反 Non-goals | Yes / No | [备注] |

---

## 6. Risk Review

### 6.1 Correctness

```text
[正确性风险]
```

### 6.2 Architecture

```text
[架构一致性风险]
```

### 6.3 Security / Permission

```text
[权限和安全风险]
```

### 6.4 Data / Storage

```text
[数据和存储风险]
```

### 6.5 Performance

```text
[性能风险]
```

### 6.6 Compatibility

```text
[兼容性风险]
```

### 6.7 Maintainability

```text
[可维护性风险]
```

---

## 7. Test Review

| Claimed Test | Evidence | Result | Notes |
|---|---|---|---|
| [测试] | [命令/截图/日志] | Pass / Fail / Unknown | [备注] |

### Missing Tests

- [缺失测试]

### Manual Verification

- [手动验证]

---

## 8. Issues by Severity

### Critical

- [必须修，不修不能合并]

### Important

- [建议修，除非明确延期]

### Optional

- [可选优化]

### FYI

- [仅记录]

---

## 9. Required Fixes

| Priority | Issue | Required Fix | Acceptance |
|---|---|---|---|
| Critical / Important | [问题] | [修复要求] | [验收] |

---

## 10. Fix Prompt for Coding Agent

```markdown
# Fix Task

请修复上一轮实现中的以下问题：

1. [问题 1]
2. [问题 2]

约束：

- 不要重构无关模块。
- 不要改变已正确实现的部分。
- 不要引入不必要依赖。
- 修复后重新说明修改文件和测试结果。

验收：

1. ...
```

---

## 11. Documentation / Memory Suggestions

### Update AI_PROJECT_MEMORY.md

- [建议]

### Update AI_DOMAIN_CONTEXT.md

- [建议]

### ADR Needed

```text
Yes / No
Reason: ...
```
