# AI Video Factory

一套由 Codex 调度、以人工确认为质量门槛的 AI 口播视频工作流。

第一阶段只有一个目标：做出一条约 2 分钟、人物稳定、声音自然、包装风格统一的可审片样片。不做无人审核和自动发布。

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

详细验收标准见 [docs/pilot-plan.md](docs/pilot-plan.md)，Codex 执行约束见 [AGENTS.md](AGENTS.md)。

## 安全

人脸照片、声音语料、API Key、中间片和成片默认只保存在本地，不进入 Git。不要将真实密钥填入 `.env.example`。
