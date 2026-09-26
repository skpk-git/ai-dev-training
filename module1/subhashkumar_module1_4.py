# subhashkumar_module1_4.py

# make python function to return today date 
# in this format (ss:mm:hh , day/month/year)

# import os to clear console
import os
from datetime import datetime


def get_current_date_time():
    """Return today's date and current time in the required format."""

    # Get the current date and time.
    current_datetime = datetime.now()

    # Format the time as seconds:minutes:hours and date as day/month/year.
    #formatted_datetime = current_datetime.strftime("%S:%M:%H, %d/%mm/%Y")

    formatted_datetime = current_datetime.strftime("%S:%M:%H, %d/%b/%Y")

    # Return the formatted date and time.
    return formatted_datetime



def generate_fibonacci_sequence():
    """Generate 2 times the current minute number of Fibonacci numbers."""

    # Get the current minute from the system time.
    current_minute = datetime.now().minute

    # Calculate how many Fibonacci numbers to generate.
    number_of_terms = current_minute * 2

    print("Fibonacci upto: ", number_of_terms)
    # Start the Fibonacci sequence with 0 and 1.
    first_number = 0
    second_number = 1

    # Store the Fibonacci numbers in a list.
    fibonacci_sequence = []

    # Generate the required number of Fibonacci numbers.
    for _ in range(number_of_terms):
        #print("range: ", _)
        fibonacci_sequence.append(first_number)

        # Calculate the next Fibonacci number.
        next_number = first_number + second_number

        # Move to the next two numbers.
        first_number = second_number
        second_number = next_number

    # Return the complete Fibonacci sequence.
    return fibonacci_sequence

def clear_console():
    """Clear the console screen."""

    # Use cls for Windows and clear for Linux/macOS.
    os.system("cls" if os.name == "nt" else "clear")




if __name__ == "__main__":

    clear_console()

    # Call the function and print the result.
    print(get_current_date_time.__doc__)
    print(get_current_date_time())

    # Generate and display the Fibonacci sequence.
    print(generate_fibonacci_sequence.__doc__)
    sequence = generate_fibonacci_sequence()

    print("Fibonacci sequence:")
    print(sequence)