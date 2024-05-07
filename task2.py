def swap_digits(number):
    # Convert the number to a string to easily access its digits
    number_str = str(number)

    # Check if the number is six digits long
    if len(number_str) != 6:
        return "Error: Please enter a valid six-digit number."

    # Swap the digits
    swapped_number = number_str[5] + number_str[1] + number_str[2] + number_str[3] + number_str[4] + number_str[0]

    return int(swapped_number)


# Get input from the user
user_input = input("Enter a six-digit number: ")

# Check if the input is a valid six-digit number
if user_input.isdigit():
    number = int(user_input)
    result = swap_digits(number)
    if isinstance(result, int):
        print("The swapped number is:", result)
    else:
        print(result)
else:
    print("Error: Please enter a valid six-digit number.")
