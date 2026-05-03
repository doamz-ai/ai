# ADR Template

ADR = Architecture Decision Record。

本模板用于记录重要架构决策的背景、选择、替代方案和后果。

ADR 不应滥用。只有当决策长期影响较大、未来维护者可能疑惑、存在多个合理方案或涉及不可逆取舍时，才需要创建 ADR。

---

# ADR-[Number]: [Decision Title]

## Status

```text
Proposed / Accepted / Superseded / Deprecated
```

## Date

```text
YYYY-MM-DD
```

## Owners

```text
[Human / Team / AI-assisted]
```

---

## 1. Context

```text
[当前背景，为什么需要做这个决策]
```

---

## 2. Problem

```text
[需要解决的架构问题]
```

---

## 3. Decision

```text
[最终决定采用什么方案]
```

---

## 4. Alternatives Considered

| Option | Description | Pros | Cons | Why Accepted / Rejected |
|---|---|---|---|---|
| A | [方案] | [优点] | [缺点] | [原因] |
| B | [方案] | [优点] | [缺点] | [原因] |

---

## 5. Consequences

### 5.1 Positive

- [正面影响]

### 5.2 Negative

- [负面影响]

### 5.3 Neutral / Trade-offs

- [中性取舍]

---

## 6. Scope

该决策影响：

- [模块 / 数据 / API / 部署 / 权限]

该决策不影响：

- [不影响的范围]

---

## 7. Implementation Notes

```text
[实现注意事项，不需要写具体代码]
```

---

## 8. Migration / Rollback

### Migration

```text
[迁移方式]
```

### Rollback

```text
[回滚方式]
```

---

## 9. Follow-up Tasks

- [ ] [任务 1]
- [ ] [任务 2]

---

## 10. Supersedes / Superseded By

- Supersedes: [ADR-xxxx / None]
- Superseded by: [ADR-xxxx / None]

---

## 11. Notes for AI Agents

```text
[未来 AI 处理相关模块时必须知道的规则]
```
