import sqlite3

def add_transaction(user_id, amount, category, trans_type, date):
    with sqlite3.connect("finance.db") as conn:
        conn.execute("INSERT INTO transactions (user_id, amount, category, type, date) VALUES (?, ?, ?, ?, ?)",
                     (user_id, amount, category, trans_type, date))

def delete_transaction(transaction_id):
    with sqlite3.connect("finance.db") as conn:
        conn.execute("DELETE FROM transactions WHERE id = ?", (transaction_id,))
