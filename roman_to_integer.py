def roman_to_integer(roman):
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    
    non_repeatables = {'V', 'L', 'D'}  #  cannot be repeated
    repeatables = {'I', 'X', 'C', 'M'}  #  can be repeated, but only up to 3 times

    # Check for invalid patterns
    for char in non_repeatables:
        if roman.count(char) > 1:
            raise ValueError(f"Invalid Roman numeral: {roman}")
    for char in repeatables:
        if char * 4 in roman:  # Check for more than 3 repetitions
            raise ValueError(f"Invalid Roman numeral: {roman}")
    
    
    integer_value = 0

    
    for i in range(len(roman)):
        current_value = roman_values.get(roman[i], None)
        if current_value is None:
            raise ValueError(f"Invalid Roman numeral: {roman[i]}")
        
        if i + 1 < len(roman):
            next_value = roman_values.get(roman[i + 1], None)
            if next_value is None:
                raise ValueError(f"Invalid Roman numeral: {roman[i + 1]}")
            if next_value > current_value:
                integer_value -= current_value
            else:
                integer_value += current_value
        else:
            integer_value += current_value

    return integer_value
