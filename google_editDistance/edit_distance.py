
def compute_edit_distance(x, y):
    diff = abs(len(x)-len(y))
    for i in range(min(len(x), len(y))):
        if (x[i] != y[i]):
            diff += 1

    return diff


assert compute_edit_distance('kitten','sitting') == 3