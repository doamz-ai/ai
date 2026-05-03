# Skill: Incremental Build

## Purpose

指导编程智能体按照任务包进行小步、可验证、可回滚的增量实现，避免一次性大改造成不可控风险。

本 skill 面向实际写代码的执行阶段。

---

## When to Use

当出现以下情况时使用：

- 编程智能体准备根据任务包修改代码。
- 任务涉及多个文件或多个模块。
- 任务需要保持系统持续可运行。
- 用户要求“按步骤实现”“不要乱改”。
- 任务已经通过 `execution-prompt-compiler` 生成执行 Prompt。

通常对应模式：

```text
Build Mode
```

---

## Core Principle

不要一次性大改。

正确方式是：

```text
定位现有实现
→ 做最小必要改动
→ 验证当前切片
→ 再进入下一个切片
→ 最后补测试、文档和清理
```

每个增量都应尽量满足：

```text
可运行
可测试
可审计
可回滚
```

---

## Required Inputs

必须读取：

```text
.ai/system/AI_AGENT_RULES.md
.ai/tasks/<current-task>/04-exec-prompt.md
```

建议读取：

```text
.ai/project/AI_REPO_CONTEXT.md
.ai/project/AI_DOMAIN_CONTEXT.md
.ai/project/AI_PROJECT_MEMORY.md
```

如任务涉及特定风险，读取对应 checklist：

```text
.ai/references/SECURITY_CHECKLIST.md
.ai/references/TESTING_CHECKLIST.md
.ai/references/API_INTERFACE_CHECKLIST.md
.ai/references/DATABASE_MIGRATION_CHECKLIST.md
.ai/references/FRONTEND_UX_CHECKLIST.md
.ai/references/PERFORMANCE_CHECKLIST.md
```

---

## Workflow

### Step 1: Read and Restate the Task

在改代码前，先确认：

```markdown
## 1. Task Understanding

- Task: ...
- Goals: ...
- Non-goals: ...
- Acceptance Criteria: ...
- Files / modules to inspect: ...
```

如果无法明确 Goals 或 Non-goals，停止并报告阻塞。

---

### Step 2: Locate Existing Implementation

先找现有模式，不要直接新建。

```markdown
## 2. Existing Implementation

| Area | Existing Path | Pattern to Reuse |
|---|---|---|
| ... | ... | ... |
```

必须确认：

- 是否已有类似 API。
- 是否已有类似组件。
- 是否已有 service / utility。
- 是否已有权限检查模式。
- 是否已有测试模式。

---

### Step 3: Define Micro-plan

把当前任务拆成小步骤。

```markdown
## 3. Micro-plan

1. ...
2. ...
3. ...
```

每一步应尽量小到可以单独验证。

---

### Step 4: Implement the Smallest Useful Change

优先完成最小闭环。

规则：

- 不要同时改太多层。
- 不要引入无关重构。
- 不要提前抽象未来需求。
- 不要顺手修 unrelated tech debt。

如果发现旁边问题，记录到 Deferred Technical Debt。

---

### Step 5: Verify After Each Important Step

每个关键增量后检查：

- 是否能编译 / 启动。
- 是否破坏旧接口。
- 是否有明显类型错误。
- 是否有权限遗漏。
- 是否满足当前 slice 的验收。

---

### Step 6: Add or Update Tests

根据任务性质：

- 新行为：补测试或验证路径。
- Bug 修复：尽量补 regression test。
- 权限逻辑：补无权限路径。
- API：补正常/异常参数。
- 前端：补手动验证路径或组件测试。

---

### Step 7: Final Self-check

提交前自查：

```markdown
## 7. Self-check

- [ ] 是否只改了相关文件？
- [ ] 是否复用了现有模式？
- [ ] 是否没有引入不必要依赖？
- [ ] 是否没有绕过权限？
- [ ] 是否没有改变无关 API？
- [ ] 是否有测试或验证说明？
- [ ] 是否记录了风险和延期技术债？
```

---

## Output Format

编程智能体完成后必须输出：

```markdown
# Implementation Summary

## 1. What changed

- ...

## 2. Modified files

| File | Reason |
|---|---|
| ... | ... |

## 3. Added files

| File | Reason |
|---|---|
| ... | ... |

## 4. Deleted files

| File | Reason |
|---|---|
| ... | ... |

## 5. Database / migration changes

- None / ...

## 6. Environment variable changes

- None / ...

## 7. Tests run

- Command: ...
- Result: ...

## 8. Manual verification

- ...

## 9. Known risks

- ...

## 10. Deferred technical debt

- ...

## 11. Follow-up suggestions

- ...
```

---

## Quality Bar

好的增量实现应该：

- 严格遵守任务包。
- 改动范围小而清晰。
- 复用现有模式。
- 每个关键改动有验证。
- 无明显无关重构。
- 完成报告可供审计。

---

## Anti-patterns

禁止：

- 一次性重写大量代码。
- 未定位现有模式就新建模块。
- 顺手修无关问题。
- 没有测试或验证说明。
- 修改旧 API 却不说明兼容性。
- 为未来能力提前引入复杂抽象。
- 任务失败后继续盲改。

---

## If Blocked

如果遇到阻塞，不要继续猜。

输出：

```markdown
# Blocked Report

## Where I got blocked

## What I confirmed

## What I tried

## Error / logs

## Possible causes

## Recommended next step
```

---

## Handoff

完成后交给：

- `tdd-feedback-loop`：补充或审查验证证据。
- `review-quality-gate`：审计 diff 和实现报告。
- `ship-and-record`：通过审计后沉淀交付结果。
