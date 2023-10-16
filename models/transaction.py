from .person import Person
from services.storage_service import StorageService
import datetime

class Transaction:
    def __init__(self, storage_service: StorageService, id: int, p1: Person, p2: Person, amount: float):
        self.id = id
        self.p1 = p1
        self.p2 = p2
        self.amount = amount
        self.time = datetime.datetime.now()
        self.storage_service = storage_service
        self.p1.pay(p2, amount)
        self.storage_service.add_transaction(self)

    def __str__(self):
        return f" {self.time} - {self.p1} -> {self.p2}: {self.amount}€"
    
    @classmethod
    def from_tuple(cls, storage_service, tpl):
        tpl.p1 = Person.from_tuple(storage_service, storage_service.get_person(tpl.p1_id))
        tpl.p2 = Person.from_tuple(storage_service, storage_service.get_person(tpl.p2_id))
        return cls(storage_service, *tpl)