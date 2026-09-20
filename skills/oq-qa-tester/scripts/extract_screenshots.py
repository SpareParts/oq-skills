#!/usr/bin/env python3
"""Recover browser screenshots from the Claude Code session transcript.

The claude-in-chrome `save_to_disk` flag is a no-op (anthropics/claude-code#40141):
no file is written, no path returned. But every screenshot/zoom result is persisted
as base64 in the session JSONL — this script lists and extracts those images.

Usage:
  extract_screenshots.py list [--transcript PATH]
  extract_screenshots.py extract IDX [IDX...] --out DIR [--transcript PATH]

Default transcript: the most recently modified *.jsonl for the current project
(~/.claude/projects/<cwd-slug>/), i.e. the running session.
"""

import argparse
import base64
import json
import re
import sys
from pathlib import Path

MEDIA_EXT = {"image/png": "png", "image/jpeg": "jpg", "image/webp": "webp", "image/gif": "gif"}


def default_transcript() -> Path:
    slug = re.sub(r"[^A-Za-z0-9]", "-", str(Path.cwd()))
    project_dir = Path.home() / ".claude" / "projects" / slug
    candidates = sorted(project_dir.glob("*.jsonl"), key=lambda p: p.stat().st_mtime)
    if not candidates:
        sys.exit(f"no transcripts found in {project_dir}")
    return candidates[-1]


def collect_images(transcript: Path) -> list[dict]:
    tool_names: dict[str, str] = {}
    images: list[dict] = []
    with transcript.open() as fh:
        for line in fh:
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            content = (rec.get("message") or {}).get("content")
            if not isinstance(content, list):
                continue
            for block in content:
                if block.get("type") == "tool_use":
                    tool_names[block.get("id", "")] = block.get("name", "?")
                if block.get("type") != "tool_result" or not isinstance(block.get("content"), list):
                    continue
                text = re.sub(r"\s+", " ", " ".join(
                    p.get("text", "") for p in block["content"] if p.get("type") == "text"
                )).strip()
                for part in block["content"]:
                    if part.get("type") != "image":
                        continue
                    src = part.get("source", {})
                    if not src.get("data"):
                        continue
                    images.append({
                        "tool": tool_names.get(block.get("tool_use_id", ""), "?").rsplit("__", 1)[-1],
                        "media_type": src.get("media_type", "image/png"),
                        "data": src["data"],
                        "context": text[:120],
                        "timestamp": rec.get("timestamp", ""),
                    })
    return images


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["list", "extract"])
    parser.add_argument("indices", nargs="*", type=int)
    parser.add_argument("--transcript", type=Path)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()

    transcript = args.transcript or default_transcript()
    images = collect_images(transcript)

    if args.mode == "list":
        print(f"transcript: {transcript}  ({len(images)} images)")
        for i, img in enumerate(images):
            kb = len(img["data"]) * 3 // 4 // 1024
            print(f"{i:3d}  {img['timestamp'][:19]:19s}  {img['tool']:12s} {img['media_type']:10s} {kb:4d}KB  {img['context']}")
        return

    if not args.indices or not args.out:
        parser.error("extract requires IDX... and --out DIR")
    args.out.mkdir(parents=True, exist_ok=True)
    for i in args.indices:
        if not 0 <= i < len(images):
            sys.exit(f"index {i} out of range (0..{len(images) - 1}); run list first")
        img = images[i]
        path = args.out / f"shot-{i}.{MEDIA_EXT.get(img['media_type'], 'png')}"
        path.write_bytes(base64.b64decode(img["data"]))
        print(path)


if __name__ == "__main__":
    main()
