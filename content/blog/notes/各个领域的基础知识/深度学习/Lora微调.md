---
title: "Lora微调"
date: 2026-04-29
draft: false
---

## Lora-微调大模型

## 全量微调

​	针对全量 Fine-tune 的昂贵问题，目前主要有两种解决方案：

1. **Adapt Tuning**：即在模型中添加 Adapter 层，在微调时冻结原参数，仅更新 Adapter 层。

   ​	每个 Adapter 模块由两个前馈子层组成，第一个前馈子层将 [Transformer](https://zhida.zhihu.com/search?content_id=232618193&content_type=Article&match_order=1&q=Transformer&zhida_source=entity) 块的输出作为输入，将原始输入维度 d 投影到 m，通过控制 m 的大小来限制 Adapter 模块的参数量，通常情况下 m << d。在输出阶段，通过第二个前馈子层还原输入维度，将 m 重新投影到 d，作为 Adapter 模块的输出(如下图右侧结构)。

   ​	LoRA 事实上就是一种改进的 Adapt Tuning 方法。但 Adapt Tuning 方法存在推理延迟问题，由于增加了额外参数和额外计算量，导致微调之后的模型计算速度相较原预训练模型更慢。	

   <div style="text-align: center;">
       <img src="/myblog/article_images/image-20250224155649571-1740383813237-23-1740383814405-25-1740383816295-27.png" width="550" height="450" />
   </div>

   

2. **Prefix Tuning**：该种方法固定预训练 LM，为 LM 添加可训练，任务特定的前缀，这样就可以为不同任务保存不同的前缀，微调成本也小。具体而言，在每一个输入 token 前构造一段与下游任务相关的 virtual tokens 作为 prefix，在微调时只更新 prefix 部分的参数，而其他参数冻结不变。

   ​	目前常用的微量微调方法的 Ptuning，其实就是 Prefix Tuning 的一种改进。但 Prefix Tuning 也存在固定的缺陷：模型可用序列长度减少。由于加入了 virtual tokens，占用了可用序列长度，因此越高的微调质量，模型可用序列长度就越低。

​	

## Lora

![image-20250225105418611](/article_images/image-20250225105418611-1740452061604-29.png)