#!/bin/bash

set -e

echo "开始构建站点..."
echo "清理旧产物..."
rm -rf public resources/_gen

echo "生成静态页面..."
hugo --gc --minify

echo "构建完成。"
echo "本地预览：hugo server"
echo "正式发布：push 到 GitHub 后由 GitHub Pages Actions 自动部署。"
