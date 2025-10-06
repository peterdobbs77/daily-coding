# stacks

class Stack:
    def __init__(self):
        self._array = []
        self._min_array = []
        self._max_array = []
    
    def push(self, val):
        self._array.append(val)
        # and set min
        if self._min_array:
            self._min_array.append(min(self._min_array[-1], val))
        else:
            self._min_array.append(val)
        # and set max
        if self._max_array:
            self._max_array.append(max(self._max_array[-1], val))
        else:
            self._max_array.append(val)
    
    def pop(self):
        self._min_array.pop()
        self._max_array.pop()
        return self._array.pop()
    
    def max(self):
        if not self._max_array:
            return None
        return self._max_array[-1]
    
    def min(self):
        if not self._min_array:
            return None
        return self._min_array[-1]
    
    def display(self):
        print(self._array)

    def top(self):
        if not self._array:
            return None
        return self._array[-1]

def processCouponStackOperations(operations):
    # Write your code here
    response = []
    s = Stack()
    
    for operation in operations:
        splt = str.split(operation, ' ')
        
        if splt[0] == "push":
            s.push(int(splt[1]))
        if s.top() >= 0:
            if splt[0] == "pop":
                _ = s.pop()
            elif splt[0] == "getMin":
                response.append(s.min())
            elif splt[0] == "top":
                response.append(s.top())
    
    return response
            