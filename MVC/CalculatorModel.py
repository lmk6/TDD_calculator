class IllegalValueException(Exception):
    def __init__(self, value):
        super().__init__(f"Cannot Perform operations on the received value! -- <{value}>")


class DivisionByZeroException(Exception):
    def __init__(self):
        super().__init__("Cannot divide by zero!!!")


class CalculatorModel:

    def compute_result(self, val1, val2, operator):
        result = None
        if operator == '+':
            result = self.add(val1, val2)
        elif operator == '-':
            result = self.subtract(val1, val2)
        elif operator == '*':
            result = self.multiply(val1, val2)
        elif operator == '/':
            result = self.divide(val1, val2)

        return result

    def add(self, *args):
        self.check_for_illegal_value(args)
        return sum(args)

    def subtract(self, *args):
        self.check_for_illegal_value(args)
        return args[0] - sum(args[1:])

    def multiply(self, *args):
        self.check_for_illegal_value(args)
        result = args[0]
        for arg in args[1:]:
            result *= arg

        return result

    def divide(self, *args):
        self.check_for_illegal_value(args)
        result = args[0]
        for arg in args[1:]:
            if arg == 0:
                raise DivisionByZeroException
            result /= arg

        return result

    def check_for_illegal_value(self, args):
        for arg in args:
            if not isinstance(arg, (float, int)):
                raise IllegalValueException(arg)
