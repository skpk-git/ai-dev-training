# subhashkumar_module3_4.py

# make python code to make an API POST person (name, phone number). 
# make python code to read person from previous API and add random number then display it.      

from urllib.request import urlopen
import random
import json
from fastapi import FastAPI
from pydantic import BaseModel


# Create the FastAPI application.
app = FastAPI()


class Person(BaseModel):
    """Define the information required for a person."""

    # Person's name.
    name: str

    # Person's phone number.
    phone_number: str

#g_person = Person()
sample_person = [
    {"name": "Hrishikesh", "phone_number": "12345678"},
    {"name": "Vasudev", "phone_number": "12345678"}
]

@app.post("/person")
def create_person(person: Person):
    """Receive a person's details and return them."""
    new_person = {
        "name": person.name,
        "phone_number": person.phone_number
    }
    sample_person.append(new_person)
    # Return the person's information as JSON.
    return new_person

@app.get("/getperson")
def get_person():
    """Receive a person's details and return them."""

    # Return the person's information as JSON.
    return sample_person



def get_person_from_api():
    """Read person information from the previous API."""

    # API URL.
    api_url = "http://127.0.0.1:8000/getperson"
    # response = urlopen(api_url)
    # print(response.read().decode())

    # Open the API URL and get the response.
    with urlopen(api_url) as response:

        # Read the response data.
        response_data = response.read()

        # Convert the JSON response into a Python dictionary.
        persons = json.loads(response_data)

    # Return the person information.
    return persons


def add_random_number(person):
    """Add a random number to the person information."""

    # Generate a random number between 1 and 100.
    random_number = random.randint(1, 100)

    # Add the random number to the dictionary.
    person["random_number"] = random_number

    # Return the updated person.
    return person

def main():
    """Read a person, add a random number, and display it."""

    # Get the person from the API.
    persons = get_person_from_api()

    for person in persons:
        

        # Add a random number to the person.
        person = add_random_number(person)

        # Display the result.
        print("Person information:")
        print(person)


if __name__ == "__main__":
    main()


# Start the server
# python -m uvicorn subhashkumar_module3_4:app --reload
# http://127.0.0.1:8000/docs
# {
#     "name": "Mohamed",
#     "phone_number": "0501234567"
# }