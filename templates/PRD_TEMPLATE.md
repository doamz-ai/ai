# PRD Template

本模板用于在写代码前形成产品需求文档。

PRD 的目标不是写长文档，而是让人类、军师模型和编程智能体对“为什么做、为谁做、做什么、不做什么、如何验收”达成一致。

---

# PRD: [Feature / Change Name]

## 1. Background

### 1.1 Current Situation

```text
[当前业务或系统现状]
```

### 1.2 Problem Source

```text
[问题从哪里来：用户反馈、运营需求、技术债、未来规划、错误修复等]
```

### 1.3 Why Now

```text
[为什么现在要做]
```

---

## 2. Problem Definition

### 2.1 Surface Problem

```text
[用户表面上提出的问题]
```

### 2.2 Real Problem

```text
[第一性原理识别出的真实问题]
```

---

## 3. Users and JTBD

| User Role | Situation | Wants To | Business Value |
|---|---|---|---|
| [角色] | [场景] | [动作] | [价值] |

---

## 4. Goals

本次要实现：

1. [目标 1]
2. [目标 2]
3. [目标 3]

---

## 5. Non-goals

本次明确不做：

1. [非目标 1]
2. [非目标 2]
3. [非目标 3]

---

## 6. User Stories

### Story 1

作为 [角色]，当 [场景] 时，我希望 [动作]，以便 [价值]。

### Story 2

作为 [角色]，当 [场景] 时，我希望 [动作]，以便 [价值]。

---

## 7. Business Flow

```text
Step 1
→ Step 2
→ Step 3
→ End State
```

---

## 8. Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| FR-001 | [需求] | Must / Should / Could | [备注] |

---

## 9. Permission Requirements

| Role | Can Do | Cannot Do | Notes |
|---|---|---|---|
| [角色] | [可做] | [不可做] | [备注] |

---

## 10. Data Requirements

| Data / Entity | Purpose | Source | Retention / Lifecycle |
|---|---|---|---|
| [数据] | [用途] | [来源] | [生命周期] |

---

## 11. UX / Interaction Requirements

### 11.1 Entry Point

```text
[页面入口 / 菜单 / 按钮 / API 调用入口]
```

### 11.2 States

需要考虑：

- Loading
- Empty
- Success
- Failed
- Permission denied
- Partial result

### 11.3 User-facing Copy

```text
[关键提示文案]
```

---

## 12. Acceptance Criteria

1. 当 [场景] 时，系统应该 [结果]。
2. 当 [异常场景] 时，系统应该 [结果]。
3. 当 [无权限场景] 时，系统应该 [结果]。
4. 当 [空数据场景] 时，系统应该 [结果]。

---

## 13. Risks

| Risk | Impact | Mitigation |
|---|---|---|
| [风险] | [影响] | [缓解方式] |

---

## 14. Open Questions

| Question | Why It Matters | Owner / Next Step |
|---|---|---|
| [问题] | [原因] | [下一步] |

---

## 15. Next Step

建议进入：

- [ ] Grill Mode
- [ ] Spec / RFC
- [ ] Plan to Slices
- [ ] Execution Prompt
- [ ] Stop / Revisit Later
