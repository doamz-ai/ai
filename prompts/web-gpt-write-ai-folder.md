# Prompt: Web GPT Write to AI Folder Only

用途：当你在网页版 GPT 中讨论出方案、PRD、计划或任务包后，让 GPT 只把产物写入目标项目 GitHub 的 `.ai/` 目录，用作传递给 IDE 智能体的工程上下文。

---

```markdown
请作为远程军师模型，把本次讨论产物写入目标项目 GitHub 的 `.ai/` 目录。

请严格遵守以下规则。

## 1. Repository

目标仓库：`[owner/repo]`
目标分支：`[branch]`

如果没有指定分支，优先创建新分支：

```text
ai/plan/[task-name]
```

## 2. Allowed Scope

你只能创建或更新 `.ai/` 目录内的文件。

允许路径示例：

```text
.ai/tasks/[task-name]/00-idea.md
.ai/tasks/[task-name]/01-clarity.md
.ai/tasks/[task-name]/02-prd.md
.ai/tasks/[task-name]/03-plan.md
.ai/tasks/[task-name]/04-exec-prompt.md
.ai/tasks/[task-name]/05-review-notes.md
.ai/tasks/[task-name]/06-ship-report.md

.ai/reviews/[review-name].md
.ai/decisions/ADR-xxxx.md
.ai/changelog/[date]-[task-name].md
```

## 3. Forbidden Scope

你绝对不能修改 `.ai/` 目录之外的任何文件。

禁止修改：

```text
src/
app/
backend/
frontend/
api/
server/
client/
packages/
lib/
components/
pages/
routes/
db/
migrations/
config/
.env*
package.json
README.md outside .ai/
任何业务代码、配置、数据库迁移、部署文件
```

## 4. Content Type

本次只写入以下工程上下文，不写业务代码：

- 想法澄清。
- PRD。
- RFC。
- 任务切片。
- 给 IDE / 编程智能体的执行 Prompt。
- 审计笔记。
- 交付总结。
- ADR 草案。

## 5. Proposal Not Command

写入 `.ai/` 的内容默认是 Proposal，不是强制命令。

请在文档顶部加入：

```text
Status: Proposal
Source: Web GPT discussion
Requires IDE repo reality check before code changes
```

## 6. Required File Structure

请为本次任务创建目录：

```text
.ai/tasks/[YYYY-MM-DD]-[short-task-name]/
```

至少写入：

```text
00-idea.md
01-clarity.md
03-plan.md
04-exec-prompt.md
```

如果当前讨论足够完整，也可以写入：

```text
02-prd.md
05-review-notes.md
06-ship-report.md
```

## 7. IDE Handoff Section

每个任务目录中必须包含给 IDE 的交接说明：

```markdown
# IDE Handoff

## Required IDE Review

Before modifying business code, IDE agent must review this proposal against real repository code and output:

- ACCEPT
- ACCEPT_WITH_CHANGES
- NEEDS_CLARIFICATION
- REJECT

## IDE Must Check

1. Does this plan match current repo structure?
2. Is there a smaller safer implementation?
3. Are there missing permission/data/testing/performance risks?
4. Does the execution prompt need adjustment?
```

## 8. Output Required

完成写入后，请输出：

```markdown
# AI Folder Write Report

## Repository

## Branch

## Files Created / Updated

## Files Not Touched

## Business Code Modified

Must be: None

## Next Step for IDE

```
```
