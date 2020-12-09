# AoC-2020-Python
Advent of Code 2020 solutions, written in Python.

## Day 1
Went for the brute force approach initially (_O(n^2)_ for the first part, _O(n^3)_ for the second), which works well for the 200 numbers in the input list. Here I added a better solution, where I look for the pair of numbers whose some is equal to 2020 in _O(n)_ time, using a dictionary. This results in _O(n)_ complexity for the first part, and _O(n^2)_ for the second.

## Day 2
Nothing special about this one, used a regex to parse the input and then counted each line that satisfied the rules.

## Day 3
Very simple puzzle, used modulo arithmetic to determine the "invisible" parts of the forest.

## Day 4
Used regexes again to validate some of the fields, however, I messed it up by using _r'[0-9]{9}'_ for the PID (without specifying where the pattern begins and ends), which marked a 10-digit PID as valid. I lost a lot of time debugging this.

## Day 5
Nice and easy problem, solved the second part by iterating through the list of seat IDs twice, first to put them in a dictionary and second to iterate from `min_id` to `max_id` and check which number is not in the dictionary. This way the solution has _O(n)_ complexity. Maybe a more elegant but less efficient way to solve it is to sort the list and then look for a 3-element window where the IDs are not consecutive.

## Day 6
Used `Counters` from the `collections` package for this, which resulted in a really short solution.

## Day 7
Some regex practice again to parse the input, then used `defaultdict` to store the trees defined by the dependencies. To make things easier, I used two trees for the two parts, in the first one if bag A contains bag B then B will be the parent of A, while in the second one A will be the parent of B.

## Day 8
Classic Advent of Code problem involving CPU instructions. In the first part I was detecting an infinite loop by simply storing the visited instruction pointers in a dictionary. For the second part, probably there is a way to determine the instruction which needs to be changed without trial and error, but I was just brute-forcing it by creating and running a new instance of the program by changing each `jmp` to `nop` and vice versa.

## Day 9
Used a dictionary similar to day 1 in order to reduce complexity to _O(n*k)_ from _O(n*k^2)_, where _n_ is the length of the input array and _k_ is the length of the window we need to check (25 in this case). Complexity for part 2 is _O(n^2)_ due to iterating through each number and start building a sum from there until there is a match.
