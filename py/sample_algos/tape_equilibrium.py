import unittest

def solution(A):
    '''Given an array `A` of `N` integers, 
        split array into two non-empty parts at position `P` (where 1<=P<N)
        such that the absolute difference between the sum of the two parts is minimized
        Return the minimum absolute difference'''
    total = sum(A)
    left_sum = 0
    min_abs_diff = None
    for p in range(1, len(A)):
        left_sum += A[p-1]
        right_sum = total - left_sum
        if min_abs_diff is None:
            min_abs_diff = abs(left_sum - right_sum)
        min_abs_diff = min(min_abs_diff, abs(left_sum - right_sum))

    return min_abs_diff

class Test_tapeEquilibrium(unittest.TestCase):
    ''''''

    def test_tape_equilibrium_simple(self):
        ''''''
        A = [3, 1, 2, 4, 3]
        expected = 1
        self.assertEqual(expected, solution(A))


if __name__ == '__main__':
    unittest.main()