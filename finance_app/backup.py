import shutil

def backup_database():
    shutil.copy("finance.db", "backup_finance.db")

def restore_database():
    shutil.copy("backup_finance.db", "finance.db")
