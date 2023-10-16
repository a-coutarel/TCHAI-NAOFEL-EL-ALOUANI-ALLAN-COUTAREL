# Systèmes d’information avancés - Projet TP Tchaî

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

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

## Exercise 3
### <span style="color:blue"> A1: Save a transaction </span>
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


### <span style="color:blue"> A2: Show a list of all transactions in chronological order </span>
To show a list of all transactions in chronological order, you have to send a `GET` request to the route `localhost:5000/transaction/view-in-chronological-order`.
#### Request Parameters

No parameters required.

#### Responses
| HTTP Status | Response     | Description                                       |
|-------------|--------------|---------------------------------------------------|
| 200         | OK           | List of all transactions in chronological order.  |


### <span style="color:blue"> A3: Show a list of transactions in chronological order linked to a given person </span>
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


### <span style="color:blue"> A4: Show the bank balance of the person given </span>
To show the bank balance of the person given, you have to send a `GET` request to the route `localhost:5000/person/bank-balance`.
#### Request Parameters

The `GET` request must include a `JSON` object with the following elements:

| Parameter  | Type         | Description                                    |
|------------|--------------|------------------------------------------------|
| `person_id`    | Integer  | The ID of the person given. |

#### Responses
| HTTP Status | Response     | Description                                       |
|-------------|--------------|---------------------------------------------------|
| 200         | OK           | The bank balance has been successfully returned.           |
| 400         | Bad Request  | Invalid request: Missing parameters or incorrect data. |

#### Example
```json
{
    "person_id": 0
}
```