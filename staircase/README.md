# daily-coding/staircase

## Prompt - from [dailycodingproblem.com](dailycodingproblem.com)
There's a staircase with N steps, and you can climb 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters. For example, if N is 4, then there are 5 unique ways:
* 1, 1, 1, 1
* 2, 1, 1
* 1, 2, 1
* 1, 1, 2
* 2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time. Generalize your function to take in X.

## My Thoughts
* Consider this problem like a classic tree-traversal problem
* The tree is constructed by the idea that each branch is subtracting some amount from its base. For visual purposes:
>                      N
>                 /    |    \
>          (N-X_1)  (N-X_2)  (N-X_m)
>         /            \            \
>     ((N-X_1)-X_2)  ((N-X_2)-X_m)  ((N-X_m)-X_1)
>              \
>         (((N-X_1)-X_2)-X_1)

* Therefore we can use recursion to count the leaves on the tree