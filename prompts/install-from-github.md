# Prompt: Install From GitHub

用途：在任意当前项目中，让 IDE 智能体从 GitHub 模板仓库 `doamz-ai/ai` 远程安装 AI Engineering Delivery OS 到当前项目本地 `.ai/` 目录。

开源仓库 URL：

```text
https://github.com/doamz-ai/ai
```

---

```markdown
请从 GitHub 开源仓库安装 AI Engineering Delivery OS 到当前项目。

仓库名称：`doamz-ai/ai`
仓库 URL：`https://github.com/doamz-ai/ai`
默认分支：`master`

请严格按以下要求执行。

## 1. Source

模板仓库：`doamz-ai/ai`
模板仓库 URL：`https://github.com/doamz-ai/ai`
默认分支：`master`

请先读取模板仓库中的：

- `README.md`
- `THREE_MINUTE_QUICK_START.md`
- `START_HERE.md`
- `REMOTE_INSTALL.md`
- `MANIFEST.md`
- `manifest.json`

## 2. Target

目标安装路径：当前项目根目录下的 `.ai/`

请注意：这是把远程模板仓库复制成本项目的本地 `.ai/` 运行副本，而不是让当前项目长期依赖远程仓库。

## 3. First-time Install Rules

如果当前项目不存在 `.ai/`：

1. 创建 `.ai/` 目录。
2. 从 `https://github.com/doamz-ai/ai` 读取并复制模板内容到 `.ai/`。
3. 不要修改当前项目业务代码。
4. 安装完成后读取 `.ai/START_HERE.md`。
5. 扫描当前项目代码，生成或补全：
   - `.ai/project/AI_REPO_CONTEXT.md`
   - `.ai/project/AI_DOMAIN_CONTEXT.md`
   - `.ai/project/AI_CONTEXT_MAP.md`
   - `.ai/project/AI_PROJECT_MEMORY.md`
6. 所有项目上下文必须基于真实代码、README、配置文件和目录结构。
7. 不确定内容必须标注为 `[Unknown]` 或 `[To Verify]`。
8. 不要脑补不存在的架构。

## 4. Existing Install Rules

如果当前项目已经存在 `.ai/`：

### 可以同步的通用系统层

可以从模板仓库更新：

- `README.md`
- `THREE_MINUTE_QUICK_START.md`
- `START_HERE.md`
- `VERSION.md`
- `INSTALL.md`
- `REMOTE_INSTALL.md`
- `MANIFEST.md`
- `SELF_CHECK.md`
- `CHANGELOG.md`
- `manifest.json`
- `system/`
- `skills/`
- `templates/`
- `references/`
- `prompts/`
- `scripts/`

### 不要自动覆盖的项目本地层

不要直接覆盖：

- `project/`
- `tasks/`
- `decisions/`
- `reviews/`
- `changelog/`

如果这些目录已经存在，请保留本地内容。若模板仓库有同名文件，请先生成差异报告，等待人类确认。

## 5. Validation

安装完成后，如果 Python 可用，请运行：

```bash
python .ai/scripts/validate-structure.py .ai
```

如果无法运行，请说明原因，并手动检查 `manifest.json` 中的 required_files 是否都存在。

## 6. Output Required

完成后请输出安装报告：

```markdown
# AI Engineering Delivery OS Install Report

## Source

- Template repo: doamz-ai/ai
- Template URL: https://github.com/doamz-ai/ai
- Branch / ref: master / [commit if known]

## Target

- Project path: [current project]
- Install path: .ai/

## Files Created

- ...

## Files Updated

- ...

## Files Skipped

- ...

## Existing Project-local Files Preserved

- ...

## Project Context Initialization

- AI_REPO_CONTEXT.md: Created / Updated / Skipped
- AI_DOMAIN_CONTEXT.md: Created / Updated / Skipped
- AI_CONTEXT_MAP.md: Created / Updated / Skipped
- AI_PROJECT_MEMORY.md: Created / Updated / Skipped

## Validation

- Structure validation: PASS / FAIL / Not run

## Unknowns / To Verify

- ...

## Next Step

- ...
```

## 7. Absolute Prohibitions

- 不要修改业务代码。
- 不要删除当前项目已有 `.ai/project/` 内容。
- 不要删除当前项目已有任务记录。
- 不要覆盖已有 ADR。
- 不要覆盖已有 review 报告。
- 不要把模板仓库作为运行时依赖。
- 不要在未确认差异时强行覆盖本地专属记忆。
```
