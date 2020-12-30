from lib import file


class Instruction(object):
    def __init__(self, op, arg):
        self.op = op
        self.arg = int(arg)

    def change_op(self, op):
        return Instruction(op, self.arg)


class Program(object):
    def __init__(self, prog):
        self.prog = list(prog)
        self.lineptr = 0
        self.accumulator = 0
        self.visited = set()
        self.terminated = False

    def acc(self, arg):
        self.accumulator += arg
        self.lineptr += 1

    def jmp(self, arg):
        self.lineptr += arg

    def nop(self, arg):
        self.lineptr += 1

    def run_next(self):
        if self.lineptr in self.visited:
            return False
        self.visited.add(self.lineptr)
        ins = self.prog[self.lineptr]
        getattr(self, ins.op)(ins.arg)
        return self.lineptr < len(self.prog)

    def run(self):
        while self.run_next():
            pass
        self.terminated = self.lineptr >= len(self.prog)
        return self.accumulator


def part1(filepath):
    prog = Program(Instruction(*line.split(' ')) for line in file.get_lines(filepath))
    return prog.run()


def part2(filepath):
    instructions = [Instruction(*line.split(' ')) for line in file.get_lines(filepath)]
    for i, ins in enumerate(instructions):
        new = list(instructions)
        if ins.op == 'jmp':
            new[i] = new[i].change_op('nop')
        elif ins.op == 'nop':
            new[i] = new[i].change_op('jmp')
        else:
            continue
        prog = Program(new)
        result = prog.run()
        if prog.terminated:
            return result
    assert False, 'Unreachable'

