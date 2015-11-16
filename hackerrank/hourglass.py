"""
https://www.hackerrank.com/challenges/encryption

This one was a very simple array question. Given a pattern, find that pattern inside a bigger array.

I initialise the pattern inside the hour_glass variable. Then I shift it from left to right and top to bottom, add all numbers together and in the end take the biggest one, which will be the biggest hourglass (or pattern) inside the array
"""

hour_glass = [
    [0, 0],
    [0, 1],
    [0, 2],
    [1, 1],
    [2, 0],
    [2, 1],
    [2, 2]
]


def extract_hourglass_at_index(offset_top, offset_left, array):
    # first we need to offset the hourglass to a certain index
    try:
        values = []
        for h in hour_glass:
            # 0 is left, 1 is top
            new_top = h[0] + offset_top
            new_left = h[1] + offset_left
            values.append(int(array[new_top][new_left]))

        return sum(values)
    except Exception:
        return None


def get_input_arr():
    arr = []
    for i in range(0, 6):
        arr.append(input().split(' '))

    return arr



# t = [['1', '1', '1', '0', '0', '0\r'], ['0', '1', '0', '0', '0', '0\r'], ['1', '1', '1', '0', '0', '0\r'], ['0', '9', '2', '-4', '-4', '0\r'], ['0', '0', '0', '-2', '0', '0\r'], ['0', '0', '-1', '-2', '-4', '0\r']]
t = get_input_arr()

m = None
for top in range(0, 4):
    for left in range(0, 4):
        if m is None or extract_hourglass_at_index(top, left, t) > m:
            m = extract_hourglass_at_index(top, left, t)

if m is not None:
    print(m)
