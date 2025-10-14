import unittest

def solution(N, A):
    '''Given `N` counters, initially set to `0`,
        and a sequence of operations represented by `A`,
        where each element of `A` is either:
        * An integer `x` such that `1<=x<=N`: incremement counter `x` by 1
        * OR `x = N+1`: set all counters to the maximum value of any counter
        Return the final state of the counters after all operations'''
    M = len(A)

    # initialize counters
    counters = [0]*N
    max_count = 0       # running maximum
    base = 0            # base maximum, set when `x=N+1`

    for x in A:
        if 1 <= x and x <= N:
            # lazy update
            if counters[x-1] < base:
                counters[x-1] = base
            # increment
            counters[x-1] += 1
            max_count = max(counters[x-1], max_count)
        elif x == N+1:
            base = max_count
    
    for i in range(len(counters)):
        if counters[i] < base:
            counters[i] = base
    
    return counters

class Test_max_counters_solution(unittest.TestCase):

    def test_max_counters_simple(self):
        ''''''
        A = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
        N = 5
        expectation = [2]*N
        self.assertEqual(expectation, solution(N, A))

    def test_max_counters_zeros(self):
        ''''''
        A = [0]*10
        N = 5
        expectation = [0]*N
        self.assertEqual(expectation, solution(N, A))

    def test_max_counters_useMax(self):
        ''''''
        A = [3, 4, 4, 6, 1, 4, 4]
        N = 5
        expectation = [3,2,2,4,2]
        self.assertEqual(expectation, solution(N, A))

if __name__ == '__main__':
    unittest.main()