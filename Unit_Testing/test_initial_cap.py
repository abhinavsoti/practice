import unittest
import initial_cap

class TestInitCap(unittest.TestCase):
    '''
    TestInitCap: Class to keep all the test cases for testing init_cap function
    '''

    def test_one_word(self):
        text = 'python'
        result = initial_cap.init_cap(text)
        self.assertEqual(result,'Python')

    def test_string(self):
        text = 'first python test case'
        result = initial_cap.init_cap(text)
        self.assertEqual(result, 'First Python Test Case')

if __name__ == '__main__':
    unittest.main()