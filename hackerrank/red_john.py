"""
https://www.hackerrank.com/challenges/red-john-is-back

This was a very interesting problem and required some knowledge about DP beforehand.
Basically we have to do is, we generate all possibilities with each permutation.

A permutation in this case is the amount of 4 blocks we can have. So for 1-3, our permutations are [1].
For 4-7, our permutations are [1,4]
For 8-11, our permutations are [1,4,4] and so on.

To further simplify, we don't actually have to permutate with each 4, we can simply do it once and multiply by the amount of 4s we have. This will greatly increase time.

For primes, I stole a optimized function from SO
"""

bricks_memo = {0: 1, 1: 1, 2: 1, 3: 1, 4: 2}
low_primes = {1:0, 2:1, 3:2, 4:2, 5:3}


def permutate(amount, amount_of_4s=0):
    #print("permutating %s with %s 4s" % (amount, amount_of_4s))
    value = 0
    rest = amount - 1
    value += bricks_memo[rest]

    rest = amount - 4
    value += (bricks_memo[rest] * amount_of_4s)

    return value


def rwh_primes2(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    correction = (n % 6 > 1)
    n = {0: n, 1: n - 1, 2: n + 4, 3: n + 3, 4: n + 2, 5: n + 1}[n % 6]
    sieve = [True] * (n / 3)
    sieve[0] = False
    for i in xrange(int(n**0.5) / 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[((k * k) / 3)::2 * k] = [False] * ((n / 6 -
                                                      (k * k) / 6 - 1) / k + 1)
            sieve[(k * k + 4 * k - 2 * k * (i & 1)) / 3::2 * k] = [False] * (
                (n / 6 - (k * k + 4 * k - 2 * k * (i & 1)) / 6 - 1) / k + 1)
    return len([2, 3] + [3 * i + 1 | 1
                         for i in xrange(1, n / 3 - correction) if sieve[i]])


def calculate(bricks):
    if bricks < 4:
        return low_primes[1]
    if bricks == 4:
        return low_primes[2]

    for i in range(5, bricks + 1):
        amount_of_4s = 1
        bricks_memo[i] = permutate(i, amount_of_4s)

        if i % 4 == 0:
            amount_of_4s += 1

    return rwh_primes2(bricks_memo[bricks] + 1)


def do():
    test_cases = int(input())
    if test_cases >= 1 and test_cases <= 20:
        for i in range(1, test_cases+1):
            val = int(input())
            if val >= 1 and val <= 40:
                print(calculate(val))

#do()

print(calculate(34))
print(calculate(3))
print(calculate(31))
print(calculate(35))
print(calculate(10))
print(calculate(38))
print(calculate(18))
print(calculate(27))
print(calculate(15))
print(calculate(3))
print(calculate(38))
print(calculate(14))
print(calculate(18))
print(calculate(4))
print(calculate(5))
print(calculate(23))
print(calculate(9))
print(calculate(31))
print(calculate(10))
print(calculate(25))
