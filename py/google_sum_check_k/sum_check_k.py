# Let X be a random list of numbers
# Let k be a random number
# Return whether any two numbers from the list add up to k


def check_if_sums(X, k):
    for i in range(0, len(X)):
        for j in range(i+1, len(X)):
            l = X[i] + X[j]
            print('{} + {} = {}'.format(X[i], X[j], l))
            if(l == k):
                return True
    return False


X = [15, 3, 10, 7]
k = 17

result = check_if_sums(X, k)
print(result)
