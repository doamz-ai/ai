# Prompt: IDE Progress Report to AI Folder

用途：当 IDE 智能体执行任务后，把执行进度、修改摘要、测试结果、风险和未完成事项回写到 `.ai/tasks/...`，方便网页版 GPT 下次连接 GitHub 时继续辅助。

---

```markdown
请进入 IDE Progress Report Mode。

你已经根据 `.ai/tasks/[task-name]/` 中的任务进行了审查或执行。

请把当前进度回写到 `.ai/tasks/[task-name]/`，方便网页版 GPT 后续读取。

## 1. Required Inputs

请基于当前真实执行情况总结：

- IDE plan review 结果。
- 是否执行了代码修改。
- 修改了哪些文件。
- 新增了哪些文件。
- 删除了哪些文件。
- 是否有数据库 / migration 变化。
- 是否有环境变量变化。
- 运行了哪些测试。
- 测试结果如何。
- 还有哪些风险。
- 还有哪些开放问题。

## 2. Files to Write

请根据实际情况创建或更新：

```text
.ai/tasks/[task-name]/05-ide-review.md
.ai/tasks/[task-name]/06-implementation-summary.md
.ai/tasks/[task-name]/07-test-results.md
.ai/tasks/[task-name]/08-open-issues.md
.ai/tasks/[task-name]/STATUS.md
```

如果某个文件暂时不适用，可以不创建，但必须说明原因。

## 3. STATUS.md Format

```markdown
# Task Status

Status: PROPOSAL / READY_FOR_IDE_REVIEW / ACCEPTED_BY_IDE / IN_PROGRESS / NEEDS_FIX / SHIPPED / ARCHIVED

Last Updated: YYYY-MM-DD
Updated By: IDE Agent

## Current Summary

...

## Next Step

...
```

## 4. Implementation Summary Format

```markdown
# Implementation Summary

## Executed

Yes / No / Partial

## Modified Files

| File | Reason |
|---|---|

## Added Files

| File | Reason |
|---|---|

## Deleted Files

| File | Reason |
|---|---|

## Database / Migration Changes

- None / ...

## Environment Variable Changes

- None / ...

## Known Risks

- ...

## Deferred Technical Debt

- ...
```

## 5. Test Results Format

```markdown
# Test Results

## Automated Tests

| Command | Result | Notes |
|---|---|---|

## Manual Verification

- ...

## Not Tested

| Item | Reason | Risk |
|---|---|---|
```

## 6. Open Issues Format

```markdown
# Open Issues

| Issue | Severity | Owner | Suggested Next Step |
|---|---|---|---|
```

## 7. Commit and Push

写入 `.ai/tasks/[task-name]/` 后，请提交并推送到 GitHub。

Commit message 建议：

```text
docs: update AI task progress for [task-name]
```

## 8. Absolute Rules

- 不要把进度只留在聊天窗口。
- 不要覆盖原始 PRD / Plan，除非用户明确要求。
- 不要隐瞒测试未运行的情况。
- 不要声称完成但不写测试结果。
```
