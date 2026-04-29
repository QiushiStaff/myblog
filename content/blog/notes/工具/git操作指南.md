---
title: "git操作指南"
date: 2026-04-29
draft: false
---

## 基础知识

![image-20250109153852745](/article_images/image-20250109153852745-1736408334314-11.png)



工作区：就是文件资源管理器。 	相当于工厂

暂存区：用于保存即将保存到git仓库的修改内容。暂存区相当于工厂与仓库之间的小货车

本地仓库：Git存储代码和版本信息的主要位置。相当于仓库

创建代码

1. git init
2. git clone

![image-20250109144409503](/article_images/image-20250109144409503-1736405058024-1.png)

这里的未修改、已暂存是指，放置在暂存区中的文件。

为跟踪是不被git管理的文件。



### **怎样将文件添加到仓库里面？**

![image-20250109144431156](/article_images/image-20250109144431156-1736405076034-3.png)



git commit -m "message" 命令**只提交**暂存区中的文件到仓库，-m用来保存提交相关信息，会被记录到参考中。

git add . ---提交当前文件夹中的文件到暂存区。

![image-20250109144505316](/article_images/image-20250109144505316-1736405106395-5.png)





### **新版的本地仓库引用远程仓库**

这个位置应该注意Github和Gitee的区别,Github必须使用token才能建立.Gitee好像直接跟ssh地址就可以.

`git remote set-url origin git@gitee.com:library-library/typora-noteb.git`

`git remote set-url origin https:///<USERNAME>/<REPO>.git` 

// 自己的命令 

<<<<<<< HEAD
`git remote set-url origin https://YOUR_TOKEN_HERE@github.com/Xinghong-jxnu/Android_Project_Glass`
=======
`git remote set-url origin `
>>>>>>> 75d4c16 (refine again)

// remote 是指远程仓库的简称。它是一个指向远程代码仓库（如 GitHub、Gitee、GitLab 等）的引用。

 // 你可以配置多个remote，比如一个指向 GitHub，另一个指向 Gitee。 

`git remote -v // 查看当前配置的远程仓库` 

`git remote add <名称> <仓库地址> // 添加新的远程仓库 git remote set-url <名称> <新的仓库地址>` 

// 修改远程仓库的URL 

// origin 是 Git 默认的远程仓库名称 



**clone指定branch的项目**

`git clone -b <branch-name> <repository-url>`





### **一个简简单单的示例（到github）**

1. 在 github 上创建一个新的仓库，给它一个合适的名字，比如 my-project。

2. 在本地创建一个文件夹，用来存放你的项目文件，比如 my-project。

3. 在本地文件夹中打开 git bash，输入 git init 命令，初始化一个本地仓库。

4. 将你的项目文件复制或移动到本地文件夹中，然后输入 git add . 命令，将所有文件添加到暂存区。

5. 输入 git commit -m "first commit" 命令，将暂存区的文件提交到本地仓库的当前分支上，并添加一个提交信息。

6. 输入看上面的remote命令，将本地仓库与远程仓库关联起来，其中 yourname 是你的 github 用户名，my-project 是你的 github 仓库名。（token是通用的）

7. git pull 同步本地仓库和远程仓库。

8. 输入 git push -u origin master 命令，将本地仓库的内容推送到远程仓库的 master 分支，并设置为默认分支。

9. 这时你可以在 github 上查看你的仓库，应该能看到你的项目文件已经上传成功了。




### **一个简简单单的示例（到Gitee）**

1. 配置git。

   `git config --global user.name "Xinghong-Qiushi"`
   `git config --global user.email "jxh@jxnu.edu.cn"`

   当我们去掉--global，当前配置只是在当前仓库生效。

2. 配置SSH连接。

   + 在本地生成密钥，公钥配置给Gitee。私钥放在本地。
   + 在`git remote`的时候我们使用SSH的地址。
   + `git pull origin master`不需要在输入用户名和密码。

   > 注: `git pull` 相当于 `git fetch` + `git merge`
   >
   > 它会从当前分支的默认远程仓库（通常是 `origin`）拉取最新的更改，并尝试将其合并到当前分支。

   > 注：`git branch`查看当前分支。
   >
   > ​	`git checkout <分支名>` 切换分支。
   >
   > ​	`git switch <分支名>` 新版的切换分支命令。

   > 知识: 当前分支,上游分支和远程分支的关系. 本地分支通过上游分支构建与远程分支的连接关系.一个本地分支可以有一个上游分支，指向某个远程分支。
   >
   > `git branch --set-upstream-to=origin/<远程分支名>`  //将当前分支与远程分支关联.

3. 在 github 上创建一个新的仓库，给它一个合适的名字，比如 my-project。

4. 在本地创建一个文件夹，用来存放你的项目文件，比如 my-project。

5. 在本地文件夹中打开 git bash，输入 git init 命令，初始化一个本地仓库。

6. 将你的项目文件复制或移动到本地文件夹中，然后输入 git add . 命令，将所有文件添加到暂存区。

7. 输入 git commit -m "first commit" 命令，将暂存区的文件提交到本地仓库的当前分支上，并添加一个提交信息。

8. 输入上面的remote命令，将本地仓库与远程仓库关联起来，其中 yourname 是你的 github 用户名，my-project 是你的 github 仓库名。（token是通用的）。关联之前先设置一下origin

   创建一个远程仓库：

    `git remote add origin_init git@gitee.com:library-library/qiushi_-initially.git`

   设置或修改已存在远程仓库的 URL 地址：

   `git remote set-url origin git@gitee.com:library-library/typora-noteb.git`

9. git pull 同步本地仓库和远程仓库。

10. 输入 `git push -u origin master` 命令，将本地仓库的内容推送到远程仓库的 master 分支，并设置为默认分支。

11. 这时你可以在 github 上查看你的仓库，应该能看到你的项目文件已经上传成功了。





### **一个简简单单的示例（到gerrit）**

1. git clone -b ,克隆指定branch到本地
2. git add .，添加文件到暂存区
3. git status，查看那个文件被修改
4. git commit -m "message" ,提交文件到本地仓库
5. git push origin HEAD:refs/for/master
6. 遇到错误，原因提交到gerrit需要有change-id。

解决办法，执行下面语句

之后使用命令“`git commit --amend --no-edit`”重新生成 commit信息并提交，也即是在之前的commit中添加change Id。

**提交过去之后要在open中设置+2,+1**

![image-20250109144859629](/article_images/image-20250109144859629-1736405340859-7.png)







### **./git文件目录**

![image-20250109145009724](/article_images/image-20250109145009724-1736405410799-9.png)

- HEAD：指向当前所在的分支（或者是一个特定的提交）。

- branches：存储了每个远程分支的相关信息。

- config：存储了项目级别的Git配置信息，包括用户名、邮箱、远程仓库等。

- description：对于空的Git仓库，此文件内容为空。对于非空的Git仓库，描述该项目的文本。

- hooks：存放各种Git钩子（hooks）的目录，包括预定义的钩子模板和用户自定义的钩子脚本。

- index：包含了暂存区（stage）的内容，记录了即将提交的文件和相关元数据。

- info：包含一些辅助性的信息。

- logs：存储了每个引用（分支、标签等）的修改历史。

- objects：存储了Git仓库的对象（commits、trees和blobs）。

- refs：存储了所有的引用（分支、标签等）。

- config、ignore等：其他配置文件和设置。