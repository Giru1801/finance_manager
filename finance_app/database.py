import sqlite3

def initialize_database():
    conn = sqlite3.connect("finance.db")
    with conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                amount REAL,
                category TEXT,
                type TEXT,
                date TEXT,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS budgets (
                user_id INTEGER,
                category TEXT,
                budget_limit REAL,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        """)

if __name__ == "__main__":
    initialize_database()
import shutil

def backup_database():
    shutil.copy("finance.db", "backup_finance.db")

def restore_database():
    shutil.copy("backup_finance.db", "finance.db")
