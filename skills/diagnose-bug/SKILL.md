# Skill: Diagnose Bug

## Purpose

用可重复反馈循环诊断 bug、报错、测试失败和异常行为，避免 AI 通过猜测盲改代码。

本 skill 的核心目标是：先复现、再假设、再收集证据、再最小修复、最后回归验证。

---

## When to Use

当出现以下情况时使用：

- 用户提供报错信息。
- 测试失败。
- 线上或本地行为异常。
- 编程智能体修复失败。
- 用户说“这里为什么不对？”
- 审计发现实现结果与预期不一致。

---

## Core Principle

不要猜。

正确诊断顺序：

```text
Reproduce
→ Minimize
→ Establish Feedback Loop
→ Hypothesize
→ Inspect Evidence
→ Fix Smallest Cause
→ Regression Test
```

---

## Required Inputs

尽量收集：

- 错误信息。
- 操作步骤。
- 期望结果。
- 实际结果。
- 相关 diff。
- 测试命令和失败输出。
- 运行环境。
- 相关日志。

建议读取：

```text
.ai/project/AI_REPO_CONTEXT.md
.ai/templates/FEEDBACK_LOOP_TEMPLATE.md
.ai/references/TESTING_CHECKLIST.md
```

如涉及安全、权限、数据或性能，读取对应 checklist。

---

## Workflow

### Step 1: Restate the Failure

```markdown
## 1. Failure Summary

- Expected: ...
- Actual: ...
- Error / symptom: ...
- Where it happens: ...
```

---

### Step 2: Reproduce

确认是否能复现。

```markdown
## 2. Reproduction

| Step | Action | Result |
|---|---|---|
```

如果无法复现，列出还缺什么信息。

---

### Step 3: Minimize

缩小问题范围。

```markdown
## 3. Minimal Case

- Minimal input: ...
- Minimal route / function / command: ...
- Minimal files involved: ...
```

---

### Step 4: Establish Feedback Loop

定义 pass/fail 信号。

```markdown
## 4. Feedback Loop

- Failing command / action: ...
- Current failure signal: ...
- Expected pass signal: ...
```

没有反馈循环，不要进入修复。

---

### Step 5: Generate Hypotheses

提出少量假设，并标注证据。

```markdown
## 5. Hypotheses

| Hypothesis | Evidence For | Evidence Against | Confidence |
|---|---|---|---|
```

---

### Step 6: Inspect Evidence

检查相关代码、配置、数据、日志。

```markdown
## 6. Evidence Inspection

| Area | Finding | Evidence |
|---|---|---|
```

---

### Step 7: Root Cause

如果能确定根因，写明。

如果不能，写：

```text
Root cause not fully confirmed. Best current hypothesis is ...
```

---

### Step 8: Fix Plan

修复计划必须最小化。

```markdown
## 8. Fix Plan

1. ...
2. ...
3. ...
```

避免：

- 顺手重构。
- 扩大问题范围。
- 修改无关模块。
- 引入新依赖。

---

### Step 9: Regression Test

Bug 修复必须尽量补回归验证。

```markdown
## 9. Regression Test

- Test case: ...
- Why it would fail before: ...
- Why it should pass after: ...
```

如无法补测试，说明原因和未来 seam。

---

## Output Format

```markdown
# Diagnose Bug Report

## 1. Failure Summary

## 2. Reproduction

## 3. Minimal Case

## 4. Feedback Loop

## 5. Hypotheses

| Hypothesis | Evidence For | Evidence Against | Confidence |
|---|---|---|---|

## 6. Evidence Inspection

## 7. Root Cause

## 8. Fix Plan

## 9. Regression Test

## 10. Fix Prompt for Coding Agent
```

---

## Quality Bar

好的诊断应该：

- 能复述失败现象。
- 能说明如何复现。
- 有 pass/fail 信号。
- 假设有证据支撑。
- 修复计划最小化。
- 有回归测试或验证路径。

---

## Anti-patterns

禁止：

- 看见报错就直接改代码。
- 同时改多个可疑点。
- 没有复现就声称修复。
- 没有回归验证。
- 把 bug 修复变成重构。
- 忽略环境和配置差异。

---

## Handoff

完成后交给：

- `execution-prompt-compiler`：生成修复 Prompt。
- `incremental-build`：执行最小修复。
- `tdd-feedback-loop`：补回归验证。
- `review-quality-gate`：审计修复结果。
