from unittest import TestCase
from calculator import Calculator

class TestCalculator(TestCase):
    def setUp(self):
        print("hey")
        self.calc = Calculator()

    def test_sum(self):
        answer = self.calc.sum(2, 4)
        self.assertEqual(answer, 6)

#https://semaphoreci.com/community/tutorials/getting-started-with-mocking-in-python
#python -m unittest
