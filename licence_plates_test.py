from plates import is_valid

def test_too_short():
    assert is_valid("A") == False

def test_too_long():
    assert is_valid("ABCDEFG") == False

def test_invalid_start():
    assert is_valid("1ABC") == False
    assert is_valid("A1BC") == False

def test_leading_zero():
    assert is_valid("CS05") == False

def test_number_middle():
    assert is_valid("CS50P") == False

def test_valid_plates():
    assert is_valid("CS50") == True
    assert is_valid("OUTATIME") == False  # too long
    assert is_valid("ABC123") == True
    assert is_valid("AAA222") == True