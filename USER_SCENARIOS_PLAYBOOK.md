# User Scenarios Playbook

本文件面向非专业 IT 用户，说明 AI Engineering Delivery OS 在真实使用中的常见场景、推荐操作和信息流转方式。

核心目标：

```text
用户提出想法
→ 网页 GPT 基于 GitHub 中的 .ai/ 做规划
→ 规划写入 .ai/tasks/
→ IDE pull 最新 .ai/
→ IDE 审查并执行
→ IDE 把进度和结果回写到 .ai/
→ 网页 GPT 再读取 GitHub 继续辅助
```

---

## 1. Golden Path: 标准闭环

最推荐的日常闭环：

```text
1. IDE 安装 .ai/
2. IDE 初始化 project/ 上下文
3. IDE 提交并推送 .ai/ 到目标项目 GitHub
4. 网页 GPT 选择目标项目 GitHub 仓库
5. 网页 GPT 冷启动读取 .ai/
6. 用户用大白话聊想法
7. 网页 GPT 输出 PRD / RFC / Plan / Exec Prompt
8. 网页 GPT 只写 .ai/tasks/，不碰业务代码
9. IDE pull 最新 GitHub
10. IDE 读取 .ai/tasks/ 并挑战性审查
11. IDE 修正或执行代码任务
12. IDE 把执行摘要、测试结果、风险回写 .ai/tasks/
13. IDE 推送代码和 .ai/ 进度
14. 网页 GPT 再读取 GitHub，继续讨论或审计
```

---

## 2. Scenario A: 新项目第一次安装

### 用户状态

用户已经在 IDE 中打开一个本地项目，但还没有 `.ai/` 文件夹。

### 推荐操作

在 IDE 中使用：

```text
prompts/install-from-github.md
```

### 目标

- 从 `doamz-ai/ai` 安装模板到当前项目 `.ai/`。
- 初始化 `.ai/project/`。
- 提交并推送 `.ai/` 到目标项目 GitHub。

### 关键提醒

安装后一定要推送到 GitHub，否则网页版 GPT 无法读取该项目的专属 `.ai/`。

---

## 3. Scenario B: 网页 GPT 第一次打开目标项目 GitHub

### 用户状态

用户已经：

- 用 IDE 安装了 `.ai/`。
- 已把 `.ai/` 推送到目标项目 GitHub。
- 在网页版 GPT 中选择了该目标项目 GitHub。

### 推荐操作

使用：

```text
prompts/web-gpt-cold-start.md
```

### 目标

让网页 GPT：

1. 读取目标项目 `.ai/START_HERE.md`。
2. 读取 `.ai/MANIFEST.md`。
3. 读取 `.ai/project/AI_REPO_CONTEXT.md`。
4. 读取 `.ai/project/AI_DOMAIN_CONTEXT.md`。
5. 读取 `.ai/project/AI_PROJECT_MEMORY.md`。
6. 判断当前项目 AI 上下文是否完整。
7. 进入“远程军师模式”。

---

## 4. Scenario C: 用户有模糊想法，想让网页 GPT 规划

### 用户状态

用户不知道怎么写 PRD，只会用大白话描述：

```text
我感觉是不是要加个查询记录页面？
这个功能未来能不能接 MCP？
这里是不是要优化一下？
```

### 推荐操作

网页 GPT 读取：

```text
prompts/raw-idea.md
```

如用户希望把讨论结果写回 GitHub，再使用：

```text
prompts/web-gpt-write-ai-folder.md
```

### 输出位置

推荐写入：

```text
.ai/tasks/YYYY-MM-DD-short-task-name/
├── 00-idea.md
├── 01-clarity.md
├── 02-prd.md
├── 03-plan.md
└── 04-exec-prompt.md
```

### 关键提醒

网页 GPT 写入的是 Proposal，不是命令。IDE 仍需要审查。

---

## 5. Scenario D: IDE 收到网页 GPT 写入的任务计划

### 用户状态

网页 GPT 已把计划写入 `.ai/tasks/...` 并推送到 GitHub。

### 推荐操作

在 IDE 中 pull 最新代码后，使用：

```text
prompts/ide-review-ai-task.md
```

### IDE 必须做

IDE 不应该直接执行，而是先输出：

```text
ACCEPT / ACCEPT_WITH_CHANGES / NEEDS_CLARIFICATION / REJECT
```

并检查：

- 计划是否符合真实代码结构。
- 是否有更小实现方式。
- 是否有遗漏风险。
- 是否需要修改执行 Prompt。

---

## 6. Scenario E: IDE 执行完成后，把进度反馈给网页 GPT

### 用户状态

IDE 已执行部分或全部任务。

### 推荐操作

使用：

```text
prompts/ide-progress-report-to-ai-folder.md
```

### 推荐写入

```text
.ai/tasks/YYYY-MM-DD-short-task-name/05-ide-review.md
.ai/tasks/YYYY-MM-DD-short-task-name/06-implementation-summary.md
.ai/tasks/YYYY-MM-DD-short-task-name/07-test-results.md
.ai/tasks/YYYY-MM-DD-short-task-name/08-open-issues.md
```

### 目的

让网页版 GPT 下次连接 GitHub 时知道：

- IDE 接受了什么。
- 改了什么。
- 测试了什么。
- 还剩什么风险。
- 下一步该聊什么。

---

## 7. Scenario F: 网页 GPT 继续接上次上下文

### 用户状态

聊天窗口变长、上下文快满，或者用户换了新 GPT 窗口。

### 推荐操作

使用：

```text
prompts/web-gpt-cold-start.md
```

然后告诉 GPT：

```text
请读取 .ai/tasks/ 最近的任务记录，并根据 IDE 回写的 progress 继续。
```

### 目的

避免依赖聊天窗口记忆，让 GitHub `.ai/` 成为真实上下文。

---

## 8. Scenario G: 用户只想要一段给 IDE 的 Prompt，不想写入 GitHub

### 推荐操作

网页 GPT 读取：

```text
prompts/compile-exec-prompt.md
```

### 输出

直接在聊天窗口输出一段可复制给 IDE 的 Prompt。

### 适合

- 小任务。
- 临时实验。
- 用户不想污染 `.ai/tasks/`。

---

## 9. Scenario H: 网页 GPT 需要审计 IDE 改完的代码

### 用户状态

IDE 已经推送代码或开了 PR。

### 推荐操作

网页 GPT 使用：

```text
prompts/review-diff.md
```

### 输出

- PASS / NEEDS_FIX / REJECT。
- Critical / Important / Optional / FYI。
- Fix Prompt。
- 是否需要更新项目记忆。

---

## 10. Scenario I: IDE 认为网页 GPT 的方案不对

### 正确处理

IDE 应输出：

```text
REJECT
```

或：

```text
ACCEPT_WITH_CHANGES
```

并把理由写回：

```text
.ai/tasks/<task-name>/05-ide-review.md
```

### 网页 GPT 下一步

网页 GPT 读取该文件后，重新调整：

- PRD。
- Plan。
- Exec Prompt。

---

## 11. Scenario J: 用户想公开分享给同事

### 推荐步骤

1. 将 `doamz-ai/ai` 仓库改为 public。
2. 让同事在自己的项目 IDE 中使用：

```text
prompts/install-from-github.md
```

3. 同事安装后，提交并推送自己项目的 `.ai/`。
4. 同事以后可以在网页版 GPT 中选择自己的项目 GitHub。

### 给同事的一句话

```text
这是一个安装到你项目里的 AI 协作文件夹。IDE 用它执行，网页 GPT 用它规划，GitHub 用它传递上下文。
```

---

## 12. Scenario K: 用户没有 GitHub 写权限

### 推荐操作

只读模式。

网页 GPT 可以读取项目和 `.ai/`，但不写入。

输出内容让用户复制给 IDE。

### 不应做

不要假装已经写入 GitHub。

---

## 13. Scenario L: 目标项目还没安装 `.ai/`

### 网页 GPT 应提示

```text
当前项目未检测到 .ai/。建议先在 IDE 中从 doamz-ai/ai 安装 AI Engineering Delivery OS，并推送到 GitHub。
```

然后给用户 `prompts/install-from-github.md` 的使用方式。

---

## 14. Scenario M: 多个任务并行

### 推荐规则

每个任务单独目录：

```text
.ai/tasks/YYYY-MM-DD-task-a/
.ai/tasks/YYYY-MM-DD-task-b/
```

不要把多个任务混在一个目录。

### 状态建议

每个任务目录可以有：

```text
STATUS.md
```

状态：

```text
PROPOSAL
READY_FOR_IDE_REVIEW
ACCEPTED_BY_IDE
IN_PROGRESS
NEEDS_FIX
SHIPPED
ARCHIVED
```

---

## 15. Scenario N: 用户不知道当前该做什么

网页 GPT 冷启动后应输出：

```text
当前项目 AI 上下文状态
最近任务
可继续的任务
建议下一步
```

而不是直接问用户“你想做什么”。

---

## 16. Recommended User Mental Model

用户只需要记住：

```text
IDE 负责安装、执行、推送。
网页 GPT 负责规划、整理、审计。
GitHub 的 .ai/ 负责传话和记忆。
```

---

## 17. Minimal Prompts Users Need

小白用户最常用 5 个 Prompt：

1. `prompts/install-from-github.md`
2. `prompts/web-gpt-cold-start.md`
3. `prompts/raw-idea.md`
4. `prompts/web-gpt-write-ai-folder.md`
5. `prompts/ide-review-ai-task.md`

---

## 18. Final Rule

如果用户迷路了，回到这个闭环：

```text
网页 GPT 产出计划 → 写入 .ai/tasks → IDE 审查执行 → IDE 回写进度 → GitHub 同步 → 网页 GPT 继续辅助
```
