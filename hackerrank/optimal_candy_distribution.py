"""
https://www.hackerrank.com/challenges/candies

Another fun DP question that requires a bit of thought.
Basically we have to walk through the array and compare the current students score to the previous one.
If our current one is better, he deserves more candy than the other one so we first check if the child has already more candy than the previous one. If he doesn't, we take the amount of the previous student and add 1 up.

Now since we need to also compare the next student, we walk twice over the array.

I decided to go with reverse() here to re-use my functino without any thought
"""

import math

candies_for_students = []


def loop(arr):
    for i in range(0, len(arr)):
        if len(candies_for_students) < i + 1:
            candies_for_students.append(1)

        # print(candies_for_students)

        if i - 1 >= 0:
            if arr[i - 1] < arr[i]:
                #print("%s is bigger than %s. Setting %s to  %s" % (arr[i], arr[i-1], i, candies_for_students[i - 1] + 1))
                if candies_for_students[i] <= candies_for_students[i-1]:
                    candies_for_students[i] = candies_for_students[i - 1] + 1
                #print("Failed. candy for %s is already higher than candy for %s" % (arr[i], arr[i-1]))
                # print(candies_for_students)


def calculate(students):
    loop(students)
    students.reverse()
    candies_for_students.reverse()
    loop(students)

    return sum(candies_for_students)


def do():
    test_cases = int(input())
    if test_cases >= 1 and test_cases <= math.pow(10, 5):
        students = []
        for i in range(1, test_cases+1):
            rating = int(input())
            if rating >= 1 and rating <= math.pow(10, 5):
                students.append(rating)

        print(calculate(students))


print("-")
print(calculate([2, 4, 2, 6, 1, 7, 8, 9, 2, 1]))
# print(calculate([3,3,2,1]))
# print(calculate([5,4,3,2,1]))
# print(calculate([1,2,2]))
