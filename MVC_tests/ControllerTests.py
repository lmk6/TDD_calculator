import unittest
from MVC.CalculatorController import *


class ControllerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.controller = CalculatorController()

    def test_change_state_to_add(self):
        self.controller.change_operator(Operator.ADD)
        self.assertEqual(self.controller.get_operator(), Operator.ADD)

    def test_change_state_to_subtract(self):
        self.controller.change_operator(Operator.SUB)
        self.assertEqual(self.controller.get_operator(), Operator.SUB)

    def test_change_state_to_multiply(self):
        self.controller.change_operator(Operator.MUL)
        self.assertEqual(self.controller.get_operator(), Operator.MUL)

    def test_change_state_to_divide(self):
        self.controller.change_operator(Operator.DIV)
        self.assertEqual(self.controller.get_operator(), Operator.DIV)

    def test_enter_number_1(self):
        self.controller.enter_value_1("123")
        self.assertEqual(self.controller.get_value_1(), 123)

    def test_enter_number_2(self):
        self.controller.enter_value_2("345")
        self.assertEqual(self.controller.get_value_2(), 345)


if __name__ == "__main__":
    unittest.main()
