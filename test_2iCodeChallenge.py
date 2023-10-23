import unittest
from 2iCode_Challenge import count_pairs_with_sum

class Test2iCodeChallenge(unittest.TestCase):

    def test_case1(self):
        required_total  = 1
        test_array = [3, 4, 5, 6]
        self.assertEqual(count_pairs_with_sum(test_array, required_total), 0)

    def test_case2(self):
        required_total = 15
        test_array = [0, 15, 32, 2000, 15000]
        self.assertEqual(count_pairs_with_sum(test_array, required_total), 1)

    def test_case3(self):
        required_total = 42
        test_array = [1, 1, 10, 32, 41]
        self.assertEqual(count_pairs_with_sum(test_array, required_total), 2)

if __name__ == "__main__":
    unittest.main()