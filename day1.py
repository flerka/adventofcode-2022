def read_lines(file):
    content = file.read()
    groups = [[int(line) for line in group.split("\n") if line != ""] for group in content.split("\n\n")]
    return sorted([sum(g) for g in groups])


result = read_lines(open("day1.txt", 'r'))

# first task
print(result[-1])

# second task
print(sum(result[-3:]))

