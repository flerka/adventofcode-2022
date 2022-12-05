import re
import copy


def read_initial_lines(file):
    lines = file.readlines()
    cols = zip(*[[[item for item in group[1] if item != ' '] for group in zip(*[iter(line)] * 4)] for line in lines])
    return [[val for val in cl if val][::-1] for cl in cols]


def read_moves_lines(file):
    return [[int(val) for val in re.split('move | from | to ', line) if val] for line in file.read().split('\n')]


columns = read_initial_lines(open("day5_1.txt", 'r'))
moves_lines = read_moves_lines(open("day5_2.txt", 'r'))

# first part
pt1_cl = copy.deepcopy(columns)
[[pt1_cl[c - 1].append(pt1_cl[b - 1].pop()) for _ in range(a)] for a, b, c in moves_lines]
print(''.join(cln.pop()[0] for cln in pt1_cl))

# second part
pt2_cl = copy.deepcopy(columns)
[[pt2_cl[c - 1].append(pt2_cl[b - 1].pop(-(a - i))) for i in range(a)] for a, b, c in moves_lines]
print(''.join(cln.pop()[0] for cln in pt2_cl))
