from collections import defaultdict
import re


# receives a color and recursively finds all the bags which contain this color
# all_colors is a dictionary which will hold the colors found
def find_colors(c, all_colors):
    for color in contained_by[c]:
        all_colors[color] = True
        if color in contained_by:
            find_colors(color, all_colors)


# receives a color and recursively finds the sum of all bags contained by this color
def find_sum(c):
    return sum([x[0] * (find_sum(x[1]) + 1) if x[1] in contains else x[0] for x in contains[c]])


# If the input is "A contains 2 B, 3 C", then `contained_by` will have these entries: B -> [A] and C -> [A],
# while `contains` will have A -> [(2, B), (3, C)]. `contained_by` is used in the first part of the puzzle,
# while `contains` is used in the second
contained_by = defaultdict(list)
contains = defaultdict(list)

with open("input") as f:
    for line in f:
        s = line.split("contain")
        p1 = re.match(r'([a-z ]+) bags', s[0]).groups()[0]
        parts = re.findall(r'(\d+) ([a-z ]+) [bag|bags,. ]+', s[1])
        for bag in parts:
            contained_by[bag[1]].append(p1)
            contains[p1].append((int(bag[0]), bag[1]))

contains_shiny_gold = {}
find_colors("shiny gold", contains_shiny_gold)

print("Part 1: ", len(contains_shiny_gold.keys()))
print("Part 2: ", find_sum("shiny gold"))

