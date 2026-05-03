# AI Agent Rules

本文件定义编程智能体在安装了 AI Engineering Delivery OS 的代码仓库中执行任务时必须遵守的规则。

编程智能体的目标不是展示能力，而是在最小必要范围内，稳定、可测试、可审计地完成任务。

---

## 1. Core Rule

在执行任何代码修改前，必须先确认：

1. 已阅读任务包。
2. 已理解 Goals。
3. 已理解 Non-goals。
4. 已理解需要检查的文件和模块。
5. 已理解禁止事项。
6. 已理解验收标准。
7. 已检查仓库中是否已有相关实现。

如果任务包不清晰，应先指出缺口，而不是猜测实现。

---

## 2. General Behavior Rules

### Always do

- 优先复用现有架构、模式、工具函数和组件。
- 修改前先定位真实代码路径。
- 只修改与任务直接相关的文件。
- 保持现有代码风格。
- 保持现有 API 风格。
- 保持现有错误处理风格。
- 保持现有权限模型。
- 每个关键改动后尽量保持项目可运行。
- 为新增或修改行为提供测试或清晰手动验证路径。
- 完成后输出完整修改摘要。

### Ask or report first

遇到以下情况，应先报告或请求确认：

- 任务目标和现有代码明显冲突。
- 需要改变数据库结构。
- 需要改变公开 API 返回结构。
- 需要引入新依赖。
- 需要重构核心模块。
- 需要删除旧功能。
- 需要改变权限模型。
- 需要处理不可逆数据迁移。
- 需要访问外部服务或敏感配置。

### Never do

- 不要在没有明确要求时进行大规模重构。
- 不要修改与任务无关的文件。
- 不要引入不必要的新依赖。
- 不要重复创建仓库中已有能力。
- 不要绕过现有 service / repository / permission 层。
- 不要只在前端做权限隐藏，后端必须校验。
- 不要把临时方案写死为长期架构。
- 不要因为未来规划提前实现完整系统。
- 不要改变现有 API 返回结构，除非任务明确要求。
- 不要删除现有功能，除非任务明确要求。
- 不要把大结果直接塞进接口响应。
- 不要长期占用服务器本地磁盘。
- 不要把 secret、token、key 写入代码或日志。

---

## 3. Repository Investigation Rules

执行前必须根据任务类型检查相关文件。

### 通用检查

优先检查：

```text
README / docs
package.json / requirements.txt / pyproject.toml / go.mod 等依赖文件
项目入口
路由 / API 层
业务 service 层
model / schema / migration
前端页面 / components
权限校验逻辑
测试文件
部署配置
```

### 如果任务涉及前端

必须检查：

- 路由结构。
- 页面目录。
- 组件复用方式。
- 状态管理方式。
- API 调用封装。
- 表单和错误提示模式。
- 现有 UI 风格。

### 如果任务涉及后端

必须检查：

- API 路由。
- controller / handler。
- service 层。
- repository / DAO 层。
- 错误处理。
- 鉴权中间件。
- 日志方式。
- 测试方式。

### 如果任务涉及数据库

必须检查：

- 现有 schema。
- migration 工具。
- model 定义。
- 索引策略。
- 历史数据兼容。
- 回滚风险。

### 如果任务涉及文件 / 对象存储

必须检查：

- 现有文件生成逻辑。
- 临时文件目录。
- 上传封装。
- 下载鉴权。
- 清理策略。
- 是否已有对象存储配置。

---

## 4. Scope Control Rules

### 4.1 Stay inside the task

只做任务包要求的事情。

如果发现旁边有问题：

- 不要顺手修。
- 记录为 Technical Debt。
- 在最终报告中说明。

### 4.2 Avoid large rewrites

除非任务明确要求，否则不要：

- 改目录结构。
- 改整体架构。
- 替换技术栈。
- 重写已有模块。
- 重命名大量文件。
- 把同步流程改成异步系统。
- 把局部功能抽象成大型框架。

### 4.3 Prefer incremental changes

复杂任务应拆成小步骤：

```text
定位现有实现
→ 添加最小模型或接口
→ 接入业务逻辑
→ 接入前端或调用方
→ 添加测试或验证路径
→ 更新文档
```

每一步都应尽量保持项目可运行。

---

## 5. Permission and Security Rules

权限和安全必须以后端为准。

### 5.1 Permission

- 所有受保护接口必须做后端鉴权。
- 用户只能访问自己有权访问的数据。
- 管理员能力必须显式校验。
- 下载、导出、详情查看接口必须检查资源归属。
- 不允许通过猜 ID、路径或 URL 访问他人数据。

### 5.2 Input validation

- 外部输入必须校验。
- 不可信输入不得直接拼 SQL、shell 命令、文件路径或 URL。
- 文件名、路径、用户 ID、任务 ID 等必须防止注入和越权。

### 5.3 Secrets

- 不要把 secret 写入代码。
- 不要把 secret 写入日志。
- 不要把 secret 放进前端包。
- 新增环境变量必须说明名称、用途和是否必需。

### 5.4 Logging

日志应帮助排查问题，但不要泄露：

- token
- 密码
- secret
- 完整个人敏感信息
- 大体量业务数据

---

## 6. Data Rules

- 数据库变更必须说明 migration。
- 不得破坏旧数据。
- 不得随意改变字段语义。
- 不得无说明删除字段。
- 新增状态字段时必须说明状态流转。
- 大结果不应直接塞进 API 响应。
- 分页、过滤、排序应遵循现有项目习惯。
- 失败状态应可追踪，不要吞异常。

---

## 7. File and Storage Rules

- 临时文件必须有清理策略。
- 大文件应放对象存储或项目既有存储层。
- 数据库优先保存 object key、元信息和摘要。
- 下载链接应经过权限校验。
- 避免长期占用服务器本地磁盘。
- 文件上传失败必须明确返回错误或记录失败状态。
- 对象存储上传成功后，应确认本地临时文件是否清理。

---

## 8. API Rules

- 新接口应遵循现有路由命名风格。
- 新接口应遵循现有响应格式。
- 新接口应遵循现有错误码或错误结构。
- 不要悄悄改变旧接口语义。
- 如果必须改变旧接口，应说明兼容性影响。
- 涉及列表接口时应考虑分页。
- 涉及下载接口时必须考虑鉴权。

---

## 9. Frontend Rules

- 复用现有页面布局和组件风格。
- 不要为了一个小功能引入大型 UI 框架。
- 空状态、加载状态、错误状态必须考虑。
- 权限差异不能只靠前端隐藏，后端仍需校验。
- 页面新增入口应遵循现有导航结构。
- 表单输入应有基本校验。
- API 错误应有用户可理解的反馈。

---

## 10. Testing Rules

完成后必须说明：

1. 运行了哪些自动测试。
2. 测试命令是什么。
3. 测试结果是什么。
4. 如何手动验证。
5. 哪些测试未能运行。
6. 未运行的原因。
7. 是否影响旧功能。

### 10.1 Normal path

验证正常业务路径。

### 10.2 Edge path

验证空数据、无权限、失败、超时、重复提交、大文件等边界情况。

### 10.3 Regression path

验证旧功能仍然正常。

### 10.4 Security path

验证用户无法访问未授权资源。

---

## 11. Documentation Rules

如果任务引入以下变化，应更新或建议更新文档：

- 新 API。
- 新环境变量。
- 新数据库表。
- 新状态机。
- 新对象存储路径。
- 新权限规则。
- 新部署步骤。
- 重要架构决策。
- 延期技术债。

不要把过程性聊天内容塞进长期项目记忆。

长期有效的信息才进入：

```text
.ai/project/AI_PROJECT_MEMORY.md
.ai/project/AI_DOMAIN_CONTEXT.md
.ai/decisions/
```

---

## 12. Final Response Format

编程智能体完成任务后，必须输出：

```markdown
# Implementation Summary

## 1. What changed

- ...

## 2. Modified files

- `path/to/file`: reason

## 3. Added files

- `path/to/file`: reason

## 4. Deleted files

- `path/to/file`: reason

## 5. Database / migration changes

- None / ...

## 6. Environment variable changes

- None / ...

## 7. Tests run

- Command: ...
- Result: ...

## 8. Manual verification

- ...

## 9. Known risks

- ...

## 10. Deferred technical debt

- ...

## 11. Suggested documentation updates

- ...
```

---

## 13. If Something Fails

如果实现中遇到问题，不要继续盲改。

请输出：

```markdown
# Blocked Report

## 1. Where I got blocked

...

## 2. What I confirmed

...

## 3. What I tried

...

## 4. Error messages / logs

...

## 5. Possible causes

...

## 6. Recommended next step

...
```

---

## 14. Final Principle

如果任务目标、现有代码、测试结果三者冲突，优先级如下：

```text
用户明确目标
→ 仓库真实代码
→ 项目既有规则
→ 测试和可验证证据
→ 模型推测
```

模型推测永远不能凌驾于代码事实和用户目标之上。
