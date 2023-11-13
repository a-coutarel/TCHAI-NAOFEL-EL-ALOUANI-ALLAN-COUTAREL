import datetime
from flask import Flask, request, jsonify, abort, Response
from models.person import Person
from models.transaction import Transaction
from flask_cors import CORS
from services.person_service import PersonService
from services.transaction_service import TransactionService

app = Flask(__name__)
CORS(app, supports_credentials=True, origins=['*'])

person_service = PersonService()
transaction_service = TransactionService()

def init():
    if person_service.is_persons_empty:
        person_service.add_person("John", "Doe", "1990-01-01", 1500)
        person_service.add_person("Jane", "Dupont", "1990-01-01", 780)
    if transaction_service.is_transactions_empty:
        transaction_service.add_transaction(1, 2, 150, datetime.datetime.now())

init()

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
    
    transaction_service.add_transaction(p1_id, p2_id, amount, datetime.datetime.now())
    return Response(status=201)

@app.route("/transaction/view-in-chronological-order", methods=["GET"])
def transactions_view():
    if transaction_service.is_transactions_empty:
        return "No transactions found."
    
    transactions = transaction_service.get_transactions()
    transactions.sort(key=lambda x: x.time)
    transactions_str = [str(transaction) for transaction in transactions]
    return jsonify({"transactions": transactions_str})
    
@app.route("/transaction/view-by-person", methods=["GET"])
def person_transactions():
    data = request.get_json()
    person_id = data["person_id"]
    
    if person_id is None:
        abort(400, "Invalid request: Person not found")
    
    person_transactions = transaction_service.get_transactions_by_person(person_id)
    transactions_str = [str(transaction) for transaction in person_transactions]
    return jsonify({"transactions": transactions_str})

@app.route("/person/bank-balance", methods=["GET"])
def person_get_bank_balance():
    data = request.get_json()
    person_id = data["person_id"]
    if person_id is None:
        abort(400, "Invalid request: Person not found")
        
    person = person_service.get_person(person_id)    
    if person is None:
        abort(400, "Invalid request: Person not found")
        
    return jsonify({"bank_balance": str(person)})

if __name__ == "__main__":
    app.run(debug=True)
