import sqlite3
from pathlib import Path

DATABASE = Path("database/users.db")


def get_connection():
    return sqlite3.connect(DATABASE)


def initialize_database():
    connection = get_connection()

    try:
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

    finally:
        connection.close()


def add_user(name, phone, user_key):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO users
                (name, phone, user_key)
            VALUES
                (?, ?, ?)
        """, (name, phone, user_key))

        connection.commit()

        return {
            "success": True,
            "id": cursor.lastrowid
        }

    finally:
        connection.close()


def get_users():
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


def get_user_by_id(user_id):
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
            return None

        return {
            "id": row[0],
            "name": row[1],
            "phone": row[2],
            "user_key": row[3]
        }

    finally:
        connection.close()  