#!/usr/bin/env python3
"""
Validate AI Engineering Delivery OS repository structure.

Usage:
  python scripts/validate-structure.py
  python scripts/validate-structure.py /path/to/installed/.ai
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


def load_manifest(root: Path) -> dict:
    manifest_path = root / "manifest.json"
    if not manifest_path.exists():
        raise FileNotFoundError(f"manifest.json not found at {manifest_path}")
    return json.loads(manifest_path.read_text(encoding="utf-8"))


def validate(root: Path) -> int:
    manifest = load_manifest(root)
    required_files = manifest.get("required_files", [])

    missing = []
    empty = []

    for rel in required_files:
        path = root / rel
        if not path.exists():
            missing.append(rel)
            continue
        if path.is_file() and path.name != ".gitkeep" and path.stat().st_size == 0:
            empty.append(rel)

    print(f"AI Engineering Delivery OS structure check")
    print(f"Root: {root}")
    print(f"Version: {manifest.get('version', 'unknown')}")
    print(f"Required files: {len(required_files)}")

    if missing:
        print("\nMissing files:")
        for item in missing:
            print(f"  - {item}")

    if empty:
        print("\nEmpty non-placeholder files:")
        for item in empty:
            print(f"  - {item}")

    if missing or empty:
        print("\nResult: FAIL")
        return 1

    print("\nResult: PASS")
    return 0


def main() -> int:
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd().resolve()
    return validate(root)


if __name__ == "__main__":
    raise SystemExit(main())
