# subhashkumar_module3_4.py

# make python code to make an API POST person (name, phone number). 
# make python code to read person from previous API and add random number then display it.      

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


@app.post("/person")
def create_person(person: Person):
    """Receive a person's details and return them."""

    # Return the person's information as JSON.
    return {
        "name": person.name,
        "phone_number": person.phone_number
    }

# Start the FastAPI server
# python -m uvicorn subhashkumar_module3_3:app --reload
# http://127.0.0.1:8000/docs
# {
#     "name": "Mohamed",
#     "phone_number": "0501234567"
# }