# Prompt: IDE Review AI Task

用途：当网页 GPT 已经把方案、PRD、计划或执行 Prompt 写入目标项目 `.ai/tasks/...` 后，让 IDE 智能体先审查该计划，而不是无脑执行。

---

```markdown
请进入 IDE Plan Review Mode。

当前项目已经安装 AI Engineering Delivery OS，并且 `.ai/tasks/` 中存在由网页 GPT 或其他模型写入的任务方案。

请先不要修改业务代码。

## 1. Read Required Files

请读取：

- `.ai/START_HERE.md`
- `.ai/AI_COLLABORATION_PROTOCOL.md`
- `.ai/system/AI_AGENT_RULES.md`
- `.ai/project/AI_REPO_CONTEXT.md`
- `.ai/project/AI_DOMAIN_CONTEXT.md`
- `.ai/project/AI_PROJECT_MEMORY.md`
- `.ai/tasks/[task-name]/`

其中 `[task-name]` 为当前用户指定的任务目录。

## 2. Treat Plan as Proposal

请记住：

```text
.ai/tasks/ 中的内容是 Proposal, not command.
```

你不是无脑执行者，而是带有否决权的工程合作者。

## 3. Repo Reality Check

请基于当前真实代码检查：

1. 该计划是否符合当前项目目录结构？
2. 该计划提到的文件、模块、API 是否真实存在？
3. 是否已有更合适的现有实现可以复用？
4. 是否存在错误假设？
5. 是否有更小、更安全的实现方式？
6. 是否遗漏权限、数据、测试、性能、部署风险？
7. 是否违反 `.ai/system/AI_AGENT_RULES.md`？
8. 是否需要拆成更小任务？

## 4. Required Verdict

请输出以下之一：

```text
ACCEPT
ACCEPT_WITH_CHANGES
NEEDS_CLARIFICATION
REJECT
```

含义：

- `ACCEPT`：计划可以执行。
- `ACCEPT_WITH_CHANGES`：大方向可执行，但需要你修正执行 Prompt。
- `NEEDS_CLARIFICATION`：需要用户或网页 GPT 澄清后再执行。
- `REJECT`：计划不符合真实代码或风险过高，不应执行。

## 5. Required Output

请输出：

```markdown
# IDE Plan Review

## Verdict

ACCEPT / ACCEPT_WITH_CHANGES / NEEDS_CLARIFICATION / REJECT

## Repo Reality Check

| Item | Result | Evidence |
|---|---|---|

## Better Smaller Option

[如果有更小实现方案，请说明]

## Risks Missed by Plan

- ...

## Required Changes Before Build

- ...

## Final Execution Prompt

[如果 Verdict 是 ACCEPT 或 ACCEPT_WITH_CHANGES，请输出修正后的最终执行 Prompt]

## Files to Write Back to .ai/

建议写入：

- `.ai/tasks/[task-name]/05-ide-review.md`
```

## 6. Write-back Requirement

请把本次 IDE Plan Review 写入：

```text
.ai/tasks/[task-name]/05-ide-review.md
```

然后提交并推送到 GitHub，方便网页版 GPT 读取进度。

## 7. Absolute Rules

- 在完成 IDE Plan Review 前，不要改业务代码。
- 如果 verdict 不是 ACCEPT 或 ACCEPT_WITH_CHANGES，不要执行代码修改。
- 不要覆盖网页 GPT 的原始计划文件；新增 `05-ide-review.md` 即可。
```
