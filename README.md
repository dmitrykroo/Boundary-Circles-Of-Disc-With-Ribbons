# Boundary Circles Of Disc With Ribbons
A program that finds "boundary circles" on a "disc with ribbons".
The program takes as input a word, consisting of lowercase Latin letters, such that each letter occurs in it exactly twice. If input is incorrect, the program outputs **'Incorrect string'**. The program outputs a line of the form **"The number of boundary components is N"**, where **N** is the number of boundary circles found. Complexity of this algorithm is **O(n)**, where **n** stands for length of an input string.

Here are some examples of inputs and outputs. 

**input:** an empty string\
**output:** The number of boundary components is 1

**input:** 'abba'\
**output:** The number of boundary components is 3

**input:** 'abacdcbd'\
**output:** The number of boundary components is 1

**input:** 'zxyxyz'\
**output:** The number of boundary components is 2

