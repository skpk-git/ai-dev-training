# subhashkumar_module4_4.py

#find method to view sql database tables. 

# Make python code to view sql databes tables 

import sqlite3

# Connect to the database
connection = sqlite3.connect("tasks.db")

cursor = connection.cursor()

# Get all table names
cursor.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type = 'table'
    ORDER BY name;
""")

tables = cursor.fetchall()

print("Tables in database:")

for table in tables:
    print(table[0])

connection.close()

import sqlite3

connection = sqlite3.connect("tasks.db")
cursor = connection.cursor()

# Get all tables
cursor.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type = 'table'
    ORDER BY name;
""")

tables = cursor.fetchall()

for table in tables:
    table_name = table[0]

    print("\n" + "=" * 40)
    print("TABLE:", table_name)
    print("=" * 40)

    cursor.execute(f"PRAGMA table_info({table_name})")

    columns = cursor.fetchall()

    print("Columns:")
    for column in columns:
        print(
            f"  {column[1]} | "
            f"Type: {column[2]} | "
            f"Primary Key: {column[5]}"
        )

connection.close()

cursor.execute("SELECT * FROM tasks")

rows = cursor.fetchall()

for row in rows:
    print(row)