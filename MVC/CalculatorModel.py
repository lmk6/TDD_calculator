class IllegalValueException(Exception):
    def __init__(self, value):
        super().__init__(f"Cannot Perform operations on the received value! -- <{value}>")


class CalculatorModel:

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
            result /= arg

        return result

    def check_for_illegal_value(self, args):
        for arg in args:
            if not isinstance(arg, (float, int)):
                raise IllegalValueException(arg)
