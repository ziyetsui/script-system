#!/usr/bin/env python3
"""把《西游记》全文切成章回，并抽取唐僧发言候选。"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
FULL_TEXT = SKILL_ROOT / "references" / "full-text" / "xiyouji-gutenberg.txt"
CHAPTER_DIR = SKILL_ROOT / "references" / "full-text" / "chapters"
SOURCE_INDEX = SKILL_ROOT / "references" / "source-index.md"
SPEECH_CORPUS = SKILL_ROOT / "references" / "speech-corpus.jsonl"

CN_NUMERAL = "零〇○一二三四五六七八九十百"
HEADING_RE = re.compile(rf"^[ \t　]*第([{CN_NUMERAL}]+)回[ \t　]*(.*)$", re.MULTILINE)

ALIASES = [
    "三藏法師",
    "三藏法师",
    "唐三藏",
    "唐僧",
    "玄奘",
    "三藏",
    "長老",
    "长老",
    "聖僧",
    "圣僧",
    "御弟",
    "法師",
    "法师",
]

VERBS = [
    "慌忙叫道",
    "高叫道",
    "忙叫道",
    "合掌道",
    "問道",
    "问道",
    "答道",
    "說道",
    "说道",
    "叫道",
    "哭道",
    "拜道",
    "奏道",
    "謝道",
    "谢道",
    "道",
    "曰",
]


@dataclass
class Chapter:
    number: int
    numeral: str
    title: str
    body: str


def chinese_number_to_int(value: str) -> int:
    digits = {"零": 0, "〇": 0, "○": 0, "一": 1, "二": 2, "三": 3, "四": 4, "五": 5, "六": 6, "七": 7, "八": 8, "九": 9}
    if value == "十":
        return 10
    if value == "百":
        return 100
    if "百" in value:
        left, _, right = value.partition("百")
        total = (digits.get(left, 1) if left else 1) * 100
        return total + (chinese_number_to_int(right) if right else 0)
    if "十" in value:
        left, _, right = value.partition("十")
        total = (digits.get(left, 1) if left else 1) * 10
        return total + (digits.get(right, 0) if right else 0)
    total = 0
    for char in value:
        total = total * 10 + digits.get(char, 0)
    return total


def strip_gutenberg_wrapper(text: str) -> str:
    first = re.search(r"^第一回", text, flags=re.MULTILINE)
    if first:
        text = text[first.start() :]
    end = re.search(r"^\*\*\* END OF (?:THE )?PROJECT GUTENBERG", text, flags=re.MULTILINE | re.IGNORECASE)
    if end:
        text = text[: end.start()]
    return text.replace("\r\n", "\n").replace("\r", "\n")


def split_chapters(text: str) -> list[Chapter]:
    text = strip_gutenberg_wrapper(text)
    matches = list(HEADING_RE.finditer(text))
    chapters: list[Chapter] = []
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        numeral = match.group(1)
        number = chinese_number_to_int(numeral)
        title = match.group(2).strip()
        body = text[start:end].strip()
        if not title:
            for line in body.splitlines():
                cleaned = line.strip()
                if cleaned:
                    title = cleaned
                    break
        chapters.append(Chapter(number=number, numeral=numeral, title=title, body=body))
    return chapters


def compact(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def extract_speech(chapter: Chapter) -> list[dict[str, object]]:
    alias_re = "|".join(re.escape(alias) for alias in sorted(ALIASES, key=len, reverse=True))
    verb_re = "|".join(re.escape(verb) for verb in sorted(VERBS, key=len, reverse=True))
    text = re.sub(r"\s+", "", chapter.body)
    speaker_chars = r"[^。！？!?\n；;：:「」『』“”\"]"
    quoted_pattern = re.compile(
        rf"(?P<speaker>{speaker_chars}{{0,24}}(?P<alias>{alias_re}){speaker_chars}{{0,16}}?)"
        rf"(?P<verb>{verb_re})[：:，,]?"
        rf"[「『“\"](?P<quote>[^」』”\"]{{2,260}})[」』”\"]"
    )
    plain_pattern = re.compile(
        rf"(?P<speaker>{speaker_chars}{{0,24}}(?P<alias>{alias_re}){speaker_chars}{{0,16}}?)"
        rf"(?P<verb>{verb_re})[：:，,]?"
        rf"(?P<quote>[^。！？!?「」『』“\"]{{2,180}}[。！？!?])"
    )
    records: list[dict[str, object]] = []
    seen: set[tuple[str, str, int]] = set()
    for pattern in (quoted_pattern, plain_pattern):
        for match in pattern.finditer(text):
            quote = compact(match.group("quote").strip("「」『』“”\"'：:，, "))
            if not quote or len(quote) < 2:
                continue
            key = (match.group("alias"), quote, match.start())
            if key in seen:
                continue
            seen.add(key)
            alias = match.group("alias")
            confidence = "high" if alias in {"唐三藏", "唐僧", "玄奘", "三藏"} else "medium"
            start = max(0, match.start() - 45)
            end = min(len(text), match.end() + 45)
            records.append(
                {
                    "chapter": chapter.number,
                    "chapter_title": chapter.title,
                    "alias": alias,
                    "verb": match.group("verb"),
                    "quote": quote,
                    "speaker_fragment": compact(match.group("speaker")),
                    "confidence": confidence,
                    "context": compact(text[start:end]),
                }
            )
    return records


def write_outputs(chapters: list[Chapter]) -> None:
    CHAPTER_DIR.mkdir(parents=True, exist_ok=True)
    for chapter in chapters:
        path = CHAPTER_DIR / f"{chapter.number:03d}.md"
        path.write_text(f"# 第{chapter.number:03d}回 {chapter.title}\n\n{chapter.body}\n", encoding="utf-8")

    lines = [
        "# 《西游记》本地章回索引",
        "",
        "此文件由 `scripts/build_corpus.py` 生成。分章全文在 `references/full-text/chapters/`。",
        "",
    ]
    for chapter in chapters:
        lines.append(f"- 第{chapter.number:03d}回：{chapter.title} -> `full-text/chapters/{chapter.number:03d}.md`")
    SOURCE_INDEX.write_text("\n".join(lines) + "\n", encoding="utf-8")

    count = 0
    with SPEECH_CORPUS.open("w", encoding="utf-8") as handle:
        for chapter in chapters:
            for record in extract_speech(chapter):
                handle.write(json.dumps(record, ensure_ascii=False) + "\n")
                count += 1
    print(f"章回数：{len(chapters)}")
    print(f"唐僧发言候选：{count}")
    print(f"章回索引：{SOURCE_INDEX}")
    print(f"发言语料：{SPEECH_CORPUS}")
    print(f"分章目录：{CHAPTER_DIR}")


def main() -> int:
    parser = argparse.ArgumentParser(description="构建《西游记》离线章回和唐僧发言候选。")
    parser.add_argument("--input", type=Path, default=FULL_TEXT, help="全文文本路径。")
    args = parser.parse_args()

    if not args.input.exists():
        print(f"找不到全文：{args.input}")
        print("请先运行：python3 scripts/fetch_xiyouji.py")
        return 1
    chapters = split_chapters(args.input.read_text(encoding="utf-8"))
    if len(chapters) < 90:
        print(f"只识别到 {len(chapters)} 回，可能文本格式不对。")
        return 1
    write_outputs(chapters)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
