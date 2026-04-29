---
title: "ONNX"
date: 2026-04-29
draft: false
---

## 开放神经网络交换（Open Neural Network Exchange, ONNX）

​	无论你使用何种训练框架训练模型（比如TensorFlow/Pytorch/OneFlow/Paddle），在训练完毕后你都可以将这些框架的模型统一转换为ONNX这种统一的格式进行存储。注意ONNX文件不仅仅存储了神经网络模型的权重，同时也存储了模型的结构信息以及网络中每一层的输入输出和一些其它的辅助信息。在获得ONNX模型之后，模型部署人员自然就可以将这个模型部署到兼容ONNX的运行环境中去。

​	**这里一般还会涉及到额外的模型转换工作，典型的比如在Android端利用NCNN部署ONNX格式模型，那么就需要将ONNX利用NCNN的转换工具转换到NCNN所支持的`bin`和`param`格式。**

​	