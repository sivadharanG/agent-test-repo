def is_palindrome(s: str) -> bool:
    """
    Checks if the given string is a palindrome.

    This function first removes non-alphanumeric characters and converts the string to lowercase.
    Then, it checks if the modified string is the same when reversed.

    Args:
        s (str): The input string to be checked.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_s = ''.join(char.lower() for char in s if char.isalnum())
    
    # Compare the cleaned string with its reverse
    return cleaned_s == cleaned_s[::-1]


# Test cases
def main():
    # Empty string
    print(is_palindrome(""))  # Expected output: True

    # Single character
    print(is_palindrome("a"))  # Expected output: True

    # Mixed case
    print(is_palindrome("Aba"))  # Expected output: True

    # Non-alphanumeric characters
    print(is_palindrome("A man, a plan, a canal: Panama"))  # Expected output: True

    # Not a palindrome
    print(is_palindrome("hello"))  # Expected output: False

if __name__ == "__main__":
    main()