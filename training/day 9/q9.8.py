week_number = int(input("Enter a week number (1-7): "))

if 1 <= week_number <= 7:
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    print("Weekday:", weekdays[week_number - 1])
else:
    print("Invalid week number")
