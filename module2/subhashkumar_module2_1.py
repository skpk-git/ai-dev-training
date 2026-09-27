# subhashkumar_module2_1.py

# make python function to show if a number is even or odd.   

def check_even_or_odd(number):
    """Check whether a number is even or odd."""

    # A number is even if it can be divided by 2 with no remainder.
    if number % 2 == 0:
        return "Even"

    # Otherwise, the number is odd.
    return "Odd"


# Get a number from the user.
number = int(input("Enter a number: "))

# Call the function and display the result.
result = check_even_or_odd(number)

print("The number is:", result)
