import re
from lib import file


def part1(filepath):
    groups = file.get_paragraphs(filepath)
    total = 0
    for group in groups:
        yes = set()
        for c in group:
            if not re.match(r'[a-z]', c):
                continue
            yes.add(c)
        total += len(yes)
    return total

