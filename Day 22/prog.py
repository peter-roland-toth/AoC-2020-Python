import re


def play_normal(p1, p2):
    while len(p1) > 0 and len(p2) > 0:
        t1 = p1.pop(0)
        t2 = p2.pop(0)

        if t1 > t2:
            p1 += [t1, t2]
        else:
            p2 += [t2, t1]

    return p1, p2


def play_sub(p1, p2):
    states = {}

    while len(p1) > 0 and len(p2) > 0:
        # doesn't matter what we return here, important is that the first array is longer than the second one
        if (tuple(p1), tuple(p2)) in states:
            return [1], []

        states[(tuple(p1), tuple(p2))] = True

        t1 = p1.pop(0)
        t2 = p2.pop(0)

        if t1 <= len(p1) and t2 <= len(p2):
            res1, res2 = play_sub(p1[:t1], p2[:t2])
            p1_win = len(res1) > len(res2)
        else:
            p1_win = t1 > t2
        if p1_win:
            p1 += [t1, t2]
        else:
            p2 += [t2, t1]

    return p1, p2


data = []
with open("input") as f:
    for row in f:
        x = re.findall(r'^(\d+)$', row)
        if x:
            data.append(int(x[0]))

p1 = data[:len(data)//2]
p2 = data[len(data)//2:]

r1, r2 = play_normal(p1[:], p2[:])
winner = r2 if len(r1) == 0 else r1

print('Part 1: ', sum([x[0] * x[1] for x in zip(winner, range(len(winner), 0, -1))]))

r1, r2 = play_sub(p1, p2)
winner = r2 if len(r1) == 0 else r1

print('Part 2: ', sum([x[0] * x[1] for x in zip(winner, range(len(winner), 0, -1))]))
