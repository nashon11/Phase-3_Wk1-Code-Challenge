def convert_to_24_hour(time_str):
    time_parts = time_str.split()
    hour, minute = map(int, time_parts[0].split(':'))
    period = time_parts[1].lower()

    if period == 'pm' and hour != 12:
        hour += 12
    elif period == 'am' and hour == 12:
        hour = 0

    return f'{hour:02d}{minute:02d}'

# Test cases
print(convert_to_24_hour("8:30 am"))  # Output: 0830
print(convert_to_24_hour("3:45 pm"))  # Output: 1545
