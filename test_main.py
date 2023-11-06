import unittest
from main import divide

class TestMain(unittest.TestCase):
    def test_divide(self):
        result = divide(10, 2)
        self.assertEqual(result, 5)

        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

        with self.assertRaises(Exception):
            divide('10', 2)

if __name__ == '__main__':
    unittest.main()
