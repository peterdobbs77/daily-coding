import random

RNG = random.Random(58)

def reservoir_sampling(input_stream: list, k: int):
    """
    Given reservoir size `k` and input stream of size `N`
    Fill reservior with first `k` elements of the input stream
    For each input stream element `x_i, i \\in {k, ..., N-1}`:
        1. Uniformly generate a random number `j \\in {0, ..., i}
        2. If j<=k, replace the j-th element of the reservoir
    """
    N = len(input_stream)
    reservoir = input_stream[:k]

    for i in range(k, N):
        j = RNG.randint(0, i)
        if j < k:
            reservoir[j] = input_stream[i]
    
    return reservoir

import unittest

class Test_reservoir_sampling(unittest.TestCase):
    """"""

    def test_simple_reservoir_sampling(self):
        """Simple test of reservoir sampling"""
        input = [x for x in range(10)]
        k = 4

        result = reservoir_sampling(input, k)
        print(f"input: {input} and k = {k}, yields reservoir: {result}")

if __name__ == '__main__':
    unittest.main()