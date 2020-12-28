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


def part2(filepath):
    class Validator(object):
        def __init__(self, data):
            self._data = data

        def is_valid(self):
            REQUIRED_FIELDS = {
                'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid',
                # 'cid',  # optional!
            }
            if data.keys() & REQUIRED_FIELDS != REQUIRED_FIELDS:
                return False
            return all(getattr(self, field)() for field in REQUIRED_FIELDS)

        def byr(self):
            val = self._data.get('byr')
            return val and len(val) == 4 and int(val) >= 1920 and int(val) <= 2002

        def iyr(self):
            val = self._data.get('iyr')
            return val and len(val) == 4 and int(val) >= 2010 and int(val) <= 2020

        def eyr(self):
            val = self._data.get('eyr')
            return val and len(val) == 4 and int(val) >= 2020 and int(val) <= 2030

        def hgt(self):
            val = self._data.get('hgt')
            if not val:
                return None
            match = re.fullmatch(r'(?P<digits>\d+)(?P<units>cm|in)', val)
            if not match:
                return False
            digits = int(match['digits'])
            if match['units'] == 'cm':
                return digits >= 150 and digits <= 193
            if match['units'] == 'in':
                return digits >= 59 and digits <= 76
            assert False

        def hcl(self):
            val = self._data.get('hcl')
            return val and bool(re.fullmatch(r'#[0-9a-fA-F]{6}', val))

        def ecl(self):
            VALID = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
            val = self._data.get('ecl')
            return val and val in VALID

        def pid(self):
            val = self._data.get('pid')
            return val and bool(re.fullmatch(r'\d{9}', val))

        def cid(self):
            return True


    paragraphs = list(file.get_paragraphs(filepath))
    count = 0
    for p in paragraphs:
        data = dict(item.split(':') for item in re.split(r'\s', p) if item)
        if Validator(data).is_valid():
            count += 1
    return count

