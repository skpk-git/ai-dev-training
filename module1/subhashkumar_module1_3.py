# subhashkumar_module1_3.py

# make python function to print any type variable. 
# It should return (variable content + data type). 

def print_variable(variable):
    """Return the variable content and its data type."""

    # Get the name of the data type without <class ''>.
    data_type = type(variable).__name__

    # Return the content and data type as a string.
    return f"Content: {variable}, Data type: {data_type}"


# Test the function with different data types.
print(print_variable(10))
print(print_variable("Hello"))
print(print_variable(10.5))
print(print_variable(True))
