from lib import file


def get_col(line):
    result = 0
    coldata = line[7:10]
    for ix, c in enumerate(coldata):
        if c == 'L':
            continue
        assert c == 'R'
        bindig = 2 - ix
        result |= 1 << bindig
    assert result < 8 and result >= 0
    return result


def get_row(line):
    result = 0
    rowdata = line[0:7]
    for ix, c in enumerate(rowdata):
        if c == 'F':
            continue
        assert c == 'B'
        bindig = 6 - ix
        result |= 1 << bindig
    assert result < 128 and result >= 0
    return result


def get_seat_ids(lines):
    for line in lines:
        row = get_row(line)
        col = get_col(line)
        seat_id = row * 8 + col
        yield seat_id


def part1(filepath):
    lines = file.get_lines(filepath)
    return max(get_seat_ids(lines))


def part2(filepath):
    lines = file.get_lines(filepath)
    missing = list()
    last = None
    for id in sorted(get_seat_ids(lines)):
        if last and id != last + 1:
            missing.append(last + 1)
        last = id
    assert len(missing) == 1
    return next(iter(missing))

