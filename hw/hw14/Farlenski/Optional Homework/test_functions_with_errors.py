import unittest
from functions_with_errors import greeting_by_name, get_symbol_position, merge


class GreetingUnitTest(unittest.TestCase):
    def test_greeting_with_valid_name(self):
        greeting_success = greeting_by_name("Vadym")
        self.assertEqual(greeting_success, "Hello Vadym!")

    def test_greeting_with_empty_name(self):
        result = greeting_by_name("")
        self.assertEqual(result, "Hello !")


class GetSymbolUnitTest(unittest.TestCase):
    def test_get_symbol_success(self):
        position = get_symbol_position("zxcvbn", "v")
        self.assertEqual(position, 4)

    def test_get_symbol_with_double_symbol(self):
        position = get_symbol_position("zxcvbn", "vv")
        self.assertEqual(position, 'Error! Symbol can be string with only one letter')

    def test_get_symbol_without_necessary_symbol(self):
        position = get_symbol_position("zxcvbn", "m")
        self.assertEqual(position, 'Not found')


class MergeUnitTest(unittest.TestCase):
    def test_merge_success(self):
        updated_dict = merge({'a': 1, 'b': 2}, {'c': 3, 'd': 4})
        self.assertEqual(updated_dict, {'a': 1, 'b': 2, 'c': 3, 'd': 4})

    def test_merge_with_empty_dict(self):
        self.assertRaises(AttributeError, merge, "", {1: "a", 2: "b", 3: "c"})

    def test_original_dict1_modified(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        merge(dict1, dict2)
        self.assertEqual(dict1, {'a': 1, 'b': 3, 'c': 4})

    def test_original_dict2_unchanged(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        merge(dict1, dict2)
        self.assertEqual(dict2, {'b': 3, 'c': 4})