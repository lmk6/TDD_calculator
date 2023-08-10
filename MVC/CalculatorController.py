from enum import Enum


class IllegalValueException(Exception):
    def __init__(self, value):
        super().__init__(f"Value --{value}-- is of incorrect type or of wrong format! Expected a number!")


class Operator(Enum):
    ADD = '+'
    SUB = '-'
    MUL = '*'
    DIV = '/'


class CalculatorController:

    def __init__(self, model):
        self.__model = model
        self.__status_operator = None
        self.__value_1 = None
        self.__value_2 = None

    def change_operator(self, new_operator):
        if self.__status_operator is not None and self.__value_2 is not None:
            self.__value_1 = self.get_result()
            self.__value_2 = None
        self.__status_operator = new_operator

    def get_operator(self):
        return self.__status_operator

    def enter_value_1(self, value):
        try:
            self.__value_1 = float(value)
        except ValueError:
            raise IllegalValueException(value)

    def get_value_1(self):
        return self.__value_1

    def enter_value_2(self, value):
        try:
            self.__value_2 = float(value)
        except ValueError:
            raise IllegalValueException(value)

    def get_value_2(self):
        return self.__value_2

    def get_result(self):
        result = self.__model.compute_result(self.__value_1, self.__value_2, self.__status_operator.value)
        self.__value_1 = result
        self.__value_2 = None
        self.__status_operator = None
        return result

