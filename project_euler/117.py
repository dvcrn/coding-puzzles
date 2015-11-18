"""
https://projecteuler.net/problem=117
(And related: https://www.hackerrank.com/challenges/euler117)
Using a combination of black square tiles and oblong tiles chosen from: red tiles measuring two units, green tiles measuring three units, and blue tiles measuring four units, it is possible to tile a row measuring five units in length in exactly fifteen different ways.

How many ways can a row measuring fifty units in length be tiled?

---

To solve this with DP, we iterate from 0..n (where n is the value we want) and then through each tile we have available.
For each tile we calculate all possibilities we have for it.
So given length 5 and tiles [1,2,3,4] (1 is the black one, or 'base length') we do:
5-1 = 4. What are the possibilities we have for filling up the space 4? Luckily we use dp so we can just use the previous result :)


Why am I using Decimals and this weird modulo here?
The hackerrank challenge required you to calculate for a value up to 10^18! There is no way we can do this without Decimals.
Even with Decimals, the hackerrank challenge specifically wanted you to find a solution under 8s with O(log n) complexity, which I wasn't able to find.

---

I later found out that the number sequence here is tetranacci. So we wouldn't even need to iterate through all the tiles - all we have to do is remember the past 4 numbers and summerize them with each iteration.

There is a way to calculate tetranacci with O(log n). I might come back to this one at some point and try that.

"""


import math
from decimal import Decimal

m = Decimal(int(math.pow(10, 9) + 7))


def calculate(length):
    max_possibilities_for_space = {
        0: Decimal(0),
        1: Decimal(1),
        2: Decimal(2),
        3: Decimal(4),
        4: Decimal(8),
        5: Decimal(15),
    }

    if length <= 5:
        return max_possibilities_for_space[length]

    tiles = [1, 2, 3, 4]

    for length_unit in range(6, length+1):
        max_possibilities = 0
        for tile in tiles:
            r = length_unit - tile
            if r >= 0:
                max_possibilities += max_possibilities_for_space[r]
        max_possibilities_for_space[length_unit] = (max_possibilities % m)

    return max_possibilities_for_space[length]


def do():
    test_cases = int(input())

    if test_cases >= 1 and test_cases <= 1000:
        for i in range(1, test_cases+1):
            try:
                n = int(input())

                if n >= 1 and n <= math.pow(10, 18):
                    print(calculate(n))
            except Exception:
                continue
#do()
# for i in range(-1000, 1000):
#     if i >= 1 and i <= math.pow(10, 18):
#         print(calculate(i))

print(calculate(50))
