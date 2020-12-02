import re

count0 = 0
count1 = 0

reg = re.compile(r'(\d+)-(\d+) ([a-z]): ([a-z]+)')

with open("input") as data:
    for d in data:
        g = reg.match(d).groups()
        lo = int(g[0])
        hi = int(g[1])
        c = g[2]
        word = g[3]
        if word.count(c) in range(lo, hi+1):
            count0 += 1

        if (word[lo-1] == c and word[hi-1] != c) or (word[lo-1] != c and word[hi-1] == c):
            count1 += 1

print("Part 1: ", count0)
print("Part 2: ", count1)
