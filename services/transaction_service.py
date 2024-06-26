import sqlite3

from models.transaction import Transaction
from services.crypto_service import CryptoService
from services.person_service import PersonService

person_service = PersonService()

class TransactionService: 
    def __init__(self, db_path = "./database/db.sqlite"):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_tables()
    
    def is_transactions_empty(self) -> bool:
        self.cursor.execute("SELECT COUNT(*) FROM transactions")
        count = self.cursor.fetchone()[0]
        return count == 0

    def create_tables(self):
        self.cursor.execute("PRAGMA foreign_keys = ON")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS transactions (id INTEGER PRIMARY KEY AUTOINCREMENT, p1_id INTEGER, p2_id INTEGER, amount REAL, time TEXT, hash TEXT, FOREIGN KEY(p1_id) REFERENCES persons(id), FOREIGN KEY(p2_id) REFERENCES persons(id))")
        self.conn.commit()
    
    def add_transaction(self, transaction_data: dict, signature: str) -> bool:
        p1 = person_service.get_person(transaction_data.get("p1_id"))
        p2 = person_service.get_person(transaction_data.get("p2_id"))
        public_key = p1.public_key

        if public_key is None:
            print("Invalid request: Public key not found for this user")
            return False
        
        if not CryptoService.verify_signature(public_key, str(transaction_data), signature):
            print("Invalid request: Invalid signature")
            return False

        previous_hash = self.get_previous_hash()
        transaction = Transaction(0, p1, p2, transaction_data.get("amount"), previous_hash=previous_hash)
        
        self.cursor.execute("INSERT INTO transactions(p1_id, p2_id, amount, time, hash) VALUES ( ?, ?, ?, ?, ?)", (p1.id, p2.id, transaction.amount, transaction.time, transaction.hash))
        self.conn.commit()
        return True
    
    def sign_transaction(self, private_key, transaction_data) -> str:
        return CryptoService.sign_transaction(private_key, str(transaction_data))

    def get_transaction(self, transaction_id) -> Transaction:
        self.cursor.execute("SELECT * FROM transactions WHERE id = ?", (transaction_id,))
        transaction = self.cursor.fetchone()
        return self.get_transaction_from_tuple(transaction)
    
    def get_transactions(self) -> [Transaction]:
        self.cursor.execute("SELECT * FROM transactions")
        transactions = self.cursor.fetchall()
        transactions = list(map(self.get_transaction_from_tuple, transactions))
        return transactions
    
    def get_transactions_by_person(self, person_id) -> [Transaction]:
        self.cursor.execute("SELECT * FROM transactions WHERE p1_id = ? OR p2_id = ?", (person_id, person_id))
        transactions = self.cursor.fetchall()
        transactions = list(map(self.get_transaction_from_tuple, transactions))
        return transactions

    def update_transaction(self, transaction):
        self.cursor.execute("UPDATE transactions SET p1_id = ?, p2_id = ?, amount = ?, time = ?, hash = ? WHERE id = ?", (transaction.p1.id, transaction.p2.id, transaction.amount, transaction.time, transaction.hash, transaction.id))
    def update_transaction(self, transaction: Transaction):
        self.cursor.execute("UPDATE transactions SET p1_id = ?, p2_id = ?, amount = ?, time = ? WHERE id = ?", (transaction.p1.id, transaction.p2.id, transaction.amount, transaction.time, transaction.id))
        self.conn.commit()

    def execute_transaction(self, p1_id, p2_id, amount):
        p1 = person_service.get_person(p1_id)
        p2 = person_service.get_person(p2_id)
        
        if p1 is None or p2 is None:
            return None
        
        p1.bank_balance -= amount
        p2.bank_balance += amount
        person_service.update_person(p1)
        person_service.update_person(p2)
        
        previous_hash = self.get_previous_hash()
        transaction = Transaction(self.get_total_transactions() + 1, p1, p2, amount, previous_hash=previous_hash)
        return transaction
    
    def check_hash_transactions(self):
        self.cursor.execute("SELECT * FROM transactions")
        transactions = self.cursor.fetchall()
        res = ''
        count = 0
        for tuple_transaction in transactions:
            Person1 = person_service.get_person(tuple_transaction[1])
            Person2 = person_service.get_person(tuple_transaction[2])
            try:
                previous_hash = self.get_previous_hash(tuple_transaction[0])
                transaction_obj = Transaction(tuple_transaction[0], Person1, Person2, tuple_transaction[3], tuple_transaction[4], tuple_transaction[5], previous_hash)
                res += "Transaction ID: " + str(transaction_obj.id) + " is valid\n"
            except Exception as e:
                count += 1
                res += "Transaction ID: " + str(tuple_transaction[0]) + " is invalid. Error during hash verification.\n"
        return {'res' : res, 'count': count}
    
    def get_previous_hash(self, id = None):
        if self.get_total_transactions() == 0 or id == 1:
            return ""
        
        if id is None:
            self.cursor.execute("SELECT hash FROM transactions ORDER BY id DESC LIMIT 1")
            hash = self.cursor.fetchone()[0]
            return hash
        else:
            self.cursor.execute("SELECT hash FROM transactions WHERE id = ?", (id - 1,))
            hash = self.cursor.fetchone()[0]
            return hash
    
    def get_total_transactions(self) -> int:
        self.cursor.execute("SELECT COUNT(*) FROM transactions")
        count = self.cursor.fetchone()[0]
        return count

    def delete_transaction(self, transaction_id):
        self.cursor.execute("DELETE FROM transactions WHERE id = ?", (transaction_id,))
        self.conn.commit()
    
    def close(self):
        self.cursor.close()
        self.conn.close()

    def clear_database(self):
        self.cursor.execute("DELETE FROM transactions")
        self.conn.commit()

    def get_transaction_from_tuple(self, tuple):
        Person1 = person_service.get_person(tuple[1])
        Person2 = person_service.get_person(tuple[2])
        previous_hash = self.get_previous_hash(tuple[0])
        return Transaction(tuple[0], Person1, Person2, tuple[3], tuple[4], tuple[5], previous_hash)