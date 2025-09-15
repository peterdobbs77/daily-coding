# Given an arithmetic expression in Reverse Polish Notation, 
# write a program to evaluate it.
# The expression is given as a list of numbers and operands. 
# For example: [5, 3, '+'] should return 5 + 3 = 8.
# For example, 
#   [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'] 
#   should return 5, since it is equivalent to 
#   ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5.
# You can assume the given expression is always valid.


import operator

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}


class Stack:
    def __init__(self, capacity):
        self._capacity = capacity
        self._top = -1
        self._array = [None] * self._capacity
    
    def push(self, val):
        self._top += 1
        self._array[self._top] = val
    
    def pop(self):
        val = self._array[self._top]
        self._array[self._top] = None
        self._top -= 1
        return val
    
    def display(self):
        print(self._array)

def compute_reverse_polish_notation(arr: list):
    _result = 0
    temp = Stack(len(arr))
    for i in range(len(arr)):
        if arr[i] in ['+', '-', '*', '/']:
            _result = ops[arr[i]](temp.pop(), temp.pop())
            temp.push(_result)
        else:
            temp.push(arr[i])
        temp.display()
    return _result


result = compute_reverse_polish_notation([5, 3, '+'])
print(f'{result} should be 8')

result = compute_reverse_polish_notation([15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'])
print(f'{result} should be 5')