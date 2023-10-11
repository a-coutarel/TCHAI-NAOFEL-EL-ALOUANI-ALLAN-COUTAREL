from flask import Flask, request, jsonify, abort, Response
from models.person import Person
from models.transaction import Transaction
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True, origins=['*'])

persons: [Person] = [
    Person(0, "25/10/2001", "Allan", "COUTAREL", 100.0),
    Person(1, "29/06/2001", "Naofel", "EL ALOUANI", 100.0)
]
transactions: [Transaction] = []

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/transaction/save", methods=["POST"])
def transaction_save():
    data = request.get_json()
    p1_id = data["p1_id"]
    p2_id = data["p2_id"]
    amount = data["amount"]

    if p1_id is None or p2_id is None or amount is None:
        abort(400, "Invalid request: Person not found")
    
    p1: Person = find_person_by_id(p1_id)
    p2: Person = find_person_by_id(p2_id)

    if p1 is None or p2 is None:
        abort(400, "Invalid request: Person not found")
    
    transaction = Transaction(len(transactions) ,p1, p2, amount)
    transactions.append(transaction)
    return Response(status=201)

def find_person_by_id(id: int) -> Person:
    for person in persons:
        if person.id == id:
            return person
    return None

def find_transaction_by_id(id: int) -> Transaction:
    for transaction in transactions:
        if transaction.id == id:
            return transaction
    return None