"""Discover project skills for the screenwriting coordinators."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1] / 'skills'


def summary(text):
    lines = text.splitlines()
    if lines and lines[0].strip() == '---' and '---' in lines[1:]:
        header = lines[1:lines.index('---', 1)]
        for i, line in enumerate(header):
            if line.startswith('description:'):
                parts = [line.partition(':')[2].strip().strip('|>+-')]
                for more in header[i + 1:]:
                    if more and not more[0].isspace():
                        break
                    parts.append(more.strip())
                description = ' '.join(' '.join(parts).split()).strip('\"\'')
                if description:
                    return description
    return next((re.sub(r'^#+\s*', '', line) for line in lines if line.startswith('# ')), '请读取正文判断用途')


if __name__ == '__main__':
    for path in sorted(ROOT.rglob('SKILL.md')):
        if path.parent not in (ROOT / 'swarm', ROOT / '群策', ROOT / '找梗'):
            print(f'{path.relative_to(ROOT.parent.parent)}\t{summary(path.read_text(encoding="utf-8-sig"))}')
