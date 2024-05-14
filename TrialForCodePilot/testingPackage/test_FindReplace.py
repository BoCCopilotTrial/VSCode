import unittest
from sourcePackage.FindReplace import FindReplace

class TestFindReplace(unittest.TestCase):
    def test_find_replace(self):
        # Test case 1: Basic find and replace
        input_str = "Hello, world!"
        find_str = "world"
        replace_str = "universe"
        expected_output = "Hello, universe!"
        self.assertEqual(FindReplace(input_str, find_str, replace_str), expected_output)

        # Test case 2: Find and replace with empty string
        input_str = "Hello, world!"
        find_str = "world"
        replace_str = ""
        expected_output = "Hello, !"
        self.assertEqual(FindReplace(input_str, find_str, replace_str), expected_output)

        # Test case 3: Find and replace with special characters
        input_str = "Hello, world!"
        find_str = "world"
        replace_str = "@#$"
        expected_output = "Hello, @#$!"
        self.assertEqual(FindReplace(input_str, find_str, replace_str), expected_output)

        # Test case 4: Find and replace with multiple occurrences
        input_str = "Hello, world! Hello, world!"
        find_str = "world"
        replace_str = "universe"
        expected_output = "Hello, universe! Hello, universe!"
        self.assertEqual(FindReplace(input_str, find_str, replace_str), expected_output)

if __name__ == '__main__':
    unittest.main()