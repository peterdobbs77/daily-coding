import sample_algos
import unittest

class Test_BasicTestCase(unittest.TestCase):

    def test_groupPeakConcurency_simple(self):
        '''example provided by prompt'''
        events = [
            ['1', '101', '500', 'login'],
            ['2', '102', '500', 'login'],
            ['5', '101', '500', 'logout'], 
            ['6', '102', '500', 'logout']
        ]
        result = sample_algos.computeGroupPeakConcurrency(events)
        print('\n'.join([' '.join(map(str, x)) for x in result]))
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

    def groupPeakConcurency_unsortedByTimestamp_singleUserMultipleGroups(self):
        '''How does the algo handle a user login on multiple groups'''
        events = [
            ['1', '101', '001', 'login'],
            ['1', '102', '002', 'login'],
            ['75', '101', '001', 'logout'],
            ['10', '102', '002', 'logout'],
            ['6', '103', '001', 'login'],
            ['40', '103', '001', 'logout'],
            ['13', '102', '001', 'login'],
            ['40', '102', '001', 'logout']
        ]
        result = sample_algos.computeGroupPeakConcurrency(events)
        self.assertEqual(result[0], ['001',3])
        self.assertEqual(result[1], ['002',1])

if __name__ == '__main__':
    unittest.main()