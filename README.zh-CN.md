# Meeting Actions · 会议行动项

[English](README.md) | 简体中文

会议结束后，先核对行动项有没有原文依据。每项任务保留引用、行号、负责人和截止日期，再看哪些还需要补问，避免把含糊讨论写成确定承诺。

[下载 v0.2.1](https://github.com/KarmenLoop/skill-meeting-actions/releases/tag/v0.2.1) · [完整教程](docs/tutorial.zh-CN.md) · [输入参考](docs/input.zh-CN.md) · [反馈问题](https://github.com/KarmenLoop/skill-meeting-actions/issues)

## 能做什么

Alex 的草稿任务已完整；预算审阅虽然有原文依据，但缺少负责人和截止日期，仍未就绪。

候选行动项由你或 AI 提供；工具核对依据和完整性，不转写音频，也不补造缺失承诺。

![会议行动项 0.2.1 版本样例的真实 JSON 输出](docs/images/example-output-v0.2.1.svg)

*图片来自 v0.2.1 的真实本地输出，采用英文键名；[完整结果](examples/expected.json) · [图片来源记录](docs/images/provenance.json)。*

## 开始使用

在发行页下载 `karmen-meeting-actions-v0.2.1.zip` 与对应 `.sha256` 文件，核对哈希后解压。在解压目录中使用 Python 3.9 或更新版本：

```sh
python3 scripts/run.py --version
python3 scripts/run.py --input examples/input.json
```

预期版本：`karmen-meeting-actions 0.2.1`。Alex 的草稿任务已完整；预算审阅虽然有原文依据，但缺少负责人和截止日期，仍未就绪。

如果宿主读取 `~/.agents/skills`，可安装完整技能：

```sh
python3 install.py --host agents
```

目标目录已存在时安装器会拒绝覆盖。宿主发现和调用方式可能不同，见[安装与实践教程](docs/tutorial.zh-CN.md)。不使用 AI 宿主也能直接运行本地工具。

## 用于自己的任务

行号从 1 开始。quote 应与 line_start..line_end 内原文吻合；负责人或日期未知时用 null，不要猜测。

把引用故意放到错误行号，查看 evidence_verified，再恢复正确引用并补入已确认信息。ready_count 只统计完整且依据通过核对的事项。

准备新输入前可查看[字段约定](docs/input.zh-CN.md)。工具只依赖 Python 标准库，本身不需要模型账号、API 密钥或网络。使用 AI 宿主时，宿主有自己的数据与权限设置。

## 常见问题

**可以直接把录音变成纪要吗？** 需要先提供文字稿和候选行动项；本包不处理录音转写或会议参会。

**结果保存在哪里？** 默认向终端输出 JSON；使用 `--output` 时只创建新文件，已有输出文件会保留。工具只读取提交的记录和输入约定中明确列出的本地路径。

## 文档与支持

- [下载、安装、配置、练习、升级与卸载](docs/tutorial.zh-CN.md)
- [输入输出约定](docs/input.zh-CN.md)与[兼容性说明](docs/COMPATIBILITY.md)（英文参考）
- [更新记录](CHANGELOG.md)、[参与贡献](CONTRIBUTING.md)、[支持](SUPPORT.md)和[安全反馈](SECURITY.md)

## 许可证

[MIT](LICENSE)。再分发时保留许可证和[声明](NOTICE.md)。由 [KarmenLoop](https://karmenloop.com) 维护。
