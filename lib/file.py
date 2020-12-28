

def get_lines(filepath):
    with open(filepath, 'r') as f:
        for line in f:
            yield line.strip()


def get_line_ints(filepath):
    yield from (int(line) for line in get_lines(filepath))


def get_paragraphs(filepath):
    result = ''
    with open(filepath, 'r') as f:
        for line in f:
            if line.strip() == '':
                yield result
                result = ''
            result += line
    if result:
        yield result

