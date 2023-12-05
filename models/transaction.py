from .person import Person
import datetime
import hashlib

class Transaction:
    def __init__(self, id: int, p1: Person, p2: Person, amount: float, time: str = datetime.datetime.now(), hash = None, previous_hash = None):
        self.id = id
        self.p1 = p1
        self.p2 = p2
        self.amount = amount
        self.time = time
        data = f"{p1.id}-{p2.id}-{float(amount)}-{time}-{previous_hash}".encode()
        
        if hash is not None:
            calculated_hash = hashlib.sha256(data).hexdigest()
            if calculated_hash == hash:
                self.hash = hash
            else:
                raise Exception("Hashes do not match")
        else:
            self.hash = hashlib.sha256(data).hexdigest()

    def __str__(self):
        return f" {self.hash} {self.time} - {self.p1} -> {self.p2}: {self.amount}€"
