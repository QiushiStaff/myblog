# Lucky J · Academic Homepage

这是一个使用 Hugo 构建、部署到 GitHub Pages 的个人学术主页。

## 本地开发

```bash
hugo server
```

默认访问地址通常是 `http://localhost:1313/`。

## 本地构建

```bash
./deploy.sh
```

或直接执行：

```bash
hugo --gc --minify
```

## 发布到 GitHub Pages

1. 将仓库推送到 GitHub。
2. 在仓库设置中打开 `Settings > Pages`。
3. 在 `Build and deployment` 的 `Source` 中选择 `GitHub Actions`。
4. 推送到 `main` 分支后，GitHub 会自动运行 `.github/workflows/hugo.yaml` 并发布站点。

站点地址：

- 项目页：`https://qiushistaff.github.io/myblog/`

## 内容组织

- `content/about.md`：个人简介
- `content/research.md`：研究方向
- `content/publications.md`：论文与成果
- `content/blog/`：公开文章与研究笔记

## 写新文章

```bash
hugo new content/blog/你的文章标题.md
```

新文章默认 `draft = false`。如果你不想立即公开，可以手动改为 `draft = true`。
