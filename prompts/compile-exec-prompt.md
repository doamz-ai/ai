# Prompt: Compile Execution Prompt

用途：当需求已经澄清、规格或任务切片已明确时，让军师模型生成可直接交给编程智能体执行的高质量 Prompt。

---

```markdown
请先阅读：

- `.ai/system/AI_MASTER_PROMPT.md`
- `.ai/system/AI_AGENT_RULES.md`
- `.ai/skills/execution-prompt-compiler/SKILL.md`
- `.ai/templates/TASK_PACKAGE_TEMPLATE.md`
- `.ai/project/AI_REPO_CONTEXT.md`
- `.ai/project/AI_DOMAIN_CONTEXT.md`
- `.ai/project/AI_PROJECT_MEMORY.md`

当前我要把下面这个任务交给编程智能体执行：

【粘贴已澄清的需求 / PRD / RFC / 任务切片】

请先判断任务是否已经达到 L2 可执行成熟度。

如果还不能执行，请指出缺口，并说明应该回到 Grill / Spec / Plan 的哪一步。

如果可以执行，请生成一段可直接复制给编程智能体的高质量 Prompt。

必须包含：

1. Task
2. Background
3. Repo Evidence
4. Goals
5. Non-goals
6. Files / Modules to Inspect First
7. Implementation Requirements
8. Constraints
9. Acceptance Criteria
10. Required Final Response

要求：

- 不要夹带讨论过程。
- 不要使用模糊词，如“顺便”“优化一下”“尽量完善”。
- 必须明确禁止事项。
- 必须明确验收标准。
- 必须要求编程智能体完成后输出修改文件、测试结果、风险和未完成事项。
```
