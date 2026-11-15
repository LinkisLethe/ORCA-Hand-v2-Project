# 打印入口与替换关系

## 官方基础件

运行 `python scripts/setup_sources.py --hardware` 后，官方右手基础版资料位于：

- [整手打印盘 Prints-1100.3mf](../official/orca_v2/base/Prints-1100.3mf)
- [硅胶模具 SiliconeMolds-1100.3mf](../official/orca_v2/base/SiliconeMolds-1100.3mf)
- [手指 STL](../official/orca_v2/base/01_Fingers)
- [手掌 STL](../official/orca_v2/base/02_Carpals)
- [装配补充说明](../official/orca_v2/base/ASSEMBLY_ADDENDUM.md)

当前官方整手 3MF 的第 1 盘为 Dynamixel 塔架，第 2 盘为 Feetech 塔架，其余盘共用。N-B 路线需要替换相关舵机安装件，不能直接把官方 FT 盘全部打印后再额外叠加替换件。

## N-B 件

作者在用户提供的 2026-10-09 评论截图中说明：“就我分享的替换，剩下的不变，用 v2”。这是总体替换原则；并未给每个文件提供逐件装配映射或锁定官方修订。

N-B 模型直接引用其源码子模块，不另复制一套，以免更新后混淆：

| 文件 | 路径 | 当前可确认内容 |
|---|---|---|
| `scs-225-case.stl` | [STL](../../software/orca_core/SCS-225/3D-model/scs-225-case.stl) | SCS225 适配壳 |
| `scs225-case.step` | [STEP](../../software/orca_core/SCS-225/3D-model/scs225-case.step) | 可编辑适配壳模型 |
| `base-holder.stl` | [STL](../../software/orca_core/SCS-225/3D-model/base-holder.stl) | 作者提供的固定件，具体安装位置及数量需结合实物图 |
| `pin-holder.stl` | [STL](../../software/orca_core/SCS-225/3D-model/pin-holder.stl) | 作者提供的固定件，具体安装位置及数量需结合实物图 |
| `ST3215 Servo v2.step` | [STEP](../../software/orca_core/SCS-225/3D-model/ST3215%20Servo%20v2.step) | 舵机外形参考，不能作为 STS 软件已适配的证据 |

参考实物图：[整手](../../software/orca_core/SCS-225/Image/post1.png)、[卷线轮](../../software/orca_core/SCS-225/Image/spool.png)。

打印前先拿所购舵机与适配壳、舵盘和卷线轮试装。外形、孔位、输出轴位置和接口一致时，SCS225/STS3215 可以复用这套机械适配，不需要仅因名字不同重画结构。

当前没有把 STL 自动替换进官方 3MF，也没有声明拼装后的整套打印盘已验证；保留原件和替换件的来源，便于实际试装后明确数量。
