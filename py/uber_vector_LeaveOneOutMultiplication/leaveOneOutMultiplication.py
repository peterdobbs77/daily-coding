import numpy as np


def leaveOutOutMultiplication(X):
    Y = np.ones(len(X))
    for i in range(len(X)):
        for j in range(len(X)):
            if(i == j):
                continue
            else:
                Y[i] = Y[i] * X[j]
    return Y


X = [1, 2, 3, 4, 5]
# expected Y = [120, 60, 40, 30, 24]

Y = leaveOutOutMultiplication(X)
print(Y)
