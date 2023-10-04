#!/usr/bin/python3

def roman_to_int(roman_string):

    """
    Convert a Roman numeral to an integer.

    Args:
        roman_string (str): a string representing a Roman numeral.

    Returns:
        int: the integer equivalent of the input Roman numeral.
             Returns 0 if the input is invalid (not a string)
             or if it is outside the range of 1 to 3999.
    """
    if not roman_string or not isinstance(roman_string, str):
        return 0

    roman_dictionary = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    roman_char = 'I'
    roman_int = 0
    prev_roman = 0

    for roman_char in roman_string[::-1]:

        current_roman = roman_dictionary.get(roman_char, 0)

        if current_roman < prev_roman:
            roman_int -= current_roman
        else:
            roman_int += current_roman

        prev_roman = current_roman

    if not (1 <= roman_int <= 3999):
        return 0

    return roman_int
