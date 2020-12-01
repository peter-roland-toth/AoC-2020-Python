def find_two_sum(s, arr):
    d = {}
    for nr in arr:
        if s-nr in d:
            return nr, s-nr
        else:
            d[nr] = True


ints = []


with open("input") as f:
    for i in f:
        ints.append(int(i))

x, y = find_two_sum(2020, ints)
print("Part 1: ", x * y)

# for each number `x` in the array, we are looking for two numbers whose sum is 2020 - x
for i in range(0, len(ints) - 2):
    diff = 2020 - ints[i]
    res = find_two_sum(diff, ints[i+1:])
    if res:
        print("Part 2: ", ints[i] * res[0] * res[1])
        break
