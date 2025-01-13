# DST Mod Config Converter

一个在线工具，用于将饥荒联机版（Don't Starve Together）的客户端mod配置转换为服务器mod配置。

## 功能
- 自动将 modoverrides.lua 转换为 dedicated_server_mods_setup.lua
- 支持主世界和洞穴世界的mod配置合并
- 自动去重并排序mod ID
- 简单的web界面，复制粘贴即可使用

## 使用方法
1. 从客户端找到 modoverrides.lua 文件
   - 通常位于：`.klei/DoNotStarveTogether/客户端设置/Cluster_1/Master/modoverrides.lua`
   - 和 `.klei/DoNotStarveTogether/客户端设置/Cluster_1/Caves/modoverrides.lua`
2. 将文件内容粘贴到网页对应的输入框
3. 点击生成按钮
4. 复制生成的内容到服务器的 dedicated_server_mods_setup.lua

## 在线使用
访问：[https://dst-mod-config-converter.vercel.app](https://dst-mod-config-converter.vercel.app)

## 本地运行

### 方法一：直接运行
1. 安装Python 3.7+
2. 克隆仓库：
3. 安装依赖：
```bash
pip install -r requirements.txt
```
4. 运行服务器：
访问 http://localhost:8000/static/index.html
方法二：Docker运行
1. 安装Docker
2. 克隆仓库并进入目录
3. 构建并运行：
```bash
docker compose up -d
```
访问 http://localhost:8000/static/index.html