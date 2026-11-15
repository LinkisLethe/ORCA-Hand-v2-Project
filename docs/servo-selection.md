# 飞特舵机与电控方案

| 项目 | 当前方案 |
|---|---|
| 舵机 | 飞特 SCS225 / STS3215，具体型号待定 |
| 数量 | 手指 16＋手腕 1，共 17 个 |
| 安装结构 | N-B 改件＋官方 v2 基础结构 |
| 转换板 | FE-URT-2（FE-URT2-C001），TTL 口 |
| 通信布局 | 单舵机试验用 1 块板；整手按 N-B 双总线用 2 块 |
| 供电 | 匹配舵机额定电压的外部直流电源 |
| 上位机 | 电脑，经 USB 发送指令和接收反馈 |

安装和编号见 [教程第 11 节](tutorial.md#step-11)，电源连接见 [供电说明](wiring.md)。本机参数在接线调试时记录。

## Reference

### 电压与驱动资料

标准 SCS225 是 7.4 V 级别；STS3215 有不同电压版本。上位机 USB 负责通信，舵机使用外部电源。两种舵机的驱动和位置换算按各自规格处理，当前代码状态集中在 [软件说明](software.md)。

### 与 Dynamixel 版本的区别

同一机械修订下，手指、手掌、皮肤和基本穿绳大体共用；区别集中在电机周围：

| 部位 | 区别 |
|---|---|
| 舵机仓 | 电机尺寸、固定孔位不同；本项目用 N-B 改件 |
| 舵盘与卷线轮连接 | 输出轴接口、固定螺钉随舵机改变 |
| 腕部支架与适配件 | 官方分别提供 FT / DX 文件 |
| 电控与线束 | DX 用 U2D2 等配套件；本项目用 FE-URT-2 与 TTL 线束 |
| 供电与调试 | 使用具体飞特型号的电压、协议和参数 |

官方 FT 采用 HL 系列；N-B 的 SCS225 安装结构是对应国产舵机的进一步适配。

- [飞特 SCS225 规格书](https://www.feetechrc.com/Data/feetechrc/upload/file/20211126/6377353179891949627084800.pdf)
- [飞特产品手册](https://www.feetechrc.com/Data/feetechrc/upload/file/20230218/%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C20230217.pdf)
- [飞特转换板说明](https://ftservo.github.io/ftservo-wiki/tools/adapters/)
- [官方硬件说明](https://github.com/orcahand/orcahand_hardware)
- [N-B 仓库](https://github.com/N-B-Studio/orca_core)
