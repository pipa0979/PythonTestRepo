import unittest
import logging


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        logging.info("called test_upper")
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        logging.info("called test_isupper")
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    unittest.main()

'''
python test.py TestStringMethods.test_isupper
'''
