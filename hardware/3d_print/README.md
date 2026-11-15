# 右手打印清单

方案：ORCA v2 右手基础结构＋N-B 舵机安装件，PLA Basic 硬质件，自制硅胶皮肤。学校优先使用拓竹 P2S，丝材为 1.75 mm。

## 结构件

| 模块 | 模型 | 单手数量 |
|---|---|---:|
| 食指 | I-IP、I-PP、I-AP-R | 各 1 |
| 中指、无名指 | M-IP、M-PP、M-AP | 各 2 |
| 小指 | P-IP、P-PP、P-AP | 各 1 |
| 拇指 | T-DP、T-PP、右手 T-AP、T-TP-R | 各 1 |
| 手掌 | R-Carpals | 1 |
| 舵机架 | N-B `scs-225-case.stl` | 2 |
| N-B 安装件 | `base-holder.stl` | 待补原件对应关系 |
| N-B 安装件 | `pin-holder.stl` | 待补原件对应关系 |
| 手指卷线轮 | BaseSpool、SpoolCover、Ratchet | 各 16 |
| 腕部传动 | CarpalsTeeth、WristTeeth | 各 1 |
| 腕部安装 | WristStructure_Feetech、WristAdapter_Feetech | 各 1；与 N-B 安装件的接口一起配合 |
| 外壳和线盖 | 匹配舵机架的前后壳、侧板、风扇盖和线盖 | 按装配位置配套，最后打印 |

N-B 舵机架模型每片安排 8 个手指舵机，按两片合计 16 个布局准备；手腕舵机另装。手指卷线轮按 16 组准备，备用件按需增加。

## N-B 提供了什么

| 文件 | 使用方式 |
|---|---|
| `scs-225-case.stl` | 打印舵机架，替换官方舵机仓 |
| `base-holder.stl` | 已有模型，需要对应原件名称或安装位置 |
| `pin-holder.stl` | 已有模型，需要对应原件名称或安装位置 |
| `scs225-case.step` | 舵机架的可编辑文件 |
| `ST3215 Servo v2.step` | 用于对照舵机外形 |

**一一对应的替换件，直接沿用原件数量。** 现在只需补清 `base-holder.stl` 和 `pin-holder.stl` 的对应关系，便可决定数量及哪些原件由它们替换。一张标出这两件位置的装配图即可，不要求另交完整工程。

N-B 还提供了整手、卷线轮实拍和 SCS225 控制代码。其公开文件没有给这两个小件标注原件名称。

## 硅胶皮肤与模具

当前 Base 皮肤目标为 DP 5 件、PP 5 件、右手掌 1 件。下表按仓库现有 1100 模具文件整理；模具与骨架成套取用。

| 皮肤 | 成品数量 | 最少模具数量 |
|---|---:|---|
| DP 中号：食指、中指、无名指 | 3 | M-DP 上模、下模、夹扣各 1，重复浇注 |
| DP 拇指 | 1 | T-DP 上模、下模、夹扣各 1 |
| DP 小指 | 1 | P-DP 上模、下模、夹扣各 1 |
| PP 中号：中指、无名指 | 2 | M-PP 上模、下模、夹扣各 1，重复浇注 |
| PP 食指、拇指、小指 | 各 1 | I-PP、T-PP、P-PP 各一套上下模和夹扣 |
| 右手掌 | 1 | R-CarpalsMold-A-Funnel、B-Funnel、CORE-R 各 1 |
| 浇注辅件 | 复用 | SingleFunnel 1，Cylinder 按浇口连接方式配置 |

模具中指定软材的掌部 B 件使用约 85A TPU，其余按工程使用 PLA。CORE-R 在多个盘中出现时只准备一份。皮肤通过浇注制作，不再打印 TPU 成品皮肤。

## Reference

### 1000 和 1100 的意思

它们是 ORCA 基础手的硬件修订编号，不是舵机型号：

- **1000**：较早的基础手文件包，FT 工程名为 `Prints-1000-FT.3mf`
- **1100**：后续修订的基础手文件包，工程名为 `Prints-1100.3mf`，同一工程中分别放置 FT 和 DX 盘

从 1000 到 1100，手指、手掌、腕部和卷线轮的一些尺寸发生变化。N-B 的说明写“用 v2”，没有注明这两个修订编号。基础件、卷线轮和模具应使用同一修订。

1100 第 10 盘是 `CNC Parts (FDM NOT RECOMMENDED!!)`，列出金属加工用途的支撑件、张紧件及机械臂安装件，不在本项目 PLA 打印清单中。

本清单已排除左手备选、官方 DX/HL 舵机仓、U2D2 固定件、直接打印的 TPU 皮肤、舵机外形参考模型和 Franka 安装件。

### 文件与来源

- [N-B 改件目录](https://github.com/LinkisLethe/orca-core-nb/tree/9224bd81343ddab9a076b16fae3e885739994ec5/SCS-225/3D-model)
- [N-B 卷线轮实拍](https://github.com/LinkisLethe/orca-core-nb/blob/9224bd81343ddab9a076b16fae3e885739994ec5/SCS-225/Image/spool.png)
- [1000 基础手](https://github.com/orcahand/orcahand_hardware/blob/v1000/orca_v2/base/Prints-1000-FT.3mf)
- [仓库现有 1100 基础手](https://github.com/LinkisLethe/orcahand-hardware/blob/0ce26465a4f67c8ab3391cf157853ac24b1fb9c1/orca_v2/base/Prints-1100.3mf)
- [1100 硅胶模具](https://github.com/LinkisLethe/orcahand-hardware/blob/0ce26465a4f67c8ab3391cf157853ac24b1fb9c1/orca_v2/base/SiliconeMolds-1100.3mf)
- [官方修订记录](https://github.com/orcahand/orcahand_hardware/commit/8b50873a90eab66f7fcb97f8d20cd88ab36c62bc)

数量依据：单手关节数、3MF 模型实例及 N-B 舵机架布局。官方盘中包含的额外副本不计入单手净用量；当前 v1000 小件盘实际有 18 个 BaseSpool、18 个 SpoolCover、17 个 Ratchet，1100 各有 20 个。
