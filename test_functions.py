import unittest
from testing_completion import factorial

class TestFactorial(unittest.TestCase):
    def test_factorial_zero(self):
        """Test factorial of 0"""
        self.assertEqual(factorial(0), 1)
        
    def test_factorial_one(self):
        """Test factorial of 1"""
        self.assertEqual(factorial(1), 1)
        
    def test_factorial_positive_numbers(self):
        """Test factorial of positive numbers"""
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(7), 5040)
        
    def test_factorial_large_number(self):
        """Test factorial of a larger number"""
        self.assertEqual(factorial(10), 3628800)
        
    def test_factorial_negative_input(self):
        """Test factorial with negative input"""
        with self.assertRaises(RecursionError):
            factorial(-1)

if __name__ == '__main__':
    unittest.main()