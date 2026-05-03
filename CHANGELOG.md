# CHANGELOG

本文件记录 AI Engineering Delivery OS 的版本演进。

---

## v0.1.1-draft — 2026-05-04

### Added

新增远程模板安装模式：

- `REMOTE_INSTALL.md`
- `prompts/install-from-github.md`

新增多智能体协作治理：

- `AI_COLLABORATION_PROTOCOL.md`
- `prompts/web-gpt-write-ai-folder.md`

新增小白用户场景手册：

- `USER_SCENARIOS_PLAYBOOK.md`

新增冷启动、IDE 审查、IDE 进度回写 Prompt：

- `prompts/web-gpt-cold-start.md`
- `prompts/ide-review-ai-task.md`
- `prompts/ide-progress-report-to-ai-folder.md`

新增可复制 Prompt：

- `prompts/install-from-github.md`
- `prompts/initialize-project.md`
- `prompts/web-gpt-cold-start.md`
- `prompts/raw-idea.md`
- `prompts/compile-exec-prompt.md`
- `prompts/review-diff.md`
- `prompts/ship-record.md`
- `prompts/web-gpt-write-ai-folder.md`
- `prompts/ide-review-ai-task.md`
- `prompts/ide-progress-report-to-ai-folder.md`

新增机器可读清单：

- `manifest.json`

新增结构校验脚本：

- `scripts/validate-structure.py`

新增版本变更记录：

- `CHANGELOG.md`

### Changed

- `README.md` 增加非专业用户快速开始。
- `README.md` 增加安装后必须推送 `.ai/` 到目标项目 GitHub 的说明。
- `MANIFEST.md` 已更新为 v0.1.1-draft 文件清单。
- `manifest.json` 已纳入远程安装、协作协议、场景手册、prompts 和 scripts。

### Purpose

v0.1.1-draft 的目标是让系统更容易安装、复制、启动、自检和跨环境协作。

重点从“文档完整”增强为：

```text
远程模板安装
+ 网页 GPT / IDE / GitHub 协作闭环
+ 可复制 Prompt
+ 小白用户场景手册
+ 机器可读 manifest
+ 结构校验脚本
+ 版本变更记录
```

---

## v0.1.0 — 2026-05-04

### Added

建立 AI Engineering Delivery OS MVP。

顶层入口：

- `README.md`
- `START_HERE.md`
- `VERSION.md`
- `INSTALL.md`
- `MANIFEST.md`
- `SELF_CHECK.md`

系统内核：

- `system/AI_MASTER_PROMPT.md`
- `system/AI_AGENT_RULES.md`
- `system/AI_OPERATING_MODES.md`
- `system/AI_DELIVERY_WORKFLOW.md`

项目适配模板：

- `project/AI_REPO_CONTEXT.md`
- `project/AI_DOMAIN_CONTEXT.md`
- `project/AI_CONTEXT_MAP.md`
- `project/AI_PROJECT_MEMORY.md`

技能系统：

- `skills/idea-to-clarity/SKILL.md`
- `skills/grill-with-repo/SKILL.md`
- `skills/spec-before-code/SKILL.md`
- `skills/plan-to-slices/SKILL.md`
- `skills/execution-prompt-compiler/SKILL.md`
- `skills/incremental-build/SKILL.md`
- `skills/tdd-feedback-loop/SKILL.md`
- `skills/diagnose-bug/SKILL.md`
- `skills/review-quality-gate/SKILL.md`
- `skills/architecture-deepening/SKILL.md`
- `skills/ship-and-record/SKILL.md`

标准模板：

- `templates/TASK_PACKAGE_TEMPLATE.md`
- `templates/PRD_TEMPLATE.md`
- `templates/RFC_TEMPLATE.md`
- `templates/ADR_TEMPLATE.md`
- `templates/ISSUE_SLICE_TEMPLATE.md`
- `templates/REVIEW_REPORT_TEMPLATE.md`
- `templates/FEEDBACK_LOOP_TEMPLATE.md`
- `templates/SHIP_REPORT_TEMPLATE.md`

质量门：

- `references/SECURITY_CHECKLIST.md`
- `references/PERFORMANCE_CHECKLIST.md`
- `references/TESTING_CHECKLIST.md`
- `references/API_INTERFACE_CHECKLIST.md`
- `references/DATABASE_MIGRATION_CHECKLIST.md`
- `references/FRONTEND_UX_CHECKLIST.md`
- `references/ANTI_OVERENGINEERING_RULES.md`

运行目录：

- `tasks/.gitkeep`
- `decisions/.gitkeep`
- `reviews/.gitkeep`
- `changelog/.gitkeep`

### Purpose

v0.1.0 的目标是建立完整 MVP：

```text
Context
→ Define
→ Spec
→ Plan
→ Prompt
→ Build
→ Verify
→ Review
→ Ship
→ Memory
```

### Status

Ready for Pilot.
