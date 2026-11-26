"""Search curated sitcom cards without opening a transcript or calling a service."""
import argparse
import json
import re
from pathlib import Path

SKILLS = Path(__file__).resolve().parents[1]
SHOWS = ('wo-ai-wo-jia', 'modern-family', 'growing-pains')
FIELDS = ('trope', 'block', 'formula', 'beat', 'episode')
RELATED = (
    ('穿帮', '露馅', '拆穿', '识破', '瞒不住', '揭穿', '圆谎'),
    ('两条线', '双线', '并线', '汇合', '串线', '交汇', '同一件事'),
    ('帮倒忙', '越帮越忙', '好心办坏事', '弄巧成拙', '适得其反'),
    ('回旋镖', '反噬', '反咬', '自食其果', '搬起石头'),
    ('掉马', '暴露身份', '揭开身份', '认出', '身份曝光'),
    ('拖时间', '拖延', '支开', '调虎离山', '争取时间'),
    ('和好', '和解', '道歉', '赔罪', '言归于好'),
)


def card_score(values, terms):
    score = 0
    matched = 0
    for term in terms:
        weight = max((5 - i for i, value in enumerate(values) if term in value), default=0)
        if weight:
            matched += 1
            score += 10 * weight
        elif len(term) >= 4:
            # Keep neighboring characters together when the writer pastes a whole sentence.
            pairs = set(re.findall(r'(?=([一-鿿]{2}))', term))
            for pair in pairs:
                score += max((5 - i for i, value in enumerate(values) if pair in value), default=0)
    return matched, score


def main():
    parser = argparse.ArgumentParser(description='按编剧卡点、梗名、人物或集号查已入库梗卡。空查询浏览各剧卡片。')
    parser.add_argument('show', choices=(*SHOWS, 'all'))
    parser.add_argument('words', nargs='*', help='一个或多个关键词，越多词命中排序越靠前')
    parser.add_argument('--limit', type=int, default=6)
    args = parser.parse_args()
    if args.limit < 1 or any(not word.strip() for word in args.words):
        parser.error('请输入有效关键词，limit 至少为 1')
    terms = list(dict.fromkeys(word.strip().casefold() for word in args.words))
    related = {alias for group in RELATED if any(key in term for term in terms for key in group) for alias in group} - set(terms)
    results = []
    for show in SHOWS if args.show == 'all' else [args.show]:
        source = SKILLS / f'{show}-tropes' / 'cards.jsonl'
        for index, line in enumerate(source.read_text(encoding='utf-8').splitlines(), 1):
            card = json.loads(line)
            values = [card[field].casefold() for field in FIELDS]
            matched, score = card_score(values, terms)
            score += sum(3 for alias in related if any(alias in value for value in values))
            if not terms or score:
                results.append((matched, score, index, show, card))
    results.sort(key=lambda item: (-item[0], -item[1], item[2], item[3]))
    for _, _, index, show, card in results[:args.limit]:
        print(json.dumps({'id': f'{show}:{index}', **card}, ensure_ascii=False))
    if not results:
        print('没有命中。试试更短的动作、关系或后果词，例如「瞒」「误会」「反悔」。')


if __name__ == '__main__':
    main()
