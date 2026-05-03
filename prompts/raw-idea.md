# Prompt: Raw Idea to Engineering Task

用途：当你有一个模糊想法、不成熟方向或业务痛点时，启动军师模型进行澄清、挑刺、收敛。

---

```markdown
请先阅读：

- `.ai/START_HERE.md`
- `.ai/system/AI_MASTER_PROMPT.md`
- `.ai/system/AI_OPERATING_MODES.md`
- `.ai/project/AI_REPO_CONTEXT.md`
- `.ai/project/AI_DOMAIN_CONTEXT.md`
- `.ai/project/AI_PROJECT_MEMORY.md`
- `.ai/skills/idea-to-clarity/SKILL.md`
- `.ai/skills/grill-with-repo/SKILL.md`

我有一个不成熟的想法：

【在这里粘贴你的想法】

请先不要写代码，也不要直接生成最终执行 Prompt。

请你按 AI Engineering Delivery OS 的流程处理：

1. 判断需求成熟度：L0 / L1 / L2 / L3 / L4。
2. 识别表层想法背后的真实问题。
3. 基于仓库上下文分析可能影响的模块。
4. 区分已确认、待确认、基于假设的内容。
5. 从业务、数据、权限、失败路径、规模、兼容性、未来扩展角度压测。
6. 最多提出 3 个必须由我确认的高价值问题。
7. 给出推荐范围边界：本次要做 / 本次不做 / 仅预留不实现。
8. 判断下一步应该进入 Spec Mode、Plan Mode 还是 Prompt Compile Mode。

请输出：

- 需求成熟度判断
- 真实问题识别
- 仓库影响面分析
- 关键假设
- 风险和不确定性
- Not Doing 清单
- 下一步建议
```
