import datetime

class Person:
    def __init__(self, id: int, date_of_birth: datetime, first_name: str, last_name: str, bank_balance: float = 100.0):
        self.id = id
        self.date_of_birth = date_of_birth
        self.first_name = first_name
        self.last_name = last_name
        self.bank_balance = bank_balance

    def __str__(self):
        return f"({self.id}) {self.first_name} {self.last_name} {self.bank_balance}"
    
    def pay(self, person: 'Person', amount: float):
        self.bank_balance -= amount
        person.bank_balance += amount
