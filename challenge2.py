def are_two_positive(a, b, c):
    positive_count = 0
    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1
    
    return positive_count == 2

# Test cases
print(are_two_positive(2, 4, -3))  # Output: True
print(are_two_positive(-4, 6, 8))  # Output: True
print(are_two_positive(0, 6, -2))  # Output: False
