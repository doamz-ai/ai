# START HERE

欢迎使用 AI Engineering Delivery OS。

如果你是人类使用者、军师模型、编程智能体、审计智能体，第一次进入本仓库时，请先阅读本文件。

---

## 1. 你现在看到的是什么？

这是一个可复制到任意代码项目中的 AI 工程交付操作系统。

它的目标不是让 AI 直接无脑写代码，而是让 AI 按完整工程流程协作：

```text
理解上下文
→ 澄清需求
→ 形成规格
→ 拆成任务
→ 增量实现
→ 测试验证
→ 质量审计
→ 交付沉淀
```

---

## 2. 如果你是人类使用者

### 2.1 安装到项目

把本仓库中的 `.ai/` 或当前完整目录复制到目标代码项目根目录。

推荐安装路径：

```text
目标项目根目录/.ai/
```

如果你下载的是完整模板仓库，请将其中的内容放入目标项目的 `.ai/` 文件夹。

---

### 2.2 第一次接入项目时，对 AI 说

```markdown
请先阅读 `.ai/START_HERE.md`。

你现在接入了一个已经安装 AI Engineering Delivery OS 的代码项目。

请不要急着改代码。

请先根据 `.ai/system/AI_MASTER_PROMPT.md` 进入工程交付模式，并阅读：

- `.ai/system/AI_AGENT_RULES.md`
- `.ai/project/AI_REPO_CONTEXT.md`
- `.ai/project/AI_DOMAIN_CONTEXT.md`
- `.ai/project/AI_PROJECT_MEMORY.md`

如果 `project/` 下的项目上下文还是空白，请先扫描仓库，生成项目上下文草案。
```

---

### 2.3 当你有一个模糊想法时，对军师模型说

```markdown
我有一个不成熟的想法：

【这里写你的想法】

请按以下文件进入工程军师模式：

- `.ai/system/AI_MASTER_PROMPT.md`
- `.ai/skills/idea-to-clarity/SKILL.md`
- `.ai/skills/grill-with-repo/SKILL.md`
- `.ai/skills/plan-to-slices/SKILL.md`

请先不要写代码。

请输出：

1. 真实问题识别。
2. 仓库影响面分析。
3. 需要确认的关键问题。
4. 推荐方案。
5. Not Doing 清单。
6. 任务切片。
7. 给编程智能体的执行 Prompt 草案。
```

---

### 2.4 当你要交给编程智能体执行时，对编程智能体说

```markdown
请先阅读：

- `.ai/START_HERE.md`
- `.ai/system/AI_AGENT_RULES.md`
- `.ai/project/AI_REPO_CONTEXT.md`
- `.ai/project/AI_DOMAIN_CONTEXT.md`
- `.ai/tasks/当前任务/04-exec-prompt.md`

然后严格按任务包执行。

执行要求：

1. 不要做无关重构。
2. 不要修改与任务无关的文件。
3. 不要绕过现有权限和架构边界。
4. 每个关键改动后尽量保持项目可运行。
5. 完成后必须输出修改摘要和测试结果。
```

---

### 2.5 当编程智能体改完代码后，对军师模型说

```markdown
请进入 Review Mode。

下面是编程智能体的修改摘要、文件列表、diff 和测试结果。

请按以下文件审计：

- `.ai/skills/review-quality-gate/SKILL.md`
- `.ai/templates/REVIEW_REPORT_TEMPLATE.md`
- `.ai/references/SECURITY_CHECKLIST.md`
- `.ai/references/TESTING_CHECKLIST.md`
- `.ai/references/ANTI_OVERENGINEERING_RULES.md`

请输出：

1. Verdict: PASS / NEEDS_FIX / REJECT。
2. 是否完成原目标。
3. 是否存在无关改动。
4. 是否存在安全、权限、数据、性能、兼容性风险。
5. 是否测试不足。
6. 需要修复的问题。
7. 给编程智能体的修复 Prompt。
```

---

## 3. 如果你是军师模型

你的职责不是直接写代码。

你的职责是：

1. 阅读项目上下文。
2. 理解用户模糊想法。
3. 识别真实问题。
4. 展开工程影响面。
5. 控制范围和技术债。
6. 拆成可执行任务。
7. 生成高质量执行 Prompt。
8. 审计编程智能体执行结果。
9. 沉淀项目长期记忆。

你应该优先阅读：

```text
.ai/system/AI_MASTER_PROMPT.md
.ai/system/AI_OPERATING_MODES.md
.ai/system/AI_DELIVERY_WORKFLOW.md
.ai/project/AI_REPO_CONTEXT.md
.ai/project/AI_DOMAIN_CONTEXT.md
.ai/project/AI_PROJECT_MEMORY.md
```

如果用户提出的是模糊想法，请优先使用：

```text
.ai/skills/idea-to-clarity/SKILL.md
.ai/skills/grill-with-repo/SKILL.md
```

如果用户要求拆任务，请使用：

```text
.ai/skills/plan-to-slices/SKILL.md
```

如果用户要求生成给编程智能体的 Prompt，请使用：

```text
.ai/skills/execution-prompt-compiler/SKILL.md
.ai/templates/TASK_PACKAGE_TEMPLATE.md
```

如果用户提供了代码修改结果，请使用：

```text
.ai/skills/review-quality-gate/SKILL.md
.ai/templates/REVIEW_REPORT_TEMPLATE.md
```

---

## 4. 如果你是编程智能体

你不是产品经理，也不是架构幻想家。

你的职责是：

1. 阅读任务包。
2. 定位真实代码路径。
3. 复用现有模式。
4. 按任务范围增量实现。
5. 不做无关重构。
6. 不引入不必要依赖。
7. 运行测试或提供清晰测试说明。
8. 输出完整修改摘要。

你必须遵守：

```text
.ai/system/AI_AGENT_RULES.md
```

你执行前必须确认：

- 是否读过任务包。
- 是否理解 Goals。
- 是否理解 Non-goals。
- 是否知道哪些文件需要检查。
- 是否知道哪些事情禁止做。
- 是否知道验收标准。

完成后必须输出：

1. 修改文件列表。
2. 新增文件列表。
3. 删除文件列表。
4. 数据库 / migration 变化。
5. 环境变量变化。
6. 测试方式。
7. 测试结果。
8. 已知风险。
9. 未完成事项。

---

## 5. 如果你是审计智能体

你的职责不是帮编程智能体圆场。

你的职责是独立判断：

- 是否完成原任务。
- 是否存在无关改动。
- 是否存在过度设计。
- 是否有权限风险。
- 是否有数据风险。
- 是否有性能风险。
- 是否有兼容性风险。
- 是否测试不足。
- 是否可以交付。

审计输出必须包含：

```text
Verdict: PASS / NEEDS_FIX / REJECT
```

问题等级建议使用：

```text
Critical：必须修，不修不能合并
Important：建议修，除非明确延期
Optional：可选优化
FYI：仅记录
```

---

## 6. 推荐上下文加载顺序

不要每次把所有文件都塞给 AI。

按任务类型加载最小必要上下文。

### 6.1 新项目初始化

读取：

```text
.ai/START_HERE.md
.ai/system/AI_MASTER_PROMPT.md
.ai/project/AI_REPO_CONTEXT.md
.ai/project/AI_DOMAIN_CONTEXT.md
```

### 6.2 模糊想法澄清

读取：

```text
.ai/system/AI_MASTER_PROMPT.md
.ai/project/AI_REPO_CONTEXT.md
.ai/project/AI_DOMAIN_CONTEXT.md
.ai/skills/idea-to-clarity/SKILL.md
.ai/skills/grill-with-repo/SKILL.md
```

### 6.3 任务拆解

读取：

```text
.ai/skills/plan-to-slices/SKILL.md
.ai/templates/ISSUE_SLICE_TEMPLATE.md
.ai/templates/TASK_PACKAGE_TEMPLATE.md
```

### 6.4 执行开发

读取：

```text
.ai/system/AI_AGENT_RULES.md
.ai/tasks/当前任务/04-exec-prompt.md
```

### 6.5 执行后审计

读取：

```text
.ai/skills/review-quality-gate/SKILL.md
.ai/templates/REVIEW_REPORT_TEMPLATE.md
.ai/references/SECURITY_CHECKLIST.md
.ai/references/TESTING_CHECKLIST.md
```

### 6.6 交付沉淀

读取：

```text
.ai/skills/ship-and-record/SKILL.md
.ai/templates/SHIP_REPORT_TEMPLATE.md
.ai/project/AI_PROJECT_MEMORY.md
.ai/project/AI_DOMAIN_CONTEXT.md
```

---

## 7. 第一次安装后的初始化任务

将系统复制到具体项目后，第一件事不是写代码，而是生成项目上下文。

对军师模型说：

```markdown
请扫描当前仓库，生成或补全以下文件：

- `.ai/project/AI_REPO_CONTEXT.md`
- `.ai/project/AI_DOMAIN_CONTEXT.md`
- `.ai/project/AI_CONTEXT_MAP.md`
- `.ai/project/AI_PROJECT_MEMORY.md`

要求：

1. 所有判断基于真实代码和文档。
2. 不确定的内容标注为“待确认”。
3. 不要脑补不存在的架构。
4. 不要修改业务代码。
5. 输出适合长期维护的 Markdown 文档。
```

---

## 8. 最重要的规则

如果只能记住一件事，请记住：

```text
先理解上下文，再定义问题；先拆任务，再写代码；先验证，再信任；先审计，再交付；交付后沉淀记忆。
```

