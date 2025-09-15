# stacks

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
    
    def max(self):
        if self._top < 0:
            return None
        _max = self._array[self._top]
        for i in range(self._top):
            if self._array[i] > _max:
                _max = self._array[i]
        return _max
    
    def display(self):
        print(self._array)


myFirstStack = Stack(5)
myFirstStack.display()
print(f'Max element: {myFirstStack.max()} (should be None/null/error)')
myFirstStack.push(10)
myFirstStack.push(20)
myFirstStack.push(0)
print(f'Popped element: {myFirstStack.pop()} (should be 0)')
print(f'Max element: {myFirstStack.max()} (should be 20)')
myFirstStack.display()
myFirstStack.push(15)
myFirstStack.push(-50)
myFirstStack.push(50)
myFirstStack.display()
print(f'Max element: {myFirstStack.max()} (should be 50)')
print(f'Popped element: {myFirstStack.pop()} (should be 50)')
myFirstStack.display()
print(f'Max element: {myFirstStack.max()} (should be 20)')