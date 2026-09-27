# subhashkumar_module3_2.py

# make python code using fast API to POST a message 
# with server time stamp     

# Install FastAPI and Uvicorn
# pip install fastapi uvicorn


from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime


# Create the FastAPI application.
app = FastAPI()


class Message(BaseModel):
    """Define the structure of the message received by the API."""

    # Store the message sent by the client.
    message: str


@app.post("/message")
def create_message(data: Message):
    """Receive a message and return it with the server timestamp."""

    # Get the current date and time from the server.
    server_time = datetime.now()

    # Return the message and server timestamp as JSON.
    return {
        "message": data.message,
        "server_timestamp": server_time.isoformat()
    }


# Start the FastAPI server
# python -m uvicorn subhashkumar_module3_2:app --reload

# http://127.0.0.1:8000/docs
# POST /message
# {
#     "message": "Hello from Python"
# }