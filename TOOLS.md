# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

## 软件安装配置

**优先使用国内镜像**，国外源速度很慢甚至无法访问。

### Rust
```bash
# 使用 USTC 镜像
set RUSTUP_DIST_SERVER=https://mirrors.ustc.edu.cn/rust-static
set RUSTUP_UPDATE_ROOT=https://mirrors.ustc.edu.cn/rust-static/rustup
```

### npm / Node.js
```bash
npm config set registry https://registry.npmmirror.com
```

### Cargo / crates.io
在 `~/.cargo/config.toml` 中配置：
```toml
[source.crates-io]
replace-with = 'ustc'

[source.ustc]
registry = "sparse+https://mirrors.ustc.edu.cn/crates.io-index"
```

### Go
```bash
go env -w GOPROXY=https://goproxy.cn,direct
```

### Python pip
```bash
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

### Solana CLI
```bash
sh -c "$(curl -sSfL https://release.anza.xyz/stable/install)"
# 或手动下载后通过代理安装
```

---

## 网络代理

本地 Clash 代理在 `127.0.0.1:7890`，系统代理未启用。

**使用规则：**
- 🚫 **国内网站**（百度、淘宝、东方财富、新浪、雪球等）：直接访问，**不加 `-x` 参数**
- ✅ **国际网站**（Google、GitHub、Twitter、BBC 等）：如果直连不通，再加 `-x http://127.0.0.1:7890`

```bash
# 国内（不加代理）
curl -s "https://emweb.securities.eastmoney.com/..."

# 国际（直连不通时加代理）
curl -x http://127.0.0.1:7890 -s "https://api.github.com/..."
```

---

Add whatever helps you do your job. This is your cheat sheet.
