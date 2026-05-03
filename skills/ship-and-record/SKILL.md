# Skill: Ship and Record

## Purpose

在任务通过审计后，完成交付总结、风险记录、项目记忆沉淀、领域词典更新和必要的 ADR / changelog 记录。

本 skill 的目标是让项目从每次 AI 协作中学习，而不是把经验散落在聊天记录里。

---

## When to Use

当出现以下情况时使用：

- Review verdict 为 PASS。
- 任务准备合并、发布或归档。
- 用户要求“总结本次改动”。
- 任务产生了长期规则、技术债、术语或架构决策。
- 需要更新 `.ai/project/AI_PROJECT_MEMORY.md`。
- 需要写 ADR 或 changelog。

---

## Core Principle

不要把所有过程都沉淀。

只记录未来仍然值得知道的信息。

应该沉淀：

```text
长期架构约定
新领域术语
重要设计取舍
明确不做的事情
延期技术债
高风险模块
常见坑
未来触发条件
```

不应该沉淀：

```text
临时讨论
大段 diff
已过期计划
无长期价值的小错误
重复信息
```

---

## Required Inputs

建议读取：

```text
.ai/templates/SHIP_REPORT_TEMPLATE.md
.ai/project/AI_PROJECT_MEMORY.md
.ai/project/AI_DOMAIN_CONTEXT.md
.ai/templates/ADR_TEMPLATE.md
```

并获取：

- 原任务目标。
- 实现摘要。
- Review Report。
- 测试结果。
- 最终风险和延期事项。

---

## Workflow

### Step 1: Confirm Ship Readiness

```markdown
## 1. Ship Readiness

- Review verdict: PASS / NEEDS_FIX / REJECT
- Critical issues resolved: Yes / No
- Tests / verification available: Yes / No
- Human accepted remaining risks: Yes / No / Not needed
```

如果 verdict 不是 PASS，通常不应进入 Ship。

---

### Step 2: Summarize Delivery

```markdown
## 2. Delivery Summary

- Completed: ...
- Key files changed: ...
- User-visible impact: ...
- Internal impact: ...
```

---

### Step 3: Summarize Verification

```markdown
## 3. Verification Summary

- Automated tests: ...
- Manual verification: ...
- Not tested: ...
- Reason: ...
```

---

### Step 4: Capture Remaining Risks

```markdown
## 4. Remaining Risks

| Risk | Severity | Accepted / Deferred | Follow-up |
|---|---|---|---|
```

---

### Step 5: Decide Memory Updates

判断是否需要更新：

```text
.ai/project/AI_PROJECT_MEMORY.md
.ai/project/AI_DOMAIN_CONTEXT.md
.ai/project/AI_REPO_CONTEXT.md
.ai/decisions/
.ai/changelog/
.ai/tasks/
.ai/reviews/
```

格式：

```markdown
## 5. Memory Update Suggestions

### AI_PROJECT_MEMORY.md
- ...

### AI_DOMAIN_CONTEXT.md
- ...

### AI_REPO_CONTEXT.md
- ...

### ADR
- Needed / Not needed

### Changelog
- ...
```

---

### Step 6: Decide ADR

需要 ADR 的情况：

- 决策长期影响大。
- 决策未来可能被质疑。
- 有多个合理方案被权衡。
- 涉及数据、权限、基础设施、架构边界。

如果需要，输出 ADR 草案标题和摘要。

---

### Step 7: Produce Ship Report

输出可归档报告。

---

## Output Format

```markdown
# Ship Report

## 1. Ship Readiness

## 2. Delivery Summary

## 3. Verification Summary

## 4. Remaining Risks

| Risk | Severity | Accepted / Deferred | Follow-up |
|---|---|---|---|

## 5. Memory Update Suggestions

### AI_PROJECT_MEMORY.md
- ...

### AI_DOMAIN_CONTEXT.md
- ...

### AI_REPO_CONTEXT.md
- ...

### ADR
- ...

### Changelog
- ...

## 6. Deferred Technical Debt

| Debt | Impact | Revisit Trigger | Priority |
|---|---|---|---|

## 7. Follow-up Tasks

- ...
```

---

## Quality Bar

好的交付沉淀应该：

- 简洁。
- 只记录长期有效信息。
- 明确剩余风险。
- 明确延期技术债。
- 判断是否需要 ADR。
- 给出项目记忆更新建议。

---

## Anti-patterns

禁止：

- 把完整聊天记录塞进项目记忆。
- 把大段 diff 塞进长期文档。
- 未通过审计就交付。
- 忽略剩余风险。
- 重要决策不记录原因。
- 技术债只口头说，不登记。

---

## Handoff

完成后：

- 人类可合并 / 发布。
- 编程智能体可更新文档。
- 军师模型可在下一次任务中读取项目记忆。
