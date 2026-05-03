# RFC Template

本模板用于形成工程方案审计文档。

RFC 适合处理涉及架构、接口、数据、权限、部署、存储、兼容性或多模块改动的需求。

---

# RFC: [Change / Architecture Proposal Name]

## 1. Summary

```text
[用 3-5 句话说明本 RFC 要解决什么问题、推荐什么方案]
```

---

## 2. Context

### 2.1 Current System

```text
[当前系统现状]
```

### 2.2 Current Pain Points

- [痛点 1]
- [痛点 2]
- [痛点 3]

### 2.3 Repo Evidence

| Fact | Evidence |
|---|---|
| [事实] | [文件/模块/路径] |

---

## 3. Problem Statement

```text
[真实工程问题定义]
```

---

## 4. Goals

1. [目标 1]
2. [目标 2]
3. [目标 3]

---

## 5. Non-goals

1. [非目标 1]
2. [非目标 2]
3. [非目标 3]

---

## 6. Proposed Solution

### 6.1 Overview

```text
[推荐方案概述]
```

### 6.2 Flow

```text
Step 1
→ Step 2
→ Step 3
→ End State
```

### 6.3 Key Design Points

- [设计点 1]
- [设计点 2]
- [设计点 3]

---

## 7. Alternatives Considered

| Option | Description | Pros | Cons | Decision |
|---|---|---|---|---|
| A | [方案] | [优点] | [缺点] | Accepted / Rejected |
| B | [方案] | [优点] | [缺点] | Accepted / Rejected |

---

## 8. System Impact

### 8.1 Frontend

```text
[前端影响，不涉及则写 Not involved]
```

### 8.2 Backend

```text
[后端影响]
```

### 8.3 Database / Storage

```text
[数据库、文件、对象存储影响]
```

### 8.4 Permission / Security

```text
[权限和安全影响]
```

### 8.5 Deployment / Config

```text
[部署、环境变量、配置影响]
```

### 8.6 Testing

```text
[测试影响]
```

---

## 9. Data Design

| Entity / Table | Field | Meaning | Notes |
|---|---|---|---|
| [实体] | [字段] | [含义] | [备注] |

### 9.1 State Machine

```text
[状态流转]
```

### 9.2 Data Lifecycle

```text
[创建、更新、归档、清理规则]
```

---

## 10. API / Interface Design

| Method | Path / Interface | Purpose | Auth | Notes |
|---|---|---|---|---|
| GET / POST | `/api/...` | [用途] | Required / Public | [备注] |

### 10.1 Request

```json
{}
```

### 10.2 Response

```json
{}
```

### 10.3 Error Cases

| Case | Expected Behavior |
|---|---|
| [错误场景] | [行为] |

---

## 11. Compatibility

| Area | Impact | Migration / Mitigation |
|---|---|---|
| Existing API | None / ... | ... |
| Existing Data | None / ... | ... |
| Existing UI | None / ... | ... |
| Existing Deployment | None / ... | ... |

---

## 12. Risks

| Risk | Severity | Mitigation |
|---|---|---|
| [风险] | Critical / Important / Optional | [缓解方式] |

---

## 13. Testing Plan

### 13.1 Automated Tests

- [测试 1]
- [测试 2]

### 13.2 Manual Verification

- [验证路径 1]
- [验证路径 2]

### 13.3 Regression Checks

- [回归检查]

---

## 14. Rollout / Rollback

### 14.1 Rollout Plan

```text
[上线或启用步骤]
```

### 14.2 Rollback Plan

```text
[回滚方式]
```

---

## 15. Open Questions

| Question | Owner | Blocking? |
|---|---|---|
| [问题] | [负责人] | Yes / No |

---

## 16. Next Steps

- [ ] 进入 Plan to Slices
- [ ] 生成执行 Prompt
- [ ] 创建 ADR
- [ ] 等待 HITL 决策
