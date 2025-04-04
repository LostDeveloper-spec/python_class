def is_valid(s: str):
    """
    Checks if a given vanity plate is valid based on Massachusetts rules.
    """
    if not (2 <= len(s) <= 6):
        return False
    
    if not s[:2].isalpha():
        return False
    
    if not s.isalnum():
        return False
    
    number_started = False
    for i, char in enumerate(s):
        if char.isdigit():
            if char == '0' and number_started is False:
                return False
            number_started = True
        elif number_started:
            return False
    
    return True


plate = input("Plate: ")

if is_valid(plate):
    print("Valid")
else:
    print("Invalid")