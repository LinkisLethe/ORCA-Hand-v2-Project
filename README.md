# ORCA Hand v2 国产舵机复现

本项目以 ORCA Hand v2 右手基础版为机械平台，按官方 v2 BOM 整理采购，并采用 N-B-Studio 的舵机机械适配件。保留 **SCS225 与 STS3215 两个选项**，目前尚未购买舵机，未进行本项目的实物验证。

仓库集中提供物料表、打印入口、装配说明、固定版本的上游源码，以及课程演示计划。目录组织参考 George121380 的项目，机械结构与物料仍使用 v2。

## 从这里开始

| 要做什么 | 入口 |
|---|---|
| 从准备材料到装配调试 | [详细中文教程](docs/tutorial.md)，含学校打印机、硅胶制作和模型下载链接 |
| 采购配件 | [中文 BOM](hardware/bom/feetech-v2-zh.md) / [Excel 清单](hardware/bom/ORCA_v2_Feetech_BOM_中文.xlsx) |
| 决定舵机和电源 | [选型说明与采购记录](docs/servo-selection.md) |

进度与课程要求见 [项目说明](docs/project.md)，控制程序的现状见 [软件说明](docs/software.md)。仓库公开，队友可以直接阅读和下载。

```text
hardware/
  bom/                  飞特中文采购表、Excel、官方 v2 原始 CSV
  3d_print/             官方模型与 N-B 替换件的取用说明
  official/             官方硬件 fork，固定版本的 Git 子模块
software/
  orca_core/            N-B fork，保留作者源码和适配模型
  orca_core_official/   同一 fork 的官方代码分支，用于参考与比较
docs/                   中文教程、选型记录、软件、演示与来源说明
scripts/                拉取源码、生成 BOM 阅读表、检查目录
experiments/            实物记录模板
local/                  本机串口、标定文件，Git 忽略
runs/                   本机实验输出，Git 忽略
```

## 获取源码

只阅读教程或下载打印文件，不需要先安装代码。准备开发控制程序时，用 Git 获取 N-B 源码：

```bash
git clone https://github.com/LinkisLethe/ORCA-Hand-v2-Project.git
cd ORCA-Hand-v2-Project
git submodule update --init --depth 1 -- software/orca_core
```

需要官方控制代码作对照时，再单独获取：

```bash
git submodule update --init --depth 1 -- software/orca_core_official
```

需要本地完整资料（两套控制源码及基础版模型）时，使用现有脚本，需要 Python 3.10+：

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
