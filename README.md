# ORCA Hand v2 国产舵机复现

本项目复现 ORCA Hand v2 右手基础版，采用 N-B 舵机安装件与飞特总线舵机。硬质件使用 PLA Basic，皮肤使用自消泡的标称食品级 0 度硅胶浇注，电脑通过 FE-URT-2 控制，舵机由外部电源供电。

学校可用打印机为拓竹 A1、P2S、H2D、P1S，优先使用 P2S。舵机型号保留 SCS225 / STS3215，整手数量为 17 个。仓库集中维护采购清单、打印清单和装配教程。

## 从这里开始

| 要做什么 | 入口 |
|---|---|
| 从准备材料到装配调试 | [详细中文教程](docs/tutorial.md)，含学校打印机、硅胶制作和模型下载链接 |
| 采购配件 | [中文 BOM](hardware/bom/feetech-v2-zh.md) / [Excel 清单](hardware/bom/ORCA_v2_Feetech_BOM_中文.xlsx) |
| 决定舵机和电源 | [选型说明与采购记录](docs/servo-selection.md) |
| 快速过一遍当前方案和要买什么 | [方案与采购顺序](docs/project.md) |

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

需要本地完整资料（两套控制源码及基础版模型）时，使用现有脚本，需要 Python 3.10+：

```bash
python scripts/setup_sources.py --hardware
```

硬件仓库使用稀疏检出，只展开 `orca_v2/base`。每个依赖都固定到本仓库记录的提交，不随上游更新自动改变。源版本见 [sources.json](sources.json)。

## Reference

- [ORCA 官方硬件](https://github.com/orcahand/orcahand_hardware)：v2 模型，CC BY 4.0
- [ORCA 官方控制](https://github.com/orcahand/orca_core)：控制软件，MIT
- [N-B-Studio](https://github.com/N-B-Studio/orca_core)：SCS225 驱动和机械适配件；保留原仓库许可及来源
- [George121380](https://github.com/George121380/ORCA_Hand_Feetech_Version)：目录与复现文档组织参考，未采用其 v1 BOM 或模型

完整来源、版本和作者截图的解释见 [来源记录](docs/sources.md)。
