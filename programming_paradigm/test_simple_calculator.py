import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up a new SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # --- Addition Tests ---
    def test_addition_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 15), 25)

    def test_addition_with_negative_numbers(self):
        self.assertEqual(self.calc.add(-1, -5), -6)
        self.assertEqual(self.calc.add(-3, 7), 4)

    def test_addition_with_zero(self):
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(5, 0), 5)

    # --- Subtraction Tests ---
    def test_subtraction_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 3), 7)
        self.assertEqual(self.calc.subtract(5, 9), -4)

    def test_subtraction_with_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-5, -2), -3)
        self.assertEqual(self.calc.subtract(-3, 4), -7)

    def test_subtraction_with_zero(self):
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(5, 0), 5)

    # --- Multiplication Tests ---
    def test_multiplication_positive_numbers(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(7, 1), 7)

    def test_multiplication_with_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-4, -5), 20)

    def test_multiplication_with_zero(self):
        self.assertEqual(self.calc.multiply(0, 10), 0)
        self.assertEqual(self.calc.multiply(25, 0), 0)

    # --- Division Tests ---
    def test_division_normal(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-9, 3), -3)

    def test_division_fraction_result(self):
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)

    def test_division_by_zero(self):
        self.assertIsNone(self.calc.divide(10, 0))

    def test_division_zero_numerator(self):
        self.assertEqual(self.calc.divide(0, 5), 0)

if __name__ == "__main__":
    unittest.main()
