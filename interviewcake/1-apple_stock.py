"""
https://www.interviewcake.com/question/stock-price

First you might think you need DP for this, but actually we don't. An easier solution is just to walk over the array from back to bottom (aka latest time to earliest).

We take the last element as the local_max, or the highest number we found so far and go next.
If the next value is higher than the current local_max, we replace local_max with the current value, because this is now our highest value available.
If it is not higher, just subtract local_max - amount. Check if that is bigger than the current max_profit we have. If it is, replace the current max_profit with it.

Rinse and repeat.

In the end we have the highest possible profit we can do in O(n) complexity!


"""
def get_max_profit(stock_prices_yesterday):
    stock_prices_yesterday.reverse()
    local_max = 0
    max_value = 0

    for i, amount in enumerate(stock_prices_yesterday):
        if amount > local_max:
            local_max = amount
            continue

        if local_max - amount > max_value:
            max_value = (local_max - amount)

    return max_value

stock_prices_yesterday = [10, 7, 5, 8, 11, 9, -4]
print(get_max_profit(stock_prices_yesterday))
