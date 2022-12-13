import functools


# Based on this https://www.reddit.com/r/adventofcode/comments/zkmyh4/comment/j016dyw/ solution
def compare_pair(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return (left > right) - (right > left)

    if isinstance(left, list) and isinstance(right, int):
        return compare_pair(left, [right])

    if isinstance(left, int) and isinstance(right, list):
        return compare_pair([left], right)

    if len(left) == 0 or len(right) == 0:
        return compare_pair(len(left), len(right))

    return compare_pair(left[0], right[0]) or compare_pair(left[1:], right[1:])


# part 1
groups_1 = [gr.split("\n") for gr in open("day13.txt", 'r').read().split("\n\n")]
data_1 = [[eval(pair, {}, {}) for pair in group] for group in groups_1]
print(sum([i + 1 if compare_pair(d[0], d[1]) == -1 else 0 for i, d in enumerate(data_1)]))

# part 2
input = open("day13.txt").read().split()
input.append("[[2]]")
input.append("[[6]]")
items_2 = [eval(item, {}, {}) for item in input]
items_2.sort(key=functools.cmp_to_key(compare_pair))
print((items_2.index([[2]]) + 1) * (items_2.index([[6]]) + 1))
