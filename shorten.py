def shorten(text: str) -> str:
    """
    Removes all vowels (A, E, I, O, U) from the given text.
    """
    vowels = "AEIOUaeiou"
    return "".join(char for char in text if char not in vowels)


# Prompt user for input
user_input = input("Input: ")

# Print the shortened text
print("Output:", shorten(user_input))
