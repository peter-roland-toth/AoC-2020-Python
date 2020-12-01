def find_two_sum(s, arr):
    # finds two numbers in `arr` whose sum equals to `s`, with O(n) complexity
    lo = 0
    hi = len(arr) - 1
    while lo <= hi and arr[lo] + arr[hi] != s:
        if arr[lo] + arr[hi] < s:
            lo += 1
        else:
            hi -= 1

    if arr[lo] + arr[hi] == s:
        return arr[lo], arr[hi]


ints = []


with open("input") as f:
    for i in f:
        ints.append(int(i))

# sorting the numbers first, which will result in O(n * log(n)) complexity for the
# first part, and O(n^2 * log(n)) for the second part
ints.sort()

x, y = find_two_sum(2020, ints)
print("Part 1: ", x * y)

# for each number `x` in the array, we are looking for two numbers whose sum is 2020 - x
for i in range(0, len(ints) - 2):
    diff = 2020 - ints[i]
    res = find_two_sum(diff, ints[i+1:])
    if res:
        print("Part 2: ", ints[i] * res[0] * res[1])
        break
