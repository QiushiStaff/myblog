---
title: "DCdetector_ Dual Attention Contrastive Representation Learning for Time Series Anomaly Detection"
date: 2026-04-29
draft: false
---

# DCdetector：用于时间序列异常检测的双重注意对比表征学习（2023，KDD，SCI一区，有代码）

![框架图](..\./article_images/1736487673881-9e5fe903-b6c7-4aac-bb3b-868ea0c3a118.png)

**背景:** 时间序列异常检测在工业监测、金融欺诈检测、故障诊断等多个领域具有重要意义。随着传感器技术发展，大量时间序列数据被收集，及时发现异常对保障安全和避免经济损失极为重要。



**挑战：**

1. 什么是**异常难以定义**。因此有标签的数据很难拿到。所以，大多数有监督和半监督的方法就不适用。
2. 异常检测模型应考虑时间序列数据的时间、多维和非平稳特征 [78]。多维性描述了多元时间序列中维度之间通常存在依赖关系，非平稳性意味着时间序列的统计特征不稳定。具体来说，时间依赖性意味着相邻点彼此之间存在潜在的依赖性。尽管每个点都应该标记为正常或异常，**但将单个点视为样本是不合理的。**



**之前方法的问题：**

1. 大多数的有监督和半监督方法不能处理标签数据少的问题，难以识别之前从没出现过的异常。

2. 基于重建的模型通过正常数据构建一个模型，因此这个模型不能重建的数据就是异常数据。在时间序列异常检测领域，由于异常数量的不确定，正常点和异常点可能出现在一个实例中，导致很难学习到一个干净、重建效果好的模型针对正常数据。（我的理解是，因为数据集中缺少对数据的评估，导致数据中可能存在异常数据，因此，难以构建重建效果好的模型）。

3. 重建难以完全考虑潜在的模式信息。

   

**创新点：**

​	构建了一种多尺度双重注意力对比表示学习模型，文章认为正常时间序列点**共享潜在模式**，这意味着正常点与其他点具有很强的相关性，异常则不然（即与其他异常相关性较弱）。因为数据集中，异常数据点很少，因此我们学习到的重建模型处理异常数据时，异常数据的重建结果会很独特。从不同的角度学习异常的一致表示会很困难，但对于正常点来说很容易，所以没有通过构建正负对的方式，而是通过构造<font style="color:rgb(25, 27, 31);">Contrastive Learning的两个Positive Input也就是Patch-wise View和Point-wise View，然后将这两个View作为输入，用Contrastive Loss来训练，最后用阈值来识别Anomaly。</font>

​	<font style="color:#DF2A3F;">对于正常点，即使在不同的视图中，它们中的大多数也会共享相同的潜在模式（强相关性不容易被破坏）。然而，由于异常很少见并且没有明确的模式，因此它们很难与正常点或它们之间共享潜在模式（即异常与其他点的相关性较弱）。因此，**不同视图中正常点表示的差异很小，而异常点的差异很大。**</font>

​	DCdetector不需要先验知识的输入，去识别正常|异常数据，因此，它可以识别从未出现过的异常。

``` 
？？？文章中提到损失函数只是对比损失，没有重建损失,因此，减少了异常事件的干扰。

answer：重构函数可以帮助我们检测异常，但是构建一个编码器和解码器并不容易，因为数据集中会存在异常。
```

> ​	**异常分数的计算，我们根据两种表现形式的差异计算异常分数，并使用先验阈值进行异常判断。**





### **Method**

#### 	**Forward Process：**

多变量的时间序列数据被实例归一化==>它可以看作是全局信息的整合和调整，以及一种更稳定的训练处理方法。(为什么要做这一步的原因).



#### 	**Dual Attention Contrastive Structure：**

两个视图：patch-wise | in-patch representations作为两个view。

本文的对比方法和正负对的方法不一样，和只使用正对的对比学习方法相似。

分块：P是patch的大小，N是patch的数量。

​		$X \in R^{T \times d} \rightarrow X \in R^{P \times N \times d}$ , $N \times d$ 这个矩阵包含，不同patch中同一位置的数据。

##### 		1、patch-wise representations：块间的依赖关系通过多头注意力机制建模。

​			1. Embedded operation：

​			$X \in R^{P \times N \times d} \xrightarrow{embeded\ operation} X_N \in R^{N \times d_{model}}$

​	想当与把一个patch中多个时间步数据，合并为一个数据，然后一个patch就变成一个整体数据。相当与块内数据合并。$X_N$就是用一个$1 \times d_{model}$向量表示一个patch。

​			2. Calculate the patch-wise representation with multi-head attention weights：

​			$X_N \in R^{N \times d_{model}} \xrightarrow{multi-head\ attention} Attn_N $

​	这个位置就想当与把每个patch的向量表示和其他patch的向量表示进行注意力机制，获得更多信息的数据表示。向量维度可能会发生变化。

##### 		2、In-patch representations：块内的依赖关系也通过多头注意力机制建模。

​	Embedded operation and calculate the in-patch representation： 

​			$X \in R^{P \times N \times d} \xrightarrow{embeded\ operation} X_P \in R^{P \times d_{model}} \xrightarrow{multi-head attention} Attn_P$		

​	相当与把不同patch中相同时间戳的内容合变成了一个patch。块内的表示每一行就是表示一个时间戳的向量表示。

> 注：1和2中注意力机制的参数是一样的。
>
> 注：我觉的文章中关于注意力机制的参数表示是有问题的。



#### 	Up-sampling and Multi-scale Design：

![上采样的示例](../../article_images/image-20250208165813167-1739005098085-3.png)

##### 		1、块间的上采样

​	貌似是把$P^i$拆分为数据点。$N = Upsampling(Attn_N)$。

> ​	这个位置不是很确定。

##### 		2、块内表示的上采样

​	把每个数据点$p_i$重复放入每个patch中。$P = Upsampling(Attn_P)$。



#### 	Representation Discrepancy

​	下面的话，可以好好理解理解。

> ​	Patch-wise and in-patch branches output representations of the same input time series in two different views. As shown in Figure 2 (c), patch-wise sample representation learns a weighted combination between sample points in the same position from each patch. In-patch sample representation, on the other hand, learns a weighted combination between points within the same patch.

​	基于双重注意力对比模块，我们获得同一个多变量时间序列的两个view。我们通过KL散度计算计算两个view的相似度。直觉是，由于异常很少见，并且正常点共享潜在模式，因此相同输入的表示应该是相似的。

​	损失函数：

​		$L_{\mathcal{P}}\{\mathcal{P}, N; X\} = \sum KL(\mathcal{P}, \text{Stopgrad}(N)) + KL(\text{Stopgrad}(N), \mathcal{P})$	

​		$L_{\mathcal{N}}\{\mathcal{P}, N; X\} = \sum KL(\mathcal{N}, \text{Stopgrad}(P)) + KL(\text{Stopgrad}(P), \mathcal{N})$

​						$L=\frac{{L_\mathcal{N}-L_\mathcal{P}}}{len(N)}$

​	Stopgrad，是指Stop-gradient operation。我们在训练时是异步更新两个branch。	

​	**总结：毫无疑问，重建有助于检测行为与预期不符的异常。然而，构建一个合适的编码器和解码器来“重建”时间序列并不容易，因为它们预计会受到异常的干扰。此外，由于没有完全考虑潜在模式信息，表示能力受到限制。**



#### 	异常分数计算

​		$AnomalyScore(X) = \sum KL(\mathcal{P}, \text{Stopgrad}(N)) + KL(\mathcal{N},\text{Stopgrad}(P))$	

​	<span style="color: red;">代码部分的参数更新思路如下，对于这样交替更新的思路不是很能理解。为什么一次反向传播，能实现两个分支的交替更新。</span>

```
# series_loss 计算部分
series_loss += (
    my_kl_loss(series[u], prior_norm.detach()) +  # 阻断 prior 分支梯度
    my_kl_loss(prior_norm.detach(), series[u])     # 同上
)

# prior_loss 计算部分
prior_loss += (
    my_kl_loss(prior_norm, series[u].detach()) +  # 阻断 series 分支梯度
    my_kl_loss(series[u].detach(), prior_norm)    # 同上
)

loss = prior_loss - series_loss  

loss.backward()

self.optimizer.step()
```





##### 	Discussion about Model Collapse

​	模型崩塌：指的是在自监督学习（Self-Supervised Learning）或无监督表示学习（Unsupervised Representation Learning）中，模型学到了一种**退化的、无信息量的表示**，导致所有输入样本的嵌入（embedding）变得相似或趋于相同。这样，模型无法有效地区分不同的输入数据，学习到的特征就失去了区分度。	

​	对比学习的输出向量Z，分解为中心向量o和残差向量r。中心向量理解为一个特征空间中，所有特征点的中心点的值。o决定输出向量，而r决定Z偏差中心点多少。

​									$Z=o+r$,

​	特征空间有特征挖掘算法决定也就是模型结构。而残差向量r是由输入数据决定。由于我们的模型是非对称结构所以我们可以避免模式崩塌的问题。

如果说两个分支是对称的（也就是结构、参数都相同），就会导致中心向量完全一致，毕竟是一个特征空间，而残差向量是由输入决定





**Channel Independence的作用以及操作？**

减少参数数量和过拟合问题， 简化 attention network。

```c
假设输入数据的形状为 (batch_size, window_size, channels)，例如 (1, 12, 3)，数据如下：
[
    # Batch 1
    [
        [1.1, 1.2, 1.3],  # 时间步 1
        [2.1, 2.2, 2.3],  # 时间步 2
        [3.1, 3.2, 3.3],  # 时间步 3
        [4.1, 4.2, 4.3],  # 时间步 4
        [5.1, 5.2, 5.3],  # 时间步 5
        [6.1, 6.2, 6.3],  # 时间步 6
        [7.1, 7.2, 7.3],  # 时间步 7
        [8.1, 8.2, 8.3],  # 时间步 8
        [9.1, 9.2, 9.3],  # 时间步 9
        [10.1, 10.2, 10.3],  # 时间步 10
        [11.1, 11.2, 11.3],  # 时间步 11
        [12.1, 12.2, 12.3]   # 时间步 12
    ]
]
重排操作
x_patch_size = rearrange(x_patch_size, 'b l m -> b m l')
x_patch_num = rearrange(x_patch_num, 'b l m -> b m l')
重排后的形状为 (1, 3, 12)，数据如下：
[
    # Batch 1
    [
        [1.1, 2.1, 3.1, 4.1, 5.1, 6.1, 7.1, 8.1, 9.1, 10.1, 11.1, 12.1],  # 通道 1
        [1.2, 2.2, 3.2, 4.2, 5.2, 6.2, 7.2, 8.2, 9.2, 10.2, 11.2, 12.2],  # 通道 2
        [1.3, 2.3, 3.3, 4.3, 5.3, 6.3, 7.3, 8.3, 9.3, 10.3, 11.3, 12.3]   # 通道 3
    ]
]
# 假设 patch_size = 3
x_patch_size = rearrange(x_patch_size, 'b m (n p) -> (b m) n p', p=patch_size)
x_patch_num = rearrange(x_patch_num, 'b m (p n) -> (b m) p n', p=patch_size)
x_patch_size 的形状为 (3, 4, 3)，数据如下：
[
    # 通道 1
    [[1.1, 2.1, 3.1], [4.1, 5.1, 6.1], [7.1, 8.1, 9.1], [10.1, 11.1, 12.1]],

    # 通道 2
    [[1.2, 2.2, 3.2], [4.2, 5.2, 6.2], [7.2, 8.2, 9.2], [10.2, 11.2, 12.2]],

    # 通道 3
    [[1.3, 2.3, 3.3], [4.3, 5.3, 6.3], [7.3, 8.3, 9.3], [10.3, 11.3, 12.3]]
]
x_patch_num 的形状为 (3, 3, 4)，数据如下：
[
    # 通道 1
    [[1.1, 4.1, 7.1, 10.1], [2.1, 5.1, 8.1, 11.1], [3.1, 6.1, 9.1, 12.1]],

    # 通道 2
    [[1.2, 4.2, 7.2, 10.2], [2.2, 5.2, 8.2, 11.2], [3.2, 6.2, 9.2, 12.2]],

    # 通道 3
    [[1.3, 4.3, 7.3, 10.3], [2.3, 5.3, 8.3, 11.3], [3.3, 6.3, 9.3, 12.3]]
]
```

**<font style="color:rgb(25, 27, 31);">为什么要做上采样?</font>**

<font style="color:rgb(25, 27, 31);">Contrastive Loss要求输入大小一致，而这里从View1和View2拿到的Representation不一致所以要做一个上采样。</font>

**阈值怎么确定？**

1. **<font style="color:rgb(64, 64, 64);">计算训练集的能量分数</font>**<font style="color:rgb(64, 64, 64);">：首先，模型在训练集上计算每个样本的能量分数（</font>`<font style="color:rgb(64, 64, 64);">train_energy</font>`<font style="color:rgb(64, 64, 64);">）。能量分数是模型输出的一个标量值，表示样本的异常程度。能量分数越高，表示样本越可能是异常的。</font>
2. **<font style="color:rgb(64, 64, 64);">计算测试集的能量分数</font>**<font style="color:rgb(64, 64, 64);">：然后，模型在测试集上计算每个样本的能量分数（</font>`<font style="color:rgb(64, 64, 64);">test_energy</font>`<font style="color:rgb(64, 64, 64);">）。</font>
3. **<font style="color:rgb(64, 64, 64);">确定阈值</font>**<font style="color:rgb(64, 64, 64);">：将训练集和测试集的能量分数合并，然后根据设定的异常比例（</font>`<font style="color:rgb(64, 64, 64);"> anormly_ratio </font>`<font style="color:rgb(64, 64, 64);">）来确定阈值。具体来说，阈值是合并后的能量分数的第 </font>`<font style="color:rgb(64, 64, 64);">(100 - anormly_ratio)</font>`<font style="color:rgb(64, 64, 64);"> 百分位数。合并训练集和测试集的能量分数可以更好地捕捉异常点的分布，从而设置一个更准确的阈值</font>
4. **<font style="color:rgb(64, 64, 64);">应用阈值进行异常检测</font>**<font style="color:rgb(64, 64, 64);">：在测试集上，将每个样本的能量分数与阈值进行比较。如果能量分数大于阈值，则认为该样本是异常的。</font>

![](/article_images/1736937936782-efe35092-3b8c-44bb-b65c-706f4472a12c.png)

![image](https://cdn.nlark.com/yuque/__latex/fc69d2868f1da397ea4ec06e256cccad.svg)**<font style="color:rgb(64, 64, 64);">中</font>**![image](https://cdn.nlark.com/yuque/__latex/94e79ad0c1aabeafef9e2fc4af6adf66.svg)**<font style="color:rgb(64, 64, 64);">是什么？</font>**

![image](https://cdn.nlark.com/yuque/__latex/94e79ad0c1aabeafef9e2fc4af6adf66.svg)<font style="color:rgb(64, 64, 64);">是一个矩阵，表示多变量时间序列,异常得分是基于 </font>![image](https://cdn.nlark.com/yuque/__latex/94e79ad0c1aabeafef9e2fc4af6adf66.svg)<font style="color:rgb(64, 64, 64);">的表示结果计算的,公式中的 </font>![image](https://cdn.nlark.com/yuque/__latex/ffd1905f6d4d60accedfa6b91be93ea9.svg)<font style="color:rgb(64, 64, 64);">和 </font>![image](https://cdn.nlark.com/yuque/__latex/459f3c80a50b7be28751b0869ef5386a.svg)<font style="color:rgb(64, 64, 64);">分别表示两个不同视图（或模型）的输出分布,通过计算 KL 散度（Kullback-Leibler Divergence）来衡量两个分布之间的差异，从而得到异常得分。</font>

**<font style="color:rgb(64, 64, 64);">怎么对比学习的呢？</font>**

Patch-wise Representation表示分块之间的特征，捕捉不同分块之间的依赖关系

In-patch Representation表示分块内部的特征，捕捉每个分块内部的依赖关系

对比学习的实现主要体现在 KL 散度计算上。具体来说，对比学习通过 KL 散度衡量 `series` 和 `prior` 之间的差异，通过最小化这个损失函数，模型试图使`series`和`prior` 的表示更加一致。为什么可以这样做？

<font style="color:rgb(64, 64, 64);">背景就是</font><font style="color:#DF2A3F;">对于正常点，即使在不同的视图中，它们中的大多数也会共享相同的潜在模式（强相关性不容易被破坏）。如果异常点是会导致差异大。</font>

**为什么要共享权重？**

<font style="color:rgb(31, 35, 41);background-color:rgb(249, 250, 251);">我的理解是在两个不同的view上的表现更加一致，提高模型的泛化能力。</font>

**<font style="color:rgb(64, 64, 64);">Scale Dot-product Attention？</font>**

<font style="color:rgb(64, 64, 64);">主要作用是通过动态分配注意力权重，捕捉输入序列中的全局依赖关系。</font>



