# Skill: Review Quality Gate

## Purpose

对编程智能体的执行结果、diff、PR、测试结果和修改摘要进行独立审计，判断是否可以交付。

本 skill 是 AI Engineering Delivery OS 的质量门。

---

## When to Use

当用户提供以下内容时使用：

- git diff。
- PR 链接。
- commit。
- 修改摘要。
- 测试结果。
- 编程智能体完成报告。
- 用户要求“帮我审计”“看看有没有问题”。

---

## Core Principle

不要只看“能不能跑”。

必须同时审计：

```text
需求符合度
正确性
架构一致性
安全与权限
数据与存储
性能与资源
测试证据
兼容性
可维护性
文档沉淀
```

---

## Required Inputs

必须尽量获取：

- 原任务包。
- 修改文件列表。
- diff / PR。
- 测试命令。
- 测试结果。
- 实现摘要。

建议读取：

```text
.ai/templates/REVIEW_REPORT_TEMPLATE.md
.ai/system/AI_AGENT_RULES.md
.ai/project/AI_REPO_CONTEXT.md
.ai/project/AI_DOMAIN_CONTEXT.md
```

按需读取：

```text
.ai/references/SECURITY_CHECKLIST.md
.ai/references/TESTING_CHECKLIST.md
.ai/references/PERFORMANCE_CHECKLIST.md
.ai/references/API_INTERFACE_CHECKLIST.md
.ai/references/DATABASE_MIGRATION_CHECKLIST.md
.ai/references/FRONTEND_UX_CHECKLIST.md
.ai/references/ANTI_OVERENGINEERING_RULES.md
```

---

## Verdicts

### PASS

可以交付。

条件：

- 完成原目标。
- 无 Critical 问题。
- 无明显无关改动。
- 测试或验证证据足够。
- 风险可接受。

### NEEDS_FIX

需要修复后再交付。

条件：

- 大方向正确。
- 存在可修复问题。
- 没有必要整体回退。

### REJECT

不建议交付，应回退或重做。

条件：

- 方向明显错误。
- 大量无关改动。
- 破坏核心架构。
- 存在严重安全/数据风险。
- 无法通过小修复补救。

---

## Severity Levels

```text
Critical：必须修，不修不能合并。
Important：建议修，除非人类明确接受延期。
Optional：可选优化。
FYI：仅记录。
```

---

## Workflow

### Step 1: Summarize Original Task

```markdown
## 1. Original Task Summary

- Task: ...
- Goals: ...
- Non-goals: ...
- Acceptance Criteria: ...
```

---

### Step 2: Summarize Submitted Changes

```markdown
## 2. Submitted Changes

### Modified Files
- ...

### Added Files
- ...

### Deleted Files
- ...
```

---

### Step 3: Goal Completion Check

```markdown
## 3. Goal Completion Check

| Goal | Status | Evidence | Notes |
|---|---|---|---|
| ... | Done / Partial / Missing | ... | ... |
```

---

### Step 4: Scope Check

检查是否改多。

```markdown
## 4. Scope Check

- 是否存在无关改动：Yes / No
- 是否存在过度重构：Yes / No
- 是否改变无关 API：Yes / No
- 是否引入新依赖：Yes / No
```

---

### Step 5: Risk Review

必须覆盖：

```markdown
## 5. Risk Review

### Correctness

### Architecture

### Security / Permission

### Data / Storage

### Performance

### Compatibility

### Maintainability
```

---

### Step 6: Test Review

```markdown
## 6. Test Review

- Tests claimed: ...
- Tests actually evidenced: ...
- Missing tests: ...
- Manual verification: ...
```

---

### Step 7: Documentation / Memory Review

判断是否需要更新：

- `AI_REPO_CONTEXT.md`
- `AI_DOMAIN_CONTEXT.md`
- `AI_PROJECT_MEMORY.md`
- ADR。
- changelog。

---

### Step 8: Verdict and Fix Prompt

```markdown
## 8. Verdict

Verdict: PASS / NEEDS_FIX / REJECT

## 9. Required Fixes

| Severity | Issue | Required Fix |
|---|---|---|

## 10. Fix Prompt for Coding Agent

```markdown
# Fix Task
...
```
```

---

## Output Format

```markdown
# Review Quality Gate Report

## 1. Verdict

Verdict: PASS / NEEDS_FIX / REJECT

## 2. Original Task Summary

## 3. Submitted Changes

## 4. Goal Completion Check

| Goal | Status | Evidence | Notes |
|---|---|---|---|

## 5. Scope Check

## 6. Risk Review

### Correctness
### Architecture
### Security / Permission
### Data / Storage
### Performance
### Compatibility
### Maintainability

## 7. Test Review

## 8. Documentation / Memory Review

## 9. Issues by Severity

### Critical
- ...

### Important
- ...

### Optional
- ...

### FYI
- ...

## 10. Required Fixes

## 11. Fix Prompt for Coding Agent
```

---

## Quality Bar

好的审计应该：

- 对照原任务，而不是只看代码风格。
- 明确 verdict。
- 标注严重等级。
- 能指出无关改动。
- 能检查权限、安全、数据和测试。
- 能生成可执行修复 Prompt。

---

## Anti-patterns

禁止：

- 只说“看起来不错”。
- 只关注格式，不关注业务正确性。
- 忽略 Non-goals。
- 忽略权限和数据风险。
- 没有明确 verdict。
- 批评问题但不给修复路径。

---

## Handoff

审计结果：

- PASS → `ship-and-record`。
- NEEDS_FIX → `execution-prompt-compiler` 或直接输出 Fix Prompt。
- REJECT → 回到 `spec-before-code` 或 `plan-to-slices`。
