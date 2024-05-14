import unittest
from sourcepackage.Calculator import Calculator

class CalculatorTests(unittest.TestCase):
    def test_addition(self):
        calculator = Calculator()
        result = calculator.add(2, 3)
        self.assertEqual(result, 5)

    def test_subtraction(self):
        calculator = Calculator()
        result = calculator.subtract(5, 2)
        self.assertEqual(result, 3)

    def test_multiplication(self):
        calculator = Calculator()
        result = calculator.multiply(4, 6)
        self.assertEqual(result, 24)

    def test_division(self):
        calculator = Calculator()
        result = calculator.divide(10, 2)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()