def reduce_range(code, lower_marker):
    r = (0, 2**len(code) - 1)
    for c in code[:-1]:
        mid = (r[0] + r[1]) // 2
        r = (r[0], mid) if c == lower_marker else (mid + 1, r[1])

    return r[0] if code[-1] == lower_marker else r[1]


max_id = 0
all_ids = []

with open("input") as f:
    for line in f:
        s = line.strip()
        row = reduce_range(s[:7], "F")
        col = reduce_range(s[7:], "L")

        seat_id = row * 8 + col
        all_ids.append(seat_id)
        max_id = max(max_id, seat_id)

    print("Part 1: ", max_id)
    min_id = max_id
    ids = {}
    for seat_id in all_ids:
        min_id = min(min_id, seat_id)
        ids[seat_id] = True

    for x in range(min_id, max_id):
        if x not in all_ids:
            print('Part 2: ', x)
            break
