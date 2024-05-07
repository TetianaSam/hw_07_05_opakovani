def is_lucky(number):
    # Convert the number to a string to easily access its digits
    number_str = str(number)

    # Check if the number is six digits long
    if len(number_str) != 6:
        return False

    # Calculate the sum of the first three digits
    first_half_sum = sum(int(digit) for digit in number_str[:3])

    # Calculate the sum of the last three digits
    last_half_sum = sum(int(digit) for digit in number_str[3:])

    # Check if the sums are equal
    return first_half_sum == last_half_sum


# Get input from the user
user_input = input("Enter a six-digit number: ")

# Check if the input is a valid six-digit number
if user_input.isdigit():
    number = int(user_input)
    if is_lucky(number):
        print("The number", number, "is lucky!")
    else:
        print("The number", number, "is not lucky.")
else:
    print("Error: Please enter a valid six-digit number.")
