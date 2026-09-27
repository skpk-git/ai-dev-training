# subhashkumar_module2_4.py

# make python function to store a class type 
# containing ( name , number , location , job title ) for 5 random people in Json file using json format. 
# Create class and json file. 

import json


class Person:
    """Store information about a person."""

    def __init__(self, name, number, location, job_title):
        # Store the person's name.
        self.name = name

        # Store the person's phone number.
        self.number = number

        # Store the person's location.
        self.location = location

        # Store the person's job title.
        self.job_title = job_title

    def to_dictionary(self):
        """Convert the Person object into a dictionary."""

        # Return the person's information as a dictionary.
        return {
            "name": self.name,
            "number": self.number,
            "location": self.location,
            "job_title": self.job_title
        }


def create_people_json():
    """Create 5 people and save their information in a JSON file."""

    # Create 5 Person objects with sample information.
    person1 = Person(
        "Ibrahim Javid",
        "0501234567",
        "Abu Dhabi",
        "Software Developer"
    )

    person2 = Person(
        "Khalid Alshehi",
        "0502345678",
        "Abu Dhabi",
        "Project Manager"
    )

    person3 = Person(
        "Paulson Peter",
        "0503456789",
        "Dubai",
        "Data Analyst"
    )

    person4 = Person(
        "Raymond Pareded",
        "0504567890",
        "Abu Dhabi",
        "Business Analyst"
    )

    person5 = Person(
        "Renjith Paniker",
        "0505678901",
        "Al Ain",
        "System Administrator"
    )

    # Store all Person objects in a list.
    people = [
        person1,
        person2,
        person3,
        person4,
        person5
    ]

    # Convert each Person object into a dictionary.
    people_data = []

    for person in people:
        people_data.append(person.to_dictionary())

    # Open the JSON file in write mode.
    with open("people.json", "w") as file:

        # Write the people information to the JSON file.
        json.dump(people_data, file, indent=4)

        #print Json string prepared
        json_string = json.dumps(people_data,  indent=4)
        print(json_string)

    
    # Display a success message.
    print("5 people's information saved to people.json")


# Call the function.
create_people_json()