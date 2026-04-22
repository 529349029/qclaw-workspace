## 任务背景
用户报告 Lingma IDE 找不到 `solana` 命令，但系统 PowerShell 正常。需排查 solana 命令不可用的根本原因。

## 执行过程
1. 对比系统 PATH 和 QClaw 终端 PATH，发现 QClaw exec 缺少 Solana 路径
2. 确认 Anchor CLI 1.0.1 已发布，Anchor 项目已迁移至 solana-foundation
3. 定位根因：Lingma Electron 应用的子进程未继承完整系统 PATH
4. 通过 PowerShell 将 Solana 和 Cargo 路径写入 Machine 级环境变量
5. 用户要求记录：以后所有环境变量统一配置在 Machine 级

## 关键结果
- 已将 `C:\Program Files\Solana\solana-release\bin` 和 `C:\Users\Administrator\.cargo\bin` 写入 Machine PATH
- 需重启 Lingma IDE 使新 PATH 生效
- 已更新 MEMORY.md：环境变量统一走 Machine 级

## 结论建议
环境变量已写入系统级，用户重启 Lingma 后 `solana` 命令应可用。MEMORY.md 已记录偏好，后续配置持续遵循 Machine 级原则。