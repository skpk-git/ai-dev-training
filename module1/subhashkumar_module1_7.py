# subhashkumar_module1_7.py

# make python code to accept only string and display it 
# (try. Except). If the pass value is not a string return NULL 

# import os to clear console
import os

def clear_console():
    """Clear the console screen."""

    # Use cls for Windows and clear for Linux/macOS.
    os.system("cls" if os.name == "nt" else "clear")

def accept_string(value):
    """Accept a string and return it; return None for other data types."""

    try:
        # Check whether the value is a string.
        if isinstance(value, str):
            return value
        else:
            raise TypeError("The given value must be a string.")

        # Return None if the value is not a string.
        #return None

    # except TypeError:
    #     # Return None if an unexpected error occurs.
    #     return None
    except Exception as X:
        #print(f"Unhandled exception: {X}")
        return None
    finally:
        pass
        #print("Final block: Do some cleanup here!")

# Clear the console screen.
clear_console()

# Test the function with a string.
print(accept_string("Hello World"))

# Test the function with an integer.
print(accept_string(123))

# Test the function with a floating-point number.
print(accept_string(10.5))

# Test the function with a Boolean value.
print(accept_string(True))