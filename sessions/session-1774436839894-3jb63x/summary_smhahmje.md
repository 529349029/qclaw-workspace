## 任务背景
QClaw工作区推送GitHub时被Push Protection拦截，chat-export/目录含GitHub Personal Access Token。
## 执行过程
1. git rm --cached移除chat-export/跟踪
2. 追加chat-export/等到.gitignore
3. git reset --soft c68a71b回退到干净commit
4. 只提交.gitignore/memory/sessions等安全文件
5. 强制推送GitHub成功
6. 推送D:\busd和D:\usdt
## 关键结果
- QClaw工作区强制推送成功 c68a71b→a703b7f
- D:\busd→Gitee+GitHub commit 9161c97 ✅
- D:\usdt→Gitee temp-branch commit 877c02c ✅
- chat-export/永久加入.gitignore
## 结论建议
chat-export/含对话记录可能有token，永远不应提交git。已记录至memory/2026-04-26.md。