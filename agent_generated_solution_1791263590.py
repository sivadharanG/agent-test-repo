import re
import unittest

def isPalindrome(s: str) -> bool:
    """
    Determine if the given string is a palindrome, ignoring case,
    spaces, punctuation, and other non‑alphanumeric characters.

    Args:
        s: Input string to check.

    Returns:
        True if the cleaned string reads the same forwards and backwards,
        False otherwise.
    """
    # Normalize: lowercase and keep only alphanumeric characters
    cleaned = re.sub(r'[^a-z0-9]', '', s.lower())
    # Compare with its reverse
    return cleaned == cleaned[::-1]

class TestIsPalindrome(unittest.TestCase):
    def test_palindrome_phrase(self):
        self.assertTrue(isPalindrome('A man, a plan, a canal: Panama'))

    def test_non_palindrome(self):
        self.assertFalse(isPalindrome('Hello World'))

if __name__ == "__main__":
    unittest.main()