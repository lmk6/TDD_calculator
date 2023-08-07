import unittest

from MVC.CalculatorController import CalculatorController


class ControllerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.controller = CalculatorController()

    def test_entered_value_is_stored(self):
        self.controller.get

if __name__ == "__name__":
    unittest.main()
