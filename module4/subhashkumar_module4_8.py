# subhashkumar_module4_8.py

#make python function given search (letters or number) it will return best rows match description. Search only description 

import sqlite3


def search_description(search_text):
    connection = sqlite3.connect("tasks.db")
    cursor = connection.cursor()

    query = """
        SELECT *
        FROM tasks
        WHERE description LIKE ?
        ORDER BY description
    """

    # % allows the search text to appear anywhere in description
    search_pattern = f"%{search_text}%"

    cursor.execute(query, (search_pattern,))
    rows = cursor.fetchall()

    connection.close()

    return rows


# Test the function
search = input("Enter search text: ")

results = search_description(search)

print("\nSearch results:")

if results:
    for row in results:
        print(row)
else:
    print("No matching rows found.")
    