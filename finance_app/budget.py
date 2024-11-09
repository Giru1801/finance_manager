import sqlite3
def set_budget(user_id, category, limit):
    with sqlite3.connect("finance.db") as conn:
        conn.execute("INSERT OR REPLACE INTO budgets (user_id, category, budget_limit) VALUES (?, ?, ?)", 
                     (user_id, category, limit))

def check_budget(user_id, category, expense):
    with sqlite3.connect("finance.db") as conn:
        total_spent = conn.execute("SELECT SUM(amount) FROM transactions WHERE user_id = ? AND category = ? AND type = 'expense'", 
                                   (user_id, category)).fetchone()[0] or 0
        budget_limit = conn.execute("SELECT budget_limit FROM budgets WHERE user_id = ? AND category = ?", 
                                    (user_id, category)).fetchone()[0]
        return total_spent + expense > budget_limit
