# subhashkumar_module3_3.py

# make an api if "Text"missing return 422 with JSON error. Learn about 422      

# Install FastAPI and Uvicorn
# pip install fastapi uvicorn


from fastapi import FastAPI
from pydantic import BaseModel


# Create the FastAPI application.
app = FastAPI()


class TextRequest(BaseModel):
    """Define the JSON data expected by the API."""

    # FastAPI/Pydantic understands that Text is required.
    # Text is a required field.
    Text: str


@app.post("/text")
def receive_text(data: TextRequest):
    """Receive text and return it as a JSON response."""

    # Return the received text.
    return {
        "message": data.Text
    }


# Start the FastAPI server
# python -m uvicorn subhashkumar_module3_3:app --reload
# {
#     "Text": "Hello Python"
# }
# http://127.0.0.1:8000/docs