import unittest
import calculator


class TestCalculator(unittest.TestCase):
    def test_addition(self):
        # Floats
        result = calculator.addition(2.5, 4.75)
        self.assertEqual(result, 7.25)
        # Zero
        result = calculator.addition(6, 0)
        self.assertEqual(result, 6)
        # Negative
        result = calculator.addition(-3, -7)
        self.assertEqual(result, -10)
        # Non-numeric
        result = calculator.addition("add", 2)
        self.assertEqual(result, None)

    def test_subtraction(self):
        # Floats
        result = calculator.subtraction(5, 2.5)
        self.assertEqual(result, 2.5)
        # Zero
        result = calculator.subtraction(0, 4.75)
        self.assertEqual(result, -4.75)
        # Negative
        result = calculator.subtraction(-4, -5)
        self.assertEqual(result, 1)
        # Non-numeric
        result = calculator.subtraction(3, "subtract")
        self.assertEqual(result, None)

    def test_multiplication(self):
        # Floats
        result = calculator.multiplication(3.3, 7.8)
        self.assertEqual(result, 25.74)
        # Zero
        result = calculator.multiplication(0, 7.5)
        self.assertEqual(result, 0)
        # Negative
        result = calculator.multiplication(-4, -9)
        self.assertEqual(result, 36)
        result = calculator.multiplication(-5, 6)
        self.assertEqual(result, -30)
        # Non-numeric
        result = calculator.multiplication("multiply", 2)
        self.assertEqual(result, None)

    def test_division(self):
        # Floats
        result = calculator.division(1, 8)
        self.assertEqual(result, .125)
        # Zero
        result = calculator.division(5, 0)
        self.assertEqual(result, None)
        result = calculator.division(0, 986)
        self.assertEqual(result, 0)
        # Negative
        result = calculator.division(-8, -2)
        self.assertEqual(result, 4)
        result = calculator.division(9, -3)
        self.assertEqual(result, -3)
        # Non-numeric
        result = calculator.multiplication("divide", 7)
        self.assertEqual(result, None)


if __name__ == "__main__":
    unittest.main()
