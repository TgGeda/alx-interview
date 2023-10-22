#!/usr/bin/python3
"""UTF-8 validation module."""


def validUTF8(data):
    """
    Checks if a list of integers represents valid UTF-8 codepoints.
    
    Args:
        data (list): A list of integers representing UTF-8 codepoints.
    
    Returns:
        bool: True if the input data is a valid UTF-8 sequence, False otherwise.
    """
    # Variable to track the number of bytes to skip
    skip = 0
    
    # Length of the input data
    n = len(data)
    
    # Iterate over each integer in the data
    for i in range(n):
        # If there are bytes to skip, continue to the next iteration
        if skip > 0:
            skip -= 1
            continue
        
        # Check if the integer is a valid codepoint
        if type(data[i]) != int or data[i] < 0 or data[i] > 0x10ffff:
            return False
        
        # Check for 1-byte UTF-8 character encoding
        elif data[i] <= 0x7f:
            skip = 0
        
        # Check for 4-byte UTF-8 character encoding
        elif data[i] & 0b11111000 == 0b11110000:
            span = 4
            if n - i >= span:
                # Check the continuation bytes in the sequence
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + span],
                ))
                if not all(next_body):
                    return False
                skip = span - 1
            else:
                return False
        
        # Check for 3-byte UTF-8 character encoding
        elif data[i] & 0b11110000 == 0b11100000:
            span = 3
            if n - i >= span:
                # Check the continuation bytes in the sequence
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + span],
                ))
                if not all(next_body):
                    return False
                skip = span - 1
            else:
                return False
        
        # Check for 2-byte UTF-8 character encoding
        elif data[i] & 0b11100000 == 0b11000000:
            span = 2
            if n - i >= span:
                # Check the continuation bytes in the sequence
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + span],
                ))
                if not all(next_body):
                    return False
                skip = span - 1
            else:
                return False
        
        # Invalid UTF-8 encoding
        else:
            return False
    
    # All checks passed, the data is a valid UTF-8 sequence
    return True