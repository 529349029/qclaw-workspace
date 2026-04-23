- **2026-04-14**：记忆系统启用
- **2026-04-19**：设置每日 Git 自动备份到 GitHub，换电脑可无缝恢复
- **计划换 Mac**，但以后再说，换机前提前告知我做好迁移准备

## Git 备份（每日自动）

- **仓库地址：** https://github.com/529349029/qclaw-workspace
- **备份时间：** 每天 21:00（Asia/Shanghai）
- **备份内容：** MEMORY.md、memory/、sessions/、TOOLS.md 等
- **Cron 任务 ID：** 2d032b85-c7c1-446c-a7e9-66dc3b4e4bf0
- **恢复方法：** 新电脑 clone 后覆盖 .qclaw/workspace 目录即可

## 当前项目与关注

- 关注巴菲特分析框架下的贵州茅台（600519.SH）投资分析
- 使用 buffett-analysis 技能进行分析，数据来源：东方财富网 API
- 正在学习 Solidity，目标是提高 Solidity 水平
- **Solana/Anchor 开发环境配置放弃**：cargo-build-sbf v4.0.0 正则 bug（`rustc 1.75.0-dev` 的 `-dev` 后缀不匹配 `rustc X.Y.Z` 正则导致 unwrap panic），等官方修复再考虑

## 软件下载偏好

- **优先下载绿色免安装版（Portable）**，不安装软件到系统目录
- **安装软件优先选择最新稳定版（latest stable）**
- 环境变量统一配置到 **Machine 级**（系统级），确保所有进程都能读取
- 避免：腾讯电脑管家软件市场、360软件管家等（安装包可能有捆绑）
- 推荐：GitHub开源项目、绿色软件站（多多软件站、ity果园等）
- 便携版优点：无残留、换电脑不丢数据、可放U盘随身带

## 技术规范偏好

- **安装软件/配置环境必须优先使用国内镜像**（外网速度太慢），详见 TOOLS.md 中的镜像配置
- 访问外网需走 Clash 代理：http://127.0.0.1:7890（curl -x）
- curl 访问东方财富网 API（含 emweb.securities.eastmoney.com、push2.eastmoney.com）需加代理参数

## 已安装软件路径

| 软件 | 版本 | 路径 |
|------|------|------|
| Solana CLI | 1.18.26 | `C:\Program Files\Solana\solana-release\bin\` |
| Rust | 1.95.0 | `$env:USERPROFILE\.cargo\bin\` |
| Anchor CLI | 1.0.1 | `$env:USERPROFILE\.cargo\bin\` |
| avm | 跳过 | 旧包编译需 OpenSSL 1.x，固定版本不需要 |
| VS Build Tools | 14.44 | `C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\` |

## 经验与决策

- **安装软件前务必先检查是否已安装**（搜索 Program Files、用户目录等），避免重复安装浪费时间

- **配置环境变量前先检查是否已存在**：用 `[Environment]::GetEnvironmentVariable("Path", "User")` 检查，避免重复添加

- buffett-analysis 脚本路径：C:\Users\Administrator\.qclaw\workspace\skills\buffett-analysis\scripts\fetch_company_data.py，依赖 mcporter 工具不可用，改用 curl 直接调用东方财富 API 绕过
- 阿尔法工坊前端：https://finstep-ai.github.io/alpha-factor-lab/fundamental.html
- PowerShell 中 Invoke-WebRequest 的 -L 参数不受支持（curl 别名问题），如需处理重定向建议直接使用 curl.exe

## 用户身份与偏好

- 学习偏好：偏好有考试和习题的学习平台；搜索/推荐内容时需附上对应网址
