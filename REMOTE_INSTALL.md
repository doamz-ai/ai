# REMOTE INSTALL

本文件说明如何通过 IDE 智能体从 GitHub 模板仓库远程安装 AI Engineering Delivery OS 到当前项目。

---

## 1. Core Idea

推荐安装方式不是手动下载再复制，而是：

```text
当前项目 IDE 智能体
→ 连接 AI Engineering Delivery OS GitHub 模板仓库
→ 读取模板文件
→ 复制到当前项目 `.ai/` 目录
→ 初始化成本项目专属 AI 工程交付系统
```

本质上，`doamz-ai/ai` 是远程模板源，当前项目的 `.ai/` 是本地运行副本。

---

## 2. Why Remote Template Install

相比手动下载，远程模板安装更适合多项目复用：

1. 不需要手动下载、解压、复制文件。
2. 可以让 IDE 智能体自动读取模板仓库。
3. 可以直接安装到当前项目根目录。
4. 安装后可以立即扫描当前项目并初始化 `project/` 上下文。
5. 后续升级时可以只同步通用系统层，避免覆盖项目本地记忆。

---

## 3. Important Principle

远程模板仓库只作为安装源，不建议作为每次运行时的实时依赖。

推荐模式：

```text
Remote template source: doamz-ai/ai
Local project runtime copy: current-project/.ai/
```

原因：

- 每个项目的 `project/`、`tasks/`、`decisions/`、`reviews/`、`changelog/` 都是本地专属。
- 模板仓库升级不应自动影响旧项目。
- 本地副本更稳定，便于 IDE 索引和 AI 读取。
- 私有仓库权限、网络、索引状态不应影响日常项目开发。

---

## 4. First-time Remote Install

首次安装到某个项目时，IDE 智能体应：

1. 连接模板仓库：`doamz-ai/ai`。
2. 读取模板仓库文件清单。
3. 在当前项目根目录创建 `.ai/`。
4. 将模板仓库内容复制到 `.ai/`。
5. 不修改当前项目业务代码。
6. 读取 `.ai/START_HERE.md`。
7. 扫描当前项目代码。
8. 初始化或补全：
   - `.ai/project/AI_REPO_CONTEXT.md`
   - `.ai/project/AI_DOMAIN_CONTEXT.md`
   - `.ai/project/AI_CONTEXT_MAP.md`
   - `.ai/project/AI_PROJECT_MEMORY.md`
9. 输出安装报告。

---

## 5. Upgrade Existing Installation

如果当前项目已经存在 `.ai/`，不要直接全量覆盖。

### 5.1 Safe to Update

通常可以从模板仓库同步这些通用系统层：

```text
README.md
START_HERE.md
VERSION.md
INSTALL.md
REMOTE_INSTALL.md
MANIFEST.md
SELF_CHECK.md
CHANGELOG.md
manifest.json

system/
skills/
templates/
references/
prompts/
scripts/
```

### 5.2 Do Not Auto-overwrite

以下是项目本地专属层，不应直接覆盖：

```text
project/
tasks/
decisions/
reviews/
changelog/
```

如果确实要更新这些文件，应先生成差异报告，并等待人类确认。

---

## 6. Recommended IDE Agent Behavior

IDE 智能体安装时必须遵守：

- 不修改业务代码。
- 不删除已有 `.ai/project/` 内容。
- 不覆盖已有任务记录。
- 不覆盖已有 ADR。
- 不覆盖已有 Review 报告。
- 不覆盖已有 Changelog。
- 如遇同名文件，先报告差异。
- 安装完成后运行结构自检，如可用：

```bash
python .ai/scripts/validate-structure.py .ai
```

---

## 7. Recommended Prompt

推荐直接使用：

```text
prompts/install-from-github.md
```

将其中内容复制给支持 GitHub 访问和本地文件写入的 IDE 智能体。

---

## 8. Install Report Format

安装完成后，IDE 智能体应输出：

```markdown
# AI Engineering Delivery OS Install Report

## Source

- Template repo: doamz-ai/ai
- Branch / ref: master / [commit]

## Target

- Project path: [current project]
- Install path: .ai/

## Files Created

- ...

## Files Skipped

- ...

## Existing Files Preserved

- ...

## Project Context Initialization

- AI_REPO_CONTEXT.md: Created / Updated / Skipped
- AI_DOMAIN_CONTEXT.md: Created / Updated / Skipped
- AI_CONTEXT_MAP.md: Created / Updated / Skipped
- AI_PROJECT_MEMORY.md: Created / Updated / Skipped

## Validation

- Structure validation: PASS / FAIL / Not run

## To Verify

- ...

## Next Step

- ...
```

---

## 9. Final Rule

远程安装的目标不是让每个项目依赖模板仓库，而是：

```text
从模板仓库复制一套 AI 工程交付操作系统，安装成本项目自己的 `.ai/` 协作层。
```
