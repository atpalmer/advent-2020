import re
from lib import file


class Contained(object):
    def __init__(self, color, count, parent):
        self.color = color
        self.count = int(count)
        self.parent = parent

    @classmethod
    def from_text(cls, text, parent):
        match = re.fullmatch(r'(?P<count>\d+)\s+(?P<color>.+)\s+bags?\s*', text)
        if not match:
            raise ValueError(f'Invalid text: "{text}"')
        return cls(parent=parent, **match.groupdict())

    def __repr__(self):
        return f'<{self.color} {self.count}>'


def create_rules(lines):
    def parse_containstext(containstext, bagcolor):
        if containstext == 'no other bags':
            return []
        else:
            return [Contained.from_text(text, bagcolor) for text in containstext.split(', ')]
    rules = dict()
    for ruletext in lines:
        match = re.fullmatch(f'(?P<bagcolor>.+?)\s+bags contain\s+(?P<containstext>.+)\.' ,ruletext)
        if not match:
            raise ValueError(f'Bad rule text: "{ruletext}"')
        bagcolor = match['bagcolor']
        rules[bagcolor] = parse_containstext(match['containstext'], bagcolor)
    return rules


def part1(filepath):
    def find_parents(color, rules):
        for item in (item for items in rules.values() for item in items):
            if item.color == color:
                yield item.parent

    def find_top_parents(color, rules):
        for parent in find_parents(color, rules):
            yield parent
            yield from find_top_parents(parent, rules)

    rules = create_rules(file.get_lines(filepath))
    parents = set(find_top_parents('shiny gold', rules))
    return len(parents)


def part2(filepath):
    def total_children(color, rules):
        total = 0
        for contained in rules[color]:
            total += contained.count
            total += contained.count * total_children(contained.color, rules)
        return total

    rules = create_rules(file.get_lines(filepath))
    return total_children('shiny gold', rules)

