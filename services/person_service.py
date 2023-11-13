import sqlite3

from models.person import Person

class PersonService: 
    def __init__(self, db_path = "./database/db.sqlite"):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_tables()
    
    def is_persons_empty(self) -> bool:
        self.cursor.execute("SELECT COUNT(*) FROM persons")
        count = self.cursor.fetchone()[0]
        return count == 0

    def create_tables(self):
        self.cursor.execute("PRAGMA foreign_keys = ON")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS persons (id INTEGER PRIMARY KEY AUTOINCREMENT, birth_date TEXT, first_name TEXT, last_name TEXT, bank_balance REAL)")
        self.conn.commit()

    def add_person(self, first_name, last_name, birth_date, bank_balance):
        self.cursor.execute("INSERT INTO persons(first_name, last_name, birth_date, bank_balance) VALUES (?, ?, ?, ?)", (first_name, last_name, birth_date, bank_balance))
        self.conn.commit()

    def get_person(self, person_id) -> Person:
        self.cursor.execute("SELECT * FROM persons WHERE id = ?", (person_id,))
        person = self.cursor.fetchone()
        return self.get_person_from_tuple(person)
    
    def get_persons(self) -> [Person]:
        self.cursor.execute("SELECT * FROM persons")
        persons = self.cursor.fetchall()
        persons = list(map(self.get_person_from_tuple, persons))
        return persons
    
    def update_person(self, person):
        self.cursor.execute("UPDATE persons SET first_name = ?, last_name = ?, birth_date = ?, bank_balance = ? WHERE id = ?", (person.first_name, person.last_name, person.birth_date, person.bank_balance, person.id))
        self.conn.commit()
    
    def delete_person(self, person_id):
        self.cursor.execute("DELETE FROM persons WHERE id = ?", (person_id,))
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def clear_database(self):
        self.cursor.execute("DELETE FROM persons")
        self.conn.commit()
    
    def get_person_from_tuple(self, tuple) -> Person:
        return Person(tuple[0], tuple[1], tuple[2], tuple[3], tuple[4])