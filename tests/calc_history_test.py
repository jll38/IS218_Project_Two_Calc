"""Testing the Calculator History"""
from calculator.history import Calculations

def test_calculation_is_instance():
    """Testing the Calculator"""
    calculation = Calculations()
    assert isinstance(calculation, Calculations)

