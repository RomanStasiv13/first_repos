import unittest
from homework16 import homework16_function_examples


# Task1
# Pick your solution to one of the exercises in this module.
# Design tests for this solution and write tests using unittest library.

class TypeDecoratorsTestCases(unittest.TestCase):
    def test_type_decorators(self):
        value1 = homework16_function_examples.to_int('6')
        value2 = homework16_function_examples.to_str(32)
        value3 = homework16_function_examples.to_float(13)
        value4 = homework16_function_examples.to_bool(10 > 3)
        self.assertEqual(value1, 6)
        self.assertEqual(value2, '32')
        self.assertEqual(value3, 13.0)
        self.assertEqual(value4, True)

if __name__ == '__main__':
    unittest.main








