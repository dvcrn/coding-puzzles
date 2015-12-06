"""
https://leetcode.com/problems/unique-paths/

At first I thought this is a graph problem and tried to solve it with a dfs implementation.
The problem then scaled up the grid and my program couldn't keep up :(

Turns out this is a DP problem:

Imagine we have this grid:
[x, 0, 0]
[0, 0, 0]
[0, 0, *]

What we have to do is iterate (height - 1)*(length - 1) times. With each iteration, we add up

First iteration. Index is 1, we add value at index 0 (1-1)
[1, 2, 1]

Second iteration. Index is 2, we add value at index 1 (2-1)
[1, 2, 3]

Now we are one more field down so we have a handful of new options.
Again, first iteration. Index is 1, we add value at index 0 (1-1)
[1, 3, 3]

Again, second iteration. Index is 2, we add value at index 1 (2-1)
[1, 3, 6]
"""

class Solution(object):
    def uniquePaths(self, m, n):
        if m == 0 or n == 0:
            return 0

        # Create array with n (length) to hold our results
        arr = []
        for i in range(0, n):
            arr.append(1)

        # Iterate over m and n, increase everything that we can add up
        for i in range(1, m): # down
            for j in range(1, n): # right
                arr[j] += arr[j-1]

        return arr[-1]
