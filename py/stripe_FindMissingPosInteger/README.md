# findMissingPosInteger

## Prompt

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input `[3, 4, -1, 1]` should give `2`. The input `[1, 2, 0]` should give `3`.

You can modify the input array in-place.

## Implementation

My first pass attempt at this challenge satisfies the "linear time" constraint, but not the "constant space" requirement. A modification to the count_sort algorithm provides a solution in linear time, but requires an additional array for counting the occurences of entries in the input array. So what can we do to fix this issue?