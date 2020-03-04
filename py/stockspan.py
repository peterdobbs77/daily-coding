import numpy as np


def stock_span(prices):
    span = list(np.ones(len(prices), dtype=int))
    for i in range(1, len(prices)):
        j = i-1
        while (j >= 0) and (prices[i] > prices[j]):
            span[i] += 1
            j -= 1
    return span


assert stock_span([100, 60, 70, 65, 80, 85]) == [1, 1, 2, 1, 4, 5]
