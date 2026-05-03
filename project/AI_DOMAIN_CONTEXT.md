# AI Domain Context

本文件记录当前项目的领域语言、业务概念、专有名词和命名约定。

它的目标是让人类、军师模型、编程智能体、审计智能体使用同一套语言理解项目，减少误解、重复解释和错误命名。

---

## 0. Maintenance Rules

### 0.1 What belongs here

本文件应记录长期有效的领域知识：

- 项目内部专有名词。
- 核心业务对象。
- 用户角色。
- 业务流程名称。
- 状态名称。
- 数据字段含义。
- 常见缩写。
- 约定俗成的命名方式。
- 容易混淆的概念差异。

### 0.2 What does not belong here

不要记录：

- 临时讨论。
- 单次任务过程。
- 已过期假设。
- 纯技术实现细节。
- 和项目无关的通用知识。

### 0.3 Update timing

以下情况应更新本文件：

- 新增重要业务概念。
- 重命名业务对象。
- 澄清容易混淆的术语。
- 用户明确纠正 AI 的理解。
- 重要功能上线后形成新领域语言。

---

## 1. Domain Summary

### 1.1 Project Domain

```text
[To Fill: 项目所在业务领域，例如跨境电商数据分析、内部运营系统、SaaS 后台、内容管理系统等]
```

### 1.2 Domain Goal

```text
[To Fill: 该项目在业务上最终帮助用户完成什么]
```

### 1.3 Core Domain Objects

| Object | Meaning | Related Code / Data |
|---|---|---|
| [To Fill] | [To Fill] | [path / table / API] |

---

## 2. Glossary

| Term | 中文名 | Definition | Use This Term When | Avoid / Do Not Confuse With |
|---|---|---|---|---|
| [To Fill] | [To Fill] | [To Fill] | [To Fill] | [To Fill] |

Example format:

| Term | 中文名 | Definition | Use This Term When | Avoid / Do Not Confuse With |
|---|---|---|---|---|
| Query Record | 查询记录 | 一次用户查询任务的元信息、状态、结果摘要和结果文件引用 | 描述用户查询历史、任务状态、下载入口 | 不等同于查询结果明细本体 |

---

## 3. User Roles

| Role | 中文名 | Meaning | Permissions | Notes |
|---|---|---|---|---|
| [To Fill] | [To Fill] | [To Fill] | [To Fill] | [To Fill] |

### 3.1 Role Distinctions

```text
[To Fill: 哪些角色容易混淆，它们的边界是什么]
```

---

## 4. Business Entities

### 4.1 Entity: [Name]

#### Meaning

```text
[To Fill]
```

#### Key Fields

| Field | Meaning | Notes |
|---|---|---|
| [To Fill] | [To Fill] | [To Fill] |

#### Lifecycle

```text
[To Fill: 创建 → 状态变化 → 完成/归档/删除]
```

#### Related Files / Tables / APIs

| Type | Path / Name | Notes |
|---|---|---|
| Table | [To Fill] | [To Fill] |
| API | [To Fill] | [To Fill] |
| File | [To Fill] | [To Fill] |

---

## 5. Business Flows and Names

| Flow Name | 中文名 | Meaning | Start Trigger | End State |
|---|---|---|---|---|
| [To Fill] | [To Fill] | [To Fill] | [To Fill] | [To Fill] |

### 5.1 Flow Details: [Name]

```text
[To Fill]
```

---

## 6. State Definitions

| Entity | State | Meaning | Can Transition To | Notes |
|---|---|---|---|---|
| [To Fill] | pending | [To Fill] | running / cancelled | [To Fill] |
| [To Fill] | running | [To Fill] | success / failed | [To Fill] |
| [To Fill] | success | [To Fill] | [To Fill] | [To Fill] |
| [To Fill] | failed | [To Fill] | [To Fill] | [To Fill] |

### 6.1 State Naming Rules

```text
[To Fill: 项目偏好使用 pending/running/success/failed，还是 queued/processing/done/error 等]
```

---

## 7. Data Terms

| Data Term | Meaning | Source | Notes |
|---|---|---|---|
| [To Fill] | [To Fill] | [To Fill] | [To Fill] |

### 7.1 Field Naming Conventions

```text
[To Fill: 例如 user_id / userId / owner_id / account_id 的使用边界]
```

### 7.2 Time and Date Conventions

```text
[To Fill: 时区、日期格式、周期定义、统计口径]
```

### 7.3 Currency / Unit / Measurement Conventions

```text
[To Fill]
```

---

## 8. Common Abbreviations

| Abbreviation | Full Name | Meaning | Notes |
|---|---|---|---|
| [To Fill] | [To Fill] | [To Fill] | [To Fill] |

---

## 9. Naming Conventions

### 9.1 User-facing Names

| Concept | Preferred User-facing Name | Avoid |
|---|---|---|
| [To Fill] | [To Fill] | [To Fill] |

### 9.2 Code Names

| Concept | Preferred Code Name | Avoid |
|---|---|---|
| [To Fill] | [To Fill] | [To Fill] |

### 9.3 API Names

| Concept | Preferred API Term | Avoid |
|---|---|---|
| [To Fill] | [To Fill] | [To Fill] |

---

## 10. Concepts That Are Easy to Confuse

| Concept A | Concept B | Difference | Example |
|---|---|---|---|
| [To Fill] | [To Fill] | [To Fill] | [To Fill] |

Example:

| Concept A | Concept B | Difference | Example |
|---|---|---|---|
| Query Record | Query Result | Query Record 是任务元信息；Query Result 是实际结果明细 | 记录表保存 result_file_key，而不保存全部结果行 |

---

## 11. Do-not-rename Terms

这些术语已经在业务、代码或文档中形成稳定含义，不应随意改名。

| Term | Reason | Related Files |
|---|---|---|
| [To Fill] | [To Fill] | [To Fill] |

---

## 12. Deprecated Terms

| Deprecated Term | Use Instead | Reason |
|---|---|---|
| [To Fill] | [To Fill] | [To Fill] |

---

## 13. AI Communication Guidance

### 13.1 Use these terms consistently

- [To Fill]

### 13.2 Avoid these vague words

| Vague Word | Better Replacement | Reason |
|---|---|---|
| data | [To Fill] | Too broad |
| task | [To Fill] | Clarify task type |
| result | [To Fill] | Clarify summary vs file vs rows |

### 13.3 When user says X, interpret as Y

| User Phrase | Interpret As | Notes |
|---|---|---|
| [To Fill] | [To Fill] | [To Fill] |

---

## 14. Open Questions

| Question | Why It Matters | Owner / Next Step |
|---|---|---|
| [To Fill] | [To Fill] | [To Fill] |

---

## 15. Last Updated

```text
Last Updated: YYYY-MM-DD
Updated By: [Human / AI]
Evidence Scope: [Full repo scan / partial / user-provided]
```
