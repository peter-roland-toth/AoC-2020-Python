with open("input") as f:
    numbers = [int(x) for x in f]

    d = {}
    for i in range(25):
        d[numbers[i]] = True

    for i in range(25, len(numbers)):
        not_found = True
        for n in d:
            if numbers[i] - n in d:
                not_found = False
        if not_found:
            target = numbers[i]
            print("Part 1:", target)
            break
        del d[numbers[i-25]]
        d[numbers[i]] = True

for i in range(0, len(numbers)):
    s = 0
    index = i
    while s < target:
        s += numbers[index]
        index += 1
    if s == target:
        print("Part 2: ", min(numbers[i:index]) + max(numbers[i:index]))
        break
