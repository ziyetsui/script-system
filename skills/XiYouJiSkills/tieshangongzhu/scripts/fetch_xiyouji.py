#!/usr/bin/env python3
"""下载《西游记》全文到本 skill 的本地 references 目录。"""

from __future__ import annotations

import argparse
import ssl
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


SKILL_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = SKILL_ROOT / "references" / "full-text" / "xiyouji-gutenberg.txt"

URLS = [
    "https://www.gutenberg.org/files/23962/23962-0.txt",
    "https://www.gutenberg.org/cache/epub/23962/pg23962.txt",
    "https://www.gutenberg.org/ebooks/23962.txt.utf-8",
]


def download(url: str, insecure: bool = False) -> str:
    request = Request(
        url,
        headers={
            "User-Agent": "tieshangongzhu-skill-offline-builder/1.0",
            "Accept": "text/plain,text/*;q=0.9,*/*;q=0.1",
        },
    )
    context = ssl._create_unverified_context() if insecure else None
    with urlopen(request, timeout=60, context=context) as response:
        data = response.read()
    for encoding in ("utf-8-sig", "utf-8", "gb18030"):
        try:
            return data.decode(encoding)
        except UnicodeDecodeError:
            continue
    return data.decode("utf-8", errors="replace")


def main() -> int:
    parser = argparse.ArgumentParser(description="下载 Project Gutenberg 的《西游记》全文。")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="输出文本路径。")
    parser.add_argument("--url", action="append", help="额外或指定下载地址，可重复。")
    parser.add_argument("--insecure", action="store_true", help="跳过 TLS 证书校验；只在本机证书链异常时使用。")
    args = parser.parse_args()

    urls = args.url or URLS
    last_error: Exception | None = None
    for url in urls:
        try:
            text = download(url, insecure=args.insecure)
            if "西遊記" not in text and "西游记" not in text and "Journey to the West" not in text:
                raise ValueError("下载内容不像《西游记》文本")
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(text, encoding="utf-8")
            print(f"已下载：{url}")
            print(f"已保存：{args.output}")
            print(f"字符数：{len(text)}")
            return 0
        except (HTTPError, URLError, TimeoutError, ValueError) as exc:
            last_error = exc
            print(f"下载失败：{url} -> {exc}", file=sys.stderr)

    print(f"全部下载地址失败：{last_error}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
