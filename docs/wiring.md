# 通信与供电

接线步骤统一维护在教程中，本页保留 BOM 的引用入口。

- [单舵机连接、共地关系与 17 个 ID 对应表](tutorial.md#step-11)
- [双总线、线束数量和风扇供电](tutorial.md#step-12)
- [实际串口与软件接入](tutorial.md#step-15)

电压和采购决定见 [舵机选型](servo-selection.md)，所需配件见 [中文 BOM](../hardware/bom/feetech-v2-zh.md)。

## 电脑能不能同时供电？

电脑可以作为上位机，通过 USB 给转换板发指令、接收反馈。**舵机电源另接，不能靠普通电脑 USB 驱动整只手。** 普通 USB 通常输出 5 V，而这里的舵机使用 7.4 V 或 12 V 等型号对应电压，17 个电机的负载也不应交给电脑 USB 端口。

```text
电脑 USB ──通信及转换板自身供电──→ FE-URT-2 ──TTL 数据──→ 舵机
外部稳压电源 ──匹配电压的 VCC/GND────────────────────→ 舵机
```

按转换板说明共地，外部电源电压与舵机额定电压匹配。

单舵机试验可先借学校的可调限流直流电源。整手电源按舵机的额定电压和负载电流选配。

## Reference

- [飞特转换板与外部供电说明](https://ftservo.github.io/ftservo-wiki/tools/adapters/)
