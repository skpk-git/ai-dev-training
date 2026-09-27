# subhashkumar_module2_3.py

# make python function for a given list of numbers. Find the unique list of numbers. 

def find_unique_numbers(numbers):
    """Return a list containing only unique numbers."""

    # Create an empty list to store unique numbers.
    unique_numbers = []

    # Go through each number in the input list.
    for number in numbers:

        # Check whether the number is already in the unique list.
        if number not in unique_numbers:

            # Add the number if it is not already present.
            unique_numbers.append(number)

    # Return the list of unique numbers.
    return unique_numbers


# Create a list of numbers.
numbers = [10, 20, 10, 30, 20, 40, 50, 30]

# Find the unique numbers.
result = find_unique_numbers(numbers)

# Display the result.
print("Original list:", numbers)
print("Unique list:", result)