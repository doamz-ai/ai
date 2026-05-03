# AI Project Memory

本文件记录当前项目长期有效的 AI 协作记忆。

它不是任务过程记录，也不是聊天记录，而是项目在长期演进中沉淀下来的架构约定、技术债、决策背景、常见坑和未来触发条件。

---

## 0. Maintenance Rules

### 0.1 What belongs here

本文件只记录未来仍然值得 AI 和人类知道的信息：

- 长期架构约定。
- 重要技术决策摘要。
- 明确不做的事情。
- 已延期技术债。
- 高风险模块。
- 常见坑。
- 项目特定 AI 协作规则。
- 未来触发条件。

### 0.2 What does not belong here

不要记录：

- 临时讨论。
- 单次任务的完整过程。
- 大段 diff。
- 已过期计划。
- 没有长期价值的报错。
- 重复的 README 内容。

### 0.3 Update timing

以下情况应更新本文件：

- 完成重要功能。
- 形成长期架构约定。
- 发现并延期技术债。
- 拒绝某个重要方案。
- 做出会影响未来开发的决策。
- 审计中发现常见风险。
- 用户明确给出长期规则。

---

## 1. Project Memory Summary

### 1.1 Current Project Identity

```text
[To Fill: 项目长期定位，一句话说明]
```

### 1.2 Current Engineering Direction

```text
[To Fill: 当前项目主要工程方向，例如稳定化、MVP、重构、性能优化、权限治理等]
```

### 1.3 Current AI Collaboration Stage

```text
[To Fill: 未初始化 / 已生成上下文 / 已建立任务流程 / 已进入审计闭环]
```

---

## 2. Permanent Architecture Rules

这些规则长期有效，除非后续 ADR 明确替代。

| Rule | Reason | Source / Evidence | Since |
|---|---|---|---|
| [To Fill] | [To Fill] | [To Fill] | YYYY-MM-DD |

Example:

| Rule | Reason | Source / Evidence | Since |
|---|---|---|---|
| Large export files must not remain on local server disk permanently. | Prevent disk bloat and leakage risk. | ADR-0001 / task report | 2026-05-03 |

---

## 3. Permanent AI Agent Rules for This Repo

这些是本项目特有的 AI 执行规则。

- [To Fill]

Examples:

- Do not rewrite the authentication system unless explicitly requested.
- Do not change existing API response shape without migration plan.
- Do not introduce new background queue infrastructure without HITL approval.

---

## 4. Important Architecture Decisions

简要记录重要决策。详细内容应放入 `.ai/decisions/ADR-xxxx.md`。

| Decision | Summary | ADR | Status | Date |
|---|---|---|---|---|
| [To Fill] | [To Fill] | ADR-xxxx | Active / Superseded | YYYY-MM-DD |

---

## 5. Explicit Non-goals / Not Doing

这些是已经明确“不做”或“暂不做”的方向。

| Not Doing | Reason | Revisit When | Source |
|---|---|---|---|
| [To Fill] | [To Fill] | [To Fill] | [To Fill] |

Example:

| Not Doing | Reason | Revisit When | Source |
|---|---|---|---|
| Do not implement full MCP commercialization in current phase. | Current priority is web query stability and export workflow. | When core query APIs are stable and permission model is complete. | Task 2026-05-03 |

---

## 6. Deferred Technical Debt

| Debt | Impact | Current Workaround | Revisit Trigger | Priority |
|---|---|---|---|---|
| [To Fill] | [To Fill] | [To Fill] | [To Fill] | High / Medium / Low |

### 6.1 Technical Debt Handling Rule

如果编程智能体在任务中发现无关技术债：

1. 不要顺手修。
2. 记录在任务报告中。
3. 由军师判断是否进入本文件。
4. 未来单独立项处理。

---

## 7. Known Risk Areas

| Area | Risk | What Agents Must Do | What Agents Must Avoid |
|---|---|---|---|
| [To Fill] | [To Fill] | [To Fill] | [To Fill] |

Examples:

- 权限模块。
- 数据迁移模块。
- 大文件导出模块。
- 支付 / 计费模块。
- 异步任务模块。
- 核心查询算法模块。

---

## 8. Common Pitfalls

| Pitfall | Why It Happens | Prevention |
|---|---|---|
| [To Fill] | [To Fill] | [To Fill] |

Example:

| Pitfall | Why It Happens | Prevention |
|---|---|---|
| AI adds frontend-only permission hiding but forgets backend enforcement. | UI tasks often hide security requirements. | Always check SECURITY_CHECKLIST and backend resource ownership. |

---

## 9. Completed Major Tasks

只记录重要任务摘要。完整过程放在 `.ai/tasks/`。

### YYYY-MM-DD — [Task Name]

#### Goal

```text
[To Fill]
```

#### Summary

- [To Fill]

#### Key Files

- `[path]`

#### Tests / Verification

- [To Fill]

#### Follow-up

- [To Fill]

---

## 10. Rejected or Superseded Approaches

记录被拒绝的重要方案，避免未来 AI 反复提出。

| Approach | Why Rejected | Revisit Condition | Date |
|---|---|---|---|
| [To Fill] | [To Fill] | [To Fill] | YYYY-MM-DD |

---

## 11. Future Roadmap Notes

这些不是承诺，只是未来可能方向。

| Idea | Why It Matters | Do Not Implement Until | Notes |
|---|---|---|---|
| [To Fill] | [To Fill] | [To Fill] | [To Fill] |

---

## 12. AI Collaboration Notes

### 12.1 Preferred Workflow for This Repo

```text
[To Fill: 例如 所有大改先 RFC，再拆任务，再 PR 审计]
```

### 12.2 Preferred Coding Agent

```text
[To Fill: 如适用]
```

### 12.3 Review Strictness

```text
[To Fill: Normal / Strict / Very Strict]
```

### 12.4 Human Approval Required For

- [To Fill]

Examples:

- Database destructive migration。
- Permission model changes。
- New infrastructure dependencies。
- Public API breaking changes。
- Cost-increasing external services。

---

## 13. Project-specific Quality Gates

| Gate | Required Evidence | Applies To |
|---|---|---|
| [To Fill] | [To Fill] | [To Fill] |

---

## 14. Last Updated

```text
Last Updated: YYYY-MM-DD
Updated By: [Human / AI]
Evidence Scope: [Full repo / partial / task-based]
```
