import re
from lib import file


PATTERN = re.compile(r'(?P<min>\d+)-(?P<max>\d+) (?P<char>[a-z]): (?P<password>[a-z]+)')


def part1(filepath):
    def fix_match(match):
        return {
            'min': int(match['min']),
            'max': int(match['max']),
            'char': match['char'],
            'password': match['password'],
        }

    def eval_policy(min, max, char, password):
        count = password.count(char)
        return count >= min and count <= max


    def eval_line(line):
        match = PATTERN.fullmatch(line)
        return eval_policy(**fix_match(match))

    lines = file.get_lines(filepath)
    return sum(1 for line in lines if eval_line(line))


def part2(filepath):
    def fix_match(match):
        return {
            'indexes': (int(match['min']) - 1, int(match['max']) - 1),
            'char': match['char'],
            'password': match['password'],
        }

    def eval_policy(indexes, char, password):
        return [password[i] == char for i in indexes]

    def eval_line(line):
        match = PATTERN.fullmatch(line)
        results = iter(eval_policy(**fix_match(match)))
        return any(results) and not any(results)

    lines = file.get_lines(filepath)
    return sum(1 for line in lines if eval_line(line))

