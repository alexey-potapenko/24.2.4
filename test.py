import pytest

from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding(self):
        assert self.calc.adding(self, 3, 4) == 7

    def test_substuct(self):
        assert self.calc.substruction(self, 9, 4)

    def test_multiply(self):
        assert self.calc.multiply(self, 8, 9)
    def test_divide(self):
        assert self.calc.division(self, 8, 4)


    def teardown(self):
        print('Выполнение метода Teardown')