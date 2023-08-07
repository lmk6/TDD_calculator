class CalculatorModel:
    def add(self, *args):
        return sum(args)

    def subtract(self, *args):
        return args[0] - sum(args[1:])
