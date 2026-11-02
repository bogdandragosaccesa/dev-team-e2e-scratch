import unittest

from app import add, subtract


class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-1, 1), 0)

    def test_subtract_positive(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_subtract_negative(self):
        self.assertEqual(subtract(3, 5), -2)

    def test_subtract_zero(self):
        self.assertEqual(subtract(4, 4), 0)


if __name__ == "__main__":
    unittest.main()
