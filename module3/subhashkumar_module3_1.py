# subhashkumar_module3_1.py

# make python code using fast API to return a message with person name 
# (/hello?name = Subhash ) - >{"message": "Hello Subhash"   


from fastapi import FastAPI


# Create the FastAPI application.
app = FastAPI()


@app.get("/hello")
def say_hello(name: str):
    """Return a greeting message for the given person's name."""

    # Create the greeting message.
    message = f"Hello {name}"

    # Return the message as JSON.
    return {"message": message}

# Install FastAPI and Uvicorn
# python -m pip install fastapi uvicorn
# verify installations
# python -m pip show fastapi
# python -m pip show uvicorn

# Start the FastAPI server
# python -m uvicorn subhashkumar_module3_1:app --reload
# http://127.0.0.1:8000/hello?name=Subhash