# Ship Report Template

本模板用于任务通过审计后，生成交付总结和项目记忆沉淀建议。

---

# Ship Report: [Task / Release Name]

## 1. Ship Readiness

| Check | Status | Notes |
|---|---|---|
| Review verdict is PASS | Yes / No | [备注] |
| Critical issues resolved | Yes / No | [备注] |
| Tests / verification available | Yes / No | [备注] |
| Remaining risks accepted | Yes / No / N/A | [备注] |

---

## 2. Delivery Summary

### Completed

- [完成内容]

### User-visible Impact

```text
[用户可见变化]
```

### Internal Impact

```text
[内部工程变化]
```

### Key Files

| File | Purpose |
|---|---|
| `[path]` | [用途] |

---

## 3. Verification Summary

### Automated Tests

| Command | Result | Notes |
|---|---|---|
| `[command]` | Pass / Fail / Not Run | [备注] |

### Manual Verification

- [验证步骤]

### Not Tested

| Item | Reason | Risk |
|---|---|---|
| [未测试项] | [原因] | [风险] |

---

## 4. Remaining Risks

| Risk | Severity | Accepted / Deferred | Follow-up |
|---|---|---|---|
| [风险] | Critical / Important / Optional | Accepted / Deferred | [后续] |

---

## 5. Deferred Technical Debt

| Debt | Impact | Revisit Trigger | Priority |
|---|---|---|---|
| [技术债] | [影响] | [触发条件] | High / Medium / Low |

---

## 6. Memory Update Suggestions

### AI_PROJECT_MEMORY.md

建议写入：

- [长期规则 / 技术债 / 常见坑]

### AI_DOMAIN_CONTEXT.md

建议写入：

- [新术语 / 概念澄清 / 命名约定]

### AI_REPO_CONTEXT.md

建议写入：

- [新模块 / 新 API / 新数据模型 / 新部署变化]

---

## 7. ADR Decision

是否需要 ADR：Yes / No

原因：

```text
[说明]
```

如需要，建议 ADR 标题：

```text
ADR-XXXX: [Title]
```

---

## 8. Changelog Entry

```markdown
## YYYY-MM-DD — [Task Name]

- Completed: ...
- Changed: ...
- Tests: ...
- Risks: ...
```

---

## 9. Follow-up Tasks

- [ ] [后续任务 1]
- [ ] [后续任务 2]

---

## 10. Final Notes

```text
[其他说明]
```
