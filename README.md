# AoC-2020-Python
Advent of Code 2020 solutions, written in Python.

## Day 1
Went for the brute force approach initially (_O(n^2)_ for the first part, _O(n^3)_ for the second), which works well for the 200 numbers in the input list. Here I added a better solution, where I look for the pair of numbers whose some is equal to 2020 in _O(n)_ time, using a dictionary. This results in _O(n)_ complexity for the first part, and _O(n^2)_ for the second.
