# Skill: TDD Feedback Loop

## Purpose

为新功能、Bug 修复、重构和复杂改动建立可重复的 pass/fail 验证信号。

本 skill 的核心目标是：不要靠感觉判断代码是否正确，而是建立能证明行为正确的反馈循环。

---

## When to Use

当出现以下情况时使用：

- 需要为新功能设计测试。
- Bug 修复需要 regression test。
- 编程智能体完成代码但测试证据不足。
- 用户要求“怎么验证”“怎么测试”。
- 改动涉及权限、数据、文件、API、核心业务逻辑。
- 审计时发现缺少测试或验证路径。

---

## Core Principle

先定义行为，再写验证。

不要测试实现细节，优先测试用户可观察行为和公共接口。

反馈循环应满足：

```text
可重复
可自动化优先
失败时能定位方向
覆盖正常与异常路径
和验收标准对应
```

---

## Required Inputs

建议读取：

```text
.ai/templates/FEEDBACK_LOOP_TEMPLATE.md
.ai/references/TESTING_CHECKLIST.md
.ai/project/AI_REPO_CONTEXT.md
```

如已有任务包，读取：

```text
.ai/tasks/<current-task>/04-exec-prompt.md
```

如已有实现，读取：

- diff。
- 修改摘要。
- 测试结果。
- 相关测试文件。

---

## Workflow

### Step 1: Extract Behaviors to Verify

从验收标准提取要验证的行为。

```markdown
## 1. Behaviors to Verify

| Behavior | Source Acceptance Criteria | Priority |
|---|---|---|
| ... | ... | High / Medium / Low |
```

---

### Step 2: Choose Feedback Type

选择验证方式。

| Feedback Type | Use When |
|---|---|
| Unit Test | 纯逻辑、函数、工具、状态转换 |
| Integration Test | API、数据库、服务协作 |
| E2E Test | 用户路径、前端交互 |
| Manual Verification | 自动测试成本过高或当前无测试框架 |
| Log / Diagnostic Check | 临时排查或生产问题 |

---

### Step 3: Define Normal Paths

```markdown
## 3. Normal Path Tests

| Scenario | Steps | Expected Result |
|---|---|---|
```

---

### Step 4: Define Edge / Failure Paths

至少考虑：

- 空数据。
- 无权限。
- 无效输入。
- 重复提交。
- 外部服务失败。
- 大数据量。
- 超时。
- 文件不存在。
- 数据库写入失败。

---

### Step 5: Define Regression Coverage

如果是 bug 修复，必须回答：

```markdown
## 5. Regression Test

- 之前如何失败：...
- 修复后如何证明不会再失败：...
- 测试位置：...
```

如果无法补 regression test，说明原因。

---

### Step 6: Map Tests to Commands

```markdown
## 6. Test Commands

```bash
# command here
```

Expected result: ...
```

---

### Step 7: Identify Missing Seams

如果测试很难写，可能是代码缺少测试 seam。

```markdown
## 7. Missing Test Seams

| Missing Seam | Impact | Suggested Future Refactor |
|---|---|---|
```

不要为了测试一次任务而大重构，但要记录技术债。

---

## Output Format

```markdown
# Feedback Loop Plan

## 1. Behaviors to Verify

| Behavior | Acceptance Criteria | Priority |
|---|---|---|

## 2. Feedback Strategy

| Behavior | Test Type | Why |
|---|---|---|

## 3. Normal Path Tests

| Scenario | Steps | Expected Result |
|---|---|---|

## 4. Edge / Failure Path Tests

| Scenario | Steps | Expected Result |
|---|---|---|

## 5. Regression Tests

- ...

## 6. Test Commands

```bash
...
```

## 7. Manual Verification

- ...

## 8. Missing Test Seams / Technical Debt

- ...
```

---

## Quality Bar

好的反馈循环应该：

- 和验收标准一一对应。
- 至少覆盖正常路径和关键异常路径。
- 能重复运行。
- 尽量通过公共接口验证行为。
- Bug 修复有 regression 思路。
- 无法自动化时提供明确手动验证路径。

---

## Anti-patterns

禁止：

- 只说“测试通过”但不给命令。
- 只测试 happy path。
- 测实现细节而非行为。
- Bug 修复没有 regression 验证。
- 没有说明无法运行测试的原因。
- 为了测试引入大规模无关重构。

---

## Handoff

完成后交给：

- `incremental-build`：根据测试计划实现。
- `review-quality-gate`：审计测试证据是否足够。
- `ship-and-record`：沉淀测试经验或缺失 seam。
