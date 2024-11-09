import sqlite3
def generate_report(user_id, month=None, year=None):
    query = "SELECT SUM(amount) FROM transactions WHERE user_id = ? AND type = ?"
    params = [user_id, 'income']
    if month:
        query += " AND strftime('%m', date) = ?"
        params.append(month)
    if year:
        query += " AND strftime('%Y', date) = ?"
        params.append(year)
    
    with sqlite3.connect("finance.db") as conn:
        income = conn.execute(query, params).fetchone()[0] or 0
        expenses = conn.execute(query.replace('income', 'expense'), params).fetchone()[0] or 0
        return {"income": income, "expenses": expenses, "savings": income - expenses}
