"""
https://www.interviewcake.com/question/product-of-other-numbers

I got asked this problem in a mock test recently and couldn't figure out how to do this faster than O(n^2).
Turns out this is actually quite simple depending on how you look at it.

If we observe the array and how it reacts when we muliply each other number, we can see that for each element in the array, we usually multiply everything before and everything after that number:

[1,7,|3|,4] = 1*7 (before) * 4 (after)
[1,|7|,3,4] = 1 (before) * 3 * 4 (after)

This observation means that for each number we just have to build this 'chain' of multiplications once and we are good.

To put this in code, for each position we build a 'memo' where each position contains the product of all integers before it:
memo[2] = 1*7 (because that comes before index 2)

This basically means that we just have to iterate twice over the same array and keep multiplying by everything that was 'before' the current position. Once we did that twice, we have all numbers * all numbers except the current index.

All together, we will get O(n) complexity :)

"""


def get_products_of_all_ints(ints):
    memo = {}
    temp = 1
    # iterate over the entire array once
    for position in range(len(ints)):
        print("%s * %s = %s" % (temp, ints[position], (temp*ints[position])))
        # multiply by the current value and save in memo
        memo[position] = temp
        temp *= ints[position]

    print memo

    # do the same thing again, but this time in reverse! ([::-1] reverses the
    # list)
    temp = 1
    for position in range(len(ints))[::-1]:
        print("%s * %s" % (memo[position], temp))
        # this time instead of just setting the memo, we multiply our value to
        # it
        memo[position] *= temp
        temp *= ints[position]

    print memo
    return memo

get_products_of_all_ints([1, 7, 3, 4])
