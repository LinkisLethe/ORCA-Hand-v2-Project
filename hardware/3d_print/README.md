# V1000＋N-B 右手打印工程

下载 [ORCA_v1000_NB_Right_P1S.3mf](ORCA_v1000_NB_Right_P1S.3mf)，用 Bambu Studio 打开。

**打印盘就是一次摆在打印平台上的一批零件。** 这个 3MF 文件已经分好 8 盘，通常分 8 批打印，同一块实体打印板可重复使用。

工程采用 P1S / 0.4 mm 喷嘴预设。使用学校 A1、P2S 或 H2D 时，在 Bambu Studio 选择实际机型、喷嘴、材料和打印板后重新切片。

## 每盘打印什么

| 盘号 | 内容 | 数量 | 材料 |
|---:|---|---|---|
| 1 | N-B 舵机仓、底座圆板、双销连接片 | 2＋1＋4 | PLA Basic |
| 2 | 右手掌 R-Carpals、右掌模具芯 CORE-R | 各 1 | PLA Basic |
| 3 | BaseSpool、SpoolCover、Ratchet | 各 16 | PLA Basic |
| 3 | 张紧工具、掌侧/腕侧带轮、A/B 线盖、飞特腕部适配件 | 张紧工具 2，其余各 1 | PLA Basic |
| 4 | PP 成组模具上下半、右掌 A 模 | 各 1 | PLA Basic |
| 5 | 右掌 B 软模 | 1 | TPU，按软模材料配置 |
| 6 | 飞特腕架 WristStructure_Feetech | 1 | PLA Basic |
| 7 | 右手五指骨架 | 16 件 | PLA Basic |
| 8 | DP 成组模具上下半 | 各 1 | PLA Basic |

按本工程打印即可，N-B 替换件和数量已包含。第 3 盘棘轮也是打印件。皮肤用第 4、5、8 盘模具浇注，CORE-R 复用。

## 材料与时间

| 材料 | 模型 | 支撑 | 合计 |
|---|---:|---:|---:|
| PLA | 669.19 g | 37.50 g | 706.69 g |
| TPU | 30.93 g | 0.52 g | 31.45 g |

先准备 **1 kg PLA Basic＋约 40–50 g 软 TPU**。当前切片估算共 51 小时 55 分钟；换机器或参数后，以重新切片的结果为准。

工程中 PLA 对应耗材槽 1，TPU 对应槽 3，槽 2 不使用。打印及硅胶制作步骤见[中文教程](../../docs/tutorial.md#step-03)。

## Reference

<details>
<summary>工程来源与整理记录</summary>

### 来源与版本

- 官方基础文件：[v1000 标签](https://github.com/LinkisLethe/orcahand-hardware/tree/v1000/orca_v2/base)，提交 `a5743dc54612371127ba8503d928ba3a6436c2d8`
- 官方原工程：`Prints-1000-FT.3mf`，一个文件包含 9 盘
- N-B 模型：[SCS-225/3D-model](https://github.com/LinkisLethe/orca-core-nb/tree/9224bd81343ddab9a076b16fae3e885739994ec5/SCS-225/3D-model)

本工程固定 V1000，共 87 个模型实例。原舵机仓已换为 N-B 的 2 片 `scs-225-case`、1 件 `base-holder` 和 4 件 `pin-holder`；删除左手备选、额外卷线轮副本、原仓长支撑条、原版外壳及侧板，补入同版 DP 成组模具。外壳留待核心机构装配后按 N-B 仓体配套。

2026-11-15 已在 Bambu Studio 修复两片 N-B 仓体的网格，并完成 8 盘切片检查；尚未实物打印。官方原文件保留在 `hardware/official/`。

原 3MF 中部分棘轮实例的嵌入几何与零件名称不一致，新工程采用同一 v1000 标签的 `Ratchet.stl` 恢复棘轮几何。其余保留件沿用原盘朝向及局部设置。

### N-B 连接件依据

`base-holder` 是约 Ø50×5 mm 的底座圆板，四个 Ø3.2 安装孔与两侧舵机仓底部配合；`pin-holder` 是带两枚约 Ø5 定位销的连接片，四个连接位置各用一片。用途和数量来自 STL 孔位与装配坐标对比。

官方硬件保留 CC BY 4.0 归属，N-B 模型保留其仓库来源与许可。本项目调整了零件选择、摆盘和工程配置，未声称完成实物装配验证。

</details>
