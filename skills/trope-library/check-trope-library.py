"""Check source locations and verbatim anchors when adding cards to the library."""
import json
from pathlib import Path
from functools import lru_cache

STACK = Path(__file__).resolve().parents[2]
VIDEOS = STACK.parent / 'docs/materials/videos'
FIELDS = 'episode source anchor trope block beat formula'.split()
SHOWS = {'modern-family': 'M_摩DJ庭_1080P', 'wo-ai-wo-jia': '《我爱我家》全集音频剪辑', 'growing-pains': 'CZ.成长l一lDF恼 id：16551'}


@lru_cache(maxsize=16)
def transcript(path):
    return path.read_text(encoding='utf-8')


def main():
    errors = []
    for show, folder in SHOWS.items():
        library = STACK / 'skills' / (show + '-tropes') / 'cards.jsonl'
        seen = set()
        episodes = set()
        names = set()
        lines = library.read_text(encoding='utf-8').splitlines()
        if not lines:
            errors.append(f'{show}: 空库')
        for n, line in enumerate(lines, 1):
            try:
                card = json.loads(line)
                for field in FIELDS:
                    if not isinstance(card[field], str) or not card[field].strip():
                        raise ValueError('空字段 ' + field)
                path = (VIDEOS / card['source']).resolve()
                if not path.is_relative_to((VIDEOS / folder).resolve()):
                    raise ValueError('出处不属于本剧')
                if card['anchor'] not in transcript(path):
                    raise ValueError('出处找不到连续原句 ' + card['anchor'])
                key = (path, card['trope'], card['anchor'])
                if key in seen:
                    raise ValueError('重复梗卡')
                seen.add(key)
                episodes.add(path)
                names.add(card['trope'])
            except (KeyError, TypeError, OSError, ValueError) as error:
                errors.append(f'{show}:{n} {error}')
        print(f'{show}：{len(seen)} 张，{len(episodes)} 份正片来源，{len(names)} 个梗名')
    if errors:
        raise SystemExit('\n'.join(errors))


if __name__ == '__main__':
    main()
