from .person import Person
import datetime
import hashlib

class Transaction:
    def __init__(self, id: int, p1: Person, p2: Person, amount: float, time: str = datetime.datetime.now(), hash = None):
        self.id = id
        self.p1 = p1
        self.p2 = p2
        self.amount = amount
        self.time = time
        if hash is not None:
            self.hash = hash
        else:
            data = f"{p1}{p2}{time}{amount}".encode()
            self.hash = hashlib.sha256(data).hexdigest()

    def __str__(self):
        return f" {self.hash} {self.time} - {self.p1} -> {self.p2}: {self.amount}€"
