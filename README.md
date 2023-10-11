# Tchaî 5A Project 

## Authors
* EL ALOUANI Naofel (email: naofel_el-alouani@etu.u-bourgogne.fr)
* COUTAREL Allan (email: allan_coutarel@etu.u-bourgogne.fr)

## Installation
- Clone the repository:  
`git clone https://github.com/a-coutarel/TCHAI-NAOFEL-EL-ALOUANI-ALLAN-COUTAREL.git`
- Enter in the repository:  
`cd TCHAI-NAOFEL-EL-ALOUANI-ALLAN-COUTAREL`
- Install Flask:  
`pip install flask`
- Export the environment variable:  
```
cd controllers  
export FLASK_APP=app.controller
```
- Launch the application:  
`flask run`

## Exercises 3
### A1: Save a transaction
To create a transaction you have to send a `POST` request to the route `localhost:5000/transaction/create`.
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
| 201         | Created      | The transaction was successfully saved.           |
| 400         | Bad Request  | Invalid request: Missing parameters or incorrect data. |

#### Example
```json
{
    "p1_id": 0,
    "p2_id": 1,
    "amount": 20.0
}
```