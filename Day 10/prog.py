adapters = [int(x) for x in open("input")]
d = {k: True for k in adapters}

ones = 0
threes = 0

current = 0
while True:
    if current+1 in d:
        ones += 1
        current += 1
    elif current+3 in d:
        threes += 1
        current += 3
    else:
        break

print("Part 1: ", ones * (threes+1))


def find(index, chain, dp):
    if index in dp:
        return dp[index]

    result = 0
    if index == len(chain) - 1:
        result = 1
    else:
        cur = chain[index]
        for p in [1, 2, 3]:
            if cur + p in chain:
                result += find(chain.index(cur + p), chain, dp)

    dp[index] = result
    return result


adapters += [0, max(adapters)+3]
adapters.sort()
print("Part 2: ", find(0, adapters, {}))
