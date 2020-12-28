from lib import file


class TreeMap(object):
    def __init__(self, lines):
        self._lines = tuple(lines)

    def getchar(self, x, y):
        yix = y
        xix = x % len(self._lines[yix])
        return self._lines[yix][xix]

    def is_tree(self, x, y):
        char = self.getchar(x, y)
        assert char in {'#', '.'}
        return char == '#'

    def try_slope(self, *, xstep, ystep):
        assert xstep > 0
        assert ystep > 0
        count = 0
        currx = 0
        for curry in range(0, len(self._lines), ystep):
            if self.is_tree(x=currx, y=curry):
                count += 1
            currx += xstep
        return count


def part1(filepath):
    lines = file.get_lines(filepath)
    treemap = TreeMap(lines)
    return treemap.try_slope(xstep=3, ystep=1)

