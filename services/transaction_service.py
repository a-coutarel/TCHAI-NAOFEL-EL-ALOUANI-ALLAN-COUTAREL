import sqlite3

from models.transaction import Transaction
from services.person_service import PersonService

class TransactionService: 
    def __init__(self, db_path = "./database/db.sqlite"):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_tables()
    
    def is_transactions_empty(self):
        self.cursor.execute("SELECT * FROM transactions")
        transactions = self.cursor.fetchall()
        return len(transactions) == 0

    def create_tables(self):
        self.cursor.execute("PRAGMA foreign_keys = ON")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS transactions (id INTEGER PRIMARY KEY AUTOINCREMENT, p1_id INTEGER, p2_id INTEGER, amount REAL, time TEXT, FOREIGN KEY(p1_id) REFERENCES persons(id), FOREIGN KEY(p2_id) REFERENCES persons(id))")
    
    def add_transaction(self, p1_id, p2_id, amount, time):
        self.cursor.execute("INSERT INTO transactions(p1_id, p2_id, amount, time) VALUES ( ?, ?, ?, ?)", (p1_id, p2_id, amount, time))
        self.conn.commit()

    def get_transaction(self, transaction_id) -> Transaction:
        self.cursor.execute("SELECT * FROM transactions WHERE id = ?", (transaction_id,))
        transaction = self.cursor.fetchone()
        return self.get_transaction_from_tuple(transaction)
    
    def get_transactions(self) -> list[Transaction]:
        self.cursor.execute("SELECT * FROM transactions")
        transactions = self.cursor.fetchall()
        transactions = list(map(self.get_transaction_from_tuple, transactions))
        return transactions
    
    def get_transactions_by_person(self, person_id) -> list[Transaction]:
        self.cursor.execute("SELECT * FROM transactions WHERE p1_id = ? OR p2_id = ?", (person_id, person_id))
        transactions = self.cursor.fetchall()
        transactions = list(map(self.get_transaction_from_tuple, transactions))
        return transactions

    def update_transaction(self, transaction):
        self.cursor.execute("UPDATE transactions SET p1_id = ?, p2_id = ?, amount = ?, time = ? WHERE id = ?", (transaction.p1.id, transaction.p2.id, transaction.amount, transaction.time, transaction.id))
        self.conn.commit()

    def execute_transaction(self, p1_id, p2_id, amount, time):
        p1 = PersonService.get_person(p1_id)
        p2 = PersonService.get_person(p2_id)
        p1.bank_balance -= amount
        p2.bank_balance += amount
        PersonService.update_person(p1)
        PersonService.update_person(p2)

    def delete_transaction(self, transaction_id):
        self.cursor.execute("DELETE FROM transactions WHERE id = ?", (transaction_id))
        self.conn.commit()
    
    def close(self):
        self.cursor.close()
        self.conn.close()

    def clear_database(self):
        self.cursor.execute("DELETE FROM transactions")
        self.conn.commit()

    def get_transaction_from_tuple(self, tuple):
        Person1 = PersonService.get_person(tuple[1])
        Person2 = PersonService.get_person(tuple[2])
        return Transaction(tuple[0], Person1, Person2, tuple[3], tuple[4])