import sequence_generator
import unittest

class Test_BasicTestCase(unittest.TestCase):

    def test_simple(self):
        '''Simple test for the sequence generator'''
        print("Simple Test")
        start, step, num = 1, 2, 3
        expected_result = (n for n in range(start, start+(step*num), step))

        with sequence_generator.sequence_generator(start, step) as gen:
            for i in range(num):
                temp_exp = next(expected_result)
                temp_act = next(gen)
                print(f"Expected: {temp_exp}, Actual: {temp_act}")
                self.assertEqual(temp_exp, temp_act)

    def test_largish_numbers(self):
        '''Testing largish numbers'''
        print("="*8)
        print("Largish Numbers Test")
        start, step, num = 1000, 10000, 20
        expected_result = (n for n in range(start, start+(step*num), step))

        with sequence_generator.sequence_generator(start, step) as gen:
            for i in range(num):
                temp_exp = next(expected_result)
                temp_act = next(gen)
                print(f"Expected: {temp_exp}, Actual: {temp_act}")
                self.assertEqual(temp_exp, temp_act)

    def test_negative_step(self):
        '''Testing a decreasing sequence by inputing a negative `step` value'''
        print("="*8)
        print("Test Negative Step Value")
        start, step, num = 10, -1, 5
        expected_result = (n for n in range(start, start+(step*num), step))

        with sequence_generator.sequence_generator(start, step) as gen:
            for i in range(num):
                temp_exp = next(expected_result)
                temp_act = next(gen)
                print(f"Expected: {temp_exp}, Actual: {temp_act}")
                self.assertEqual(temp_exp, temp_act)

    def test_nested_generators(self):
        '''Testing behavior for nested calls to generators'''
        print("="*8)
        print("Test Nested Generators")
        start, step, num = 1, 2, 3
        expected_result1 = (n for n in range(start, start+(step*num), step))

        with sequence_generator.sequence_generator(start, step) as gen1:
            for i in range(num):
                temp_exp1 = next(expected_result1)
                temp_act1 = next(gen1)
                print(f"Expected: {temp_exp1}, Actual: {temp_act1}")
                self.assertEqual(temp_exp1, temp_act1)

                with sequence_generator.sequence_generator(start, step) as gen2:
                    expected_result2 = (n for n in range(start, start+(step*num), step))
                    for j in range(num):
                        temp_exp2 = next(expected_result2)
                        temp_act2 = next(gen2)
                        print(f"Expected: {temp_exp2}, Actual: {temp_act2}")
                        self.assertEqual(temp_exp2, temp_act2)

if __name__ == '__main__':
    unittest.main()