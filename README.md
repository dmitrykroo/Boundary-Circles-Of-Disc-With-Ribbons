# Boundary Circles Of Disc With Ribbons
To test the program, you can use any online compiler, for example https://ideone.com.
The programming language can be defined by the file extension.

A program that finds boundary circles on a disc with ribbons (also referred to as a "ribbon graph" with 1 vertex and no twisted edges, https://en.wikipedia.org/wiki/Ribbon_graph). Example pictures of such discs with ribbons can be found in "discs.pdf".
The program takes as input a word (string), consisting of lowercase Latin letters, such that each letter occurs in it exactly twice. If input is incorrect, the program outputs **'Incorrect word'**. The program outputs a line of the form **"The number of boundary components is N"**, where **N** is the number of boundary circles found. Complexity of this algorithm is **O(n)**, where **n** stands for length of an input string.

Here are some examples of inputs and outputs. 

**input:** 'abacbc'\
**output:** The number of boundary components is 2

**input:** 'abcabc'\
**output:** The number of boundary components is 2

**input:** an empty string\
**output:** The number of boundary components is 1

**input:** 'abba'\
**output:** The number of boundary components is 3

**input:** 'abacdcbd'\
**output:** The number of boundary components is 1

**input:** 'zxyxyz'\
**output:** The number of boundary components is 2

There is a way to complete this task using BFS (https://en.wikipedia.org/wiki/Breadth-first_search) or other graph traversal algorithms to find the number of connected components of a graph representation of a disc with ribbons. It is used by Dmitry Protasov's solution (protasov.cpp, language C++) and is not used by Dmitry Kroo's solution (kroo.py, language Python). The latter one uses a set of rules, which are used to travel through the string and mark the letters.

The program is created as part of the "Discrete structures and algorithms in topology" course by A.B.Skopenkov at Moscow Institute of Physics and Technology. 
Website of the course: https://www.mccme.ru/circles/oim/home/combtop13.htm
