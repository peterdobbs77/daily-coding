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
#   considers positive integers. But this isn't constant space... :(


def findMissingPosInteger(X):
    # find the maximum value in `X` = O(n)
    maxX = max(X)

    # add 1 for if lowest decimal is greater than the maximum decimal in the list
    count = [0 for i in range(maxX+1)]

    # store count of each number in `arr` = O(n)
    for x_i in X:
        if(x_i > 0):
            count[x_i-1] += 1
            # shift indexing down for only positive integers

    return count.index(0) + 1  # account for index shift in final answer


assert findMissingPosInteger([3, 4, -1, 1]) == 2
assert findMissingPosInteger([1, 2, 0]) == 3

li = [i for i in range(23)]
li.remove(13)
assert findMissingPosInteger(li) == 13
