import datetime

class Person:
    def __init__(self, id: int, birth_date: datetime, first_name: str, last_name: str, bank_balance: float = 100.0, public_key: str = None):
        self.id = id
        self.birth_date = birth_date
        self.first_name = first_name
        self.last_name = last_name
        self.bank_balance = bank_balance
        self.public_key = public_key

    def __str__(self):
        return f"(id: {self.id}) {self.first_name} {self.last_name} {self.bank_balance}€"