# INSTALL

本文件说明如何把 AI Engineering Delivery OS 安装到任意代码项目中。

---

## 1. What You Are Installing

AI Engineering Delivery OS 是一套可复制到任意项目的 AI 工程交付操作系统。

安装后，目标项目会获得一套 `.ai/` 协作层，用于支持：

```text
项目上下文
→ 领域语言
→ 需求澄清
→ 任务切片
→ 编程执行 Prompt
→ 增量实现
→ 测试反馈
→ 质量审计
→ 项目记忆沉淀
```

---

## 2. Recommended Install Path

推荐把本系统安装到目标项目根目录的 `.ai/` 文件夹：

```text
your-project/
├── .ai/
│   ├── README.md
│   ├── START_HERE.md
│   ├── VERSION.md
│   ├── system/
│   ├── project/
│   ├── skills/
│   ├── templates/
│   ├── references/
│   ├── tasks/
│   ├── decisions/
│   ├── reviews/
│   └── changelog/
└── your-project-code...
```

---

## 3. Installation Methods

### Method A: Manual Copy

1. 下载本仓库。
2. 将仓库内容复制到目标项目的 `.ai/` 目录。
3. 提交 `.ai/` 到目标项目 Git 仓库。
4. 让 AI 阅读 `.ai/START_HERE.md`。

适合：简单、直接、最容易理解。

---

### Method B: Git Subtree / Vendor Copy

如果你希望多个项目复用同一套系统，可以把本仓库作为 vendor 目录同步到 `.ai/`。

注意：

- 通用系统层可以从本仓库更新。
- 项目适配层不要被覆盖。

建议区分：

```text
通用系统层：system/ skills/ templates/ references/
项目适配层：project/ tasks/ decisions/ reviews/ changelog/
```

---

### Method C: Copy System Layer Only

如果目标项目已经有自己的任务记录和项目记忆，只更新通用层：

```text
system/
skills/
templates/
references/
README.md
START_HERE.md
VERSION.md
```

不要覆盖：

```text
project/
tasks/
decisions/
reviews/
changelog/
```

---

## 4. First-time Initialization

安装后第一步不是写代码，而是生成项目本地上下文。

对军师模型说：

```markdown
请先阅读 `.ai/START_HERE.md`。

你现在接入了一个已经安装 AI Engineering Delivery OS 的代码项目。

请不要改业务代码。

请先扫描当前仓库，生成或补全以下项目上下文文件：

- `.ai/project/AI_REPO_CONTEXT.md`
- `.ai/project/AI_DOMAIN_CONTEXT.md`
- `.ai/project/AI_CONTEXT_MAP.md`
- `.ai/project/AI_PROJECT_MEMORY.md`

要求：

1. 所有判断必须基于真实代码、README、配置和目录结构。
2. 没有看到的内容标注为 `[Unknown]` 或 `[To Verify]`。
3. 不要脑补不存在的架构。
4. 不要修改业务代码。
5. 输出适合长期维护的 Markdown 文档。
```

---

## 5. Recommended First Commit in Target Project

建议第一次安装时单独提交：

```bash
git add .ai
git commit -m "docs: install AI Engineering Delivery OS"
```

然后第二次提交再补项目上下文：

```bash
git add .ai/project
git commit -m "docs: initialize AI project context"
```

这样以后容易区分：

- 哪些是通用系统文件。
- 哪些是项目本地适配内容。

---

## 6. Daily Usage

### 6.1 When You Have a Raw Idea

对军师模型说：

```markdown
我有一个不成熟的想法：

[写你的想法]

请按 `.ai/skills/idea-to-clarity/SKILL.md` 和 `.ai/skills/grill-with-repo/SKILL.md` 处理。
先不要写代码。
请输出真实问题、影响面、范围边界、Not Doing 和下一步建议。
```

---

### 6.2 When You Need a Coding Agent Prompt

对军师模型说：

```markdown
请基于当前已确认的需求和 `.ai/skills/execution-prompt-compiler/SKILL.md`，生成一段可直接交给编程智能体执行的 Prompt。

要求包含：

- Task
- Background
- Repo Evidence
- Goals
- Non-goals
- Files / Modules to Inspect
- Implementation Requirements
- Constraints
- Acceptance Criteria
- Required Final Response
```

---

### 6.3 When Coding Agent Executes

对编程智能体说：

```markdown
请先阅读：

- `.ai/START_HERE.md`
- `.ai/system/AI_AGENT_RULES.md`
- `.ai/project/AI_REPO_CONTEXT.md`
- `.ai/project/AI_DOMAIN_CONTEXT.md`
- 当前任务包

然后严格按任务包执行。

不要做无关重构。
不要修改无关文件。
不要绕过后端权限校验。
完成后必须输出修改摘要、测试结果、风险和未完成事项。
```

---

### 6.4 When Reviewing Code Changes

对军师模型说：

```markdown
请进入 Review Mode。

下面是编程智能体的修改摘要、diff 和测试结果。
请按：

- `.ai/skills/review-quality-gate/SKILL.md`
- `.ai/templates/REVIEW_REPORT_TEMPLATE.md`
- `.ai/references/SECURITY_CHECKLIST.md`
- `.ai/references/TESTING_CHECKLIST.md`
- `.ai/references/ANTI_OVERENGINEERING_RULES.md`

进行审计，并输出：

- Verdict: PASS / NEEDS_FIX / REJECT
- Critical / Important / Optional / FYI
- Required Fixes
- Fix Prompt
```

---

## 7. Updating the Installed System

当本模板仓库升级后，可以把通用层同步到目标项目。

建议更新：

```text
.ai/system/
.ai/skills/
.ai/templates/
.ai/references/
.ai/README.md
.ai/START_HERE.md
.ai/VERSION.md
```

谨慎更新或不要直接覆盖：

```text
.ai/project/
.ai/tasks/
.ai/decisions/
.ai/reviews/
.ai/changelog/
```

这些属于项目本地记忆。

---

## 8. Version Tracking in Installed Projects

安装到具体项目后，建议保留 `.ai/VERSION.md`，并补充：

```text
Installed AI Engineering Delivery OS Version: v0.1.0
Project Local AI Context Version: v0.1.0-project-draft
Last AI Context Refresh: YYYY-MM-DD
```

---

## 9. Minimal Installation

如果你不想安装完整系统，最小可用版本为：

```text
.ai/
├── START_HERE.md
├── system/
│   ├── AI_MASTER_PROMPT.md
│   └── AI_AGENT_RULES.md
├── project/
│   ├── AI_REPO_CONTEXT.md
│   ├── AI_DOMAIN_CONTEXT.md
│   └── AI_PROJECT_MEMORY.md
├── skills/
│   ├── idea-to-clarity/
│   ├── execution-prompt-compiler/
│   └── review-quality-gate/
└── templates/
    ├── TASK_PACKAGE_TEMPLATE.md
    └── REVIEW_REPORT_TEMPLATE.md
```

---

## 10. Final Rule

安装本系统后，每个项目都应该遵循：

```text
先生成项目上下文，再讨论需求。
先澄清真实问题，再生成 Prompt。
先拆任务，再写代码。
先验证，再信任。
先审计，再交付。
交付后沉淀长期记忆。
```
