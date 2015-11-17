"""
https://www.hackerrank.com/challenges/encryption

The description is more or less telling you what to do. I tried to break this problem done in subproblems and created a separate function for each.

I know that this effectively increases complexity because I do unneccessary things but I liked the composing part where you just end up piping data from one function to the next.

Again, this is not optimized.
"""
import math


def calculate_grid(min, max, length):
    if (min*max) >= length:
        return (min, max,)

    if min == max:
        return calculate_grid(min, max+1, length)
    elif min < max:
        return calculate_grid(min+1, max, length)


def get_grid(length):
    min = int(math.floor(math.sqrt(length)))
    max = int(math.ceil(math.sqrt(length)))

    grid_x, grid_y = calculate_grid(min, max, length)

    grid = []
    for _col in range(0, grid_x):
        row = []
        for _row in range(0, grid_y):
            row.append(None)
        grid.append(row)

    return grid


def prepare_string(s):
    s = s.strip()
    s = s.replace(" ", "")
    s = s.split()[0]
    return s


def fill_grid(grid, string):
    rows = len(grid[0])
    columns = len(grid)

    row = 0
    column = 0
    for s in string:
        grid[column][row] = s
        row += 1

        if row > rows-1:
            row = 0
            column += 1

    return grid


def get_vertical(array, index):
    l = len(array)
    out = []
    for i in range(0, l):
        if array[i][index] is None:
            return out

        out.append(array[i][index])

    return out

i = input()
if len(i) <= 81:
    s = prepare_string(i)
    g = get_grid(len(s))
    g = fill_grid(g, s)

    verts = []
    for i in range(0, len(g[0])):
        verts.append(''.join(get_vertical(g, i)))

    print(' '.join(verts))
