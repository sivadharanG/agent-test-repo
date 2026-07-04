import re
import unittest

def is_palindrome(s: str) -> bool:
    """
    Checks if the given string is a palindrome, ignoring non-alphanumeric characters and case sensitivity.

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Remove non-alphanumeric characters and convert to lower case
    cleaned_s = re.sub(r'\W+', '', s).lower()
    # Compare the cleaned string with its reverse
    return cleaned_s == cleaned_s[::-1]


class TestPalindromeChecker(unittest.TestCase):
    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

    def test_single_character(self):
        self.assertTrue(is_palindrome("a"))

    def test_mixed_case_input(self):
        self.assertTrue(is_palindrome("Aba"))

    def test_string_with_special_characters(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))

    def test_string_with_numbers(self):
        self.assertFalse(is_palindrome("wasitacaroracatisaw12321"))

    def test_valid_palindrome(self):
        self.assertTrue(is_palindrome("madam"))

if __name__ == '__main__':
    unittest.main()