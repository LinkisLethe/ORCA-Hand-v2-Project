# 软件接入

本项目使用 STS3215。控制程序以 `software/orca_core` 中的 N-B 代码为基础，STS3215 接入和真机测试待完成。

软件阶段按这个顺序推进：

1. 先接 1 只空载舵机，用飞特调试软件完成通信、编号和低速试动
2. 接入 STS3215 驱动，核对位置范围、方向和反馈单位
3. 配置本机串口、关节映射和标定参数，再测试单指与整手
4. 加入姿态回放和电流阈值抓取

操作顺序见[教程第 15 节](tutorial.md#step-15)。

## Reference

<details>
<summary>源码、开发环境与上游差异</summary>

### 源码目录

| 目录 | 角色 |
|---|---|
| `software/orca_core` | N-B 的当前 `main`，保留 SCS225 驱动、适配模型与作者配置 |
| `software/orca_core_official` | 官方原版，独立目录用于比较和查接口 |

它们的 Python 包名都叫 `orca_core`，不要装进同一个虚拟环境。GitHub 只保留同一 fork 网络下的一个个人 fork，因此公开仓库 `LinkisLethe/orca-core-nb` 的 `main` 保留 N-B 版本、`official-main` 保留官方版本；整合仓库以不同提交引用。

### N-B 的 SCS225 代码记录

检查日期：2026-11-15；版本见 `sources.json`。

- README 提到 `scs225-dual-bus`，当前远端只列出 `main`
- `scs225_client.py` 与 `dual_scs225_client.py` 已存在，但 `SUPPORTED_MOTOR_TYPES` 与 `motor_factory.py` 尚未注册 `scs225`，现有整手配置会在验证/创建驱动时遇到缺口
- README 使用 `ftservo-python-sdk==2.0.0`，当前 `pyproject.toml` 未声明该依赖
- 双总线默认串口写的是作者本机设备路径
- SCS225 驱动用 4096 格/360°；原厂标准 SCS225 手册列 1024 格/300°，需对所购版本确认

以上是原 SCS225 适配的记录。本项目的 STS3215 使用对应协议驱动。

### 阅读、开发 N-B 代码

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

这是上游开发环境的安装方法，STS3215 接入后按实际驱动调整依赖。

查驱动时从 [SCS225](../software/orca_core/orca_core/hardware/scs225_client.py)、[双总线](../software/orca_core/orca_core/hardware/dual_scs225_client.py)、[驱动工厂](../software/orca_core/orca_core/hardware/motor_factory.py)进入。STS3215 需要对应的 STS 协议接入，不把官方 HLS 驱动或 SCS 驱动当作通用实现。

### 电流和抓取

N-B 的 `write_desired_current` 与 `set_max_current` 路径实际设置原生扭矩限制，数值 500 不等于 500 mA。其反馈读取另有电流比例，需结合具体规格确认。

抓取目标是缓慢闭合、识别接触负载、停止继续收紧并保持，具体流程见[教程](tutorial.md#step-15)。

### 更新源码

子模块只在明确更新时改变。修改前先建立本项目分支，完成修改及相关测试后提交到个人 fork，再在整合仓库更新子模块指针与 `sources.json`。不要用 `git submodule update --remote` 在装配中途同时换掉所有基线。

</details>
