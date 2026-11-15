# 软件入口与当前可用范围

## 两份源码

| 目录 | 角色 |
|---|---|
| `software/orca_core` | N-B 的当前 `main`，保留 SCS225 驱动、适配模型与作者配置 |
| `software/orca_core_official` | 官方原版，独立目录用于比较和查接口 |

它们的 Python 包名都叫 `orca_core`，不要装进同一个虚拟环境。GitHub 只保留同一 fork 网络下的一个个人 fork，因此公开仓库 `LinkisLethe/orca-core-nb` 的 `main` 保留 N-B 版本、`official-main` 保留官方版本；整合仓库以不同提交引用。

## N-B 的 README 与实际代码差异

检查日期：2026-11-15；版本见 `sources.json`。

- README 提到 `scs225-dual-bus`，当前远端只列出 `main`
- `scs225_client.py` 与 `dual_scs225_client.py` 已存在，但 `SUPPORTED_MOTOR_TYPES` 与 `motor_factory.py` 尚未注册 `scs225`，现有整手配置会在验证/创建驱动时遇到缺口
- README 使用 `ftservo-python-sdk==2.0.0`，当前 `pyproject.toml` 未声明该依赖
- 双总线默认串口写的是作者本机设备路径
- SCS225 驱动用 4096 格/360°；原厂标准 SCS225 手册列 1024 格/300°，需对所购版本确认

因此这里纳入的是可追溯的代码基线，不能将 README 的“已验证”直接变成本仓库当前 checkout 已能整手运行的结论。本轮未修改上游驱动，也未连接硬件。后续首先补齐注册入口、双总线端口配置和位置比例，再进行单舵机联调。

## 在本机阅读、开发 N-B 代码

在项目根目录运行：

```bash
git submodule update --init --depth 1 -- software/orca_core
python -m venv .venv
```

Windows：

```powershell
.\.venv\Scripts\python.exe -m pip install -e software/orca_core ftservo-python-sdk==2.0.0
```

Linux：

```bash
.venv/bin/python -m pip install -e software/orca_core ftservo-python-sdk==2.0.0
```

这里只准备依赖，不会控制舵机；安装依赖也不代表上述主程序缺口已经修复。当前任务未执行这套环境的全量安装与测试。

查驱动时从 [SCS225](../software/orca_core/orca_core/hardware/scs225_client.py)、[双总线](../software/orca_core/orca_core/hardware/dual_scs225_client.py)、[驱动工厂](../software/orca_core/orca_core/hardware/motor_factory.py)进入。STS3215 需要对应的 STS 协议接入，不把官方 HLS 驱动或 SCS 驱动当作通用实现。

## 电流和抓取

N-B 的 `write_desired_current` 与 `set_max_current` 路径实际设置原生扭矩限制，数值 500 不等于 500 mA。其反馈读取另有电流比例，需结合具体规格确认。

计划实现的抓取逻辑是缓慢闭合、识别接触负载、停止继续收紧并保持。仅停止发送新目标而保留过深目标，仍可能持续拉紧。电流反馈不是指尖力，阈值抓取也还不是本项目已经完成的功能。

## 更新源码

子模块只在明确更新时改变。修改前先建立本项目分支，完成修改及相关测试后提交到个人 fork，再在整合仓库更新子模块指针与 `sources.json`。不要用 `git submodule update --remote` 在装配中途同时换掉所有基线。
