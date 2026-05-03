# Testing Checklist

本清单用于审查新功能、Bug 修复、重构、API、权限、数据和前端交互是否有足够测试或验证证据。

目标：防止“看起来完成了”但没有可重复 pass/fail 信号。

---

## 1. When to Use

涉及以下情况时必须使用：

- 新增功能。
- Bug 修复。
- 数据库改动。
- API 改动。
- 权限改动。
- 文件上传 / 下载 / 导出。
- 前端关键交互。
- 重构。
- 审计 PR / diff。

---

## 2. Acceptance Criteria Mapping

- [ ] 每条验收标准是否有对应验证方式？
- [ ] 正常路径是否验证？
- [ ] 异常路径是否验证？
- [ ] 权限路径是否验证？
- [ ] 回归路径是否验证？

建议表格：

| Acceptance Criteria | Test / Verification | Status |
|---|---|---|
| [AC] | [测试或手动验证] | Covered / Missing |

---

## 3. Test Types

### Unit Tests

- [ ] 纯函数、工具、状态转换是否可单元测试？
- [ ] 是否避免测试实现细节？
- [ ] 是否覆盖边界输入？

### Integration Tests

- [ ] API + service + DB 是否需要集成测试？
- [ ] 权限和资源归属是否覆盖？
- [ ] 错误返回是否覆盖？

### E2E / UI Tests

- [ ] 用户关键路径是否需要 E2E？
- [ ] loading / empty / error 状态是否验证？
- [ ] 权限差异是否验证？

### Manual Verification

- [ ] 如果没有自动测试，是否提供明确手动步骤？
- [ ] 手动步骤是否可重复？
- [ ] 是否说明预期结果？

---

## 4. Bug Fix Regression

Bug 修复必须尽量回答：

- [ ] 之前如何失败？
- [ ] 现在如何证明不会再失败？
- [ ] 是否有 regression test？
- [ ] 如果没有，为什么？
- [ ] 是否记录缺失测试 seam？

---

## 5. Permission Testing

- [ ] 未登录用户访问受保护资源。
- [ ] 普通用户访问他人资源。
- [ ] 普通用户访问管理员功能。
- [ ] 管理员访问全局资源。
- [ ] 下载 / 导出接口资源归属。

---

## 6. Data Testing

- [ ] 空数据。
- [ ] 重复数据。
- [ ] 无效数据。
- [ ] 大数据量。
- [ ] 历史数据兼容。
- [ ] migration 前后行为。

---

## 7. API Testing

- [ ] 正常参数。
- [ ] 缺失参数。
- [ ] 无效参数。
- [ ] 无权限。
- [ ] 不存在资源。
- [ ] 分页边界。
- [ ] 错误格式一致。

---

## 8. File / Storage Testing

- [ ] 文件生成成功。
- [ ] 文件上传成功。
- [ ] 上传失败。
- [ ] 下载鉴权。
- [ ] 临时文件清理。
- [ ] 文件不存在。
- [ ] 大文件场景。

---

## 9. Test Evidence

审计时需要看到：

- [ ] 测试命令。
- [ ] 测试结果。
- [ ] 失败输出，如失败。
- [ ] 手动验证步骤。
- [ ] 未测试项说明。

不要接受只有“测试通过”但没有证据的汇报。

---

## 10. If Tests Cannot Run

必须说明：

```text
Why tests could not run:
What was verified instead:
Risk of not running tests:
Recommended follow-up:
```

---

## 11. Review Gate Questions

1. 是否每个关键验收都有验证？
2. 是否覆盖权限路径？
3. 是否覆盖异常路径？
4. 是否有 regression test？
5. 测试证据是否可信？
6. 未测试风险是否被明确接受？
