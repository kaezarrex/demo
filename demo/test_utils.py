import unittest

import utils


class TestMathFunctions(unittest.TestCase):

    def test_add(self):
        result = utils.add(1, 2)
        self.assertEqual(result, 3)

    def test_subtract(self):
        result = utils.subtract(1, 2)
        self.assertEqual(result, -1)


if __name__ == '__main__':
    unittest.main()
