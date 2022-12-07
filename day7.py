class Node(object):
    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.parent = parent
        self.children = []

    def add_child(self, child):
        self.children.append(child)


def get_file_tree(lines):
    tree = Node('root', 0, None)
    current = tree;

    for line in lines:
        parts = line.split(" ")
        match parts:
            case ['$', 'cd', ".."]:
                current = current.parent
            case ['$', 'cd', *rest]:
                n = Node(parts[2], 0, current)
                current.add_child(n)
                current = n
            case ['$', 'ls']:
                continue
            case ['dir', *rest]:
                continue
            case [*rest]:
                current.add_child(Node(parts[1], int(parts[0]), current))

    return tree


def fill_folder_size(tree, result):
    for child in tree.children:
        if child.parent not in result:
            result[child.parent] = 0

        if child.size == 0:
            if child not in result:
                fill_folder_size(child, result)
            result[child.parent] += result[child]
        else:
            result[child.parent] += child.size

    return result


tree = get_file_tree(open("day7.txt", 'r').read().split("\n"))
folder_sizes = fill_folder_size(tree, {})

# part 1
print(sum([v for (_, v) in folder_sizes.items() if v < 100000]))

# part 2
space_to_free = 30000000 - (70000000 - folder_sizes[tree.children[0]])
print(sorted([v for (_, v) in folder_sizes.items() if v >= space_to_free])[0])
