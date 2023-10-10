from person import Person
import datetime

class Transaction:
    def __init__(self, p1: Person, p2: Person, time: datetime, amount: float):
        self.p1 = p1
        self.p2 = p2
        self.amount = amount