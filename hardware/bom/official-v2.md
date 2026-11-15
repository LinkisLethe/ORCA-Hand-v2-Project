# 官方 ORCA v2 BOM

来源：[官方页面](https://www.orcahand.com/bill-of-materials) · [原始 CSV](https://www.orcahand.com/bom/bom-1000.csv)

下载日期：2026-11-15。原始文件原样保存在 [official-v2-original.csv](official-v2-original.csv)。本页自动提取条目，保留名称、Qty、Spares 和用途；空备件栏表示源表未列。

国产方案使用共用件，并另看 [替换项](substitutions.md)。DX/FT 专用件为二选一。文件名中的 1000 是官网源文件名称，不代表它与当前 1100 CAD 已逐项同步。


## COMMON PARTS  ·  both variants

| 材料 / 规格 | Qty | Spares | 用途 |
|---|---|---|---|
| **3D Printed Parts** | | | |
| All plates (Left or Right) | 1 |  |  |
| **Silicone Skin** | | | |
| Carpals Skin (Black) | 1 |  | Palm |
| Middle Skin (White) | 3 |  | Fingers |
| Thumb Skin (White) | 1 |  | Fingers |
| Pinky Skin (White) | 1 |  | Fingers |
| **Power & Connectivity** | | | |
| USB-C Cable | 1 |  | PC connection (orca_core) |
| **Mechanical Parts** | | | |
| Bearing 6×13×5 | 2 |  | Wrist |
| Bearing 4×8×3 | 55 | 4 | WristAdapter (7), TopSpool (16), Fingers (32) |
| Magnets 3×5 | 16 |  | Hulls |
| GT2 Belt, 142 mm, 6 mm wide | 1 |  | Wrist |
| Pin 4×10 | 1 |  | Wrist |
| Dowel Pin 2×10 | 2 |  | T-AP (2) |
| Dowel Pin 2×8 | 13 |  | AP (8), PP (5) |
| Dowel Pin 2×6 | 12 |  | PP (10) |
| Dowel Pin M3×50 | 2 |  | Wrist |
| Micro PTFE tube, 4 mm dia, flexible, 2 cm | 2 |  | Wrist |
| Washer M4 | 2 | 1 | Wrist |
| Quad Nut M4 | 2 | 1 | Wrist |
| Hex Nut M4 | 3 |  | TopTower (3) |
| Nut M3 | 20 | 2 | Fans, Board, Tower connectors, SpoolHolders |
| Nut M2 | 16 | 4 | BottomSpools (16) |
| Screw M4×20 DIN 912 | 2 |  | Wrist |
| Screw M4×10 DIN 912 | 3 | 1 | TopTower (3) |
| Screw M4×10 DIN 912 | 3 | 1 | Connecting Top & Bottom (3) |
| Screw M3×14 DIN 912 | 6 | 2 | Fan fixation (6) |
| Screw M3×12 DIN 912 | 14 |  | SpoolHolders (4), Cooling Fan (6), Franka (4) |
| Screw M3×8 DIN 912 | 2 | 2 | Connecting Top & Bottom |
| Screw M3×6 DIN 912 | 2 | 1 | Board (2) |
| Screw M2×8 DIN 912 | 20 | 2 | Spools (16), WristSpool (4) |
| Screw M2×4 DIN 912 | 64 | 6 | Spools (64) |
| Robot arm connector plate (CNC) | 1 |  | Franka connector |
| Screw M6×8 low-profile DIN 912 | 4 |  | Franka connector |
| Threaded rod M5×100 | 2 |  | Franka connector |
| Fishing Line Tendon (UHMWPE, 0.39 mm, e.g. WFT 67 kg) | 24 m | 6 m | Fingers (tendons) |

## DYNAMIXEL (DX) VARIANT

| 材料 / 规格 | Qty | Spares | 用途 |
|---|---|---|---|
| **Motors, Boards & Fan** | | | |
| XC430-T240BB-T | 1 |  | Wrist actuator |
| XC330-T288-T | 16 |  | Finger actuator |
| Dynamixel PowerBoard | 1 |  |  |
| U2D2 | 1 |  | USB communication converter |
| Electronic Fan 50×50×10 (90 mm cable, pre-soldered) | 2 |  | Tower |
| Screw M2×8 DIN 912 | 4 |  | Wrist |
| 12V 5A AC Adapter | 1 |  | Power of the orcahand |
| **Motor Connector PCBs** | | | |
| **Cables JST EH 2.5 mm, 3-pin female (EHR-3)** | | | |
| 3XP Cable 180 mm (custom) | 1 | 2 | Circuit Board → Servo |
| 3XP Cable 100 mm | 4 | 2 | Servo daisy chaining |

## FEETECH (FT) VARIANT

| 材料 / 规格 | Qty | Spares | 用途 |
|---|---|---|---|
| **Motors, Boards & Fan** | | | |
| HL-3930-Plastic | 1 |  | Wrist motor (plastic casing) |
| HL-2915-Plastic | 16 |  | Finger motor (plastic casing) |
| Feetech FE-URT-2 (USB-C) | 1 |  | Control board |
| Electronic Fan 50×50×10 (70 mm cable, cables soldered together) | 2 |  | Tower |
| Screw M3×6 DIN 912 | 1 |  | Wrist |
| Screw M3×8 DIN 912 | 4 |  | Wrist |
| 12V 5A AC Adapter | 1 |  | Power of the orcahand |
| **Cables, 3-pin female, AWG 28 — board side = Molex Mini-SPOX 5264, 2.5 mm (UART) · motor side = JST PH, 1.25 mm** | | | |
| 3XP Cable 160 mm (2.5 → 1.25 mm) | 2 | 2 | Circuit Board → Servo |
| 3XP Cable 100 mm (1.25 → 1.25 mm) | 3 | 2 | Finger servo daisy chaining |
| 3XP Cable 100 mm (2.5 → 1.25 mm) | 1 | 2 | Finger → Wrist servo |
| 3XP Cable 50 mm (1.25 → 1.25 mm) | 12 | 4 | Finger servo daisy chaining |
