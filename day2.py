def read_lines(file):
    content = file.read()
    return [[line for line in group.split(" ") if line != ""] for group in content.split("\n")]


# score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
def get_numeric_value(value):
    match value:
        case 'A' | 'X':
            return 1
        case 'B' | 'Y':
            return 2
        case 'C' | 'Z':
            return 3


# opponent A for Rock, B for Paper, and C for Scissors
# your response: X for Rock, Y for Paper, and Z for Scissors
# + 6 because you won, + 3 because a draw
def get_result(val):
    match val:
        case ('A', 'Y') | ('B', 'Z') | ('C', 'X'):
            return 6
        case ('A', 'X') | ('B', 'Y') | ('C', 'Z'):
            return 3
    return 0


def get_score(group):
    return get_numeric_value(group[1]) + get_result(group)


# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
def get_group_pt2(group):
    match group:
        case ('A', 'Y'):
            return ['A', 'X']
        case ('B', 'Y'):
            return ['B', 'Y']
        case ('C', 'Y'):
            return ['C', 'Z']
        case ('A', 'Z'):
            return ['A', 'Y']
        case ('B', 'Z'):
            return ['B', 'Z']
        case ('C', 'Z'):
            return ['C', 'X']
        case ('A', 'X'):
            return ['A', 'Z']
        case ('B', 'X'):
            return ['B', 'X']
        case ('C', 'X'):
            return ['C', 'Y']


groups = read_lines(open("day2.txt", 'r'))

# first part
print(sum([get_score(group) for group in groups]))

# second part
print(sum([get_score(get_group_pt2(group)) for group in groups]))