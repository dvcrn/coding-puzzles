"""
https://www.hackerrank.com/challenges/unbounded-knapsack/

The sad thing about knapsack is that once you solved it, you can solve it again very easily. On hackerrank, someone didn't understand the editorial solution so I wrote one myself. Here's what I wrote:

Here's the 'David' explanation:
To solve this problem, we break it up into sub-problems in the fashion of DP: If we want to know the highest result we can form for 10 and options [3,8] we would do it like this:

_(To make this a bit easier, imagine 10 is a jar with the size of 10 and [3,8] are marbles that you want to put into that jar. You want to make the jar as full as possible.)_

First we break it down for 1:

```
1. With a jar of size 1, can we put 3 in? no.
2. With a jar of size 1, can we put 8 in? no.
```

So we remember at a notepad:
```
Jar with size 1 has max marbles volume: 0
```

We repeat that until we are at 10 which is our maximum value.

2 is the same as 1, so we skip that for the sake of this examle, but for 3:
```
1. With a jar of size 3, can we put 3 in? Yes!
1.1 If we put 3 in, how much space do we have left? 0
1.2 How can we fill 0 space? We can't because it's 0.

2. With a jar of size 3, can we put 8 in? No.
```
Our 'notepad' looks like this now:
```
Jar with size 1 has max marbles volume: 0
Jar with size 2 has max marbles volume: 0
Jar with size 3 has max marbles volume: 3
```


Let's again, skip 4 and 5 because they are the same.

```
1. With a jar of size 6, can we put 3 in? Yes!
1.1. If we put 3 in, how much space do we have left? 3.
1.2. How can we fill 3 spaces? We look at our notepad!
1.3. 1x 3 marble + the maximum value we can form with the leftover space (which is 3) = 3+3 = 6.
```

```
Jar with size 1 has max marbles volume: 0
Jar with size 2 has max marbles volume: 0
(...)
Jar with size 6 has max marbles volume: 6
```

Let's look at 10!
```
1. With a jar of size 10, can we put 3 in? Yes!
1.1. If we put 3 in, how much space do we have left? 7.
1.2. How can we fill 7 spaces? We look at our notepad!
1.3. 1x 3 marble + the maximum value we can form with the leftover space 7 (which is 6) = 3+6 = 9

Remember 9

2. With a jar of size 10, can we put 8 in? Yes!
2.1. If we put 8 in, how much space do we have left? 2.
2.2. How can we fill 2 spaces? We look at our notepad!
.2.3 1x 8 marble + the max of the leftover space 2 (which is 0) = 8+0 = 8

Is 8 bigger than the other option we have (9)? No it's not.
We don't have any other options so let's write 9 into our notepad :)
```
"""
max_value_for_i = {0: 0}

def knapsack(highest_sum, options):
    for i in range(1, highest_sum+1):
        local_max = 0
        for option in options:
            if i - option >= 0:
                if local_max < (option + max_value_for_i[i - option]) and (option + max_value_for_i[i-option] <= highest_sum):
                    # take it!
                    local_max = (option + max_value_for_i[i-option])

        max_value_for_i[i] = local_max

    return max_value_for_i[highest_sum]

#print(knapsack(9, [3,4,4,4,8]))

def do():
    test_cases = int(input())
    if test_cases >= 1 and test_cases <= 10:
        for i in range(1, test_cases+1):
            n, k = input().strip().split(' ')
            options = input().strip().split(' ')

            n,k = list(map(int, [n,k]))

            if n >= 1 and n <= 2000:
                if k >= 1 and k <= 2000:
                    options = list(map(int, options[0:n]))
                    print(knapsack(k, options))

do()
