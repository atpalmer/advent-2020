import re
from lib import file


def part1(filepath):
    REQUIRED_FIELDS = {
        'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid',
        # 'cid',  # optional!
    }
    paragraphs = file.get_paragraphs(filepath)
    count = 0
    for p in paragraphs:
        data = dict(item.split(':') for item in re.split(r'\s', p) if item)
        if data.keys() & REQUIRED_FIELDS == REQUIRED_FIELDS:
            count += 1
    return count

