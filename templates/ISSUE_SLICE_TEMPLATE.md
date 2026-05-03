# Issue Slice Template

本模板用于把一个需求拆成小而可执行、可验证、可审计的任务切片。

优先使用 vertical slice，而不是按技术层横切。

---

# Slice [ID]: [Slice Name]

## 1. Summary

```text
[本切片一句话目标]
```

---

## 2. Slice Type

选择一个：

- Investigation
- Spec
- Data
- Backend
- Frontend
- Permission
- Storage
- Test
- Docs
- Review

```text
[Type]
```

---

## 3. HITL / AFK

```text
HITL / AFK
```

### Reason

```text
[为什么需要人类参与，或为什么智能体可独立执行]
```

---

## 4. Goal

本切片必须完成：

1. [目标 1]
2. [目标 2]

---

## 5. Non-goals

本切片明确不做：

1. [非目标 1]
2. [非目标 2]

---

## 6. Inputs

| Input | Source |
|---|---|
| [输入] | [来源] |

---

## 7. Outputs

| Output | Expected Location |
|---|---|
| [输出] | [文件/代码/文档路径] |

---

## 8. Files / Modules to Inspect

| Path / Module | Reason |
|---|---|
| `[path]` | [原因] |

---

## 9. Implementation Notes

```text
[实现注意事项]
```

---

## 10. Acceptance Criteria

1. 当 [场景] 时，系统应该 [结果]。
2. 当 [异常场景] 时，系统应该 [结果]。
3. 不应破坏 [旧功能]。

---

## 11. Test / Verification

| Verification | Method | Expected Result |
|---|---|---|
| [验证项] | [自动测试/手动验证] | [结果] |

---

## 12. Risks

| Risk | Severity | Mitigation |
|---|---|---|
| [风险] | High / Medium / Low | [缓解方式] |

---

## 13. Dependencies

| Dependency | Type | Notes |
|---|---|---|
| [依赖] | Before / After | [备注] |

---

## 14. Done Definition

本切片完成的定义：

- [ ] 满足 Goals。
- [ ] 没有违反 Non-goals。
- [ ] 验收标准可验证。
- [ ] 输出修改摘要。
- [ ] 记录未解决风险或技术债。
