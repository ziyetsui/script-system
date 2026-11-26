"""在本地《我爱我家》转写中定位场面；标准库、只读。"""
import argparse
import re
from pathlib import Path


ARCHIVE = Path(__file__).resolve().parents[1] / 'references' / 'transcripts'
TITLE = re.compile(r'^「(\d{3})」(.+)\.md$')
SEGMENT = re.compile(r'^\*\*(\d\d:\d\d:\d\d)\s*[–—-]\s*(\d\d:\d\d:\d\d)\*\*\s*(.*)$')


def seconds(clock):
    h, m, s = map(int, clock.split(':'))
    return h * 3600 + m * 60 + s


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('word', nargs='?', help='逐段匹配的原文片段，可省略')
    parser.add_argument('--episode', type=int, help='集号，如 65')
    parser.add_argument('--title', help='篇名片段，匹配上下集')
    parser.add_argument('--at', help='段内时间 HH:MM:SS，需指定集号')
    parser.add_argument('--context', type=int, default=1, help='命中段前后各显示几段')
    parser.add_argument('--limit', type=int, default=3, help='最多显示几处命中')
    parser.add_argument('--root', type=Path, help='迁移技能后可指定转写目录')
    args = parser.parse_args()
    if not (args.word or args.episode or args.title):
        parser.error('请给关键词、集号或篇名')
    if args.at and (not args.episode or not re.fullmatch(r'\d\d:[0-5]\d:[0-5]\d', args.at)):
        parser.error('--at 需要 --episode 和 HH:MM:SS 时间')
    if args.context < 0 or args.limit < 1:
        parser.error('--context 应为非负数，--limit 应大于零')
    root = args.root or ARCHIVE
    if not root.is_dir():
        parser.error('未找到转写目录，请用 --root 指定')
    at = seconds(args.at) if args.at else None
    hits = 0
    for path in sorted(root.glob('「*」*.md')):
        title = TITLE.match(path.name)
        if not title or (args.episode is not None and int(title[1]) != args.episode):
            continue
        if args.title and args.title not in title[2]:
            continue
        rows = []
        for number, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
            seg = SEGMENT.match(line)
            if seg:
                rows.append((number, *seg.groups()))
        for index, (line, start, end, text) in enumerate(rows):
            if args.word and args.word not in text:
                continue
            if at is not None and not seconds(start) <= at < seconds(end):
                continue
            print(f'{path.name}:{line}  {start}–{end}')
            for row in rows[max(0, index-args.context):index+args.context+1]:
                print(f'  {">" if row[0] == line else " "} L{row[0]} {row[1]}–{row[2]}  {row[3]}')
            hits += 1
            if hits >= args.limit:
                return
    if not hits:
        print('没有匹配的时间段。可放宽词语或按集号查看；转写可能有错字。')


if __name__ == '__main__':
    main()
