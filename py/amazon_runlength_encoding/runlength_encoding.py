
def run_length_encoding(string):
    l = list(string.upper())
    count = 1
    encoding = temp = ""
    for i in range(1, len(l)):
        if l[i] != l[i-1]:
            encoding = encoding + str(count) + l[i-1]
            count = 1
            if i == len(l)-1:
                encoding = encoding + str(count) + l[i]
        else:
            count += 1
            if i == len(l)-1:
                encoding = encoding + str(count)+l[i-1]

    return encoding


def run_length_decoding(string):
    l = list(string)
    decoded = ""
    for i in range(0, len(l), 2):  # doesn't work if number of successive same characters > 9
        for j in range(int(l[i])):
            decoded = decoded + l[i+1]
    return decoded


test_string = "AAAABBBCCDAA"
assert run_length_decoding(run_length_encoding(test_string)) == test_string

test_string = "ABABBCDDXAQA"
assert run_length_decoding(run_length_encoding(test_string)) == test_string
