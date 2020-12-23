class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def play_game(s, rounds, extend=None):
    d = list(map(int, s))
    if extend:
        d += list(range(10, extend + 1))

    max_nr = max(d)

    mem = {}
    prev = None
    for i in d:
        n = Node(i)
        if prev:
            prev.next = n
        mem[i] = n
        prev = n
    prev.next = mem[d[0]]

    current = mem[d[0]]
    for _ in range(rounds):
        pick_up = current.next
        excluded = [pick_up.val, pick_up.next.val, pick_up.next.next.val]
        # this is the node after the group of 3 we need to move away
        after_pick_up = current.next.next.next.next

        destination = current.val - 1
        while destination in excluded:
            destination -= 1
        if destination < 1:
            destination = max_nr
            while destination in excluded:
                destination -= 1

        # inserting the group of the after the destination node
        destination_node = mem[destination]
        temp = destination_node.next
        destination_node.next = pick_up
        pick_up.next.next.next = temp
        # current node's next node becomes the one which was after the group of 3
        current.next = after_pick_up
        current = current.next

    return mem[1]


input_string = "589174263"

one_node = play_game(input_string, 100)
curr = one_node.next
result = ""
while curr.val != 1:
    result += str(curr.val)
    curr = curr.next

print("Part 1: ", result)

one_node = play_game(input_string, 10000000, 1000000)

x1 = one_node.next.val
x2 = one_node.next.next.val
print("Part 2: ", x1 * x2)
