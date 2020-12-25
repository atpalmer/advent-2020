

def get_lines(filepath):
    with open(filepath, 'r') as f:
        for line in f:
            yield line.strip()


def get_line_ints(filepath):
    yield from (int(line) for line in get_lines(filepath))

