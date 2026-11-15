# N-B 路线打印清单

范围：一只右手基础版、自制硅胶皮肤、N-B 国产舵机安装结构。更新：2026-11-15。

**本页已经排除明确不用的重复件，但整套打印尚未放行。** N-B 没有发布完整装配工程，也没有说明三个改件的全部安装数量和所对应的官方 1000/1100 修订。先取回这些信息，再按本页数量制作；不能把当前 1100 文件称为已确认兼容 N-B。

## 1. 已核实的版本事实

| 文件 | 实际内容 | 本项目处理 |
|---|---|---|
| [v1000 的 Prints-1000-FT.3mf](https://github.com/orcahand/orcahand_hardware/blob/v1000/orca_v2/base/Prints-1000-FT.3mf) | 9 个盘，混有左右手备选、模具和额外卷线轮 | 保留作旧版对照，不整盘全打印 |
| [当前 Prints-1100.3mf](https://github.com/LinkisLethe/orcahand-hardware/blob/0ce26465a4f67c8ab3391cf157853ac24b1fb9c1/orca_v2/base/Prints-1100.3mf) | 10 个盘，DX/FT 两套电机结构、左右手、TPU 皮肤及加工件 | 不能与旧版零件混拼 |
| 1100 第 10 盘 | 名称为 `CNC Parts (FDM NOT RECOMMENDED!!)`；包含 SpoolHolder、SpoolTensioner 和 FrankaConnector | **不要因为存在 STL 就按 PLA 打印；这盘先跳过** |
| [N-B 改件目录](https://github.com/LinkisLethe/orca-core-nb/tree/9224bd81343ddab9a076b16fae3e885739994ec5/SCS-225/3D-model) | 3 个 STL、适配壳 STEP、舵机外形参考 STEP | 按下面替换表使用 |

1000→1100 更新修改了手指、手掌、腕部、卷线轮等 28 个 STL，不只是材质变化。[官方更新记录](https://github.com/orcahand/orcahand_hardware/commit/8b50873a90eab66f7fcb97f8d20cd88ab36c62bc)

当前本地官方子模块仍固定在 1100 来源版本，尚未擅自换为 v1000。确认作者组合之后，应一次性选择同版骨架、卷线轮、五金和模具，而不是逐个凑最新文件。

## 2. N-B 替换件与原件的处理

尺寸来自 STL 外包围盒，单位 mm，用于辨识模型，不等于孔距或装配兼容证明。

| N-B 文件 | 外包围盒 | 当前决定 | 尚缺什么 |
|---|---|---|---|
| `scs-225-case.stl` | 142×34.44×104.6 | 使用这个舵机安装结构；官方 `ForeArmStructure_*` 舵机仓不额外打印 | 整手所需件数、与上方腕架的连接组合 |
| `base-holder.stl` | 5×50×49.99 | 纳入 N-B 套件，不按名字猜成官方 BaseSpool 或 SpoolHolder | 安装位置、件数、紧固件规格 |
| `pin-holder.stl` | 10×18×5.5 | 纳入 N-B 套件；不能直接宣称替代整条官方 SpoolHolder | 安装位置、件数、配合销/螺钉 |
| `scs225-case.step` | 编辑源文件 | 与同名 STL 是同一设计的编辑入口，不重复打印 | 无 |
| `ST3215 Servo v2.step` | 舵机外形参考 | **不打印** | 无 |

N-B 仓库的提交记录与说明没有再提供完整 BOM 或装配数量。照片可辅助辨认，但不足以确定三个件的所有配合关系。[N-B 实拍](https://github.com/LinkisLethe/orca-core-nb/blob/9224bd81343ddab9a076b16fae3e885739994ec5/SCS-225/Image/spool.png)

## 3. 一只右手需要的骨架与驱动件

数量是单手功能用量；文件必须从最后确定的同一修订取用。官方整盘中的额外副本不等于都必须打印。

| 模块 | 文件 / 零件 | 数量 | 取舍 |
|---|---|---:|---|
| 食指 | I-IP、I-PP、I-AP-R | 各 1 | 不取 I-AP-L |
| 中指和无名指 | M-IP、M-PP、M-AP | 各 2 | 两根手指共用这组型号 |
| 小指 | P-IP、P-PP、P-AP | 各 1 | 保留 |
| 拇指 | T-DP、T-PP、右手 T-AP、T-TP-R | 各 1 | 旧版右手 AP 名为 R-T-AP；新版为 T-AP-R，二选一 |
| 手掌 | R-Carpals | 1 | 不打印 L-Carpals |
| 手掌皮肤芯件 | CORE-R | 1 份 | 同时出现在整手盘和模具盘时，只准备一份可复用芯件；不取 CORE-L |
| 手指电机输出 | BaseSpool、SpoolCover、Ratchet | 各 16 | 要先确认 N-B 使用的修订与舵盘固定接口；原盘备件不自动全部复制 |
| 腕部传动 | CarpalsTeeth、WristTeeth | 各 1 | 随最终腕部版本一起选 |
| 腕架及电机适配 | WristStructure_Feetech、WristAdapter_Feetech（旧名 WristAdaper） | 各 1 候选 | 未确认 N-B 腕部组合前暂停打印，不买一套原件再赌能接上 |
| 卷线轮支撑 / 张紧工具 | 官方 SpoolHolder、SpoolTensioner | 原盘 4、2 | 与 N-B 小改件的关系未明，**目前先不打印或采购这组原件** |
| 线盖、外壳、侧板 | CableHolder-A/B、HullFront、HullBack、风扇盖、SidePlate | 按所选结构配套 | N-B 外壳和布线空间未逐件对应，放在最后；不先打 DX/HIVE 板专用壳 |

官方 v1000 第 3 盘有两个对象显示成 `ForeArmStructure_Dynamixel.stl`，但对象的 `source_file` 实际是 `Ratchet.stl`。检查真实模型与来源字段后，它们应计入棘轮，不是需要再打印的两个 DX 舵机仓。

该盘实际为 BaseSpool 18、SpoolCover 18、Ratchet 17，包含超过单手 16 组的额外件；1100 小件盘则各有 20 个。预算紧时先按确定版本做 16 组，备件另选，不把整个盘当成净用量。

## 4. 自制硅胶皮肤的模具

先确认骨架修订，再取其配套模具。以下为**当前 1100 模具工程的最省料复用安排**，只有最后选定该版本时才执行；若作者用 1000，则改取该标签下的 `07_Molds/`，不把下面新模具与旧骨架混用。

| 皮肤位置 | 需要成品 | 同时打印的最小模具 | 说明 |
|---|---:|---|---|
| DP 中号（食指、中指、无名指） | 3 | M-DP 上模 1＋下模 1＋配套夹扣 1 | 同一套浇注 3 次 |
| DP 拇指 | 1 | T-DP 上模 1＋下模 1＋夹扣 1 | 单独型号 |
| DP 小指 | 1 | P-DP 上模 1＋下模 1＋夹扣 1 | 单独型号 |
| PP 中号（中指、无名指） | 2 | M-PP 上模 1＋下模 1＋夹扣 1 | 同一套浇注 2 次 |
| PP 食指、拇指、小指 | 各 1 | I-PP、T-PP、P-PP 各一套上下模和夹扣 | 三种尺寸不混用 |
| 右手掌 | 1 | R-CarpalsMold-A-Funnel、R-CarpalsMold-B-Funnel、CORE-R 各 1 | A/芯件按工程；B 为软 TPU 盘；CORE-R 已列过时不再重复 |
| 浇注辅件 | 复用 | SingleFunnel 1；Cylinder 连接件按实际浇口取用 | 单个模具依次浇注，不默认打印三套 PentaFunnel |

共需要 5 个 DP 皮肤＋5 个 PP 皮肤＋1 个掌部皮肤。这里的 11 件按当前官方 Base 文字清单整理；原 BOM 只写了较粗的皮肤汇总，不能理解成整手只有 6 块皮肤。

1100 模具工程的 PP/DP 盘内副本用于批量生产，单手可复用同款模具。夹扣、上模和下模必须同款，漏斗连接件数以实际选择的单模浇注方式确认，不能擅自省掉必要连接。

## 5. 明确不用先打印的东西

1. 全部左手备选件
2. DX 专用舵机仓、腕部适配、U2D2 固定件
3. 被 N-B `scs-225-case` 替代的官方 HL 舵机仓
4. 直接用 TPU 打印的 DP、PP、掌部皮肤盘——本项目选择液态硅胶浇注
5. `ST3215 Servo v2.step` 舵机外形模型，以及与 STL 重复的 STEP 编辑源
6. 1100 的 `CNC Parts (FDM NOT RECOMMENDED!!)` 整盘
7. Franka 机械臂安装板；本项目先做桌面演示
8. 多余的同款模具、左右手模具、原盘默认备件；只有实际需要并行浇注或备件时才增加

## 6. 给 N-B 作者的一次性确认内容

需要确认：使用的是 `Prints-1000-FT.3mf` 还是 `Prints-1100.3mf`（或可直接提供原始工程）；三个改件分别用几个、替换哪些原件；腕部使用哪个支架/适配件/带轮；BaseSpool、SpoolCover、Ratchet 用哪版，以及舵盘与中心螺钉规格。

拿到原始整套 3MF/装配工程通常比逐个问零件快。此信息未公开，无法仅凭尺寸和照片保证整套兼容。本仓库不会把这些未知项标成“已验证”，也不会用统一缩放或混用五金来掩盖缺口。
