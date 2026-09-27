# subhashkumar_module4_3.py

# make python POST API to insert information into the table 
# (add 2 rows ) when called 

import sqlite3
from datetime import datetime
from fastapi import FastAPI

# Create the FastAPI application.
app = FastAPI()


def insert_two_tasks():
    """Insert two tasks into the SQLite database."""

    # Connect to the SQLite database.
    connection = sqlite3.connect("tasks.db")

    # Create a cursor to execute SQL commands.
    cursor = connection.cursor()

    # Get the current date and time.
    created_at = datetime.now().isoformat()

    # First task.
    task1 = (
        "Learn Python",
        "Complete Python exercises",
        "Pending",
        created_at
    )

    # Second task.
    task2 = (
        "Learn SQL",
        "Practice SQLite database operations",
        "Pending",
        created_at
    )

    # SQL statement for inserting a task.
    insert_sql = """
    INSERT INTO tasks (title, description, status, created_at)
    VALUES (?, ?, ?, ?)
    """

    # Insert the first task.
    cursor.execute(insert_sql, task1)

    # Insert the second task.
    cursor.execute(insert_sql, task2)

    # Save the changes.
    connection.commit()

    # Close the database connection.
    connection.close()


@app.post("/tasks")
def create_tasks():
    """Insert two tasks into the database when the API is called."""

    # Insert two tasks.
    insert_two_tasks()

    # Return a success message.
    return {
        "message": "Two tasks inserted successfully"
    }


if __name__ == "__main__":
    insert_two_tasks()
    print("Two tasks inserted successfully")

# Start the server
# python -m uvicorn subhashkumar_module4_3:app --reload