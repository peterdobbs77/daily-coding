# Given a string and a set of characters, 
#   return the shortest substring containing 
#   all the characters in the set.
# For example, given the string "figehaeci" 
#   and the set of characters {a, e, i}, 
#   you should return "aeci".
# If there is no substring containing all 
#   the characters in the set, return null.

import string

def shortest_substring_On2(str: string, chars: list):
    '''Given a string and a set of characters,
        return the shortest substring containing
        all the characters in the set.'''
    temp_substr = str
    for i in range(len(str)):
        track_chars = [0]*len(chars) # keep track of if each char has been seen
        if str[i] in chars:
            track_chars[chars.index(str[i])] = 1
            for j in range(i+1, len(str)):
                if str[j] in chars:
                    track_chars[chars.index(str[j])] = 1
                if sum(track_chars) == len(chars):
                    if j - i < len(temp_substr):
                        temp_substr = str[i:j+1]
                    break
    return temp_substr

# def position_difference(i_chars: list):
#     '''Given a list of positional integers,
#         return the difference between all
#         indexes contained in the list'''
#     result = abs(i_chars[0] - i_chars[len(i_chars)])
#     for i in range(len(i_chars)-1):
#         result += abs(i_chars[i] - i_chars[i+1])
#     return result

# def shortest_substring(str: string, chars: list):
#     '''Given a string and a set of characters,
#         return the shortest substring containing
#         all the characters in the set.'''
#     i_chars = [0](len(chars)) # position of characters
#     for i in range(len(str)):
#         if str[i] in chars:
#             i_chars[chars.index(str[i])] = i

# provided example
result = shortest_substring_On2("figehaeci", ['a', 'e', 'i'])
print(f'{result} should be "aeci"')

# palindrome test
result = shortest_substring_On2("amanaplanacanalpanama", ['a','p','c','n'])
print(f'{result} should be "canalp" (but could equally be "planac")')