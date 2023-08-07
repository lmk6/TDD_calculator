import unittest
from MVC.CalculatorModel import CalculatorModel


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

    def test_subtract(self):
        self.assertEqual(self.model.subtract(1, 3), -2)


if __name__ == "__name__":
    unittest.main()
