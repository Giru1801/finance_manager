import sqlite3
import bcrypt

def register_user(username, password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    with sqlite3.connect("finance.db") as conn:
        conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed))

def login_user(username, password):
    with sqlite3.connect("finance.db") as conn:
        user = conn.execute("SELECT password FROM users WHERE username = ?", (username,)).fetchone()
        if user and bcrypt.checkpw(password.encode(), user[0]):
            return True
        return False
