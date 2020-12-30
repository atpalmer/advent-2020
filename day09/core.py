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

