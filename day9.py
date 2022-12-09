def get_head_movement(direction):
    match direction:
        case 'L':
            return [-1, 0]
        case 'R':
            return [1, 0]
        case 'U':
            return [0, -1]
        case 'D':
            return [0, 1]


def sign(number):
    return (number > 0) - (number < 0)


def get_all_tail_moves(movements, knots):
    head_pos = [0, 0]
    rope_pos = [[0, 0] for _ in range(knots)]

    tail_moves = [(0, 0)]

    for line in movements:
        gr = line.split(' ')
        direction = gr[0]
        mov = int(gr[1])

        for _ in range(mov):
            head_mov = get_head_movement(direction)
            head_pos[0] += head_mov[0]
            head_pos[1] += head_mov[1]
            prev_pos = head_pos

            for i in range(len(rope_pos)):
                tail_mov = get_tail_movement(prev_pos, rope_pos[i])
                rope_pos[i][0] += tail_mov[0]
                rope_pos[i][1] += tail_mov[1]

                prev_pos = rope_pos[i]
                if (i == (knots - 1)) and (tail_mov[0] != 0 or tail_mov[1] != 0):
                    tail_moves.append((rope_pos[i][0], rope_pos[i][1]))

    return tail_moves


def get_tail_movement(head_pos, tail_pos):
    h_x, h_y = head_pos
    t_x, t_y = tail_pos

    if h_y == t_y and h_x == t_x:
        return [0, 0]

    if (h_y == t_y and abs(h_x - t_x) == 1)\
            or (h_x == t_x and abs(h_y - t_y) == 1)\
            or (abs(h_y - t_y) == 1 and abs(h_x - t_x) == 1):
        return [0, 0]

    if h_y == t_y and abs(h_x - t_x) > 1:
        return [sign(h_x - t_x), 0]

    if h_x == t_x and abs(h_y - t_y) > 1:
        return [0, sign(h_y - t_y)]

    return [sign(h_x - t_x), sign(h_y - t_y)]


lines = open("day9.txt", 'r').read().split("\n")

# part 1
print(len(set(get_all_tail_moves(lines, 1))))

# part 2
print(len(set(get_all_tail_moves(lines, 9))))
