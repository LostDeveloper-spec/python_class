def camel_to_snake(camel_case: str):
    """
    Converts a camelCase string to snake_case.
    """
    snake_case = ""
    for char in camel_case:
        if char.isupper():  # If the character is uppercase
            snake_case += "_" + char.lower()  # Add an underscore
        else:
            snake_case += char  # Otherwise, keep the character as is
    return snake_case.lstrip("_")  # Remove any underscore


# Prompt user for input
camel_case_input = input("Enter a variable name in camelCase: ")

# Convert to snake_case and print the result
print("Snake case:", camel_to_snake(camel_case_input))
