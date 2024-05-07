def get_season(month):
    if month in [1, 2, 12]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    elif month in [9, 10, 11]:
        return "Autumn"
    else:
        return "Error: Please enter a number between 1 and 12."

# Get input from the user
user_input = input("Enter the number of the month: ")

# Check if the input is a valid integer between 1 and 12
if user_input.isdigit():
    month = int(user_input)
    if 1 <= month <= 12:
        season = get_season(month)
        print("The season for month", month, "is:", season)
    else:
        print("Error: Please enter a number between 1 and 12.")
else:
    print("Error: Please enter a valid integer.")
