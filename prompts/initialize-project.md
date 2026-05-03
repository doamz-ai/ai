# Prompt: Initialize Project Context

用途：把 AI Engineering Delivery OS 安装到一个真实项目后，让军师模型先扫描仓库并生成项目本地上下文。

---

```markdown
请先阅读 `.ai/START_HERE.md`。

你现在接入了一个已经安装 AI Engineering Delivery OS 的代码项目。

请不要改业务代码。

请根据以下文件进入 Context Mode：

- `.ai/system/AI_MASTER_PROMPT.md`
- `.ai/system/AI_OPERATING_MODES.md`
- `.ai/system/AI_DELIVERY_WORKFLOW.md`
- `.ai/project/AI_REPO_CONTEXT.md`
- `.ai/project/AI_DOMAIN_CONTEXT.md`
- `.ai/project/AI_CONTEXT_MAP.md`
- `.ai/project/AI_PROJECT_MEMORY.md`

请扫描当前仓库，生成或补全以下项目上下文文件草案：

1. `.ai/project/AI_REPO_CONTEXT.md`
2. `.ai/project/AI_DOMAIN_CONTEXT.md`
3. `.ai/project/AI_CONTEXT_MAP.md`
4. `.ai/project/AI_PROJECT_MEMORY.md`

要求：

1. 所有判断必须基于真实代码、README、配置文件、目录结构和可见文档。
2. 不确定内容必须标注为 `[Unknown]` 或 `[To Verify]`。
3. 不要脑补不存在的架构。
4. 不要修改业务代码。
5. 不要一次性读取无关文件；按 `.ai/project/AI_CONTEXT_MAP.md` 的原则逐步加载上下文。
6. 输出适合长期维护的 Markdown 文档。
7. 最后列出“下一步建议”和“仍需人工确认的问题”。
```
