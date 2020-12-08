def run(program):
    acc = 0
    ip = 0
    visited = {}
    while True:
        if ip >= len(program):
            return "normal", acc
        if ip in visited:
            return "infinite", acc
        visited[ip] = True

        instruction = program[ip]
        if instruction.startswith("acc"):
            nr = int(instruction.split("acc")[1])
            acc += nr
            ip += 1
        elif instruction.startswith("nop"):
            ip += 1
        elif instruction.startswith("jmp"):
            nr = int(instruction.split("jmp")[1])
            ip += nr


with open("input") as f:
    data = [s.strip() for s in f]

    print("Part 1: ", run(data)[1])

    programs = []
    for i in range(len(data)):
        new_data = data.copy()
        if data[i].startswith("nop"):
            new_data[i] = data[i].replace("nop", "jmp")
        elif data[i].startswith("jmp"):
            new_data[i] = data[i].replace("jmp", "nop")

        programs.append(new_data)

    for p in programs:
        result = run(p)
        if result[0] == "normal":
            print("Part 2: ", result[1])
            break
