import unittest

import utils


class TestMathFunctions(unittest.TestCase):

    def test_add(self):
        result = utils.add(1, 2)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
