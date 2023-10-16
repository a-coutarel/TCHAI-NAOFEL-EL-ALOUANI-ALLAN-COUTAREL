import sqlite3

class StorageService:
    def __init__(self, db_path = "./database/db.sqlite"):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("PRAGMA foreign_keys = ON")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS persons (id INTEGER PRIMARY KEY AUTOINCREMENT, first_name TEXT, last_name TEXT, birth_date TEXT, bank_balance REAL)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS transactions (id INTEGER PRIMARY KEY AUTOINCREMENT, p1_id INTEGER, p2_id INTEGER, amount REAL, time TEXT, FOREIGN KEY(p1_id) REFERENCES persons(id), FOREIGN KEY(p2_id) REFERENCES persons(id))")

    def add_person(self, person):
        self.cursor.execute("INSERT INTO persons(first_name, last_name, birth_date, bank_balance) VALUES (?, ?, ?, ?)", (person.first_name, person.last_name, person.birth_date, person.bank_balance))
        self.conn.commit()
    
    def add_transaction(self, transaction):
        print(transaction.p1.id, transaction.p2.id, transaction.amount, transaction.time)
        self.cursor.execute("INSERT INTO transactions(p1_id, p2_id, amount, time) VALUES ( ?, ?, ?, ?)", (transaction.p1.id, transaction.p2.id, transaction.amount, transaction.time))
        self.conn.commit()
    
    def get_person(self, person_id):
        self.cursor.execute("SELECT * FROM persons WHERE id = ?", (person_id,))
        person = self.cursor.fetchone()
        return person
    
    def get_persons(self):
        self.cursor.execute("SELECT * FROM persons")
        persons = self.cursor.fetchall()
        return persons
    
    def get_transaction(self, transaction_id):
        self.cursor.execute("SELECT * FROM transactions WHERE id = ?", (transaction_id,))
        transaction = self.cursor.fetchone()
        return transaction
    
    def get_transactions(self):
        self.cursor.execute("SELECT * FROM transactions")
        transactions = self.cursor.fetchall()
        return transactions
    
    def get_transactions_by_person(self, person_id):
        self.cursor.execute("SELECT * FROM transactions WHERE p1_id = ? OR p2_id = ?", (person_id, person_id))
        transactions = self.cursor.fetchall()
        return transactions
    
    def delete_person(self, person_id):
        self.cursor.execute("DELETE FROM persons WHERE id = ?", (person_id,))
        self.conn.commit()

    def delete_transaction(self, transaction_id):
        self.cursor.execute("DELETE FROM transactions WHERE id = ?", (transaction_id,))
        self.conn.commit()

    def update_person(self, person):
        self.cursor.execute("UPDATE persons SET first_name = ?, last_name = ?, birth_date = ?, bank_balance = ? WHERE id = ?", (person.first_name, person.last_name, person.birth_date, person.bank_balance, person.id))
        self.conn.commit()
    
    def update_transaction(self, transaction):
        self.cursor.execute("UPDATE transactions SET p1_id = ?, p2_id = ?, amount = ?, time = ? WHERE id = ?", (transaction.p1.id, transaction.p2.id, transaction.amount, transaction.time, transaction.id))
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def clear_database(self):
        self.cursor.execute("DELETE FROM persons")
        self.cursor.execute("DELETE FROM transactions")
        self.conn.commit()