---
title: "dart基础知识"
date: 2026-04-29
draft: false
---

## Stream和Future

​	dart:async 库中有两个类型，它们对许多 Dart API 来说都非常重要： [Stream](https://api.dart.cn//dart-async/Stream-class.html) 和 [Future](https://api.dart.cn//dart-async/Future-class.html)。 Future 用于表示**单个**运算的结果，而 Stream 则表示**多个结果的序列**。Future 表示一个不会立即完成的计算过程。与普通函数直接返回结果不同的是异步函数返回一个将会**包含结果的 Future**。该 Future 会在结果准备好时通知调用者。Stream 是一系列异步事件的序列。其类似于一个异步的 Iterable，不同的是当你向 Iterable 获取下一个事件时它会立即给你，但是 Stream 则不会立即给你而是在它准备好时告诉你。

​	你可以监听 Stream 以获取其结果（包括数据和错误）或其关闭事件。也可以在 Stream 完成前对其暂停或停止监听。

关键点：

- Stream 提供一个异步的数据序列。
- 数据序列包括用户生成的事件和从文件读取的数据。
- 你可以使用 Stream API 中的 `listen()` 方法和 **await for** 关键字来处理一个 Stream。
- 当出现错误时，Stream 提供一种处理错误的方式。
- Stream 有两种类型：Single-Subscription 和 Broadcast。

![image.png](/article_images/e9bf85e7ba8a42b386720e43f8e7ee31tplv-k3u1fbpfcp-zoom-in-crop-mark1512000.webp)







## get方法和普通方法的区别：

- 调用时不需要加括号，就像访问属性一样。
- 不能接受参数。
- 它只是用于获取某个值。

```
// get 方法
int get count => _count;
print(count); // 直接访问，不需要括号

// 普通方法
int getCount() => _count;
print(getCount()); // 需要加括号
```



## 变量命名

- 变量名以 `_` 开头，表示这是一个私有变量，只能在当前库（文件）中访问。