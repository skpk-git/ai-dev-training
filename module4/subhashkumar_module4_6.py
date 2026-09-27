# subhashkumar_module4_6.py

# add new field name to your exisiting table name it : missing_field 
# and populate with one random characters 

import sqlite3
import random
import string

DB_NAME = "tasks.db"

connection = sqlite3.connect(DB_NAME)
cursor = connection.cursor()

# 1. Add the new column
cursor.execute("""
    ALTER TABLE tasks
    ADD COLUMN missing_field TEXT
""")

# 2. Get all existing task IDs
cursor.execute("SELECT id FROM tasks")
rows = cursor.fetchall()

# 3. Generate one random character for each row
for row in rows:
    task_id = row[0]

    random_character = random.choice(string.ascii_letters)

    cursor.execute("""
        UPDATE tasks
        SET missing_field = ?
        WHERE id = ?
    """, (random_character, task_id))

# 4. Save changes
connection.commit()

# 5. Display the updated table
print("Updated tasks table:")

cursor.execute("""
    SELECT *
    FROM tasks
""")

for row in cursor.fetchall():
    print(row)

connection.close()

#python subhashkumar_module4_4_view_data.py