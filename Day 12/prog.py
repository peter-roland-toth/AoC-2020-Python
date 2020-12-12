from collections import namedtuple

Instruction = namedtuple('Instruction', 'direction parameter')

with open("input") as f:
    inst = [Instruction(i[0], int(i[1:])) for i in f]

position_part1 = 0+0j
position_part2 = 0+0j
direction = 1
waypoint = 10 - 1j

for i in inst:
    if i.direction == 'N':
        position_part1 -= i.parameter * 1j
        waypoint -= i.parameter * 1j
    elif i.direction == 'S':
        position_part1 += i.parameter * 1j
        waypoint += i.parameter * 1j
    elif i.direction == 'W':
        position_part1 -= i.parameter
        waypoint -= i.parameter
    elif i.direction == 'E':
        position_part1 += i.parameter
        waypoint += i.parameter
    elif i.direction == 'L':
        for t in range(i.parameter // 90):
            direction *= -1j
            waypoint *= -1j
    elif i.direction == 'R':
        for t in range(i.parameter // 90):
            direction *= 1j
            waypoint *= 1j
    elif i.direction == 'F':
        position_part1 += i.parameter * direction
        position_part2 += i.parameter * waypoint

print("Part 1: ", int(abs(position_part1.real) + abs(position_part1.imag)))
print("Part 2: ", int(abs(position_part2.real) + abs(position_part2.imag)))
