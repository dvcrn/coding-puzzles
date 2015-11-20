print("Sorting algs in python")

def insertion_sort(items):
    """
    Iterate over the list starting with 1
    Compare the current element to the previous element
    If the current element is smaller, swap it and check the element after it
    """
    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j] < items[j-1]:
            items[j], items[j-1] = items[j-1], items[j]
            j -= 1

test_data = [1, 9, 8, 60, 22, 39, 47, 2, 5, 0, 2, 3, 77, -10]
insertion_sort(test_data)
print(test_data)


def selection_sort(items):
    """
    Iterate over the list twice
    With every sub-iteration, find the lowest number and swap it with the first
    """
    for i in range(0, len(items)):
        local_min = items[i]
        local_min_pos = None
        for j in range(i+1, len(items)):
            if items[j] <= local_min:
                local_min = items[j]
                local_min_pos = j
        # Swap!
        if local_min_pos:
            items[local_min_pos], items[i] = items[i], items[local_min_pos]


test_data = [1, 9, 8, 60, 22, 39, 47, 2, 5, 0, 2, 3, 77, -10]
selection_sort(test_data)
print(test_data)


def bubble_sort(items):
    """
    Recursively go over list. Compare adjacent values and swap if necessary
    """
    for i in range(0, len(items)):
        for j in range(0, len(items) - i - 1):
            if items[j] > items[j+1]:
                items[j+1], items[j] = items[j], items[j+1]


test_data = [1, 9, 8, 60, 22, 39, 47, 2, 5, 0, 2, 3, 77, -10]
bubble_sort(test_data)
print(test_data)


def quicksort(items):
    """
    Take middle
    Re-arrange values into bigger / smaller groups
    Recurse
    """
    if len(items) > 1:
        middle = len(items) // 2
        smaller = []
        bigger = []

        for i, item in enumerate(items):
            if i == middle:
                continue
            if item < items[middle]:
                smaller.append(item)
            else:
                bigger.append(item)

        # recurse
        quicksort(smaller)
        quicksort(bigger)

        items[:] = smaller + [items[middle]] + bigger

test_data = [1, 9, 8, 60, 22, 39, 47, 2, 5, 0, 2, 3, 77, -10]
quicksort(test_data)
print(test_data)


def mergesort(items):
    """
    Similar to quicksort. Find middle, split into equal parts
    Recurse
    Find smallest value from broken sets and merge
    """
    if len(items) > 1:
        middle = len(items) // 2
        left = items[0:middle]
        right = items[middle:]

        mergesort(left)
        mergesort(right)

        lindex, rindex = 0,0
        for i, item in enumerate(items):
            lval = None
            rval = None

            if lindex < len(left):
                lval = left[lindex]

            if rindex < len(right):
                rval = right[rindex]

            # check if we can take from left
            if (rval is None) or ((lval is not None) and (rval is not None) and lval < rval):
                items[i] = lval
                lindex += 1

            # same for right
            if (lval is None) or ((lval is not None) and (rval is not None) and rval <= lval):
                items[i] = rval
                rindex += 1


test_data = [1, 9, 8, 60, 22, 39, 47, 2, 5, 0, 2, 3, 77, -10]
mergesort(test_data)
print(test_data)
