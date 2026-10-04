# subhashkumar_module7_1.py

# make python program to print user input as it is. Deploy it using docker. What is docker? 


"""
What is Docker?

Docker is a tool that packages an application together with everything it needs to run, such as:

Python
Python libraries
Your application code
Configuration

This package is called a Docker image.

When you run the image, Docker creates a container.

Think of it like this:

Without Docker

Your PC
 ├── Python
 ├── Libraries
 ├── Your program
 └── Configuration


With Docker

Docker Container
 ┌─────────────────────┐
 │ Python              │
 │ Libraries           │
 │ Your program        │
 │ Configuration       │
 └─────────────────────┘
          │
          ▼
       Runs the app

The advantage is that the application can run consistently on another computer without manually installing all the dependencies.
"""

# Get input from the user
user_input = input("Enter something: ")

# Print exactly what the user entered
print("You entered:", user_input)

