## 任务背景
用户先后请求：导出聊天记录、查看运行日志位置、安装 wechat-cli 工具。
## 执行过程
1. 从lcm.db导出81个对话为Markdown
2. 定位QClaw日志目录（加密.enc格式）
3. 尝试安装wechat-cli发现仅支持Mac
## 关键结果
- 聊天导出：`C:\Users\Administrator\.qclaw\workspace\chat-export\`，82文件3.2MB
- 日志查看：F12开发者工具最直接，日志文件为AES加密
- wechat-cli：无win32-x64平台包，安装失败
## 结论建议
wechat-cli仅支持Mac，需等作者发Windows版或换环境。聊天记录已完整导出可随时查看。