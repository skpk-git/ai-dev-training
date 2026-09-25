# subhashkumar_module1_1_addnums.py
# This file contains a simple add number function, performs one mathematical operation.

"""
This program performs basic add operatios.
used for docstring a test
"""

import sys

def add(a, b):
    """Add two numbers and return the result."""
    
    # Add the two input numbers.
    return a + b

# call the add function and print the result when this file is executed directly.
if __name__ == "__main__":
    a = int(sys.argv[1])
    b = int(sys.argv[2])

    print(__doc__)
    print("Result:", add(a, b))
    print(add.__doc__)
    
    