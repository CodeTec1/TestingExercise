def test_roman_to_integer():
    test_cases = {
        "I": 1,             
        "V": 5,             
        "XI": 11,           
        "IV": 4,            
        "XIV": 14,          
        "XV": 15,           
        "II": 2,            
        "Z": "Invalid Roman numeral: Z",  
        "XIZ": "Invalid Roman numeral: Z",  
        "VV": "Invalid Roman numeral: VV",  
        "": 0  
    }

    for roman, expected in test_cases.items():
        try:
            # Import the roman_to_integer function
            from roman_to_integer import roman_to_integer
            result = roman_to_integer(roman)
            assert result == expected, f"Test failed for '{roman}': expected {expected}, got {result}"
            print(f"Test passed for '{roman}': {result}")
        except ValueError as e:
            assert str(e) == expected, f"Test failed for '{roman}': expected {expected}, got {str(e)}"
            print(f"Test passed for '{roman}': {str(e)}")


if __name__ == "__main__":
    test_roman_to_integer()
