import datetime
from services.storage_service import StorageService

class Person:
    def __init__(self, storage_service: StorageService, id: int, birth_date: datetime, first_name: str, last_name: str, bank_balance: float = 100.0):
        self.id = id
        self.birth_date = birth_date
        self.first_name = first_name
        self.last_name = last_name
        self.bank_balance = bank_balance
        self.storage_service = storage_service
        self.storage_service.add_person(self)

    def __str__(self):
        return f"(id: {self.id}) {self.first_name} {self.last_name} {self.bank_balance}€"
    
    def pay(self, person: 'Person', amount: float):
        if amount > 0:
            self.bank_balance -= amount
            person.bank_balance += amount
            self.storage_service.update_person(self)
            self.storage_service.update_person(person)

    @classmethod
    def from_tuple(cls, storage_service, tpl):
        return cls(storage_service, *tpl)
