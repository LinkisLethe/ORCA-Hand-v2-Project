"""获取已固定的源码；不安装依赖，不连接硬件。"""
import argparse
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def git(*args, cwd=ROOT):
    subprocess.run(["git", *args], cwd=cwd, check=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--hardware", action="store_true", help="同时获取官方 v2 base 打印模型")
    args = parser.parse_args()
    manifest = json.loads((ROOT / "sources.json").read_text(encoding="utf-8"))
    for source in manifest["repositories"]:
        path = source["path"]
        if source["kind"] == "hardware":
            if not args.hardware:
                continue
            destination = ROOT / path
            if not (destination / ".git").exists():
                git("clone", "--filter=blob:none", "--sparse", "--no-checkout", source["fork"], path)
            git("sparse-checkout", "set", "orca_v2/base", cwd=destination)
            git("checkout", "--detach", source["commit"], cwd=destination)
            git("submodule", "absorbgitdirs", path)
        else:
            git("submodule", "update", "--init", "--depth", "1", "--", path)
        print(f"Ready: {path}")
    print("完成。未打开串口，未执行舵机动作。")


if __name__ == "__main__":
    main()
