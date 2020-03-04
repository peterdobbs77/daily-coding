
def detect_palindrome(text):
    forward = list(filter(lambda i: i not in ' ', text.lower()))
    backward = forward.copy()
    backward.reverse()
    for i in range(len(forward)):
        if forward[i] == backward[i]:
            continue
        else:
            return False
    return True


assert detect_palindrome("A man a plan a canal Panama") == True
assert detect_palindrome("nOt a PaLiNdRoMe") == False
assert detect_palindrome("RaCecAr R a C e c A R") == True
