# subhashkumar_module4_5.py

#Make python code to change values for existing row in the created db then after 15 second revert back. Show the change with your sql viewer. 

import sqlite3
import time

DB_NAME = "tasks.db"
TASK_ID = 1

connection = sqlite3.connect(DB_NAME)
cursor = connection.cursor()

# 1. Get the existing row
cursor.execute("""
    SELECT id, title, description, status, created_at
    FROM tasks
    WHERE id = ?
""", (TASK_ID,))

row = cursor.fetchone()

if row is None:
    print(f"Task with ID {TASK_ID} was not found.")
    connection.close()
    exit()

# Save original values
original_title = row[1]
original_description = row[2]
original_status = row[3]

print("Original row:")
print(row)

# 2. Change the existing row
new_status = "IN_PROGRESS"

cursor.execute("""
    UPDATE tasks
    SET status = ?
    WHERE id = ?
""", (new_status, TASK_ID))

connection.commit()

print("\nRow changed:")
cursor.execute("""
    SELECT id, title, description, status, created_at
    FROM tasks
    WHERE id = ?
""", (TASK_ID,))

print(cursor.fetchone())

# 3. Wait 15 seconds
print("\nWaiting 15 seconds...")
time.sleep(15)

# 4. Revert the row
cursor.execute("""
    UPDATE tasks
    SET title = ?,
        description = ?,
        status = ?
    WHERE id = ?
""", (
    original_title,
    original_description,
    original_status,
    TASK_ID
))

connection.commit()

# 5. Show reverted row
print("\nRow reverted:")
cursor.execute("""
    SELECT id, title, description, status, created_at
    FROM tasks
    WHERE id = ?
""", (TASK_ID,))

print(cursor.fetchone())

connection.close()

#python view_database.py