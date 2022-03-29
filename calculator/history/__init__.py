from calculator import Calculator
class Calculations:
    history = []
    calc = Calculator()
    def add_history(self):
        return self.history.append(self.calc.get_result())
