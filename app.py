from flask import Flask, request, jsonify, abort, Response
from models.person import Person
from models.transaction import Transaction
from flask_cors import CORS
from services.storage_service import StorageService

app = Flask(__name__)
CORS(app, supports_credentials=True, origins=['*'])

storage_service = StorageService()

def init():
    if storage_service.is_persons_empty:
        storage_service.add_person(Person(storage_service, 1, "John", "Doe", "1990-01-01"))
        storage_service.add_person(Person(storage_service, 2, "Jane", "Doe", "1990-01-01"))
    if storage_service.is_transactions_empty:
        storage_service.add_transaction(
            Transaction(
                storage_service, 
                0, 
                Person.from_tuple(storage_service, storage_service.get_person(1)), 
                Person.from_tuple(storage_service, storage_service.get_person(2)), 
                50
            )
        )

@app.route('/healthz')
def healthz():
    return Response(status=200)

@app.route("/transaction/create", methods=["POST"])
def transaction_save():
    data = request.get_json()
    p1_id = data["p1_id"]
    p2_id = data["p2_id"]
    amount = data["amount"]
    
    if amount <= 0:
        abort(400, "Invalid request: Amount must be positive")

    if p1_id is None or p2_id is None or amount is None:
        abort(400, "Invalid request: Person not found")
    
    p1: Person = Person.from_tuple(storage_service, storage_service.get_person(p1_id))
    p2: Person = Person.from_tuple(storage_service, storage_service.get_person(p2_id))

    if p1 is None or p2 is None:
        abort(400, "Invalid request: Person not found")
    
    transaction = Transaction(storage_service, len(transactions) ,p1, p2, amount)
    transactions.append(transaction)
    return Response(status=201)

@app.route("/transaction/view-in-chronological-order", methods=["GET"])
def transactions_view():
    if len(transactions) == 0:
        return "No transactions found."
    
    transactions.sort(key=lambda x: x.time)
    transactions_str = [str(transaction) for transaction in transactions]
    return jsonify({"transactions": transactions_str})
    
@app.route("/transaction/view-by-person", methods=["GET"])
def person_transactions():
    data = request.get_json()
    person_id = data["person_id"]
    
    if person_id is None:
        abort(400, "Invalid request: Person not found")
    
    person: Person =  Person.from_tuple(storage_service, storage_service.get_person(int(person_id)))
    
    if person is None:
        abort(400, "Invalid request: Person not found")
    
    person_transactions = [str(transaction) for transaction in transactions if transaction.p1.id == person.id or transaction.p2.id == person.id]
    return jsonify({"transactions": person_transactions})

@app.route("/person/bank-balance", methods=["GET"])
def person_get_bank_balance():
    data = request.get_json()
    person_id = data["person_id"]
    
    if person_id is None:
        abort(400, "Invalid request: Person not found")
        
    person: Person = Person.from_tuple(storage_service, storage_service.get_person(int(person_id)))
    
    if person is None:
        abort(400, "Invalid request: Person not found")
        
    return jsonify({"bank_balance": str(person)})
