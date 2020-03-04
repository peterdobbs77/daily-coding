# Elevation Map - Water Volume

## Prompt

This problem was asked by Facebook.

You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

For example, given the input `[2, 1, 2]`, we can hold `1` unit of water in the middle.

Given the input `[3, 0, 1, 3, 0, 5]`, we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap `8` units of water.

## Implementation

So I got a little distracted by overcomplicating the system, but I took a step back and figured it out. First, we can't start collecting water until we hit a maximum point, or a wall taller than the next space. So we can identify that local maxima are important for solving this problem.

We can start by looping until we reach a local maximum. Then, we start adding the difference between that local maximum and the next wall element. When we reach a maximum point greater than the previous local maximum, that becomes the new height for determining the difference. This is flawed since if the global maximum is unique and occurs very early in the array, then we will always be adding an extra amount to the sum. 