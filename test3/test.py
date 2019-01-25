from unittest import TestCase
from unittest.mock import patch
import calculator


class TestCalculator(TestCase):
    def setUp(self):
        print("hey")

    @patch('calculator.Calculator.summ', return_value=9)
    def test_sum( self, mock_object):
        print(mock_object())
        self.assertEqual(mock_object(2, 3), 9)
#
# #python -m unittest
