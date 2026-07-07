def count_vowels(input_string: str) -> int:
    """
    Returns the number of vowels in the input string.

    Args:
        input_string (str): The string to count vowels in.

    Returns:
        int: The number of vowels in the input string.
    """
    # Convert the input string to lowercase to simplify vowel matching
    input_string = input_string.lower()
    
    # Initialize a counter variable to zero
    vowel_count = 0
    
    # Iterate over each character in the string
    for char in input_string:
        # Check each character against the set of vowels and increment the counter if it matches
        if char in 'aeiou':
            vowel_count += 1
    
    # Return the final count of vowels
    return vowel_count

# Example usage:
print(count_vowels("Hello World"))  # Output: 3