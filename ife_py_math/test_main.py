from main import power, factorial, permutation, combination
import unittest

class TestMain(unittest.TestCase):
    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(2, 0), 1)
        self.assertEqual(power(2, -1), 0.5)
        self.assertEqual(power(-3, 2), 9)
        self.assertEqual(power(-3, 3), -27)

    def test_factorial(self):
        self.assertEqual(factorial(6), 720)
        self.assertEqual(factorial(0), 1)


    def test_permutation(self):
        self.assertEqual(permutation(4, 2), 12.0)
        self.assertRaises(ValueError, permutation, 2,3)

    def test_combination(self):
        self.assertEqual(combination(4, 2), 6.0)
        self.assertRaises(ValueError, combination, 3,4)

if __name__ == "__main__":
    unittest.main()