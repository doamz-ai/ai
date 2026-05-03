# AI Engineering Delivery OS

> 中文名：AI 工程交付操作系统  
> 定位：一套可安装到任意代码仓库的 AI 多智能体工程协作系统。

AI Engineering Delivery OS 不是一段单独的 Prompt，也不是某个具体项目的开发文档。它是一套可以安装到任意 GitHub 项目中的 AI 协作运行环境，用来把 AI 编程从“聊天式写代码”升级为“上下文驱动、任务切片、增量实现、测试反馈、质量审计、长期沉淀”的工程交付流程。

---

## 0. 非专业用户快速开始

如果你不懂 Git、脚本或工程目录，也可以这样用。

### 推荐方式：让 IDE 智能体自动安装

在你的任意代码项目中，打开支持 GitHub 和本地文件操作的 AI IDE，然后复制下面这段话给 IDE 智能体：

```markdown
请从 GitHub 仓库 `doamz-ai/ai` 安装 AI Engineering Delivery OS 到当前项目。

请先读取该仓库中的 `prompts/install-from-github.md`，然后严格按照其中规则执行。

目标：
1. 在当前项目根目录创建 `.ai/` 文件夹。
2. 从 `doamz-ai/ai` 复制模板内容到 `.ai/`。
3. 不要修改当前项目业务代码。
4. 安装后扫描当前项目，初始化 `.ai/project/` 下的项目上下文。
5. 输出安装报告。
```

安装完成后，当前项目就拥有自己的专属 `.ai/` 协作层。

### 日常使用方式

1. 你在网页 GPT 或 IDE 里提出模糊想法。
2. AI 把想法整理到 `.ai/tasks/`。
3. IDE 模型读取 `.ai/tasks/` 后，先审查方案是否符合真实代码。
4. IDE 模型确认后再改业务代码。
5. 改完后用 `.ai/skills/review-quality-gate/` 审计。
6. 通过后把长期经验沉淀到 `.ai/project/AI_PROJECT_MEMORY.md`。

### 最重要的安全边界

如果你用网页版 GPT 连接目标项目 GitHub，它默认只应该写 `.ai/` 文件夹，用于传递想法、PRD、计划、任务包和审计报告。

```text
网页 GPT：只写 .ai/，不碰业务代码。
IDE 模型：读取 .ai/，基于真实代码挑战方案，再决定是否执行。
GitHub：作为网页 GPT 与 IDE 模型之间的信息传递通道。
```

详细规则见：

```text
REMOTE_INSTALL.md
AI_COLLABORATION_PROTOCOL.md
prompts/install-from-github.md
prompts/web-gpt-write-ai-folder.md
```

---

## 1. 为什么需要这个系统？

普通 AI 编程流程通常是：

```text
用户提出模糊想法
→ AI 直接猜需求
→ AI 修改代码
→ 用户发现不对
→ 反复返工
```

这个模式的问题不是 AI 不会写代码，而是缺少工程交付纪律：

- 缺少统一上下文。
- 缺少项目共享语言。
- 缺少需求澄清机制。
- 缺少任务拆解机制。
- 缺少执行边界。
- 缺少测试反馈。
- 缺少执行后审计。
- 缺少长期项目记忆。

AI Engineering Delivery OS 要解决的是：

```text
如何让不同 AI 模型在同一个代码项目里，按统一上下文、统一流程、统一质量门、统一审计标准，高效、低返工、低技术债地交付代码。
```

---

## 2. 核心目标

本系统的目标是帮助一个项目形成完整的 AI 工程交付闭环：

```text
项目安装 AI Engineering Delivery OS
→ AI 读取项目上下文
→ 用户提出模糊想法
→ 军师模型澄清、展开、收敛
→ 拆成可执行任务切片
→ 编程智能体按任务包执行
→ 测试反馈验证
→ 审计智能体检查 diff 和风险
→ 交付报告沉淀到项目记忆
```

最终希望实现：

1. 降低昂贵编程模型的试错成本。
2. 减少 AI 误改、乱改、过度设计。
3. 让项目上下文和领域语言长期沉淀。
4. 让每次 AI 改代码都有任务依据、测试证据和审计记录。
5. 让不同 AI 模型可以在同一套规则下协作。

---

## 3. 系统不是做什么的？

AI Engineering Delivery OS 不是：

- 不是某个具体项目的 PRD。
- 不是普通 Prompt 模板合集。
- 不是让 AI 无脑写代码的万能咒语。
- 不是替代人类判断的自动开发流水线。
- 不是要求每个小改动都写长文档的官僚系统。
- 不是让弱模型强迫强模型执行错误规划。

它是：

```text
一个面向 AI 协作的软件工程交付协议。
```

它帮助人类和 AI 共同回答：

- 当前项目是什么？
- 用户真正想解决什么问题？
- 这次应该做什么？
- 这次不应该做什么？
- 应该拆成哪些任务？
- 编程智能体应该如何执行？
- 执行结果如何审计？
- 哪些经验应该沉淀？

---

## 4. 协作治理原则

IDE 里的强模型不是无脑执行者，而是带有否决权的工程合作者。

任何网页 GPT、人类或其他模型写入 `.ai/` 的方案，都默认是：

```text
Proposal, not command.
```

IDE 模型在执行前必须基于真实仓库做挑战性审查：

```text
ACCEPT / ACCEPT_WITH_CHANGES / NEEDS_CLARIFICATION / REJECT
```

推荐协作方式：

```text
网页 GPT 讨论并生成方案
→ 写入目标项目 .ai/tasks/...
→ 推送到 GitHub
→ IDE pull 最新内容
→ IDE 审查 .ai/tasks/...
→ IDE 修正或执行
→ IDE 推送代码或 PR
→ 网页 GPT 可再次审计 diff
```

详细见：

```text
AI_COLLABORATION_PROTOCOL.md
```

---

## 5. 推荐安装结构

将本系统安装到任意项目根目录下的 `.ai/` 文件夹中：

```text
.ai/
├── README.md
├── START_HERE.md
├── VERSION.md
├── INSTALL.md
├── REMOTE_INSTALL.md
├── AI_COLLABORATION_PROTOCOL.md
├── MANIFEST.md
├── SELF_CHECK.md
├── CHANGELOG.md
├── manifest.json
│
├── system/
├── project/
├── skills/
├── templates/
├── references/
├── prompts/
├── scripts/
├── tasks/
├── decisions/
├── reviews/
└── changelog/
```

---

## 6. 分层设计

### 6.1 `system/`：通用系统内核

`system/` 定义所有项目通用的 AI 协作规则。

它回答：

- AI 应该扮演什么角色？
- 有哪些工作模式？
- 如何处理模糊想法？
- 如何拆任务？
- 如何防止过度设计？
- 如何审计执行结果？

这部分可以跨项目复用。

---

### 6.2 `project/`：项目本地上下文

`project/` 定义当前项目独有的事实和记忆。

它回答：

- 这个项目是什么？
- 技术栈是什么？
- 核心业务流程是什么？
- 有哪些领域术语？
- 哪些模块高风险？
- 有哪些历史决策？
- 有哪些长期技术债？

这部分需要每个项目安装后单独生成和维护。

---

### 6.3 `skills/`：可触发的工作流能力

`skills/` 不是普通说明文，而是 AI 的工作流能力模块。

例如：

```text
用户说“我有个不成熟的想法”
→ 触发 idea-to-clarity

用户说“帮我拆成任务”
→ 触发 plan-to-slices

用户说“代码改完了，帮我审计 diff”
→ 触发 review-quality-gate
```

---

### 6.4 `templates/`：标准交付物模板

`templates/` 用来统一 AI 的输出格式，避免每次任务包、PRD、Review Report、ADR 结构不一致。

---

### 6.5 `references/`：质量检查清单

`references/` 是质量门和防呆系统。

它覆盖：

- 安全。
- 性能。
- 测试。
- API。
- 数据库迁移。
- 前端交互。
- 反过度设计。

---

### 6.6 `prompts/`：可复制启动 Prompt

`prompts/` 供普通用户直接复制给 IDE 或网页 GPT。

最常用的是：

```text
prompts/install-from-github.md
prompts/raw-idea.md
prompts/compile-exec-prompt.md
prompts/review-diff.md
prompts/web-gpt-write-ai-folder.md
```

---

### 6.7 `tasks/`、`decisions/`、`reviews/`、`changelog/`

这些目录用于记录项目实际运行过程：

- `tasks/`：每次真实任务的过程记录。
- `decisions/`：重要架构决策记录。
- `reviews/`：执行后审计报告。
- `changelog/`：系统或项目 AI 协作层变更记录。

---

## 7. 推荐角色分工

本系统不要求真的同时启动多个 AI，但建议按角色理解协作职责。

### 7.1 军师模型

负责：

- 理解项目上下文。
- 接住模糊想法。
- 澄清真实问题。
- 拆解影响面。
- 控制范围。
- 生成任务包。
- 审计执行结果。

### 7.2 编程智能体

负责：

- 阅读任务包。
- 结合真实代码挑战方案。
- 必要时反驳或修正计划。
- 增量实现。
- 运行测试。
- 输出修改摘要。

### 7.3 审计智能体

负责：

- 检查是否完成原目标。
- 检查是否有无关改动。
- 检查安全、权限、数据、性能、测试风险。
- 输出 PASS / NEEDS_FIX / REJECT。

---

## 8. 标准生命周期

每个重要任务建议遵循以下生命周期：

```text
0. Context：读取上下文与领域语言
1. Define：澄清想法，定义真实问题
2. Spec：形成规格，明确目标和非目标
3. Plan：拆成任务切片，区分 HITL / AFK
4. Prompt：编译给编程智能体的执行 Prompt
5. Build：增量实现，每个切片保持可运行
6. Verify：测试反馈，提供 pass/fail 证据
7. Review：质量门审计，输出 PASS / NEEDS_FIX / REJECT
8. Ship：交付报告，沉淀项目记忆
9. Memory：更新长期项目上下文
```

---

## 9. 关键原则

### 9.1 Process, not prose

文档不是为了好看，而是为了驱动流程。每个文件都要能帮助 AI 做出更稳定的工程行为。

### 9.2 Context before code

在没有理解项目上下文之前，不要直接改代码。

### 9.3 Proposal, not command

`.ai/` 中的计划默认是提案，不是命令。IDE 模型必须结合真实代码审查。

### 9.4 Clarify before build

需求不清时，先澄清、追问、查代码，而不是直接实现。

### 9.5 Not Doing is part of scope

每个任务都要明确“不做什么”。没有 Not Doing，AI 容易过度实现。

### 9.6 Vertical slices over big rewrites

优先端到端薄切片，而不是一次性大重构。

### 9.7 Feedback loop first

调 bug 和做复杂改动时，先建立可重复验证信号。

### 9.8 Review before trust

编程智能体执行完以后，不要直接信任结果。必须审计 diff、范围、风险和测试证据。

### 9.9 Memory after ship

重要任务完成后，必须沉淀项目记忆。

---

## 10. 常见使用场景

### 10.1 新项目安装

推荐让 IDE 智能体读取：

```text
prompts/install-from-github.md
```

从 GitHub 模板仓库安装到当前项目 `.ai/`。

### 10.2 模糊想法收敛

用户提出一个不成熟想法，军师模型通过 `idea-to-clarity` 和 `grill-with-repo` 收敛成任务包。

### 10.3 网页 GPT 向 IDE 传递想法

网页 GPT 只写目标项目 `.ai/` 目录，不碰业务代码。

推荐读取：

```text
prompts/web-gpt-write-ai-folder.md
```

### 10.4 生成给编程智能体的 Prompt

军师模型通过 `execution-prompt-compiler` 输出高质量执行 Prompt。

### 10.5 编程智能体执行

编程智能体读取 `AI_AGENT_RULES.md` 和任务包后，先审查方案，再增量实现。

### 10.6 执行后审计

军师模型通过 `review-quality-gate` 审计修改结果。

### 10.7 交付沉淀

任务通过后，更新 `AI_PROJECT_MEMORY.md`、`AI_DOMAIN_CONTEXT.md`、`decisions/` 或 `changelog/`。

---

## 11. 当前状态

当前版本：`v0.1.1-draft`  
当前状态：Ready for Pilot  
当前目标：支持 IDE 自动远程安装，并支持网页 GPT 与 IDE 通过 GitHub `.ai/` 文件夹协作。
