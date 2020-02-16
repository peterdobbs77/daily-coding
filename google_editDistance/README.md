# edit_distance

## Prompt

This problem was asked by Google.

The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.

## Implementation

Ah yes, an alignment problem. I've encountered this question before in [peterdobbs77/bioc_c_cpp](https://github.com/peterdobbs77/bioc_c_cpp). I did that program in C while this will be in Python. Also, the previous algorithm was much more intensive, as it required construction of a full comparison matrix. This program just needs to how many differences there are between two strings.

