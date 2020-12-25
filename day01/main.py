from lib import file


def findpair(items, target):
    haystack=set(items)
    for val in haystack:
        needle = target - val
        if needle in haystack:
            return val, needle


def findtriplet(items, target):
    haystack = set(items)
    for val1 in haystack:
        for val2 in haystack:
            needle = target - val1 - val2
            if needle in haystack:
                return val1, val2, needle


def part1(filepath):
    pair = findpair(
        items=file.get_line_ints(filepath),
        target=2020)
    result = pair[0] * pair[1]
    print(result)


def part2(filepath):
    trip = findtriplet(
        items=file.get_line_ints(filepath),
        target=2020)
    result = trip[0] * trip[1] * trip[2]
    print(result)
