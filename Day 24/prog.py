from collections import defaultdict
import re

rows = [row for row in open("input")]
tiles = defaultdict(bool)
neighbor_mem = {}


def neighbors_of(pos):
    if pos in neighbor_mem:
        return neighbor_mem[pos]

    positions = [(pos[0] + 1, pos[1] + 1), (pos[0] - 1, pos[1] + 1), (pos[0] - 2, pos[1]), (pos[0] + 2, pos[1]),
                 (pos[0] - 1, pos[1] - 1), (pos[0] + 1, pos[1] - 1)]
    neighbor_mem[pos] = positions

    return positions


for r in rows:
    pos = (0, 0)
    f = re.findall(r'se|sw|w|e|nw|ne', r)
    for inst in f:
        if inst == 'se':
            pos = (pos[0] + 1, pos[1] + 1)
        elif inst == 'sw':
            pos = (pos[0] - 1, pos[1] + 1)
        elif inst == 'w':
            pos = (pos[0] - 2, pos[1])
        elif inst == 'e':
            pos = (pos[0] + 2, pos[1])
        elif inst == 'nw':
            pos = (pos[0] - 1, pos[1] - 1)
        elif inst == 'ne':
            pos = (pos[0] + 1, pos[1] - 1)

    tiles[pos] = not tiles[pos]

print("Part 1: ", len([x for x, y in tiles.items() if y]))


for _ in range(100):
    new_tiles = {}
    to_consider = tiles.copy()
    for k in tiles.keys():
        neighbors = neighbors_of(k)
        for n in neighbors:
            if n not in to_consider:
                to_consider[n] = False

    for k, v in to_consider.items():
        neighbors = neighbors_of(k)
        colors = [tiles[x] if x in tiles else False for x in neighbors]
        if v:
            new_tiles[k] = not (colors.count(True) == 0 or colors.count(True) > 2)
        else:
            new_tiles[k] = colors.count(True) == 2

    tiles = new_tiles

print("Part 2: ", len([x for x, y in tiles.items() if y]))
