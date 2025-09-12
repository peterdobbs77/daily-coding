# Starting with any positive integer:
#   * if n is even, the next number in the sequence is n / 2
#   * if n is odd, the next number in the sequence is 3n + 1
# It is conjectured that every such sequence eventually reaches the number 1. 
# Test this conjecture.
# Bonus: What input n <= 1000000 gives the longest sequence?


def next_collatz(N):
    if N < 1:
        return None
    if N % 2 == 0:
        next_collatz(N/2)
    else:
        next_collatz(3*N + 1)