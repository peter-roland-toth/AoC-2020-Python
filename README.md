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

## Day 10
Solved the second part using Dynamic Programming, by memorizing for each adapter in the chain, how many ways are to reach the end of the chain from there.

## Day 12
Used Python's built-in complex numbers to handle changes on the ship's position and direction. Moving can be achieved by adding another complex number, while turning can be done with multiplying by `j` (right) or `-1j` (left).

## Day 14
An easy puzzle with a lot of bit manipulation involved. In the second part I used dynamic programming to generate all the possible memory addresses from the bit masks.

## Day 15
Just used brute force for the second part as it does the job in under a minute.

## Day 22
Nice puzzle, especially the recursive part. Nothing special about the implementation though.

## Day 23
My favorite day so far. Part 1 can be easily solved by using arrays, however the complexity is _O(n*m)_ (n being the length of the chain, m being the number of iterations), since in each iteration we have to find the destination cup, which is _O(n)_ complexity.

This leads us to a better solution for part 2, where _O(n*m)_ would be terrible. Instead of an array, I used a linked list to store the chain, and a dictionary where I stored value -> node pairs. By using a linked list, moving nodes can be done in constant time, while the dictionary helps to locate the destination node also in constant time. This way the algorithm has _O(m)_ complexity, which is still not super fast but it runs in a couple of seconds.

## Day 24
Modelled the hex grid by adding -1 or +1 to the X and Y dimensions to get the NW, NE, SW or SE neighbor of a tile and adding -2 or +2 to the X dimension to get W or E. Then used dictionaries to store the tiles and to memorize the neighbors of each tile.

## Day 25
Nice and easy puzzle to end this edition of Advent of Code :)
