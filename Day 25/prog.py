a, b = [int(x) for x in open("input")]

divider = 20201227
count, nr = 0, 1

while nr != a:
    count += 1
    nr = (nr * 7) % divider

print("Part 1: ", pow(b, count, divider))
