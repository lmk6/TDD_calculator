from enum import Enum


class Operator(Enum):
    ADD = '+'
    SUB = '-'
    MUL = '*'
    DIV = '/'


class CalculatorController:

    def __init__(self):
        self.__status_operator = None
        self.__value_1 = None
        self.__value_2 = None

    def change_operator(self, new_operator):
        self.__status_operator = new_operator

    def get_operator(self):
        return self.__status_operator

    def enter_value_1(self, value):
        self.__value_1 = float(value)

    def get_value_1(self):
        return self.__value_1

    def enter_value_2(self, value):
        self.__value_2 = float(value)

    def get_value_2(self):
        return self.__value_2
