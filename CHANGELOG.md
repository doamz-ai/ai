# CHANGELOG

本文件记录 AI Engineering Delivery OS 的版本演进。

---

## v0.1.1-draft — 2026-05-04

### Added

新增可复制 Prompt：

- `prompts/initialize-project.md`
- `prompts/raw-idea.md`
- `prompts/compile-exec-prompt.md`
- `prompts/review-diff.md`
- `prompts/ship-record.md`

新增机器可读清单：

- `manifest.json`

新增结构校验脚本：

- `scripts/validate-structure.py`

新增版本变更记录：

- `CHANGELOG.md`

### Purpose

v0.1.1-draft 的目标是让系统更容易安装、复制、启动和自检。

重点从“文档完整”增强为：

```text
可复制 Prompt
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
