import unittest
import sqlite3
import os
from finance_app.auth import register_user, login_user
from finance_app.transactions import add_transaction, delete_transaction
from finance_app.reports import generate_report
from finance_app.budget import set_budget, check_budget
from finance_app.backup import backup_database, restore_database

class TestFinanceApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Initialize database
        if os.path.exists("finance.db"):
            os.remove("finance.db")
        # Re-run database initialization to create fresh tables
        from finance_app.database import initialize_database
        initialize_database()

    def setUp(self):
        # Clear data from the users table to avoid conflicts
        with sqlite3.connect("finance.db") as conn:
            conn.execute("DELETE FROM users")

    def test_register_and_login(self):
        # Test registration and login
        register_user("testuser", "password123")
        self.assertTrue(login_user("testuser", "password123"))

    def test_add_and_delete_transaction(self):
        add_transaction(1, 100.0, "Food", "expense", "2023-11-08")
        # Validate transaction add/delete

    def test_generate_report(self):
        report = generate_report(1, "11", "2023")
        self.assertIn("income", report)
        self.assertIn("expenses", report)
        self.assertIn("savings", report)

    def test_set_and_check_budget(self):
        set_budget(1, "Food", 500)
        self.assertFalse(check_budget(1, "Food", 100))

    def test_backup_and_restore(self):
        backup_database()
        self.assertTrue(os.path.exists("backup_finance.db"))
        restore_database()
        self.assertTrue(os.path.exists("finance.db"))

if __name__ == "__main__":
    unittest.main()
