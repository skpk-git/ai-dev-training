# subhashkumar_module7_5.py

# adjust the same docker image in (Q.4) to add user inputted information. The docker image MUST NOT delete old version database 

import sqlite3
import random
import string


DATABASE = "data/users.db"


# ---------------------------------------------------------
# Create database and table
# ---------------------------------------------------------

def create_database():

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            user_key TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


# ---------------------------------------------------------
# Generate random user
# ---------------------------------------------------------

def generate_random_user():

    names = [
        "John",
        "David",
        "Michael",
        "Robert",
        "James",
        "William",
        "Daniel",
        "Thomas",
        "Richard",
        "Joseph"
    ]

    name = random.choice(names)

    phone = "05" + "".join(
        random.choices(string.digits, k=8)
    )

    user_key = "".join(
        random.choices(
            string.ascii_letters + string.digits,
            k=12
        )
    )

    return name, phone, user_key


# ---------------------------------------------------------
# Insert user
# ---------------------------------------------------------

def insert_user(name, phone, user_key):

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO users
        (name, phone, user_key)
        VALUES (?, ?, ?)
    """, (
        name,
        phone,
        user_key
    ))

    connection.commit()

    user_id = cursor.lastrowid

    connection.close()

    return user_id


# ---------------------------------------------------------
# Display existing users
# ---------------------------------------------------------

def display_users():

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, phone, user_key
        FROM users
        ORDER BY id
    """)

    rows = cursor.fetchall()

    connection.close()

    print("\nExisting users:")

    if not rows:
        print("No users found.")
        return

    for row in rows:

        print(
            f"ID={row[0]}, "
            f"Name={row[1]}, "
            f"Phone={row[2]}, "
            f"UserKey={row[3]}"
        )


# ---------------------------------------------------------
# Main program
# ---------------------------------------------------------

create_database()

print("================================")
print("       User Management")
print("================================")

while True:

    print("\n1. Add user")
    print("2. Generate random user")
    print("3. Show users")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    # -----------------------------------------------------
    # Add user manually
    # -----------------------------------------------------

    if choice == "1":

        name = input("Enter name: ")
        phone = input("Enter phone: ")
        user_key = input("Enter user key: ")

        user_id = insert_user(
            name,
            phone,
            user_key
        )

        print(
            f"\nUser created successfully. ID = {user_id}"
        )

    # -----------------------------------------------------
    # Generate random user
    # -----------------------------------------------------

    elif choice == "2":

        name, phone, user_key = generate_random_user()

        user_id = insert_user(
            name,
            phone,
            user_key
        )

        print(
            f"\nRandom user created:"
        )

        print(f"ID       : {user_id}")
        print(f"Name     : {name}")
        print(f"Phone    : {phone}")
        print(f"User Key : {user_key}")

    # -----------------------------------------------------
    # Display users
    # -----------------------------------------------------

    elif choice == "3":

        display_users()

    # -----------------------------------------------------
    # Exit
    # -----------------------------------------------------

    elif choice == "4":

        print("Application closed.")
        break

    else:

        print("Invalid choice.")
