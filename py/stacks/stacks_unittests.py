import unittest
import stacks

class Test_stacks(unittest.TestCase):

    def test_stacks_simple(self):
        myFirstStack = stacks.Stack()
        myFirstStack.display()
        print(f'Max element: {myFirstStack.max()} (should be None/null/error)')
        myFirstStack.push(10)
        myFirstStack.push(20)
        myFirstStack.push(0)
        self.assertEqual(myFirstStack.pop(), 0)
        self.assertEqual(myFirstStack.max(), 20)
        myFirstStack.display()
        myFirstStack.push(15)
        myFirstStack.push(-50)
        myFirstStack.push(50)
        myFirstStack.display()
        self.assertEqual(myFirstStack.max(), 50)
        self.assertEqual(myFirstStack.pop(), 50)
        myFirstStack.display()
        self.assertEqual(myFirstStack.max(), 20)

    def test_processCouponStackOperations_simple(self):
        operations = ['push 2', 'push 0', 'push 3', 'push 0', 'getMin', 'pop', 'getMin', 'pop', 'top', 'getMin']
        response = stacks.processCouponStackOperations(operations)
        self.assertEqual(response, [0,0,0,0])

if __name__ == '__main__':
    unittest.main()