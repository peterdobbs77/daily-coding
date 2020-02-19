# N Queens

## Prompt

I've been feeling a bit bored with some of the coding interview questions. So I thought I'd spice it up a bit. I remember solving this CLASSIC computer science question during undergrad, but I hadn't thought about it in a while and honestly forget how I solved it. So let's revisit it together!

The basic idea of this puzzle is: how to fit `n` chess qeens on an `n`-by-`n` chessboard so that no queens are in danger. The key here is in the rules of chess. *If you don't understand the rules of chess, go look them up. It's a lovely game.* In order to avoid putting any of the queens in danger, only one queen can occur in each row, column, and diagonal.

For example, say that `n = 4`. One resulting alignment would be:
```
[ ][Q][ ][ ]
[ ][ ][ ][Q]
[Q][ ][ ][ ]
[ ][ ][Q][ ]
```
You could, however, have three other solutions that are just rotated versions of this (and look the same).

For an in depth explanation of the problem, see [How to Think Like a Computer Scientist](http://openbookproject.net/thinkcs/python/english3e/list_algorithms.html#eight-queens-puzzle-part-1).

## Implementation

The source mentioned previously has provided some insight that I doubt I considered during my undergraduate studies. If you look at the coordinates for the `n` queens, you get a tuple of the form `(r, c)`, where `r` is the row number and `c` is the column number. The set of coordinates from our example above are:
```
(0,1), (1,3), (2,1), (3,2)
```

Notice that the `r` values are just sequential values `[0, ..., n-1]` and that the `c` values are also unique values from `[0, ..., n-1]`, **but not in order**. These findings help us simplify the problem to choosing the optimal row to avoid danger on the diagonal.



