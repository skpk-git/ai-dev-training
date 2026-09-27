# subhashkumar_module4_7.py

# order the content of your table based on missing_field. Find two approach (two code) 

import sqlite3

connection = sqlite3.connect("tasks.db")
cursor = connection.cursor()

cursor.execute("""
    SELECT *
    FROM tasks
    ORDER BY missing_field ASC
""")

rows = cursor.fetchall()

print("Tasks ordered by missing_field:")

for row in rows:
    print(row)

connection.close()

import sqlite3

connection = sqlite3.connect("tasks.db")
cursor = connection.cursor()

cursor.execute("""
    SELECT *
    FROM tasks
""")

rows = cursor.fetchall()

# Sort rows using missing_field
sorted_rows = sorted(rows, key=lambda row: row[5])

print("Tasks ordered by missing_field:")

for row in sorted_rows:
    print(row)

connection.close()

# | Approach | Where sorting happens | SQL                      |
# | -------- | --------------------- | ------------------------ |
# | **1**    | Database              | `ORDER BY missing_field` |
# | **2**    | Python                | `sorted(..., key=...)`   |

