# ORCA Hand v2 国产舵机复现

本项目以 ORCA Hand v2 右手基础版为机械平台，按官方 v2 BOM 整理采购，并采用 N-B-Studio 的舵机机械适配件。保留 **SCS225 与 STS3215 两个选项**，目前尚未购买舵机，未进行本项目的实物验证。

仓库集中提供物料表、打印入口、装配说明、固定版本的上游源码，以及课程演示计划。目录组织参考 George121380 的项目，机械结构与物料仍使用 v2。

## 从这里开始

1. 阅读 [方案与进度](docs/project.md)，了解哪些已经确定、哪些仍待选择
2. 查看 [官方 v2 BOM](hardware/bom/official-v2.md) 和 [国产替换项](hardware/bom/substitutions.md)
3. 根据 [舵机选型](docs/servo-selection.md) 确定完整型号和电源
4. 按 [打印与替换关系](hardware/3d_print/README.md) 准备模型
5. 按 [装配顺序](docs/assembly.md)、[软件入口](docs/software.md) 推进

```text
hardware/
  bom/                  官方 v2 原始 CSV、可读物料表、国产替换项
  3d_print/             官方模型与 N-B 替换件的取用说明
  official/             官方硬件 fork，固定版本的 Git 子模块
software/
  orca_core/            N-B fork，保留作者源码和适配模型
  orca_core_official/   同一 fork 的官方代码分支，用于参考与比较
configs/                SCS225、STS3215 方案记录；不是可直接上机的标定配置
docs/                   选型、装配、接线、软件、演示与来源说明
scripts/                拉取源码、生成 BOM 阅读表、检查目录
experiments/            实物记录模板
local/                  本机串口、标定文件，Git 忽略
runs/                   本机实验输出，Git 忽略
```

## 获取源码

需要 Git 和 Python 3.10+。在新电脑上执行：

```bash
git clone https://github.com/LinkisLethe/ORCA-Hand-v2-Project.git
cd ORCA-Hand-v2-Project
python scripts/setup_sources.py
python scripts/check_project.py
```

默认只获取两套控制源码。需要打印模型时再运行：

```bash
python scripts/setup_sources.py --hardware
```

硬件仓库使用稀疏检出，只展开 `orca_v2/base`。每个依赖都固定到本仓库记录的提交，不随上游更新自动改变。源版本见 [sources.json](sources.json)。

## 当前能力与边界

| 内容 | 状态 |
|---|---|
| 官方 v2 BOM、官方模型、N-B 替换件 | 已整理并固定来源 |
| SCS225 | 保留为主要候选；原厂标准规格为 7.4 V 级别，作者使用拆机件 |
| STS3215 | 保留为另一候选；具体电压版和减速比未选定 |
| N-B 控制代码 | 已纳入；主分支有驱动，但 SCS225 主程序入口有缺口，见软件说明 |
| 电流阈值抓取、姿态回放 | 本项目计划，尚未实现或验证 |
| 实体手装配与抓取 | 尚未验证 |

SCS225 的电源不能直接照抄官方 HL 舵机的 12 V 配置。N-B 的 `set_max_current` 适配值是原生扭矩限制单位，不是毫安。

## 上游与许可

- [ORCA 官方硬件](https://github.com/orcahand/orcahand_hardware)：v2 模型，CC BY 4.0
- [ORCA 官方控制](https://github.com/orcahand/orca_core)：控制软件，MIT
- [N-B-Studio](https://github.com/N-B-Studio/orca_core)：SCS225 驱动和机械适配件；保留原仓库许可及来源
- [George121380](https://github.com/George121380/ORCA_Hand_Feetech_Version)：目录与复现文档组织参考，未采用其 v1 BOM 或模型

完整来源、版本和作者截图的解释见 [来源记录](docs/sources.md)。
