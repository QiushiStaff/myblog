import os
import re

root_dir = 'content/blog/notes'

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. 添加 Frontmatter (如果缺失)
    if not content.startswith('---'):
        title = os.path.splitext(os.path.basename(filepath))[0]
        title = title.replace('"', '\\"')
        frontmatter = f'---\ntitle: "{title}"\ndate: 2026-04-29\ndraft: false\n---\n\n'
        content = frontmatter + content

    # 2. 修复图片路径 (极致兼容版)
    # 处理反斜杠
    content = content.replace('\\article_images\\', '/article_images/')
    content = content.replace('article_images\\', '/article_images/')
    
    # 匹配各种形式的 src 路径
    # 使用更安全的正则
    # 匹配 src=" 或 src=' 后面接可选的 ./ 或 ../ 然后是 article_images/
    content = re.sub(r'src=["\'](?:\.\.?/|\.\.?\\)?article_images/', 'src="/article_images/', content)
    # 匹配 markdown 图片语法 ![alt](article_images/...)
    content = re.sub(r'\((?:\.\.?/|\.\.?\\)?article_images/', '(/article_images/', content)
    
    # 再次处理可能残留的反斜杠
    content = content.replace('/article_images\\', '/article_images/')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith('.md'):
            process_file(os.path.join(root, file))
