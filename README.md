# AI Engineering Delivery OS

> 中文名：AI 工程交付操作系统  
> 定位：一套可复制到任意代码仓库的 AI 多智能体工程协作系统。

AI Engineering Delivery OS 不是一段单独的 Prompt，也不是某个具体项目的开发文档。它是一套可以安装到任意 GitHub 项目中的 AI 协作运行环境，用来把 AI 编程从“聊天式写代码”升级为“上下文驱动、任务切片、增量实现、测试反馈、质量审计、长期沉淀”的工程交付流程。

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

## 4. 推荐安装结构

将本系统复制到任意项目根目录下的 `.ai/` 文件夹中：

```text
.ai/
├── README.md
├── START_HERE.md
├── VERSION.md
│
├── system/
│   ├── AI_MASTER_PROMPT.md
│   ├── AI_AGENT_RULES.md
│   ├── AI_OPERATING_MODES.md
│   └── AI_DELIVERY_WORKFLOW.md
│
├── project/
│   ├── AI_REPO_CONTEXT.md
│   ├── AI_DOMAIN_CONTEXT.md
│   ├── AI_CONTEXT_MAP.md
│   └── AI_PROJECT_MEMORY.md
│
├── skills/
│   ├── idea-to-clarity/
│   │   └── SKILL.md
│   ├── grill-with-repo/
│   │   └── SKILL.md
│   ├── spec-before-code/
│   │   └── SKILL.md
│   ├── plan-to-slices/
│   │   └── SKILL.md
│   ├── execution-prompt-compiler/
│   │   └── SKILL.md
│   ├── incremental-build/
│   │   └── SKILL.md
│   ├── tdd-feedback-loop/
│   │   └── SKILL.md
│   ├── diagnose-bug/
│   │   └── SKILL.md
│   ├── review-quality-gate/
│   │   └── SKILL.md
│   ├── architecture-deepening/
│   │   └── SKILL.md
│   └── ship-and-record/
│       └── SKILL.md
│
├── templates/
│   ├── TASK_PACKAGE_TEMPLATE.md
│   ├── PRD_TEMPLATE.md
│   ├── RFC_TEMPLATE.md
│   ├── ADR_TEMPLATE.md
│   ├── ISSUE_SLICE_TEMPLATE.md
│   ├── REVIEW_REPORT_TEMPLATE.md
│   ├── FEEDBACK_LOOP_TEMPLATE.md
│   └── SHIP_REPORT_TEMPLATE.md
│
├── references/
│   ├── SECURITY_CHECKLIST.md
│   ├── PERFORMANCE_CHECKLIST.md
│   ├── TESTING_CHECKLIST.md
│   ├── API_INTERFACE_CHECKLIST.md
│   ├── DATABASE_MIGRATION_CHECKLIST.md
│   ├── FRONTEND_UX_CHECKLIST.md
│   └── ANTI_OVERENGINEERING_RULES.md
│
├── tasks/
│   └── .gitkeep
│
├── decisions/
│   └── .gitkeep
│
├── reviews/
│   └── .gitkeep
│
└── changelog/
    └── .gitkeep
```

---

## 5. 分层设计

### 5.1 `system/`：通用系统内核

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

### 5.2 `project/`：项目本地上下文

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

### 5.3 `skills/`：可触发的工作流能力

`skills/` 不是普通说明文，而是 AI 的工作流能力模块。

每个 skill 都应包含：

- 触发条件。
- 输入要求。
- 执行步骤。
- 禁止事项。
- 输出格式。
- 退出条件。
- 质量标准。

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

### 5.4 `templates/`：标准交付物模板

`templates/` 用来统一 AI 的输出格式，避免每次任务包、PRD、Review Report、ADR 结构不一致。

---

### 5.5 `references/`：质量检查清单

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

### 5.6 `tasks/`、`decisions/`、`reviews/`、`changelog/`

这些目录用于记录项目实际运行过程：

- `tasks/`：每次真实任务的过程记录。
- `decisions/`：重要架构决策记录。
- `reviews/`：执行后审计报告。
- `changelog/`：系统或项目 AI 协作层变更记录。

---

## 6. 推荐角色分工

本系统不要求真的同时启动多个 AI，但建议按角色理解协作职责。

### 6.1 军师模型

负责：

- 理解项目上下文。
- 接住模糊想法。
- 澄清真实问题。
- 拆解影响面。
- 控制范围。
- 生成任务包。
- 审计执行结果。

### 6.2 编程智能体

负责：

- 阅读任务包。
- 定位代码。
- 增量实现。
- 运行测试。
- 输出修改摘要。

### 6.3 测试智能体

负责：

- 建立反馈循环。
- 设计测试路径。
- 验证正常路径、异常路径、权限路径、回归路径。

### 6.4 安全审计智能体

负责：

- 权限边界。
- 数据泄露。
- 输入验证。
- 密钥安全。
- 文件访问风险。

### 6.5 架构审计智能体

负责：

- 模块边界。
- 技术债。
- 过度抽象。
- 重复实现。
- 长期维护成本。

### 6.6 发布沉淀智能体

负责：

- 交付报告。
- ADR。
- 项目记忆更新。
- 术语表更新。
- 技术债登记。

---

## 7. 标准生命周期

每个重要任务建议遵循以下生命周期：

```text
0. Context：读取上下文与领域语言
1. Define：澄清想法，定义真实问题
2. Spec：形成规格，明确目标和非目标
3. Plan：拆成任务切片，区分 HITL / AFK
4. Build：增量实现，每个切片保持可运行
5. Verify：测试反馈，提供 pass/fail 证据
6. Review：质量门审计，输出 PASS / NEEDS_FIX / REJECT
7. Ship：交付报告，沉淀项目记忆
```

---

## 8. 关键原则

### 8.1 Process, not prose

文档不是为了好看，而是为了驱动流程。每个文件都要能帮助 AI 做出更稳定的工程行为。

### 8.2 Context before code

在没有理解项目上下文之前，不要直接改代码。

### 8.3 Clarify before build

需求不清时，先澄清、追问、查代码，而不是直接实现。

### 8.4 Not Doing is part of scope

每个任务都要明确“不做什么”。没有 Not Doing，AI 容易过度实现。

### 8.5 Vertical slices over big rewrites

优先端到端薄切片，而不是一次性大重构。

### 8.6 Feedback loop first

调 bug 和做复杂改动时，先建立可重复验证信号。

### 8.7 Tests as proof

测试不是装饰，而是证明。

### 8.8 Review before trust

编程智能体执行完以后，不要直接信任结果。必须审计 diff、范围、风险和测试证据。

### 8.9 Memory after ship

重要任务完成后，必须沉淀项目记忆。

---

## 9. 常见使用场景

### 9.1 新项目安装

把 `.ai/` 文件夹复制到项目根目录，然后让 AI 读取 `START_HERE.md` 初始化项目上下文。

### 9.2 模糊想法收敛

用户提出一个不成熟想法，军师模型通过 `idea-to-clarity` 和 `grill-with-repo` 收敛成任务包。

### 9.3 生成给编程智能体的 Prompt

军师模型通过 `execution-prompt-compiler` 输出高质量执行 Prompt。

### 9.4 编程智能体执行

编程智能体读取 `AI_AGENT_RULES.md` 和任务包后进行增量实现。

### 9.5 执行后审计

军师模型通过 `review-quality-gate` 审计修改结果。

### 9.6 交付沉淀

任务通过后，更新 `AI_PROJECT_MEMORY.md`、`AI_DOMAIN_CONTEXT.md`、`decisions/` 或 `changelog/`。

---

## 10. 最小可用版本

如果不想一次性使用完整系统，可以先使用最小版本：

```text
.ai/
├── README.md
├── START_HERE.md
├── VERSION.md
├── system/
│   ├── AI_MASTER_PROMPT.md
│   └── AI_AGENT_RULES.md
├── project/
│   ├── AI_REPO_CONTEXT.md
│   ├── AI_DOMAIN_CONTEXT.md
│   └── AI_PROJECT_MEMORY.md
├── templates/
│   ├── TASK_PACKAGE_TEMPLATE.md
│   └── REVIEW_REPORT_TEMPLATE.md
└── skills/
    ├── idea-to-clarity/
    │   └── SKILL.md
    ├── execution-prompt-compiler/
    │   └── SKILL.md
    └── review-quality-gate/
        └── SKILL.md
```

---

## 11. 版本策略

建议使用语义化版本：

```text
MAJOR.MINOR.PATCH
```

例如：

```text
v0.1.0
```

含义：

- `MAJOR`：系统结构或核心协议有破坏性变化。
- `MINOR`：新增 skills、templates、references。
- `PATCH`：修正文档、优化措辞、补充示例。

---

## 12. 当前状态

当前版本：`v0.1.0`  
当前状态：Draft / MVP  
当前目标：先建立可复制到任意项目的 AI 工程交付基础协议。

