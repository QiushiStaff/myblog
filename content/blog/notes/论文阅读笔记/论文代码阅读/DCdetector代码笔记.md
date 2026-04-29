---
title: "DCdetector代码笔记"
date: 2026-04-29
draft: false
---

### MSL数据集

```
MSL_train.npy--(58317,55),55个特征。
MSL_test.npy--(73729,55),也是55个特征。
MSL_test_label.npy--(73729),test中对应的标签，false or true
```

​	win_size=90, 表示一个patch的大小为90。	

​	batch_size=10, 表示一个batch中有10个时间步长的数据。



---

### 模型结构

