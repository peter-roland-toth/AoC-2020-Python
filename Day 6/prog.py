from collections import Counter

count0, count1 = 0, 0
with open("input") as f:
    entries = f.read().strip().split("\n\n")
    for e in entries:
        rows = e.split("\n")
        c = Counter(e.replace("\n", ""))
        count0 += len(c.keys())
        count1 += len([k for k, v in c.items() if v == len(rows)])

print("Part 1: {}\nPart 2: {}".format(count0, count1))
