def apply_mask_part_1(bitmask, val):
    val = f"{val:>36}".replace(" ", "0")
    return ''.join([bitmask[i] if x != "X" else val[i] for i, x in enumerate(bitmask)])


def apply_mask_part_2(bitmask, val):
    val = f"{val:>36}".replace(" ", "0")
    return ''.join(["X" if x == "X" else x if x == "1" else val[i] for i, x in enumerate(bitmask)])


def addresses_from(bitmask, index):
    if index == len(bitmask):
        return ['']

    results = []
    for r in addresses_from(bitmask, index + 1):
        if bitmask[index] == 'X':
            results.append(r + '1')
            results.append(r + '0')
        else:
            results.append(r + bitmask[index])

    return results


def binary_to_decimal(b):
    return sum([2**(len(b)-i-1) for i, x in enumerate(b) if x == '1'])


def apply(mem, bitmask, address, value):
    updated_mask = apply_mask_part_2(bitmask, address)
    for address in addresses_from(updated_mask, 0):
        mem[binary_to_decimal(address)] = value


data = [x for x in open("input")]

memory_part_1 = {}
memory_part_2 = {}
mask = None

for line in data:
    if line.startswith("mask"):
        mask = line.strip().split(" = ")[1]
    else:
        s = line.strip().split(" = ")
        p1 = int(s[0].split("[")[1].strip("]"))
        p2 = int(s[1])
        memory_part_1[p1] = binary_to_decimal(apply_mask_part_1(mask, "{0:b}".format(p2)))
        apply(memory_part_2, mask, "{0:b}".format(p1), p2)

print("Part 1: ", sum(memory_part_1.values()))
print("Part 2: ", sum(memory_part_2.values()))
