# author: Peter N. Dobbs (@peeetahdobbs)
# author_GitHub: peterdobbs77
# date: 1/15/2020
# prompt from dailycodingproblem.com

# PROMPT:
# There's a staircase with N steps, and you can climb 1 or 2 steps at a time.
# Given N, write a function that returns the number of unique ways you can
# climb the staircase. The order of the steps matters.
# For example, if N is 4, then there are 5 unique ways:
# * 1, 1, 1, 1
# * 2, 1, 1
# * 1, 2, 1
# * 1, 1, 2
# * 2, 2
# What if, instead of being able to climb 1 or 2 steps at a time, you could
# climb any number from a set of positive integers X? For example, if
# X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
# Generalize your function to take in X.

# DEFINITIONS:
# Let N be the number of steps on a staircase
# Let X be the set of 'm' possible step sizes you can take to climb the stairs
# Let Y be the number of unique ways to climb N steps

# MY THOUGHTS:
# * Consider this problem like a classic tree-traversal problem
# * The tree is constructed by the idea that each branch is subtracting
#   some amount from its base. For visual purposes:
#                   N
#              /    |    \
#       (N-X_1)  (N-X_2)  (N-X_m)
#      /            \           \
# ((N-X_1)-X_2)  ((N-X_2)-X_m)  ((N-X_m)-X_1)
# * Therefore we can use recursion to count the leaves on the tree

import numpy as np


def staircase(N, X):
    global Y
    for x_i in X:
        print("X_i = ", x_i)
        if((N - x_i) > 0):
            print(N-x_i)
            staircase((N - x_i), X)
        if((N - x_i) == 0):
            print("reached a leaf")
            Y = Y + 1


# initialize the variables (as defined in the prologue)
X = np.array([1, 2, 4])
N = 6
Y = 0

# traverse the staircase
staircase(N, X)
print("Y = ", Y)
