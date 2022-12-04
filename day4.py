def read_lines(file):
    content = file.read()
    return [[line.split("-") for line in group.split(",") if line != ""] for group in content.split("\n")]


def is_full_overlap(line):
    first, second = line[0], line[1]
    if int(second[0]) >= int(first[0]) and int(second[1]) <= int(first[1]):
        return 1
    if int(first[0]) >= int(second[0]) and int(first[1]) <= int(second[1]):
        return 1
    return 0


def is_partial_overlap(line):
    first, second = line[0], line[1]
    if int(first[0]) <= int(second[0]) <= int(first[1]) \
            or (int(first[0]) <= int(second[1]) <= int(first[1])):
        return 1
    if int(second[0]) <= int(first[0]) <= int(second[1]) \
            or (int(second[0]) <= int(first[1]) <= int(second[1])):
        return 1
    return 0


lines = read_lines(open("day4.txt", 'r'))

# first part
print(sum([is_full_overlap(line) for line in lines]))

# second part
print(sum([is_partial_overlap(line) for line in lines]))