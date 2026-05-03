# MANIFEST

本文件是 AI Engineering Delivery OS v0.1.0 的完整文件清单与用途说明。

它用于帮助人类和 AI 快速理解：

- 每个文件的职责。
- 哪些文件是通用系统层。
- 哪些文件是项目适配层。
- 哪些文件用于任务过程记录。
- 不同角色应该优先读取哪些文件。

---

## 1. Root Files

| File | Purpose | Who Should Read |
|---|---|---|
| `README.md` | 系统总说明，解释 AI Engineering Delivery OS 是什么、为什么需要、整体目录和生命周期 | 人类、军师模型 |
| `START_HERE.md` | 第一次进入系统时的入口文件，分别指导人类、军师模型、编程智能体、审计智能体如何开始 | 所有角色 |
| `VERSION.md` | 版本号、版本策略、升级原则 | 人类、维护者 |
| `INSTALL.md` | 安装说明，说明如何把本系统复制到任意项目的 `.ai/` 目录中 | 人类、维护者 |
| `MANIFEST.md` | 当前文件清单和用途说明 | 人类、AI |
| `SELF_CHECK.md` | 当前版本自检报告和后续补强项 | 维护者、军师模型 |

---

## 2. `system/` — 通用系统内核

这些文件定义系统的核心规则。它们可以跨项目复用。

| File | Purpose | Typical Use |
|---|---|---|
| `system/AI_MASTER_PROMPT.md` | 军师模型 / 调度器总提示词，定义角色、原则、需求成熟度、skill 路由、Review Mode | 军师模型处理复杂任务前读取 |
| `system/AI_AGENT_RULES.md` | 编程智能体行为规则，规定执行前读取、范围控制、权限、安全、测试、汇报格式 | 编程智能体改代码前必须读取 |
| `system/AI_OPERATING_MODES.md` | 定义 Context / Idea / Grill / Spec / Plan / Build / Verify / Review / Ship 等工作模式 | 判断当前任务该进入哪个模式 |
| `system/AI_DELIVERY_WORKFLOW.md` | 定义从 Context 到 Memory 的完整工程交付生命周期 | 规划复杂任务和流程治理时读取 |

---

## 3. `project/` — 项目适配层

这些文件在每个具体项目中都需要基于真实仓库单独生成和维护。

| File | Purpose | Update When |
|---|---|---|
| `project/AI_REPO_CONTEXT.md` | 项目画像：技术栈、目录结构、核心流程、API、数据模型、权限、部署、高风险区域 | 项目结构、技术栈、API、数据库、部署方式变化时 |
| `project/AI_DOMAIN_CONTEXT.md` | 领域词典：业务术语、角色、状态、命名约定、易混概念 | 新增术语、用户纠正术语、业务对象变化时 |
| `project/AI_CONTEXT_MAP.md` | 上下文地图：不同任务场景应该加载哪些文件，避免上下文不足或过载 | 系统新增 skill/template/reference 或项目上下文策略变化时 |
| `project/AI_PROJECT_MEMORY.md` | 长期项目记忆：架构约定、技术债、重要决策、常见坑、未来触发条件 | 完成重大任务、形成规则、发现技术债、拒绝重要方案后 |

---

## 4. `skills/` — 可触发工作流能力

每个 skill 都是一个可执行工作流，不是普通说明文。

### 4.1 需求与规划类

| Skill | Purpose | Trigger |
|---|---|---|
| `skills/idea-to-clarity/SKILL.md` | 将模糊想法转成真实问题、用户角色、假设、初步成功标准和 Not Doing | 用户说“我有个想法” |
| `skills/grill-with-repo/SKILL.md` | 基于仓库事实追问、挑刺、压测需求边界 | 需求方向明确但边界不清 |
| `skills/spec-before-code/SKILL.md` | 在写代码前形成 PRD/RFC/规格文档 | 需求需要规格化或审计 |
| `skills/plan-to-slices/SKILL.md` | 把需求拆成 vertical slices，并区分 HITL / AFK | 需求较大，需要任务拆解 |
| `skills/execution-prompt-compiler/SKILL.md` | 将任务切片编译成可直接交给编程智能体的高质量 Prompt | 准备执行代码修改 |

### 4.2 执行、验证、审计、沉淀类

| Skill | Purpose | Trigger |
|---|---|---|
| `skills/incremental-build/SKILL.md` | 指导编程智能体小步、可验证、可回滚地实现 | 编程智能体开始执行任务 |
| `skills/tdd-feedback-loop/SKILL.md` | 为功能、Bug、重构建立 pass/fail 验证信号 | 需要测试或验证计划 |
| `skills/diagnose-bug/SKILL.md` | 用复现、最小化、假设、证据、回归测试诊断 bug | 有报错、失败测试、异常行为 |
| `skills/review-quality-gate/SKILL.md` | 审计 diff / PR / 修改摘要，输出 PASS / NEEDS_FIX / REJECT | 编程智能体完成后 |
| `skills/architecture-deepening/SKILL.md` | 分析模块边界、技术债、架构治理触发条件 | 模块变乱、重复踩坑、需要架构治理 |
| `skills/ship-and-record/SKILL.md` | 交付总结、项目记忆沉淀、ADR/changelog 建议 | 任务通过审计后 |

---

## 5. `templates/` — 标准交付物模板

这些模板统一 AI 的输出结构。

| File | Purpose |
|---|---|
| `templates/TASK_PACKAGE_TEMPLATE.md` | 编程智能体执行任务包模板 |
| `templates/PRD_TEMPLATE.md` | 产品需求文档模板 |
| `templates/RFC_TEMPLATE.md` | 工程方案 / 审计文档模板 |
| `templates/ADR_TEMPLATE.md` | 架构决策记录模板 |
| `templates/ISSUE_SLICE_TEMPLATE.md` | 任务切片模板 |
| `templates/REVIEW_REPORT_TEMPLATE.md` | 执行后审计报告模板 |
| `templates/FEEDBACK_LOOP_TEMPLATE.md` | 测试反馈循环模板 |
| `templates/SHIP_REPORT_TEMPLATE.md` | 交付总结与沉淀模板 |

---

## 6. `references/` — 质量门和检查清单

这些文件供执行、测试、审计阶段调用。

| File | Purpose | Use When |
|---|---|---|
| `references/SECURITY_CHECKLIST.md` | 权限、安全、输入校验、密钥、文件访问检查 | 涉及用户数据、权限、文件、API、外部服务 |
| `references/PERFORMANCE_CHECKLIST.md` | 查询、批处理、文件、API、前端性能检查 | 涉及大数据、列表、导出、外部调用 |
| `references/TESTING_CHECKLIST.md` | 自动测试、手动验证、回归测试检查 | 任何重要功能或 Bug 修复 |
| `references/API_INTERFACE_CHECKLIST.md` | API 路由、参数、返回、错误、兼容性检查 | 新增或修改 API |
| `references/DATABASE_MIGRATION_CHECKLIST.md` | 数据库 schema、migration、兼容性、回滚检查 | 涉及数据库变更 |
| `references/FRONTEND_UX_CHECKLIST.md` | 前端页面状态、权限 UX、表单、列表、交互检查 | 涉及前端页面或组件 |
| `references/ANTI_OVERENGINEERING_RULES.md` | 反过度设计、反无关重构、反提前平台化规则 | 任何可能范围膨胀的任务 |

---

## 7. Runtime Directories

这些目录用于具体项目运行过程中沉淀内容。

| Directory | Purpose | Notes |
|---|---|---|
| `tasks/` | 每次任务过程记录，如 idea、clarity、prd、plan、exec-prompt、review、ship-report | 可按日期和任务名建子目录 |
| `decisions/` | ADR 架构决策记录 | 只记录长期重要决策 |
| `reviews/` | 代码审计报告 | 可按 PR 或任务编号归档 |
| `changelog/` | AI 协作层或项目重要交付变化记录 | 可按日期记录 |

---

## 8. Recommended Reading by Role

### Human User

优先阅读：

```text
README.md
START_HERE.md
INSTALL.md
MANIFEST.md
```

### Strategist / 军师模型

优先阅读：

```text
START_HERE.md
system/AI_MASTER_PROMPT.md
system/AI_OPERATING_MODES.md
system/AI_DELIVERY_WORKFLOW.md
project/AI_REPO_CONTEXT.md
project/AI_DOMAIN_CONTEXT.md
project/AI_PROJECT_MEMORY.md
```

### Coding Agent / 编程智能体

优先阅读：

```text
START_HERE.md
system/AI_AGENT_RULES.md
project/AI_REPO_CONTEXT.md
project/AI_DOMAIN_CONTEXT.md
tasks/<current-task>/04-exec-prompt.md
```

### Review Agent / 审计智能体

优先阅读：

```text
skills/review-quality-gate/SKILL.md
templates/REVIEW_REPORT_TEMPLATE.md
references/SECURITY_CHECKLIST.md
references/TESTING_CHECKLIST.md
references/ANTI_OVERENGINEERING_RULES.md
```

---

## 9. Current v0.1.0 File Count

| Layer | Count |
|---|---:|
| Root docs | 6 |
| system | 4 |
| project | 4 |
| skills | 11 |
| templates | 8 |
| references | 7 |
| runtime placeholder dirs | 4 |

Total documented files/directories: 44 entries.

---

## 10. Final Note

如果你不知道当前应该读取哪个文件，请从这里开始：

```text
START_HERE.md
MANIFEST.md
project/AI_CONTEXT_MAP.md
```
