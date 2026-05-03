# Feedback Loop Template

本模板用于为功能、Bug 修复、重构或复杂改动建立可重复的验证反馈。

---

# Feedback Loop: [Task / Behavior Name]

## 1. Behaviors to Verify

| Behavior | Acceptance Criteria | Priority |
|---|---|---|
| [行为] | [对应验收标准] | High / Medium / Low |

---

## 2. Feedback Strategy

| Behavior | Test Type | Why |
|---|---|---|
| [行为] | Unit / Integration / E2E / Manual | [原因] |

---

## 3. Normal Path Tests

| Scenario | Steps | Expected Result |
|---|---|---|
| [正常场景] | [步骤] | [预期结果] |

---

## 4. Edge / Failure Path Tests

| Scenario | Steps | Expected Result |
|---|---|---|
| Empty data | [步骤] | [结果] |
| Invalid input | [步骤] | [结果] |
| Permission denied | [步骤] | [结果] |
| External service failure | [步骤] | [结果] |
| Large data | [步骤] | [结果] |

---

## 5. Regression Tests

如果是 Bug 修复，请填写：

```text
之前如何失败：
修复后如何证明不会再失败：
测试位置：
```

---

## 6. Test Commands

```bash
# command here
```

Expected result:

```text
[预期输出]
```

---

## 7. Manual Verification

| Step | Action | Expected Result |
|---|---|---|
| 1 | [操作] | [结果] |

---

## 8. Evidence to Capture

- [ ] 测试命令。
- [ ] 测试结果。
- [ ] 失败日志。
- [ ] 手动验证步骤。
- [ ] 截图或 API 响应，如适用。

---

## 9. Missing Test Seams / Technical Debt

| Missing Seam | Impact | Suggested Future Refactor |
|---|---|---|
| [缺失 seam] | [影响] | [建议] |

---

## 10. Pass / Fail Definition

### Pass

```text
[什么情况下认为通过]
```

### Fail

```text
[什么情况下认为失败]
```
