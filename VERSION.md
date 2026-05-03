# VERSION

## Current Version

```text
AI Engineering Delivery OS v0.1.0
```

状态：Draft / MVP  
维护者：doamz-ai  
默认安装目录：`.ai/`

---

## Version Meaning

本项目建议使用语义化版本：

```text
MAJOR.MINOR.PATCH
```

### MAJOR

当系统结构、核心协议、目录布局或工作流发生破坏性变化时升级。

示例：

- `.ai/` 目录结构重构。
- 核心角色模型重构。
- skills 触发机制重构。
- 任务生命周期发生不兼容变化。

### MINOR

当新增能力但保持向后兼容时升级。

示例：

- 新增 skill。
- 新增 template。
- 新增 reference checklist。
- 新增 operating mode。
- 增强已有文档结构但不破坏旧版本。

### PATCH

当修正措辞、补充示例、优化模板或修复小问题时升级。

示例：

- 修正文档错误。
- 优化 Prompt 表述。
- 补充示例。
- 调整 checklist 项目。

---

## Release History

### v0.1.0

日期：2026-05-03

初始 MVP 版本。

目标：建立一个可复制到任意代码仓库的 AI 工程交付操作系统基础协议。

包含规划中的核心模块：

```text
.ai/
├── README.md
├── START_HERE.md
├── VERSION.md
├── system/
├── project/
├── skills/
├── templates/
├── references/
├── tasks/
├── decisions/
├── reviews/
└── changelog/
```

核心理念：

```text
Context before code.
Clarify before build.
Plan before execute.
Verify before trust.
Review before ship.
Memory after delivery.
```

---

## Upgrade Policy

当把本系统复制到多个项目后，建议每个项目保留自己的 `.ai/VERSION.md`。

升级时注意区分：

```text
通用系统层：system/ skills/ templates/ references/
项目适配层：project/ tasks/ decisions/ reviews/ changelog/
```

升级通用系统层时，不应覆盖项目适配层的本地记忆。

---

## Compatibility Notes

v0.1.0 仍处于 Draft / MVP 阶段。

预期后续会继续优化：

1. skills 目录下的具体 SKILL.md。
2. templates 标准交付物模板。
3. references 检查清单。
4. project 初始化模板。
5. 多智能体协作细则。
6. GitHub PR / Review 工作流。

---

## Recommended Version Header For Installed Projects

当本系统安装到具体项目时，建议在项目的 `.ai/VERSION.md` 中保留：

```text
Installed AI Engineering Delivery OS Version: v0.1.0
Project Local AI Context Version: v0.1.0-project-draft
Last AI Context Refresh: YYYY-MM-DD
```

