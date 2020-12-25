

def get_lines(filepath):
    with open(filepath, 'r') as f:
        for line in f:
            yield line.strip()


def get_line_ints(filepath):
    yield from (int(line) for line in get_lines(filepath))


def findpair(items, target):
    haystack=set(items)
    for val in haystack:
        needle = target - val
        if needle in haystack:
            return val, needle


def part1(filepath):
    pair = findpair(
        items=get_line_ints(filepath),
        target=2020)
    result = pair[0] * pair[1]
    print(result)
