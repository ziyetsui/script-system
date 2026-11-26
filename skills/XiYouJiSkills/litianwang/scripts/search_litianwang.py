#!/usr/bin/env python3
"""离线检索托塔李天王发言候选和《西游记》分章文本。"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
SPEECH_CORPUS = SKILL_ROOT / "references" / "speech-corpus.jsonl"
CHAPTER_DIR = SKILL_ROOT / "references" / "full-text" / "chapters"

VARIANT_FOLD = str.maketrans(
    {
        "師": "师",
        "聖": "圣",
        "孫": "孙",
        "齊": "齐",
        "龍": "龙",
        "馬": "马",
        "溫": "温",
        "黃": "黄",
        "國": "国",
        "門": "门",
        "裡": "里",
        "裏": "里",
        "這": "这",
        "個": "个",
        "說": "说",
        "問": "问",
        "聽": "听",
        "見": "见",
        "來": "来",
        "過": "过",
        "還": "还",
        "與": "与",
        "為": "为",
        "無": "无",
        "沒": "没",
        "難": "难",
        "寶": "宝",
        "風": "风",
        "雲": "云",
        "變": "变",
        "認": "认",
        "樣": "样",
        "眾": "众",
        "歡": "欢",
        "頭": "头",
        "實": "实",
        "處": "处",
        "緊": "紧",
        "兒": "儿",
        "觀": "观",
        "勸": "劝",
        "罷": "罢",
        "鬧": "闹",
        "鐵": "铁",
        "罵": "骂",
        "厲": "厉",
        "長": "长",
        "聲": "声",
        "謝": "谢",
        "禮": "礼",
        "齋": "斋",
        "經": "经",
        "願": "愿",
        "發": "发",
        "惡": "恶",
        "氣": "气",
        "離": "离",
        "擔": "担",
        "淨": "净",
        "薩": "萨",
        "緣": "缘",
        "靈": "灵",
        "臺": "台",
        "覺": "觉",
        "廣": "广",
        "圓": "圆",
        "滿": "满",
        "歸": "归",
        "傳": "传",
        "驚": "惊",
        "將": "将",
        "軍": "军",
        "宮": "宫",
        "亂": "乱",
        "賞": "赏",
        "罰": "罚",
        "祿": "禄",
        "職": "职",
        "詔": "诏",
        "籙": "箓",
        "萬": "万",
        "從": "从",
        "寬": "宽",
        "壇": "坛",
        "會": "会",
        "潑": "泼",
        "欽": "钦",
        "雙": "双",
        "臂": "臂",
        "劍": "剑",
        "縛": "缚",
        "輪": "轮",
        "鏡": "镜",
        "羅": "罗",
        "網": "网",
        "帥": "帅",
    }
)


def load_records() -> list[dict[str, object]]:
    if not SPEECH_CORPUS.exists():
        return []
    records: list[dict[str, object]] = []
    with SPEECH_CORPUS.open(encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def normalize(value: str) -> str:
    return re.sub(r"\s+", "", value).translate(VARIANT_FOLD)


def record_matches(record: dict[str, object], query: str, chapter: int | None) -> bool:
    if chapter is not None and int(record.get("chapter", -1)) != chapter:
        return False
    if not query:
        return True
    needle = normalize(query)
    haystack = normalize(" ".join(str(record.get(key, "")) for key in ("quote", "context", "chapter_title", "alias")))
    return needle in haystack


def search_chapter_text(query: str, chapter: int | None, limit: int) -> list[str]:
    if not CHAPTER_DIR.exists() or not query:
        return []
    paths = [CHAPTER_DIR / f"{chapter:03d}.md"] if chapter else sorted(CHAPTER_DIR.glob("*.md"))
    hits: list[str] = []
    for path in paths:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        normalized = normalize(text)
        needle = normalize(query)
        index = normalized.find(needle)
        if index < 0:
            continue
        title = text.splitlines()[0].lstrip("# ").strip() if text.splitlines() else path.stem
        raw_index = text.find(query)
        if raw_index < 0:
            raw_index = 0
        excerpt = re.sub(r"\s+", " ", text[max(0, raw_index - 80) : raw_index + 180]).strip()
        hits.append(f"{title}\n  ...{excerpt}...")
        if len(hits) >= limit:
            break
    return hits


def main() -> int:
    parser = argparse.ArgumentParser(description="离线搜索托塔李天王发言候选。")
    parser.add_argument("query", nargs="?", default="", help="关键词；不填则按章回列出候选。")
    parser.add_argument("--chapter", type=int, help="限定第几回。")
    parser.add_argument("--limit", type=int, default=10, help="最多输出多少条。")
    args = parser.parse_args()

    records = load_records()
    matches = [record for record in records if record_matches(record, args.query, args.chapter)]
    if matches:
        for record in matches[: args.limit]:
            print(f"第{int(record['chapter']):03d}回 {record.get('chapter_title', '')}")
            print(f"  称呼/动词：{record.get('alias')} {record.get('verb')}，置信度：{record.get('confidence')}")
            print(f"  候选发言：{record.get('quote')}")
            print(f"  上下文：{record.get('context')}")
            print()
        return 0

    hits = search_chapter_text(args.query, args.chapter, args.limit)
    if hits:
        for hit in hits:
            print(hit)
            print()
        return 0

    if not SPEECH_CORPUS.exists():
        print("还没有本地发言语料。请先运行：")
        print("  python3 scripts/fetch_xiyouji.py")
        print("  python3 scripts/build_corpus.py")
    else:
        print("没有找到匹配结果。")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
