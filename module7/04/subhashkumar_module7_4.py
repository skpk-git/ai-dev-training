# subhashkumar_module7_4.py

# make a python program store information into SQL database to store the following { id , name , phone,  user_key , } make random data . Luanch through docker. 

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
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            user_key TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


# ---------------------------------------------------------
# Generate random user information
# ---------------------------------------------------------

def generate_user():

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
# Insert user into database
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

    generated_id = cursor.lastrowid

    connection.close()

    return generated_id


# ---------------------------------------------------------
# Main program
# ---------------------------------------------------------

create_database()


number_of_users = int(
    input("How many users should be created? ")
)


for i in range(number_of_users):

    name, phone, user_key = generate_user()

    user_id = insert_user(
        name,
        phone,
        user_key
    )

    print(
        f"Created: ID={user_id}, "
        f"Name={name}, "
        f"Phone={phone}, "
        f"UserKey={user_key}"
    )


print("\nUsers created successfully.")