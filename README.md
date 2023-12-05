# Systèmes d’information avancés - Projet TP Tchaî

<p align="center">
    <img width="240" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Masala_Chai.JPG/220px-Masala_Chai.JPG">
    <br>
    <br>
    <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
    <img src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white">
    <img src="https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white">
</p>

## Authors
* __EL ALOUANI Naofel__ 

    _📧: naofel_el-alouani@etu.u-bourgogne.fr_
    
* __COUTAREL Allan__ 

    _📧: allan_coutarel@etu.u-bourgogne.fr_

## Installation
- Clone the repository:  
`git clone https://github.com/a-coutarel/TCHAI-NAOFEL-EL-ALOUANI-ALLAN-COUTAREL.git`
- Enter in the repository:  
`cd TCHAI-NAOFEL-EL-ALOUANI-ALLAN-COUTAREL`
- Install Flask:  
`pip install flask`
- Export the environment variable (first place yourself in the project folder):
```
export FLASK_APP=app.py
```
- Launch the application:  
`flask run`

# Tchaî v1
## Exercise 3
### A1: Save a transaction
To create a transaction, you have to send a `POST` request to the route `localhost:5000/transaction/create`.
#### Request Parameters

The `POST` request must include a `JSON` object with the following elements:

| Parameter  | Type         | Description                                    |
|------------|--------------|------------------------------------------------|
| `p1_id`    | Integer      | The ID of the first person involved in the transaction. |
| `p2_id`    | Integer      | The ID of the second person involved in the transaction. |
| `amount`   | Decimal      | The amount of the transaction.                 |

#### Responses
| HTTP Status | Response     | Description                                       |
|-------------|--------------|---------------------------------------------------|
| 201         | Created      | The transaction has been successfully saved.           |
| 400         | Bad Request  | Invalid request: Missing parameters or incorrect data. |

#### Example
```json
{
    "p1_id": 0,
    "p2_id": 1,
    "amount": 20.0
}
```


### A2: Show a list of all transactions in chronological order
To show a list of all transactions in chronological order, you have to send a `GET` request to the route `localhost:5000/transaction/view-in-chronological-order`.
#### Request Parameters

No parameters required.

#### Responses
| HTTP Status | Response     | Description                                       |
|-------------|--------------|---------------------------------------------------|
| 200         | OK           | List of all transactions in chronological order.  |


### A3: Show a list of transactions in chronological order linked to a given person
To show a list of transactions in chronological order linked to a given person, you have to send a `GET` request to the route `localhost:5000/transaction/view-by-person`.
#### Request Parameters

The `GET` request must include a `JSON` object with the following elements:

| Parameter  | Type         | Description                                    |
|------------|--------------|------------------------------------------------|
| `person_id`    | Integer  | The ID of the person linked to the transactions. |

#### Responses
| HTTP Status | Response     | Description                                       |
|-------------|--------------|---------------------------------------------------|
| 200         | OK           | The list of transactions has been successfully returned.           |
| 400         | Bad Request  | Invalid request: Missing parameters or incorrect data. |

#### Example
```json
{
    "person_id": 0
}
```


### A4: Show the bank balance of the person given
To show the bank balance of the person given, you have to send a `GET` request to the route `localhost:5000/person/bank-balance`.
#### Request Parameters

The `GET` request must include a `JSON` object with the following elements:

| Parameter  | Type         | Description                                    |
|------------|--------------|------------------------------------------------|
| `person_id`    | Integer  | The ID of the person given. |

#### Responses
| HTTP Status | Response     | Description                                       |
|-------------|---++++---------------|---------------------------------------------------|.
+-*+-*-+-*+/-++-*++++++++++++-+|+-++.+---*-.3+ +-+2+-+0++.+-+-+--+0+- + +.--*--*.-*3.3*+3.*+3.-*-*-*+ -*  +-+ +.   | OK           | The bank balance has been successfully returned.           |0
| 400         | Bad Request  | Invalid request: Missing parameters or incorrect data. |

#### Example
```json
{
    "person_id": 0
}
```


## Choice of technologies
For this project, we have chosen to use Python as main programming language, the Flask web framework and the SQLite database management system.Our choices are motivated by several considerations:

### 1. Simplicity and ease of learning
Python is renowned for its clear syntax and its ease of learning, which makes it an ideal choice, especially in an educational context.Flask, as a minimalist web framework, shares this philosophy of simplicity, allowing rapid and efficient web development.

### 2. Speed of development
Flask offers rapid development of web applications while allowing in -depth personalization.Its modular approach allows us to add features as our project develops, which is particularly useful given our time constraint.

### 3. Flexibility and total control
Flask offers us the flexibility necessary to design an application that specifically meets our needs.Using Flask, we have total control over the structure of our application, which is essential to achieve our design objectives.

### 4. Abundant documentation and active community
Python, Flask and Sqlite benefit from large developer communities and many online documentation resources.This provides us with quick access to relevant information and solutions to any problems that we could encounter during development.

### 5. SQLite for data management
We have opted for SQLite as a database management system because of its simplicity and its transparent integration with Python.For our project, which involves relatively simple data storage, SQLite offers a light and effective solution without requiring complex configuration.

### 6. Portability and compatibility
Python being an interpreted language, our application will be portable and will be able to run on any platform compatible with Python.This guarantees coherent user experience, regardless of the execution environment.

In summary, our choice of Python, Flask and SQLite is based on their simplicity, their speed of development, their flexibility, their exhaustive documentation and their compatibility.These technologies allow us to create a robust and functional web application that meets our requirements while offering us the possibility of demonstrating our programming and application design skills.


## Exercise 4
After executing the following request `SELECT * FROM transactions;` on the database, we obtain the following result:
`(1, 1, 2, 150.0, '2023-11-13 21:36:58.939091')`.  
It means that the transaction with the ID 1 has been created between the person with the ID 1 and the person with the ID 2, the amount of the transaction is 150.0€ and the date of the transaction is 2023-11-13 21:36:58.939091.  
We ran the SQL request `UPDATE transactions SET amount = 100 WHERE id = 1` to change the amount of the transaction with the ID 1 to 100€.
Now, if we execute the request `SELECT * FROM transactions;` on the database, we obtain the following result:
`(1, 1, 2, 100.0, '2023-11-13 21:36:58.939091')`.  
The amount of the transaction with the ID 1 has been changed to 100€, it can be a potential security vulnerability because it is possible to change the amount of a transaction after it has been created.  
The script can be found in the file `tests/tests.ipynb`.

# Tchaî v2

The hash function used in the code is SHA-256. This hash function is employed to generate a hash token for each transaction carried out.

SHA-256 is a cryptographic hash function that takes input of any size and converts it into a fixed output of 256 bits. This means that once an input is hashed using SHA-256, it will consistently produce the same 256-bit output, regardless of the original input size. Furthermore, the hash function is a one-way operation, implying that it is highly challenging, if not impossible, to deduce the original input from the hash output.

In this code, the hash function is utilized to create a hash token for every transaction performed. Transaction data is converted into a string (str(transaction_data)), then encoded into bytes (encode()). The sha256() function from the hashlib library is employed to create the hash token. Finally, the hexdigest() function is used to return the hash token as a hexadecimal string.

The choice of SHA-256 is a sound one as it is considered secure and widely used in security applications for reliably generating hash tokens.

## Exercise 6
To know if the transactions are valid, you have to send a `GET` request to the route `localhost:5000/transaction/check-hash`.
#### Request Parameters

No parameters required.

#### Responses
| HTTP Status | Response     | Description                                                  |
|-------------|--------------|--------------------------------------------------------------|
| 200         | OK           | List of all transactions with the information valid or not.  |

## Exercise 7
To address this potential security vulnerability, the transactions table in the database has been updated to include a hash column. This column stores the hash of each transaction. When a transaction is retrieved, the program computes the hash of the transaction data and compares it with the stored hash in the database. If the two hashes do not match, it indicates that the transaction data has been altered manually after its creation, and the program will raise an error. This mechanism ensures the integrity of the transaction data and prevents unauthorized modifications.  
A demonstration of this mechanism can be found in the file `tests/tests.ipynb`.

## Exercise 8
While the hash column in the transactions table helps ensure the integrity of transaction data, it does not prevent rows from being deleted from the table. If a row is deleted, the corresponding transaction data is lost, which could be a potential security vulnerability. This is because unauthorized users could potentially delete transaction records, leading to loss of important data. Measures should be taken to prevent unauthorized deletion of rows from the transactions table to ensure complete data integrity and security.
The script for line deletion can be found in the file `tests/tests.ipynb`.

