"""
https://www.hackerrank.com/challenges/stockmax

Very similar to the apple stock problem from the interviewcake/ folder but instead of 1 buy and 1 sale, we want the highest profit for any kind of sales.

We again, iterate from back to forth and keep a local_max.

This time, if the new price for the current day is higher than the current local_max (highest value for previous days), we push the existing stocks that have a max sell for the current day into `max_prices`.
Everything in between old max and new max has a max profit with the previous max.

If todays price is smaller than the previous max, just add max-price to the existing stocks array
"""

import math

def calculate_profit(day_prices):
    day_prices = list(map(int, day_prices))
    day_prices.reverse()

    local_max = 0
    local_prices = []
    current_max = 0
    for price in day_prices:
        if price > local_max:
            current_max += sum(local_prices)

            local_prices = []
            local_max = price
            continue

        local_prices.append(local_max - price)

    current_max += sum(local_prices)
    return current_max



test_cases = int(input())
if test_cases <= 10 and test_cases >= 1:
    for i in range(1, test_cases+1):
        vals = int(input())
        days = input()
        days = days.split(' ')
        days = days[0:vals]

        if vals <= 50000 and vals >= 1:
            print(calculate_profit(days))
