import numpy as np


def longestSubstring_KDistinctCharacters(k, s):
    a = list(s)
    n = 0
    sub = ""

    for i in range(len(a)):
        z = np.zeros(128, int)
        z[ord(a[i])] = 1
        for j in range(i+1, len(a)):
            z[ord(a[j])] = 1
            if (sum(z) > k):
                continue
            if (n < 1+j-i):
                n = 1+j-i
                sub = a[i:j+1]
                if (n >= len(a)-i):
                    break

    return (n, ''.join(sub))


assert longestSubstring_KDistinctCharacters(2, "abcba") == (3, "bcb")

k = 4
s = "aafaaasbckafcbfbffaba"
assert longestSubstring_KDistinctCharacters(k, s) == (11, "afcbfbffaba")
