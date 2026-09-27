# subhashkumar_module4_4_view_data.py

# view data from tasks.db.tasks

import sqlite3

# Connect again
connection = sqlite3.connect("tasks.db")
cursor = connection.cursor()

print("SELECT * FROM tasks")
cursor.execute("SELECT * FROM tasks ORDER BY Length(description) desc")

rows = cursor.fetchall()
print(f"{len(rows)} rows fetched.")

# Extract column headers
headers = [description[0] for description in cursor.description]

if len(rows) > 0:
    # Convert all data cells to strings for width calculation
    string_rows = [[str(cell) for cell in row] for row in rows]

    # Find the maximum width needed for each column (checking headers + data)
    col_widths = []
    for col_idx in range(len(headers)):
        header_len = len(headers[col_idx])
        max_data_len = max(len(row[col_idx]) for row in string_rows) if string_rows else 0
        col_widths.append(max(header_len, max_data_len))

    # Create a formatting template (e.g., "|  %-10s  |  %-5s  |")
    format_template = " | ".join([f"{{:<{w}}}" for w in col_widths])
    separator = "-+-".join(["-" * w for w in col_widths])

    # Print the table
    print(format_template.format(*headers))
    print(separator)
    for row in string_rows:
        print(format_template.format(*row))


# Close database connection
connection.close()