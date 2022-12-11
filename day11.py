from functools import reduce
import copy

class Monkey(object):
    def __init__(self, number, items, op, div_by, if_true, if_false):
        self.number = number
        self.items = items
        self.op = op
        self.div_by = div_by
        self.if_true = if_true
        self.if_false = if_false


def simulate_monkeys(monkeys_inp, range_v, low_worry, max_val):
    monkeys = copy.deepcopy(monkeys_inp)
    monkey_insp = {}

    for round in range(range_v):
        for i, monkey in enumerate(monkeys):
            if i not in monkey_insp:
                monkey_insp[i] = 0
            monkey_insp[i] += len(monkey.items)
            for item in monkey.items:
                worry = inspect_item(item, monkey.op, low_worry, max_val)
                if worry % monkey.div_by == 0:
                    monkeys[monkey.if_true].items.append(worry)
                else:
                    monkeys[monkey.if_false].items.append(worry)
            monkey.items = []
    return monkey_insp


def inspect_item(worry, op, low_worry, f_w):
    res = worry

    if op[1] != 'old':
        res = int(op[1])
    if (op[0]) == '+':
        res += worry
    else:
        res *= worry
    if low_worry:
        res = res // 3
    else:
        res %= f_w
    return res


def parse_monkeys_info(monkeys_lines):
    id = int(monkeys_lines[0].split(' ')[1][0])
    items = [int(val) for val in monkeys_lines[1].split(': ')[1].split(', ')]
    op = monkeys_lines[2].split(' new = old ')[1].split(' ')
    div_by = int(monkeys_lines[3].split('by ')[1])
    if_true = int(monkeys_lines[4].split('to monkey ')[1])
    if_false = int(monkeys_lines[5].split('to monkey ')[1])
    return Monkey(id, items, op, div_by, if_true, if_false)


monkeys = [parse_monkeys_info(gr.split('\n')) for gr in open("day11.txt", 'r').read().split("\n\n")]
max_worry = reduce(lambda x, y: x*y, [x.div_by for x in monkeys])

# part 1
sorts1 = sorted(list(simulate_monkeys(monkeys, 20, True, max_worry).values()))
print(sorts1[-1] * sorts1[-2])

# part 2
sorts2 = sorted(list(simulate_monkeys(monkeys, 10000, False, max_worry).values()))
print(sorts2[-1] * sorts2[-2])