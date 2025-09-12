# Starting with any positive integer:
#   * if n is even, the next number in the sequence is n / 2
#   * if n is odd, the next number in the sequence is 3n + 1
# It is conjectured that every such sequence eventually reaches the number 1. 
# Test this conjecture.
# Bonus: What input n <= 1000000 gives the longest sequence?


def next_collatz(N, sequence):
    sequence.append(N)
    if N < 1:
        return None
    if N == 1:
        # print(f'N={N}, sequence has converged, sequence length is: {len(sequence)}')
        return sequence
    elif N % 2 == 0:
        # print(f'N={N} is even, current sequence length is: {len(sequence)}')
        next_collatz(N/2, sequence)
    else:
        # print(f'N={N} is odd, current sequence length is: {len(sequence)}')
        next_collatz(3*N + 1, sequence)
    return sequence

max_seq_len = 1
for i in range(1,1000000):
    i_sequence = next_collatz(i, [])
    # print(f'When N={i}, Sequence Length is: {len(i_sequence)}')
    if len(i_sequence) > max_seq_len:
        max_seq_len = len(i_sequence)

print(f'Max Sequence Length Where N <= 1000000 is: {max_seq_len}')