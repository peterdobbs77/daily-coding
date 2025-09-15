# Given a string and a set of characters, 
#   return the shortest substring containing 
#   all the characters in the set.
# For example, given the string "figehaeci" 
#   and the set of characters {a, e, i}, 
#   you should return "aeci".
# If there is no substring containing all 
#   the characters in the set, return null.

import string

def shortest_substring(str: string, chars: list):
    '''Given a string and a set of characters,
        return the shortest substring containing
        all the characters in the set.'''
    
    temp_substr = str
    for i in range(len(str)):
        track_chars = [0]*len(chars) # keep track of if each char has been seen
        if str[i] in chars:
            track_chars[] = 1
            for j in range(1, len(str)):
                if str[j] in chars:
                    track_chars[] = 1
                if track_chars == 2**len(chars) - 1:
                    if j - i < len(temp_substr):
                        temp_substr = str(i, j)
                    break
    return temp_substr



result = shortest_substring("figehaeci", ['a', 'e', 'i'])
print(f'{result} should be "aeci"')