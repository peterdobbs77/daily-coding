import sample_algos
import unittest

class Test_groupPeakConcurency(unittest.TestCase):

    def test_groupPeakConcurency_simple(self):
        '''example provided by prompt'''
        events = [
            ['1', '101', '500', 'login'],
            ['2', '102', '500', 'login'],
            ['5', '101', '500', 'logout'], 
            ['6', '102', '500', 'logout']
        ]
        result = sample_algos.computeGroupPeakConcurrency(events)
        # print('\n'.join([' '.join(map(str, x)) for x in result]))
        self.assertEqual(result[0], ['500', 2])

    def test_groupPeakConcurency_unsortedByTimestamp(self):
        '''How does the algo handle an unordered list of events'''
        events = [
            ['1', '101', '001', 'login'],
            ['1', '102', '002', 'login'],
            ['75', '101', '001', 'logout'],
            ['10', '102', '002', 'logout'],
            ['6', '103', '001', 'login'],
            ['40', '103', '001', 'logout'],
            ['13', '102', '002', 'login'],
            ['40', '102', '002', 'logout']
        ]
        result = sample_algos.computeGroupPeakConcurrency(events)
        self.assertEqual(result[0], ['001', 2])
        self.assertEqual(result[1], ['002', 1])

    def test_groupPeakConcurency_singleUserMultipleGroups(self):
        '''How does the algo handle a user login on multiple groups'''
        events = [
            ['1', '101', '001', 'login'],
            ['1', '102', '002', 'login'],
            ['75', '101', '001', 'logout'],
            ['10', '102', '002', 'logout'],
            ['6', '103', '001', 'login'],
            ['40', '103', '001', 'logout'],
            ['13', '102', '001', 'login'],
            ['40', '102', '001', 'logout'],
            ['11', '103', '002', 'login'],
            ['32', '103', '002', 'logout']
        ]
        result = sample_algos.computeGroupPeakConcurrency(events)
        self.assertEqual(result[0], ['001',3])
        self.assertEqual(result[1], ['002',1])

    def test_groupPeakConcurency_outlierTimestamp(self):
        '''ensures that timestamp is not used improperly by an inefficient algorithm'''
        events = [
            ['1', '101', '500', 'login'],
            ['2', '102', '500', 'login'],
            ['5', '101', '500', 'logout'],
            ['1000000', '102', '500', 'logout']
        ]
        result = sample_algos.computeGroupPeakConcurrency(events)
        # print('\n'.join([' '.join(map(str, x)) for x in result]))
        pass

    def test_groupPeakConcurency_overlappingTimestamps(self):
        '''How does algorithm handle overlapping timestamps'''
        events = [
            ['1', '101', '500', 'login'],
            ['1', '102', '500', 'login'],
            ['1', '103', '400', 'login'],
            ['10', '102', '500', 'logout'],
            ['10', '104', '500', 'login'],
            ['10', '103', '400', 'logout'],
            ['10', '101', '500', 'logout']
        ]
        result = sample_algos.computeGroupPeakConcurrency(events)
        # print('\n'.join([' '.join(map(str, x)) for x in result]))


class Test_findSmallestMissingPositive(unittest.TestCase):

    def test_findSmallestMissingPositive_emptyList(self):
        ''''''
        orderNumbers = []
        result = sample_algos.findSmallestMissingPositive(orderNumbers)
        self.assertEqual(result, 1)

    def test_findSmallestMissingPositive_simple(self):
        ''''''
        orderNumbers = [3, 4, -1, 1]
        result = sample_algos.findSmallestMissingPositive(orderNumbers)
        self.assertEqual(result, 2)


    def test_findSmallestMissingPositive_longrange(self):
        ''''''
        orderNumbers = []
        orderNumbers += [x for x in range(-1000, 1001, 2)]
        orderNumbers += [x for x in range(-1000, 1001, 2)]
        orderNumbers += [x for x in range(1001) if x != 101]
        orderNumbers += [x for x in range(-1000, 1001, 2)]
        orderNumbers.reverse()
        result = sample_algos.findSmallestMissingPositive(orderNumbers)
        self.assertEqual(result, 101)

if __name__ == '__main__':
    unittest.main()