# AI 视频工厂（AI Video Factory）

一套由 Codex 调度、以人工确认为质量门槛的 AI 口播视频工作流。

第一阶段只有一个目标：做出一条约 2 分钟、人物稳定、声音自然、包装风格统一的可审片样片。不做无人审核和自动发布。

## 仓库导读

| 你想看什么 | 打开哪里 |
| --- | --- |
| 首条视频说什么 | [`projects/pilot-001/script.md`](projects/pilot-001/script.md) |
| 每一段用什么画面 | [`projects/pilot-001/strategy.md`](projects/pilot-001/strategy.md) |
| 哪些步骤必须人工确认 | [`docs/pilot-plan.zh.md`](docs/pilot-plan.zh.md) |
| Codex 必须遵守的制作规则 | [`AGENTS.md`](AGENTS.md) |
| 配置文件的中文解释 | [`config/配置说明.md`](config/%E9%85%8D%E7%BD%AE%E8%AF%B4%E6%98%8E.md) |
| 如何运行工具 | [`scripts/使用说明.md`](scripts/%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E.md) |

`templates/hyperframes/tech-editorial/` 里的 `AGENTS.md` 和 `CLAUDE.md` 是 HyperFrames 自动生成的框架内部指令，普通用户无需阅读，也不建议手工翻译。

## 试制顺序

1. 用 3–5 张真实照片锁定身份，生成 2–4 张 16:9 场景候选图。
2. 人工选定唯一的人物场景母图。
3. 生成 10–15 秒声音与嘴型测试。
4. 通过后再生成约 2 分钟的数字人片段。
5. Codex 按脚本生成视觉方案，HyperFrames 生成字幕、信息卡和图表。
6. FFmpeg 合成预览，抽帧和试听后人工确认成片。

## 开始前

```bash
python3 scripts/check_env.py
python3 scripts/estimate_cost.py --duration 120 --avatar-seconds 35 --engine photo
```

详细验收标准见 [docs/pilot-plan.zh.md](docs/pilot-plan.zh.md)，Codex 执行约束见 [AGENTS.md](AGENTS.md)。

## 目录是干什么的

```text
config/       视频尺寸、颜色、字体、字幕等公共配置
docs/         需求、验收标准和制作说明
projects/     每条视频的文案、需求和剪辑方案
scripts/      环境检查、费用估算、新建项目和成片质检工具
templates/    可重复使用的字幕、信息卡和动效模板
```

## 安全

人脸照片、声音语料、API Key、中间片和成片默认只保存在本地，不进入 Git。不要将真实密钥填入 `.env.example`。
