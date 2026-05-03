# Prompt: Review Diff / PR

用途：当编程智能体完成代码修改后，让军师模型进入 Review Mode，审计 diff、PR、修改摘要和测试结果。

---

```markdown
请进入 Review Mode。

请先阅读：

- `.ai/system/AI_MASTER_PROMPT.md`
- `.ai/system/AI_AGENT_RULES.md`
- `.ai/skills/review-quality-gate/SKILL.md`
- `.ai/templates/REVIEW_REPORT_TEMPLATE.md`
- `.ai/project/AI_REPO_CONTEXT.md`
- `.ai/project/AI_DOMAIN_CONTEXT.md`
- `.ai/references/SECURITY_CHECKLIST.md`
- `.ai/references/TESTING_CHECKLIST.md`
- `.ai/references/ANTI_OVERENGINEERING_RULES.md`

如本次改动涉及 API / 数据库 / 前端 / 性能，请额外参考：

- `.ai/references/API_INTERFACE_CHECKLIST.md`
- `.ai/references/DATABASE_MIGRATION_CHECKLIST.md`
- `.ai/references/FRONTEND_UX_CHECKLIST.md`
- `.ai/references/PERFORMANCE_CHECKLIST.md`

下面是原任务目标、编程智能体修改摘要、diff 和测试结果：

【粘贴原任务包】

【粘贴编程智能体完成报告】

【粘贴 diff / PR 内容 / 文件列表 / 测试结果】

请按质量门审计，并输出：

1. Verdict: PASS / NEEDS_FIX / REJECT
2. Original Task Summary
3. Submitted Changes
4. Goal Completion Check
5. Scope Check
6. Risk Review
   - Correctness
   - Architecture
   - Security / Permission
   - Data / Storage
   - Performance
   - Compatibility
   - Maintainability
7. Test Review
8. Issues by Severity
   - Critical
   - Important
   - Optional
   - FYI
9. Required Fixes
10. Fix Prompt for Coding Agent
11. Documentation / Memory Suggestions

要求：

- 不要只说“看起来不错”。
- 必须明确 verdict。
- Critical 问题不得放行。
- 如果需要修复，请输出可直接复制给编程智能体的 Fix Prompt。
```
