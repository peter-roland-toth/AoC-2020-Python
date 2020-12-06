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
