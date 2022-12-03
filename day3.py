from collections import Counter
import string


def get_sum(chars):
    return sum([(string.ascii_letters.index(char) + 1) for char in chars])


def get_chars_pt1(file):
    content = open(file, 'r').read()
    lines = [[group[:len(group) // 2], group[len(group) // 2:]] for group in content.split("\n")]
    return [(Counter(line[0]) & Counter(line[1]).keys()) for line in lines]


def get_chars_pt2(file):
    content = open(file, 'r').read()
    lines = content.split("\n")
    groups = [lines[i:i + 3] for i in range(0, len(lines), 3)]
    return [(Counter(line[0]) & Counter(line[1]) & Counter(line[2])).keys() for line in groups]


# first part
inters_pt1 = get_chars_pt1("day3.txt")
print(sum([get_sum(chars) for chars in inters_pt1]))

# second part
inters_pt2 = get_chars_pt2("day3.txt")
print(sum([get_sum(chars) for chars in inters_pt2]))
