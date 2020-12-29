import re
import string
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


def part2(filepath):
    groups = file.get_paragraphs(filepath)
    total = 0
    for group in groups:
        result = set(c for c in string.ascii_lowercase)
        lines = (line for line in group.splitlines() if line)
        for line in lines:
            chars = set(c for c in line)
            result &= chars
        total += len(result)
    return total

