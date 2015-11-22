"""
https://www.interviewcake.com/question/highest-product-of-3

The 'tricky' part here is that we have to think about negative numbers. Otherwise we could just sort it, take the first 3 and print it, right?

Adding negatives doesn't really make this more complex. Here's why:
What is the only case we have to think about negative numbers? When we have 2, because negative * negative = positive.

So what do we have to check?
Compare num[0] * num[1] to num[last] * num[last-1]. If the first multiplication (a.k.a. the negatives) are bigger than the positives, multiply the negatives * the biggest positive number.
If not, build the product of the last 3 numbers (the positives) and return that

We could probably write this a lot more dynamic.
"""

def highest_product(list_of_ints):
    # sort it first!
    list_of_ints = sorted(list_of_ints)

    # we really only have to care about minus values if we have more than 3 values in general.
    if len(list_of_ints) == 3:
        return list_of_ints[0] * list_of_ints[1] * list_of_ints[2]

    v1 = list_of_ints[0] * list_of_ints[1]
    v2 = list_of_ints[len(list_of_ints) - 1] * list_of_ints[len(list_of_ints) - 2]

    # is the product of the 2 smallest numbers bigger than the product of the 2 biggest numbers?
    if v1 > v2:
        # yup, so return 2 smallest numbers * the biggest number (the last)
        return v1 * list_of_ints[len(list_of_ints) - 1]

    # else just return the 3 biggest numbers
    return v2 * list_of_ints[len(list_of_ints) - 3]

print(highest_product([-10,-10,1,3,2]))
print(highest_product([-10,10,1,3,2]))
