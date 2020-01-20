# Given an array of integers, find the first missing positive integer
#   in linear time and constant space. In other words, find the lowest
#   positive integer that does not exist in the array. The array can
#   contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2.
#   The input [1, 2, 0] should give 3.
# You can modify the input array in-place.

# Thoughts:
#   After doing some reading, I've arrived at an idea. I think I need
#   to implement a version of the count_sort algorithm that only
#   considers positive integers


def findMissingPosInteger(arr):
    # find the maximum value in `arr` = O(n)
    maxA = max(arr)

    # add 1 for if lowest decimal is greater than the maximum decimal in the list
    count = [0 for i in range(maxA+1)]

    # store count of each number in `arr` = O(n)
    for a_i in arr:
        if(a_i > 0):
            count[a_i-1] += 1
            # shift indexing down for only positive integers

    return count.index(0) + 1  # account for index shift in final answer


assert findMissingPosInteger([3, 4, -1, 1]) == 2
assert findMissingPosInteger([1, 2, 0]) == 3

li = [i for i in range(23)]
li.remove(13)
assert findMissingPosInteger(li) == 13
