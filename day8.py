def is_visible(grid, i, k):
    if is_border(grid, i, k):
        return True

    is_visible_up = True
    # check up
    for up_i in range(i):
        if grid[up_i][k] >= grid[i][k]:
            is_visible_up = False;
            break

    is_visible_left = True
    # check left
    for left_k in range(k):
        if grid[i][left_k] >= grid[i][k]:
            is_visible_left = False;
            break

    is_visible_down = True
    # check down
    for down_i in range(i + 1, len(grid)):
        if grid[down_i][k] >= grid[i][k]:
            is_visible_down = False
            break

    is_visible_right = True
    # check right
    for right_k in range(k + 1, len(grid[0])):
        if grid[i][right_k] >= grid[i][k]:
            is_visible_right = False
            break

    return is_visible_right or is_visible_up or is_visible_down or is_visible_left


def get_viewing_distance(grid, i, k):
    if is_border(grid, i, k):
        return 0
#
    distance_up = 0
    # check up
    for up_i in range(i - 1, -1, -1):
        distance_up += 1
        if grid[up_i][k] >= grid[i][k]:
            break

    distance_left = 0
    # check left
    for left_k in range(k - 1, -1, -1):
        distance_left += 1
        if grid[i][left_k] >= grid[i][k]:
            break

    distance_down = 0
    # check down
    for down_i in range(i + 1, len(grid)):
        distance_down += 1
        if grid[down_i][k] >= grid[i][k]:
            break


    distance_right = 0
    # check right
    for right_k in range(k + 1, len(grid[0])):
        distance_right += 1
        if grid[i][right_k] >= grid[i][k]:
            break

    return distance_right * distance_up * distance_down * distance_left


def is_border(grid, i, k):
    return i == 0 or k == 0 or i == len(grid) - 1 or k == len(grid[0]) - 1


lines = open("day8.txt", 'r').read().split("\n")

# part 1
visible_res = [sum([is_visible(lines, i, k) for k in range(len(lines[0]))]) for i in range(len(lines))]
print(sum(visible_res))

# part 2
distances = [sorted([get_viewing_distance(lines, i, k) for k in range(len(lines[0]))])[-1] for i in range(len(lines))]
print(distances)
print(sorted(distances)[-1])