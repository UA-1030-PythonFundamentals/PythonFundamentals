import unittest

from funktions import largest


class MyTestCase(unittest.TestCase):

    def test_something_1(self):
        actual = largest(10, 10)
        self.assertEqual("Two number are equal", actual)

    def test_something_2(self):
        actual = largest(10, 1)
        self.assertEqual("The largest number is 10", actual)

    def test_something_3(self):
        actual = largest(-10, 1)
        self.assertEqual("The largest number is 1", actual)

    def test_something_4(self):
        actual = largest(50, 49)
        self.assertEqual(540, actual)

    def test_something_5(self):
        actual = largest(500, 490)
        self.assertEqual("foo", actual)

    def test_something_fail(self):
        actual = largest(10, 1)
        self.assertEqual("Two number are equal", actual, "test")  #
    # add assertion here


if __name__ == '__main__':
    unittest.main()
