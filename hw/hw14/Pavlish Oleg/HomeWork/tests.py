import unittest

from functions_with_errors import greeting_by_name, get_symbol_position, merge


class MyTestCase(unittest.TestCase):

    def test_greeting_by_name(self):
        actual = greeting_by_name("Name")
        self.assertEqual("Hello Name!", actual)

    def test_incorrect_symbol(self):
        actual = get_symbol_position('qwerty', 'qq')
        self.assertEqual("Error! Symbol can be string with only one letter", actual)

    def test_get_symbol_position(self):
        actual = get_symbol_position('qwerty', 'q')
        self.assertEqual(1, actual)

    def test_symbol_not_found(self):
        actual = get_symbol_position('qwerty', 'a')
        self.assertEqual("Not found", actual)

    def test_merge(self):
        dict1 = {1: 'one', 2: 'two'}
        dict2 = {3: "three"}
        actual = merge(dict1, dict2)
        self.assertEqual({1: 'one', 2: 'two', 3: 'three'}, actual)

    def test_dict1_immutability(self):
        dict1 = {1: 'one', 2: 'two'}
        dict2 = {3: "three"}
        merge(dict1, dict2)
        actual = dict1
        self.assertEqual({1: 'one', 2: 'two'}, actual)

    def test_dict2_immutability(self):
        dict1 = {1: 'one', 2: 'two'}
        dict2 = {3: "three"}
        merge(dict1, dict2)
        actual = dict2
        self.assertEqual({3: "three"}, actual)


if __name__ == '__main__':
    unittest.main()
