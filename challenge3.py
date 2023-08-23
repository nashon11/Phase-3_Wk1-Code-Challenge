def solve(word):
    consonant_values = {'a': 0, 'b': 2, 'c': 3, 'd': 4, 'e': 0,
                        'f': 6, 'g': 7, 'h': 8, 'i': 0, 'j': 10,
                        'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 0,
                        'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
                        'u': 0, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    
    max_value = 0
    current_value = 0
    
    for char in word:
        if char in consonant_values:
            current_value += consonant_values[char]
            max_value = max(max_value, current_value)
        else:
            current_value = 0
    
    return max_value

# Test cases
print(solve("zodiacs"))  # Output: 26
print(solve("strength"))  # Output: 57
print(solve("aeiou"))  # Output: 0
