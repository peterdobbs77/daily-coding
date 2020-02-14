# run-length encoding

## Prompt

Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.

## Implementation

Let's make a few additional assumptions to make our lives easier
 * Assume that the input string does not have more than 9 successive same characters

Depending on how you want to pass through the string, you have to deal with complications at the start and end of the string.