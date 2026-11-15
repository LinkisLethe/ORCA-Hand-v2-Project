"""检查目录引用、JSON 和固定源码版本，不连接硬件。"""
import json
import re
import subprocess
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]


def main():
    errors = []
    manifest = json.loads((ROOT / "sources.json").read_text(encoding="utf-8"))
    for path in (ROOT / "configs").glob("*.json"):
        json.loads(path.read_text(encoding="utf-8"))
    absent = []
    for item in manifest["repositories"]:
        directory = ROOT / item["path"]
        if not (directory / ".git").exists():
            absent.append(item["path"])
            continue
        head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=directory, text=True).strip()
        if head != item["commit"]:
            errors.append(f"版本不同: {item['path']}: {head}")
    docs = [ROOT / "README.md", *list((ROOT / "docs").glob("*.md")), *list((ROOT / "hardware/bom").glob("*.md")), ROOT / "hardware/3d_print/README.md"]
    for document in docs:
        for target in re.findall(r"\]\(([^)]+)\)", document.read_text(encoding="utf-8")):
            if "://" in target or target.startswith("#"):
                continue
            resolved = (document.parent / unquote(target.split("#")[0])).resolve()
            if any(resolved.is_relative_to(ROOT / path) for path in absent):
                continue
            if not resolved.exists():
                errors.append(f"链接缺失: {document.relative_to(ROOT)} → {target}")
    if errors:
        raise SystemExit("\n".join(errors))
    for path in absent:
        print(f"未下载，跳过对应文件检查: {path}")
    print("检查通过：本地链接、方案 JSON 与已下载源码版本一致；不代表硬件已验证。")


if __name__ == "__main__":
    main()
