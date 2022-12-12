import string


def get_path(data, start_p, end_p):
    explored = []

    queue = [[start_p]]
    if start_p == end_p:
        return

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in explored:
            neighbours = get_neighbors(data, node)
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                if neighbour == end_p:
                    return len(new_path) - 1

            explored.append(node)

    return


def get_neighbors(data, point):
    y, x = point
    neighbors = [(y, x + 1), (y, x - 1), (y + 1, x), (y - 1, x)]
    neighbors = [n for n in neighbors if 0 <= n[0] < len(data) and 0 <= n[1] < len(data[0])]
    return [n for n in neighbors if
            (string.ascii_letters.index(data[n[0]][n[1]].lower()) - string.ascii_letters.index(
                data[y][x].lower())) <= 1]


lines = [list(line) for line in open("day12.txt", 'r').read().split("\n")]
start, end = (), ()
all_a = []

for i, line in enumerate(lines):
    for k, char in enumerate(line):
        if char == 'E':
            end = (i, k)
        if char == 'S':
            start = (i, k)
            all_a.append(start)
        if char == 'a':
            all_a.append((i, k))

lines[start[0]][start[1]] = 'a'
lines[end[0]][end[1]] = 'z'

# part 1
print(get_path(lines, start, end))

# part 2
print(len(all_a))
p2_res = []
for i, a in enumerate(all_a):
    val = get_path(lines, a, end)
    if val is not None:
        p2_res.append(val)
print(min(p2_res))
