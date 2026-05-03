# Prompt: Ship and Record

用途：当任务通过审计后，让军师模型生成交付报告，并判断哪些内容应沉淀到项目长期记忆、领域词典、ADR 或 changelog。

---

```markdown
请进入 Ship Mode。

请先阅读：

- `.ai/skills/ship-and-record/SKILL.md`
- `.ai/templates/SHIP_REPORT_TEMPLATE.md`
- `.ai/project/AI_PROJECT_MEMORY.md`
- `.ai/project/AI_DOMAIN_CONTEXT.md`
- `.ai/templates/ADR_TEMPLATE.md`

下面是本次任务的原目标、最终实现摘要、Review Report 和测试结果：

【粘贴原任务目标】

【粘贴最终实现摘要】

【粘贴 Review Report】

【粘贴测试结果】

请输出 Ship Report，包含：

1. Ship Readiness
2. Delivery Summary
3. Verification Summary
4. Remaining Risks
5. Deferred Technical Debt
6. Memory Update Suggestions
   - AI_PROJECT_MEMORY.md
   - AI_DOMAIN_CONTEXT.md
   - AI_REPO_CONTEXT.md
7. ADR Decision
8. Changelog Entry
9. Follow-up Tasks

要求：

- 只沉淀长期有效信息。
- 不要把完整聊天记录或大段 diff 塞进项目记忆。
- 如果存在重要架构取舍，判断是否需要 ADR。
- 如果存在延期技术债，给出 revisit trigger。
```
