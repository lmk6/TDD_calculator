import unittest
from MVC.CalculatorController import *
from MVC.CalculatorModel import CalculatorModel


class ControllerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.controller = CalculatorController(CalculatorModel())

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

    def test_enter_incorrect_type_values(self):
        with self.assertRaises(IllegalValueException):
            self.controller.enter_value_1("2a1")
            self.controller.enter_value_2("2a2")

    def test_give_value1_operand_and_value_2_and_enter_giving_result(self):
        self.controller.enter_value_1("530")
        self.controller.change_operator(Operator.ADD)
        self.controller.enter_value_2("530")
        self.assertEqual(self.controller.get_result(), 1060)

        self.controller.enter_value_1("100")
        self.controller.change_operator(Operator.SUB)
        self.controller.enter_value_2("200")
        self.assertEqual(self.controller.get_result(), -100)

        self.controller.enter_value_1("-2")
        self.controller.change_operator(Operator.MUL)
        self.controller.enter_value_2("-3")
        self.assertEqual(self.controller.get_result(), 6)

        self.controller.enter_value_1("5")
        self.controller.change_operator(Operator.DIV)
        self.controller.enter_value_2("2")
        self.assertEqual(self.controller.get_result(), 2.5)

    def test_get_result_resets_values(self):
        self.controller.enter_value_1("530")
        self.controller.change_operator(Operator.ADD)
        self.controller.enter_value_2("530")
        self.assertEqual(self.controller.get_result(), 1060)
        self.assertEqual(self.controller.get_value_1(), 1060)
        self.assertEqual(self.controller.get_value_2(), None)
        self.assertEqual(self.controller.get_operator(), None)

    def test_enter_operator_and_both_values_and_choose_new_operator_returns_result_and_makes_it_value1(self):
        self.controller.enter_value_1("530")
        self.controller.change_operator(Operator.ADD)
        self.controller.enter_value_2("530")
        self.controller.change_operator(Operator.SUB)
        self.assertEqual(self.controller.get_value_1(), 1060)
        self.assertEqual(self.controller.get_value_2(), None)


if __name__ == "__main__":
    unittest.main()
