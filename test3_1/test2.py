from unittest import TestCase
from unittest.mock import patch
from calculator import Calculator

'''
https://stackoverflow.com/questions/29152170/what-is-the-difference-between-mock-patch-object-and-mock-patch

mock.patch() takes a string which will be resolved to an object when applying the patch, mock.patch.object() takes a direct reference.
This means that mock.patch() doesn't require that you import the object before patching, while mock.patch.object() does require that you import before patching.

The latter is then easier to use if you already have a reference to the object.


'''


class TestCalculator(TestCase):
    def setUp(self):
        pass

    @patch.object(Calculator, 'summ', return_value="mocked success")
    def test_sum(self, mock_object):
        print(mock_object())
        self.assertEqual(mock_object(2, 3), "mocked success")
#
# #python -m unittest
