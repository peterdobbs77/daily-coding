import numpy as np


def largestsum_nonadjacent(l):
    z = np.zeros(len(l))
    for i in range(len(l)-1):
        if (l[i]-l[i+1]) > 0:
            z[i] += 1


largestsum_nonadjacent([2, 4, 6, 2, 5])
largestsum_nonadjacent([5, 1, 1, 5])
# assert largestsum_nonadjacent([2, 4, 6, 2, 5]) == 13
# assert largestsum_nonadjacent([5, 1, 1, 5]) == 10
