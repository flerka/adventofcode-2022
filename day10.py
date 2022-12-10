def simulate_cycles(lines):
    cycles = {1:1}

    for line in lines:
        cycles[list(cycles.keys())[-1] + 1] = cycles[list(cycles.keys())[-1]]
        if line != 'noop':
            int(line.split(' ')[1])
            cycles[list(cycles.keys())[-1] + 1] = cycles[list(cycles.keys())[-1]] + int(line.split(' ')[1])

    return cycles


def draw_pixels(cycles):
    result = [{}, {}, {}, {}, {}, {}]
    for row_n in range(0, 6, 1):
        for pos_row in range(0, 40, 1):
            cur_cycle = 40 * row_n + pos_row + 1
            if abs(cycles[cur_cycle] - pos_row) <= 1:
                result[row_n][pos_row] = '#'
            else:
                    result[row_n][pos_row] = '.'

    return result


lines = open("day10.txt", 'r').read().split("\n")
sim_res = simulate_cycles(lines)

# part 1
print(sim_res[20]*20 + sim_res[60]*60 + sim_res[100]*100 + sim_res[140]*140 + sim_res[180]*180 + sim_res[220]*220)

# part 2
[print(' '.join(list(row.values()))) for row in draw_pixels(sim_res)]
