# subhashkumar_module4_2.py

# make python code to make sql3 db to  create tasks 
# table : id , title , description , status , created_at provide schema and script      

import sqlite3


def create_tasks_database():
    """Create a SQLite database and the tasks table."""

    # Connect to the SQLite database.
    # If tasks.db does not exist, SQLite will create it.
    connection = sqlite3.connect("tasks.db")

    # Create a cursor to execute SQL commands.
    cursor = connection.cursor()

    # SQL statement to create the tasks table.
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        status TEXT NOT NULL,
        created_at TEXT NOT NULL
    )
    """

    # Execute the CREATE TABLE statement.
    cursor.execute(create_table_sql)

    # Save the changes to the database.
    connection.commit()

    # Close the database connection.
    connection.close()

    print("Database and tasks table created successfully.")


if __name__ == "__main__":
    create_tasks_database()