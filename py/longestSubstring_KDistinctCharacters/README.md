# longestSubstring_KDistinctCharacters
## Prompt

Given an integer `k` and a string `s`, find the length of the longest substring that contains at most `k` distinct characters.

For example, given `s = "abcba"` and `k = 2`, the longest substring with `k` distinct characters is `"bcb"`.

# Implementation

Constructing substrings is handled by a nested loop to run through characters following a set starting point. To keep track of the number of distinct characters, I created an array for counting the presence of a distinct ASCII character and called it `z`. This counting array would need to be reset each time you try to construct new a substring that conforms to the required `k` distinct characters.