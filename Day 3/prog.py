import math


def count_trees(forest, step):
    pos = (0, 0)
    nr_trees = 0

    while pos[1] < len(forest):
        if forest[pos[1]][pos[0] % len(forest[0])] == '#':
            nr_trees += 1

        pos = (pos[0] + step[0], pos[1] + step[1])

    return nr_trees


with open("input") as f:
    forest = []
    for row in f:
        forest.append(row.strip())

    print("Part 1: ", count_trees(forest, (3, 1)))

    to_check = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    print("Part 2: ", math.prod([count_trees(forest, x) for x in to_check]))
