# subhashkumar_module3_4.py

# make log file to store all request method, path, status to console + file my_file.log    

from fastapi import FastAPI, Request
from pydantic import BaseModel
import logging
import time

# Create the FastAPI application.
app = FastAPI()


# Configure logging.
# The log will be written to both the console and my_file.log.
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),                 # Display log in console.
        logging.FileHandler("my_file.log")       # Save log to file.
    ]
)

# Create a logger.
logger = logging.getLogger(__name__)


class Person(BaseModel):
    """Define the information required for a person."""

    # Person's name.
    name: str

    # Person's phone number.
    phone_number: str

#Middleware runs for every HTTP request, so  don't need to put logging code separately inside every API endpoint.

@app.middleware("http")
async def log_requests(request: Request, call_next):
    """Log every HTTP request method, path, and status code."""

    # Record the start time of the request.
    start_time = time.time()

    # Process the request and get the response.
    response = await call_next(request)

    # Calculate how long the request took.
    duration = time.time() - start_time

    # Create the log message.
    log_message = (
        f"Method={request.method} "
        f"Path={request.url.path} "
        f"Status={response.status_code} "
        f"Duration={duration:.3f}s"
    )

    # Write the log to console and my_file.log.
    logger.info(log_message)

    # Return the response to the client.
    return response


@app.post("/person")
def create_person(person: Person):
    """Receive a person's details and return them."""

    # Return the person's information.
    return {
        "name": person.name,
        "phone_number": person.phone_number
    }


@app.get("/person")
def get_person():
    """Return a sample person."""

    return {
        "name": "Mohamed",
        "phone_number": "0501234567"
    }

# Start the FastAPI server
# python -m uvicorn subhashkumar_module3_5:app --reload
# http://127.0.0.1:8000/docs
# POST /person
# GET /person