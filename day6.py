def get_marker_index(text):
    vals = list(text[: 3])

    for i, val in enumerate(text[3:]):
        vals.append(val)
        if len(set(vals)) == len(vals):
            return i + 4
        vals.pop(0)


def get_message_index(text):
    vals = list(text[: 13])

    for i, val in enumerate(text[13:]):
        vals.append(val)
        if len(set(vals)) == len(vals):
            return i + 14
        vals.pop(0)


text = open("day6.txt", 'r').read()

# part 1
print(get_marker_index(text))

# part 2
print(get_message_index(text))





