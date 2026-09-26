# subhashkumar_module1_6.py

# make python function to make a class 
# to save address of person (name, contact, address, phone number). 
# The use will input the values. 
# The address should be saved in .text file 

# import os to clear console
import os

class PersonAddress:
    """Store the contact and address details of a person."""

    def __init__(self, name, contact, address, phone_number):
        # Store the person's name.
        self.name = name

        # Store the contact information.
        self.contact = contact

        # Store the person's address.
        self.address = address

        # Store the person's phone number.
        self.phone_number = phone_number

    def save_to_file(self):
        """Save the person's address details to a text file."""

        # Open the text file in write mode.
        with open("address.txt", "w") as file:

            # Write each person's detail to the file.
            file.write(f"Name: {self.name}\n")
            file.write(f"Contact: {self.contact}\n")
            file.write(f"Address: {self.address}\n")
            file.write(f"Phone Number: {self.phone_number}\n")

def create_person_address():
    """Get user input and create a PersonAddress object."""

    # Get the person's details from the user.

    name = input("Enter name: ")
    contact = input("Enter contact: ")
    address = input("Enter address: ")
    phone_number = input("Enter phone number: ")

    # Create a PersonAddress object using the entered information.
    # Create and return the person address object.
    return PersonAddress(name, contact, address, phone_number)


# Save the person's information to the text file.
#person.save_to_file()

# Inform the user that the information was saved.
#print("Address saved successfully to address.txt")

def clear_console():
    """Clear the console screen."""

    # Use cls for Windows and clear for Linux/macOS.
    os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    clear_console()


    # Create the address object from user input.
    person = create_person_address()

    # Save the address to a text file.
    person.save_to_file()

    print("Address saved successfully.")