# subhashkumar_module8_2.py

# make MCP to connect to any SQL database you created to provide the information via the MCP viewer. 

import sqlite3

from mcp.server.fastmcp import FastMCP


DATABASE = "data/users.db"

mcp = FastMCP("SQL Database Server")


def get_connection():
    return sqlite3.connect(DATABASE)


@mcp.tool()
def get_users() -> list:
    """
    Get all users from the users table.
    """

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, name, phone, user_key
            FROM users
            ORDER BY id
        """)

        rows = cursor.fetchall()

        users = []

        for row in rows:
            users.append({
                "id": row[0],
                "name": row[1],
                "phone": row[2],
                "user_key": row[3]
            })

        return users

    finally:
        connection.close()


@mcp.tool()
def get_user_by_id(user_id: int) -> dict:
    """
    Get one user by ID.
    """

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, name, phone, user_key
            FROM users
            WHERE id = ?
        """, (user_id,))

        row = cursor.fetchone()

        if row is None:
            return {
                "error": "User not found"
            }

        return {
            "id": row[0],
            "name": row[1],
            "phone": row[2],
            "user_key": row[3]
        }

    finally:
        connection.close()


if __name__ == "__main__":
    mcp.run()
