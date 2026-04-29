## 任务背景
WSL连接Windows Clash代理（192.168.3.20:7890）仍然失败，深入排查根因。
## 执行过程
1. netstat发现Clash Meta进程(PID 9476)只监听127.0.0.1:7890，未监听0.0.0.0
2. config.yaml虽有bind-address: "0.0.0.0"，但进程未重启未生效
3. 之前修复的EdgeTraversalPolicy是防火墙侧，根本问题是进程监听地址
## 关键结果
- 根因：进程绑定127.0.0.1非0.0.0.0，WSL无法访问
- 解决方法：重启Clash Meta进程让其重新加载config.yaml
- 记录至memory/2026-04-29.md
## 结论建议
config.yaml修改后必须重启Clash进程才能生效。WSL访问Clash代理需确认进程监听0.0.0.0而非仅127.0.0.1。