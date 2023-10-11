from .person import Person
import datetime

class Transaction:
    def __init__(self, id: int, p1: Person, p2: Person, amount: float):
        self.id = id
        self.p1 = p1
        self.p2 = p2
        self.amount = amount
        self.time = datetime.datetime.now()
        self.p1.pay(p2, amount)

    def __str__(self):
        return f" {self.time} - {self.p1} -> {self.p2}: {self.amount}€"