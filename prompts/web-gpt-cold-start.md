# Prompt: Web GPT Cold Start

用途：当用户在网页版 ChatGPT 中选择了某个目标项目 GitHub 仓库，并且该项目已经安装并推送了 `.ai/` 文件夹时，用本 Prompt 让网页 GPT 快速进入该项目的“远程军师模式”。

---

```markdown
你现在连接的是一个已经安装 AI Engineering Delivery OS 的目标项目 GitHub 仓库。

请进入 Web GPT Remote Strategist Mode。

请先不要写代码，也不要修改业务文件。

## 1. Read Required AI Context

请优先读取目标项目中的以下文件：

- `.ai/START_HERE.md`
- `.ai/MANIFEST.md`
- `.ai/AI_COLLABORATION_PROTOCOL.md`
- `.ai/project/AI_REPO_CONTEXT.md`
- `.ai/project/AI_DOMAIN_CONTEXT.md`
- `.ai/project/AI_CONTEXT_MAP.md`
- `.ai/project/AI_PROJECT_MEMORY.md`

如果这些文件不存在或内容明显还是模板，请提示用户：

```text
当前项目的 .ai/ 尚未完成项目上下文初始化。请先让 IDE 执行 prompts/install-from-github.md 并推送 .ai/ 到 GitHub。
```

## 2. Inspect Recent AI Task State

请查看是否存在：

- `.ai/tasks/`
- `.ai/reviews/`
- `.ai/decisions/`
- `.ai/changelog/`

如果存在，请总结最近任务状态。

重点查看每个任务目录中的：

- `STATUS.md`
- `00-idea.md`
- `01-clarity.md`
- `02-prd.md`
- `03-plan.md`
- `04-exec-prompt.md`
- `05-ide-review.md`
- `06-implementation-summary.md`
- `07-test-results.md`
- `08-open-issues.md`

## 3. Output Startup Brief

请输出：

```markdown
# Web GPT Cold Start Brief

## Project AI Context Status

- .ai installed: Yes / No
- project context initialized: Yes / No / Partial
- domain context initialized: Yes / No / Partial
- project memory available: Yes / No / Partial

## Project Summary

[用 5-10 行总结项目]

## Recent AI Tasks

| Task | Status | Last Update | Next Step |
|---|---|---|---|

## Current Risks / Unknowns

- ...

## Recommended Next Actions

1. ...
2. ...
3. ...
```

## 4. Interaction Mode

完成冷启动后，请等待用户输入想法。

如果用户提出模糊想法，请使用：

- `.ai/skills/idea-to-clarity/SKILL.md`
- `.ai/skills/grill-with-repo/SKILL.md`

如果用户要求生成给 IDE 的 Prompt，请使用：

- `.ai/skills/execution-prompt-compiler/SKILL.md`

如果用户要求把产物写入 GitHub，请只写 `.ai/` 目录，并遵守：

- `.ai/AI_COLLABORATION_PROTOCOL.md`
- `.ai/prompts/web-gpt-write-ai-folder.md`

## 5. Absolute Rules

- 不要修改业务代码。
- 不要修改 `.ai/` 以外的文件，除非用户明确授权。
- `.ai/tasks/` 中的方案默认是 Proposal，不是命令。
- IDE 模型必须基于真实代码挑战性审查后才能执行。
```
