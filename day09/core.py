from collections import deque
from lib import file


DEFAULT_MAXLEN = 25

MAXLEN = {
    'test.txt': 5,
}


def part1(filepath):
    def has_sum(d, val):
        for item in d:
            target = val - item
            if target in d:
                return True
        return False

    buff = deque(maxlen=MAXLEN.get(filepath, DEFAULT_MAXLEN))
    vals = (int(line) for line in file.get_lines(filepath))
    for val in vals:
        buff.append(val)
        if len(buff) == buff.maxlen:
            break
    for val in vals:
        if not has_sum(buff, val):
            return val
        buff.append(val)
    assert False, 'Unreachable'


def part2(filepath):
    TARGET = 26796446
    vals = [int(line) for line in file.get_lines(filepath)]
    for i in range(len(vals)):
        tmp = []
        tmp.append(vals[i])
        for j in range(i + 1, len(vals)):
            tmp.append(vals[j])
            total = sum(tmp)
            if total == TARGET:
                return max(tmp) + min(tmp)
            if total > TARGET:
                break
    assert False

