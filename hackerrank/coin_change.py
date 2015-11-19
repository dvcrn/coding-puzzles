"""
https://www.hackerrank.com/challenges/coin-change
How many different ways can you make change for an amount, given a list of coins? In this problem, your code will need to efficiently compute the answer.

This one was a tough nut and I still have problems re-doing it every time.
The main problem is that we can't have duplicate solutions, so [1, 3] is the same as [3, 1]. (It's still 1x 3c coin + 1x 1c coin in either case)

Because of that, we can't just add up all possibilities which really confused me a good amount.

The solution is actually super simple: We construct a list from 0..n where n is the amount we want.
We initialise each of these with 0, except for the first element (which holds the value of 0), which we initialise with 1 as a starting point.
In the next step we iterate from coin..n and increase each list element in between by list[coin-n]. This step is very important!

For 1, can we add a 2 amount coin? No we cant. But since we start at the coin value, we always end up at 0 for the first loop:
2-2 = 0, 0 in our list has the value 1. Increase list[2] by 1. Meaning for value 2 and coins=[2], we have 1 option.

Can we put a 2 coin into 3? yes we can! But doing that means we take the value of list[3-2] = list[1] which is 0. So list[3] += 0 is still 0. Meaning for value 3 and coins[2], we have 0 options.

After we do this for all coins, we end up with a matrix that gives us each amounts option for the coin combination we have. Take the highest and we have our result.
"""


def calculate(amount, denominations):
    denominations = sorted(denominations)

    # Start by creating an empty matrix from 0 - length + 1
    matrix = {}
    for i in range(0, amount + 1):
        matrix[i] = 0

    # Set the first element to 1. Our starting point.
    matrix[0] = 1

    for coin in denominations:
        # Iterate through coin -> amount
        # To find all things that are possible
        for i in range(coin, amount+1):
            # i is the current number
            # print("%s - %s = %s" % (i, coin, (i - coin)))
            # Subtract the coin and add all combinations for that result
            matrix[i] += matrix[i - coin]

    return matrix[amount]


def do():
    info = input()
    info = list(map(int, info.split(' ')))
    amount, denomination_amount = info

    if amount >= 1 and amount <= 250:
        if denomination_amount >= 1 and denomination_amount <= 50:
            denominations = input()
            print(denominations)
            denominations = list(map(int, denominations.strip().split(' ')))
            denominations = denominations[0:denomination_amount]

            print(calculate(amount, denominations))

# do()

print(calculate(10, [3]))
