from unittest import TestCase
from unittest.mock import patch

'''
https://stackoverflow.com/questions/29152170/what-is-the-difference-between-mock-patch-object-and-mock-patch

This means that mock.patch() doesn't require that you import the object before patching.
mock.patch() takes a string which will be resolved to an object when applying the patch.
'''

class TestCalculator(TestCase):
    def setUp(self):
        pass

    @patch('calculator.Calculator.summ', return_value="mocked success")
    def test_sum(self, mock_object):
        print(mock_object())
        self.assertEqual(mock_object(2, 3), "mocked success")
#
# #python -m unittest
