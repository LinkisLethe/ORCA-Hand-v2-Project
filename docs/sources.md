# 来源与版本

上游提交和引用路径记录在 [sources.json](../sources.json)。源代码与模型使用 Git 子模块保留来源，未把不同版本文件混成一个无出处的目录。

| 来源 | 本项目用途 |
|---|---|
| [官方硬件](https://github.com/orcahand/orcahand_hardware) | v2 base 模型、打印盘和装配补充说明 |
| [官方 BOM 页面](https://www.orcahand.com/bill-of-materials) | 官方 v2 物料基准 |
| [官方 v2 原始 CSV](https://www.orcahand.com/bom/bom-1000.csv) | 原样下载保存，不用 George v1 或 Jack 改版 BOM 替代 |
| [官方控制](https://github.com/orcahand/orca_core) | 控制接口、维护与标定参考 |
| [N-B](https://github.com/N-B-Studio/orca_core) | SCS225 机械适配、驱动和作者配置 |
| [George](https://github.com/George121380/ORCA_Hand_Feetech_Version) | 目录组织与复现流程写法参考，不复制其 v1 模型、BOM 或仿真成果 |
| [SCS225 原厂规格书](https://www.feetechrc.com/Data/feetechrc/upload/file/20211126/6377353179891949627084800.pdf) | 标准 SCS225 的电压、类型 |
| [飞特产品手册](https://www.feetechrc.com/Data/feetechrc/upload/file/20230218/%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C20230217.pdf) | SCS225 的电压范围和位置行程规格 |

## 用户提供的作者回复

- 2026-09-29：作者称使用约 15 元一只的拆机 SCS225，原货源无货，相同外观的可以用
- 2026-10-09：作者称其分享的模型用于替换，其余保持官方 v2

上述是截图中的作者陈述，不是本项目实测。它支持机械替换路线，但不提供拆机件完整后缀、电压铭牌或 STS3215 的软件验证记录。截图不上传到公开 fork。

## 许可

官方硬件根目录 LICENSE 为 CC BY 4.0；官方与 N-B 控制仓库根目录 LICENSE 为 MIT。保留各子模块自己的声明。N-B 适配件保留在原仓库路径中，不另改许可证。官方网页 BOM 保留来源，仅作为复现物料参考，不将其原表宣称为本项目原创。

本仓库新增说明尚未指定单独的开放源代码许可证，整合仓库目前私有；上游材料继续遵循各自许可。
