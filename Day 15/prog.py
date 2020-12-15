numbers = [int(x) for x in open("input").readline().split(",")]


def play(turns):
    mem = {nr: x+1 for x, nr in enumerate(numbers[:-1])}
    last = numbers[-1]
    for count in range(len(numbers), turns):
        mem[last], last = count, count - mem[last] if last in mem else 0
    return last


print("Part 1: ", play(2020))
print("Part 2: ", play(30000000))
