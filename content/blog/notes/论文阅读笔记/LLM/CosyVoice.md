---
title: "CosyVoice"
date: 2026-04-29
draft: false
---

## CosyVoice(arxiv, Alibaba, 2024.12, https://github.com/FunAudioLLM/CosyVoice.git)

摘要：

​	当前：语音tokens$\xrightarrow{无监督}$ 语音。一个简单的重建任务可能无法学习到语音中的语音信息。

​	多语言语音识别模型，模型的encoder被插入一个Vector Quantization$\xrightarrow{获得}$ 自监督语音tokens (supervised semantic tokens) $\xrightarrow{表示}$ 语音

​	基于自监督语音tokens $\xrightarrow{构建}$  Codec-based synthesizer，包括文本到tokens的LLM和一个用于tokens到语音合成的条件流匹配模型。



---

Introduciton：

​	作者提到无监督学习的方法没有办法拿到包含语义信息的speech tokens。所以文章用的是Whisper的Encoder + Vector Quantization $\xrightarrow{获得}$ speech tokens。Whisper是一个多语言语音识别模型，通过一个自回归的任务训练得到，因此可以得到包含语义信息的speech tokens。后面还说明了为什么要用Vector Quantization。

​	Speech tokens $\xrightarrow{构建}$  CosyVoice一个可扩展且高效的zero-shot TTS 生成器。包括文本到tokens的LLM和一个把tokens合成为语音的条件流匹配模型。条件流匹配模型==denoising diffusion probabilistic models (DDPM)，目前不太清楚这里是怎么做的？？

​	



---





### Optimal-transport Conditional Flow Matching

​	speech tokens转换为Mel频谱图。

​	optimal-transport conditional flow matching model (OT-CFM)这个方法是怎么做到的。文中提到相较于条件扩散模型 (diffusion probabilistic models , DPMs)，OT-CFM梯度更简单、训练更轻松、生成速度更快。
