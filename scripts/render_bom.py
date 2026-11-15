"""从官方原始 CSV 生成 Markdown 阅读表，保留数量与备件原值。"""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "hardware/bom/official-v2-original.csv"
TARGET = ROOT / "hardware/bom/official-v2.md"


def cell(value):
    return value.replace("|", "\\|").replace("\r", " ").replace("\n", " ")


def main():
    lines = [
        "# 官方 ORCA v2 BOM", "",
        "来源：[官方页面](https://www.orcahand.com/bill-of-materials) · [原始 CSV](https://www.orcahand.com/bom/bom-1000.csv)", "",
        "下载日期：2026-11-15。原始文件原样保存在 [official-v2-original.csv](official-v2-original.csv)。本页自动提取条目，保留名称、Qty、Spares 和用途；空备件栏表示源表未列。", "",
        "国产方案使用共用件，并另看 [替换项](substitutions.md)。DX/FT 专用件为二选一。文件名中的 1000 是官网源文件名称，不代表它与当前 1100 CAD 已逐项同步。", "",
    ]
    with SOURCE.open(encoding="utf-8-sig", newline="") as stream:
        for row in csv.DictReader(stream):
            kind = row["kind"]
            if kind == "section":
                lines.extend(["", "## " + cell(row["component"]), "", "| 材料 / 规格 | Qty | Spares | 用途 |", "|---|---|---|---|"])
            elif kind == "subhead":
                lines.append("| **" + cell(row["component"]) + "** | | | |")
            elif row["component"]:
                lines.append("| " + " | ".join(cell(row.get(k, "")) for k in ("component", "qty", "spares", "used_in")) + " |")
    TARGET.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(TARGET.relative_to(ROOT))


if __name__ == "__main__":
    main()
