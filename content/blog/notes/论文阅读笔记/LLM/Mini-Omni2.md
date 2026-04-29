---
title: "Mini-Omni2"
date: 2026-04-29
draft: false
---

**Mini-Omni2: Towards Open-source GPT-4o with Vision, Speech and Duplex Capabilities (2024，arxiv，清华)---实现STS的实时语音对话模型**

![模型架构](../../article_images/image-20250206202602544-1738844766795-1.png)

### 核心

1. **音频编码器（Audio Encoder）：Whisper-small**
2. **视觉编码器（Vision Encoder）+视觉适配器（Vision Adapter）：CLIP+single-layer LlamaMLP**
3. **基础语言模型（LLM）：Qwen2-0.5B**
4. **实时双工交互（Duplex Interaction）**--- 打断机制
5. **延迟并行解码（Parallel Decoding）**
6. 通过 **TTS（SNAC 语音合成）** 生成高质量语音。-- 接收LLM输出的语音token和文本token







### 流程

1. 语音输入：Mini-Omni2 采用 OpenAI 的 Whisper-small 作为语音编码器，将音频转换为特征表示。

2. 语音理解：

   1. 语音输入（Whisper 处理后）和文本输入（文本 Token）拼接，统一转换为 LLM 可处理的格式。
   2. 采用 **三阶段训练策略**（见后文），确保多模态数据能被有效对齐。

3. 语音输出：

   1. 同时生成文本 Token 和语音 Token，并通过 TTS（Text-to-Speech）转换为语音输出。
   2. **SNAC 语音编码器** 生成高质量的语音输出，确保语音流畅度。

   

#### 三阶段训练策略：

(1) 第一阶段：多模态编码器适配 (Multimodal Encoder Adaptation)目标：让 LLM 适应 **文本任务**，确保它能正常进行 **文本问答** 和 **推理**。

(2) 第二阶段：模态对齐 (Modality Alignment)：**让 LLM 能够处理语音和图片输入，但仍然只生成文本输出**。

- 让 LLM **适应语音和视觉输入**，确保它能理解 **语音和图片信息**，并用文本回答。
- 训练 LLM **能够处理多种模态输入，并输出文本**。
- 输入：语音+图片。输出：文本

(3) 第三阶段：多模态输出训练（端到端 STS）

- 目标：让 LLM **同时生成文本和语音**（即 STS: Speech-to-Speech）。**训练双工交互能力**（支持用户实时打断 AI 说话）。
- 数据：
  - **语音问答数据（VoiceAssistant-400K）** → 训练 LLM **如何用语音回答问题**。
  - **语音任务数据（LibriTTS, VCTK, MLS）** → 训练 **TTS（Text-to-Speech）能力**。
- 关键：LLM输出文本+语音token。

|      **阶段**       |        **输入数据**         |  **输出数据**   |           **任务目标**           |
| :-----------------: | :-------------------------: | :-------------: | :------------------------------: |
| **训练 - 第一阶段** | 文本数据（Open-Orca, Moss） |     仅文本      |      训练 LLM 文本推理能力       |
| **训练 - 第二阶段** |     语音 / 图片 + 文本      |     仅文本      |      让 LLM 学会跨模态理解       |
| **训练 - 第三阶段** | 语音数据（LibriTTS, VCTK）  | **文本 + 语音** |       让 LLM 生成语音输出        |
|    **测试阶段**     |          语音输入           | **文本 + 语音** | 评估 STS（Speech-to-Speech）能力 |