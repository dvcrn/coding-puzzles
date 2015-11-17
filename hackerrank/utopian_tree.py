"""
https://www.hackerrank.com/challenges/utopian-tree

Seems like a alternative form of fizzbuzz.
There is a bitwise solution by analyzing the pattern which you should really check out! https://www.hackerrank.com/challenges/utopian-tree/forum

I didn't think about that.

"""


def grow_tree(cycles):
    length = 1
    if cycles == 0:
        return 1

    for i in range(1, cycles+1):
        if i % 2 == 0:
            length += 1
        else:
            length = length*2

    return length


cases = int(input())
if cases <= 10 and cases >= 1:
    for i in range(1, cases+1):
        if i <= 60 and i >= 0:
            cycles = int(input())
            print(grow_tree(cycles))
