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
| 舵机仓底座圆板 | N-B `base-holder.stl` | 1 |
| 两片舵机仓的双销连接片 | N-B `pin-holder.stl` | 4 |
| 手指卷线轮 | BaseSpool、SpoolCover、Ratchet | 各 16 |
| 腕部传动 | CarpalsTeeth、WristTeeth | 各 1 |
| 腕部安装 | WristStructure_Feetech、WristAdapter_Feetech | 各 1；与 N-B 安装件的接口一起配合 |
| 外壳和线盖 | 匹配舵机架的前后壳、侧板、风扇盖和线盖 | 按装配位置配套，最后打印 |

N-B 舵机架模型每片安排 8 个手指舵机，按两片合计 16 个布局准备；底座用一块圆板连接，四处边缘连接位各用一片双销连接片。手腕舵机另装。手指卷线轮按 16 组准备，备用件按需增加。

## N-B 提供了什么

| 文件 | 使用方式 |
|---|---|
| `scs-225-case.stl` | 打印舵机架，替换官方舵机仓 |
| `base-holder.stl` | 新舵机仓底部的圆形连接板，四个螺钉孔连接两侧仓体 |
| `pin-holder.stl` | 跨接两片仓体的双销连接片，一枚销插入一侧仓体 |
| `scs225-case.step` | 舵机架的可编辑文件 |
| `ST3215 Servo v2.step` | 用于对照舵机外形 |

这三种零件共同构成 N-B 舵机仓组件，整组替换官方 `ForeArmStructure_*` 舵机仓。`base-holder` 和 `pin-holder` 是分体舵机仓的配套连接件，数量按新仓体的连接位置计算，不直接套用原厂 `SpoolHolder` 长支撑条的数量。

用途与用量依据 STL 几何配合判断，测量依据见文末 Reference。N-B 另提供整手、卷线轮实拍和 SCS225 控制代码。

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

它们是 ORCA v2 基础手的硬件修订编号。两套文件都位于官方 `orca_v2/base/` 目录，均属于 v2 系列。

- **1000**：较早的基础手文件包，FT 工程名为 `Prints-1000-FT.3mf`
- **1100**：后续修订的基础手文件包，工程名为 `Prints-1100.3mf`，同一工程中分别放置 FT 和 DX 盘

`.stl` 保存单个零件的表面几何，`.3mf` 工程还包含模型摆盘、材质分配和切片预设；它们是制作零件的文件，不是材料采购表。材料种类与用量见 BOM。

| 对比项 | 1000 | 仓库当前 1100 |
|---|---|---|
| 基础手工程 | FT、DX 各一份 3MF | 同一 3MF 中分别放置 FT、DX 盘 |
| 打印机预设 | P1S，0.4 mm 喷嘴 | P2S，0.4 mm 喷嘴 |
| 腕部飞特适配件外包围尺寸 | 20.5×7×20.5 mm | 20.5×10.5×20.5 mm |
| 底部卷线轮固定孔 | 旧版 5 孔 | 修订为 4 孔 |
| 其他几何 | 早期手指、掌部、腕部和卷线轮 | 官方更新记录列出 28 个修改的 STL |

N-B 的说明写“用 v2”，没有注明基础件修订。骨架、卷线轮和模具按同版配套取用。

### 打印机预设

| 工程 | 文件内保存的机器 | 喷嘴 |
|---|---|---|
| `Prints-1000-FT.3mf` | Bambu Lab P1S | 0.4 mm |
| 当前 `Prints-1100.3mf` | Bambu Lab P2S | 0.4 mm |
| `SiliconeMolds-1100.3mf` | Bambu Lab P2S | 0.4 mm |

学校的 A1、H2D 也可以使用这些模型：在 Bambu Studio 中选择对应机器、喷嘴和打印板，再切片。P2S 是当前 1100 工程保存的预设，不是唯一可用机器。

### N-B 零件几何对比

| N-B 件 | STL 中的特征 | 与舵机仓的配合证据 |
|---|---|---|
| `base-holder` | 直径约 50 mm、厚 5 mm；中心孔约 Ø15；4 个 Ø3.2 通孔，带约 Ø6 沉孔 | 其中一侧两孔的 Y/Z 中心约为 (-10.171,128.435)、(-10.186,153.655)，与 `scs-225-case` 底部两孔一致；另两孔连接另一半仓体 |
| `pin-holder` | 10×18×5.5 mm；两个约 Ø5、伸出 2.5 mm 的定位销，中心距约 10 mm | 单侧销中心约 (-63.093,-14.010)，对应仓体边缘 Ø5 孔；片体跨过两片仓体接缝。仓体共四处配对连接位置，按 4 片准备 |

原厂 `SpoolHolder` 是约 10×113.275×5.5 mm 的长支撑条，形状和安装特征不同。原厂 `FrankaConnector` 约 Ø63×8 mm，孔系也不同。N-B 的两个件是新仓体的连接结构，并非这两个原件的等尺寸复制。

上述结论来自三角网格、截面及原始装配坐标对比，未作为实体装配试验结果。

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
