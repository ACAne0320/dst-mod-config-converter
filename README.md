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

## 本地运行
1. 安装Python 3.7+
2. 安装依赖：
