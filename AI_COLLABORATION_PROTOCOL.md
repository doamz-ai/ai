# AI Collaboration Protocol

本文件定义 AI Engineering Delivery OS 在多模型、多环境、多智能体协作中的治理原则。

重点解决：

1. IDE 模型可能比当前规划模型更强，如何避免无脑执行错误规划。
2. 网页 GPT 与 IDE 智能体如何通过 GitHub 中的 `.ai/` 文件夹传递想法。
3. GPT 是否可以写入目标项目 GitHub。
4. 如何限制 GPT 只写 `.ai/`，坚决不碰业务代码。

---

## 1. Core Principle

AI Engineering Delivery OS 不是命令 IDE 模型无脑执行的上级系统。

它是一个协作协议。

更准确的关系是：

```text
网页 GPT / 军师模型：负责需求澄清、结构化表达、方案草案、审计思路。
IDE 模型 / 编程智能体：负责读取真实本地代码、校验方案、执行实现、提出反驳。
GitHub `.ai/`：负责在两者之间保存可追踪、可版本化的工程上下文。
```

所以 IDE 模型不是“执行奴隶”，而是“带有否决权的工程合作者”。

---

## 2. Planning Authority Rule

任何由网页 GPT、其他模型或人类写入 `.ai/` 的方案，都默认是：

```text
Proposal, not command.
```

也就是说：

- 方案可以被 IDE 模型质疑。
- 方案可以被 IDE 模型修正。
- 方案可以被 IDE 模型拒绝。
- 方案必须经过仓库事实校验后才能进入代码实现。

---

## 3. IDE Model Challenge Rule

IDE 智能体在执行 `.ai/` 中的计划前，必须先做一次挑战性审查。

必须回答：

1. 该计划是否符合当前真实代码结构？
2. 是否有过度设计？
3. 是否有更小、更安全的实现方式？
4. 是否遗漏权限、数据、测试、性能、部署风险？
5. 是否存在错误假设？
6. 是否需要拆成更小任务？
7. 是否应先回到 Spec / Plan，而不是直接 Build？

如果发现问题，IDE 模型应输出：

```text
ACCEPT / ACCEPT_WITH_CHANGES / NEEDS_CLARIFICATION / REJECT
```

---

## 4. Decision Levels

### 4.1 Proposal

来自网页 GPT、人类、其他模型的想法或方案。

位置：

```text
.ai/tasks/<task-name>/
```

状态：可讨论，不可直接视为最终执行命令。

---

### 4.2 Reviewed Plan

经过 IDE 模型结合真实代码审查后的计划。

状态：可进入执行 Prompt 编译。

---

### 4.3 Execution Prompt

给编程智能体的具体任务包。

状态：可执行，但仍受 `AI_AGENT_RULES.md` 约束。

---

### 4.4 Implemented Code

业务代码改动。

状态：必须经过 Review Quality Gate。

---

### 4.5 Shipped Memory

通过审计后沉淀到项目长期记忆。

状态：长期上下文。

---

## 5. Web GPT GitHub Write Policy

网页 GPT 可以作为“远程军师”写入目标项目 GitHub，但默认只允许写 `.ai/` 目录。

### 5.1 Allowed

网页 GPT 可以创建或更新：

```text
.ai/tasks/<task-name>/00-idea.md
.ai/tasks/<task-name>/01-clarity.md
.ai/tasks/<task-name>/02-prd.md
.ai/tasks/<task-name>/03-plan.md
.ai/tasks/<task-name>/04-exec-prompt.md
.ai/tasks/<task-name>/05-review-notes.md
.ai/tasks/<task-name>/06-ship-report.md

.ai/reviews/<review-name>.md
.ai/decisions/ADR-xxxx.md
.ai/changelog/<date>.md
```

用途：传递想法、计划、审计意见、任务包。

---

### 5.2 Forbidden

网页 GPT 不得修改：

```text
src/
app/
backend/
frontend/
api/
server/
client/
packages/
lib/
components/
pages/
routes/
db/
migrations/
config/
.env*
任何业务代码、配置、数据库迁移或部署文件
```

除非用户在当前对话中明确授权，并且任务本身就是代码修改。

本协议默认用途是“传递想法给 IDE”，不是让网页 GPT 直接改业务代码。

---

## 6. Git as Communication Bus

推荐协作方式：

```text
网页 GPT 讨论并生成方案
→ 网页 GPT 写入目标项目 `.ai/tasks/...`
→ 推送到 GitHub
→ IDE 同步 / pull 最新 GitHub 内容
→ IDE 读取 `.ai/tasks/...`
→ IDE 挑战性审查
→ IDE 生成或修正执行 Prompt
→ IDE 执行业务代码修改
→ IDE 推送代码或 PR
→ 网页 GPT 可再次审计 diff
```

这样信息传递通过 Git 完成，不需要手动复制本地文件夹。

---

## 7. Recommended Branch Strategy

### 7.1 Web GPT Writes

网页 GPT 写入 `.ai/` 时，推荐使用独立分支：

```text
ai/plan/<task-name>
```

或：

```text
ai/context/<task-name>
```

再开 PR，方便 IDE 和人类查看。

### 7.2 Direct Commit Exception

如果目标项目是个人实验项目，且用户明确希望快速推进，可以直接提交到主分支，但仍只允许 `.ai/` 目录。

---

## 8. IDE Review of AI-folder Plans

IDE 模型读取 `.ai/tasks/<task-name>/` 后，不应直接执行。

应先输出：

```markdown
# IDE Plan Review

## Verdict

ACCEPT / ACCEPT_WITH_CHANGES / NEEDS_CLARIFICATION / REJECT

## Repo Reality Check

## Better Smaller Option

## Risks Missed by Plan

## Required Changes Before Build

## Final Execution Prompt
```

---

## 9. When Web GPT Should Be Read-only

网页 GPT 应保持只读，不写 GitHub 的情况：

- 用户只是想快速讨论。
- 方案还很模糊。
- 当前任务涉及敏感业务代码。
- 目标项目尚未安装 `.ai/`。
- 用户没有明确要求写入 GitHub。

---

## 10. When Web GPT Can Write `.ai/`

网页 GPT 可以写入 `.ai/` 的情况：

- 用户明确要求把讨论结果沉淀到 GitHub。
- 内容是计划、PRD、RFC、任务包、审计报告，而不是业务代码。
- 写入路径在 `.ai/` 内。
- 文件名和任务目录清晰。
- 不会覆盖已有项目长期记忆，或覆盖前已确认。

---

## 11. Final Rule

```text
网页 GPT 负责把想法变成可追踪的工程上下文。
IDE 模型负责基于真实代码挑战、修正并执行。
GitHub 的 `.ai/` 文件夹负责做两者之间的通信总线。
业务代码只能由明确授权的编程执行流程修改。
```
