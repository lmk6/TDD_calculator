import unittest
from MVC.CalculatorModel import *


class ModelTests(unittest.TestCase):
    def setUp(self) -> None:
        self.model = CalculatorModel()

    def test_add(self):
        self.assertEqual(self.model.add(1, 1), 2)
        self.assertEqual(self.model.add(1, 3), 4)
        self.assertEqual(self.model.add(-1, 4), 3)
        self.assertEqual(self.model.add(1, 2, 3), 6)
        self.assertEqual(self.model.add(0, 0), 0)
        self.assertEqual(self.model.add(0, -1), -1)

    def test_illegal_value_exception(self):
        with self.assertRaises(IllegalValueException):
            self.model.add('a', 0)

        with self.assertRaises(IllegalValueException):
            self.model.subtract('b', 1)

        with self.assertRaises(IllegalValueException):
            self.model.multiply('c', 2)

        with self.assertRaises(IllegalValueException):
            self.model.divide('d', 3)

    def test_subtract(self):
        self.assertEqual(self.model.subtract(1, 3), -2)
        self.assertEqual(self.model.subtract(1, 1, 1), -1)
        self.assertEqual(self.model.subtract(1, -2), 3)

    def test_multiply(self):
        self.assertEqual(self.model.multiply(1, 1), 1)
        self.assertEqual(self.model.multiply(3, 3), 9)
        self.assertEqual(self.model.multiply(5, 0), 0)
        self.assertEqual(self.model.multiply(-1, -5), 5)
        self.assertEqual(self.model.multiply(-1, -5, -3), -15)

    def test_divide(self):
        self.assertEqual(self.model.divide(1, 1), 1)
        self.assertEqual(self.model.divide(2, -2), -1)
        self.assertEqual(self.model.divide(-3, -3), 1)
        self.assertEqual(self.model.divide(-6, 3, -2), 1)
        with self.assertRaises(DivisionByZeroException):
            self.model.divide(1, 0)


if __name__ == "__name__":
    unittest.main()
