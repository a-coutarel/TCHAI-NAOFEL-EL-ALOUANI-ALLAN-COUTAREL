from flask import Flask, request, jsonify, abort, Response
from flask_cors import CORS
from services.person_service import PersonService
from services.transaction_service import TransactionService

app = Flask(__name__)
CORS(app, supports_credentials=True, origins=['*'])

person_service = PersonService()
transaction_service = TransactionService()

@app.route('/healthz')
def healthz():
    return Response(status=200)

@app.route("/register", methods=["POST"])
def register_user():
    data = request.get_json()
    firstname = data.get("firstname")
    lastname = data.get("lastname")
    birthdate = data.get("birthdate")
    bank_balance = data.get("bank_balance")
    if firstname is None or lastname is None or birthdate is None or bank_balance is None:
        abort(400, "Invalid request: Missing arguments: request must contain firstname, lastname, birthdate, and bank_balance")

    user, private_key = person_service.add_person(firstname, lastname, birthdate, bank_balance)
    if user.id is None:
        abort(400, "Invalid request: User registration failed")
    return jsonify({"private_key": private_key, "user_id": user.id}), 201

@app.route("/transaction/create", methods=["POST"])
def transaction_save():
    data: dict = request.get_json()
    transaction_data: dict = data.get("transaction")
    p1_id: int = transaction_data.get("p1_id")
    p2_id: int = transaction_data.get("p2_id")
    amount: float = transaction_data.get("amount")
    signature: str = data.get("signature")

    if p1_id is None or p2_id is None or amount is None or signature is None:
        abort(400, "Invalid request: Missing arguments: request must contain p1_id, p2_id, amount, and signature")

    if transaction_service.add_transaction(transaction_data, signature):
        return jsonify({"message": "Transaction réussie"}), 201
    else:
        abort(400, "Invalid request: Transaction failed")


@app.route("/transaction/sign", methods=["GET"])
def transaction_sign():
    data: dict = request.get_json()
    private_key: str = data.get("private_key")
    transaction_data: str = str(data.get("transaction"))
    
    signature: str = transaction_service.sign_transaction(private_key, transaction_data)
    if signature is None:
        abort(400, "Invalid request: Invalid private key")
    
    print("Signature: " + signature)
    return jsonify({"signature": signature}), 201

@app.route("/transaction/view-in-chronological-order", methods=["GET"])
def transactions_view():
    transactions = transaction_service.get_transactions()
    if len(transactions) == 0:
        abort(400, "Invalid request: No transactions found")
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

@app.route("/transaction/check-hash", methods=["GET"])
def check_hash_transactions():
    results = transaction_service.check_hash_transactions()
    if results['count'] == 0:
        return "All transactions are valid:\n" + results['res']
    else: 
        return str(results['count']) + " invalid transactions found:\n" + results['res']

if __name__ == "__main__":
    app.run(debug=True)
