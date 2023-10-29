import json
import requests
import scratch
from getAmounts import getData
from drawingSpending import drawSpending


from spending_projection import spendingProj



def main():

    transactions = [
        {
            "transactionUUID": "0673bca4-fbb2-46bd-aa76-36243305ceed",
            "accountUUID": "72965642",
            "merchant": {
                "name": "Capital Two",
                "category": "Bills & Utilities",
                "description": "Credit Card Company",
                "pointOfSale": ["Online"]
            },
            "amount": 843.92,
            "creditDebitIndicator": "Credit",
            "currency": "GBP",
            "timestamp": "2023-10-25 08:19:03",
            "emoji": "🤑",
            "latitude": -4.38849,
            "longitude": 52.33594,
            "status": "Successful",
            "message": "Weekly groceries shopping",
            "pointOfSale": "Online"
        },
        {
            "transactionUUID": "0673bca4-fbb2-46bd-aa76-36243305ceed",
            "accountUUID": "72965642",
            "merchant": {
                "name": "Capital Two",
                "category": "Bills & Utilities",
                "description": "Credit Card Company",
                "pointOfSale": ["Online"]
            },
            "amount": 12.92,
            "creditDebitIndicator": "Credit",
            "currency": "GBP",
            "timestamp": "2023-09-18 08:19:03",
            "emoji": "🤑",
            "latitude": -4.38849,
            "longitude": 52.33594,
            "status": "Successful",
            "message": "Weekly groceries shopping",
            "pointOfSale": "Online"
        },
        {
            "transactionUUID": "0673bca4-fbb2-46bd-aa76-36243305ceed",
            "accountUUID": "72965642",
            "merchant": {
                "name": "Capital Two",
                "category": "Bills & Utilities",
                "description": "Credit Card Company",
                "pointOfSale": ["Online"]
            },
            "amount": 1123.92,
            "creditDebitIndicator": "Credit",
            "currency": "GBP",
            "timestamp": "2023-09-02 08:19:03",
            "emoji": "🤑",
            "latitude": -4.38849,
            "longitude": 52.33594,
            "status": "Successful",
            "message": "Weekly groceries shopping",
            "pointOfSale": "Online"
        },
        {
            "transactionUUID": "093c805f-31c1-4721-8642-b7e9a09964f0",
            "accountUUID": "72965642",
            "merchant": {
                "name": "Blahbucks",
                "category": "Food & Dining",
                "description": "Supplying all your coffee needs",
                "pointOfSale": ["In-store"]
            },
            "amount": 517.06,
            "creditDebitIndicator": "Credit",
            "currency": "GBP",
            "timestamp": "2023-07-09 11:47:47",
            "emoji": "🥰",
            "latitude": -1.86852,
            "longitude": 53.39733,
            "status": "Successful",
            "message": "Holiday souvenirs",
            "pointOfSale": "In-store"
        }
    ]
    allTransactions = getData(transactions)



    #spendingProj(transactions, allTransactions)
    drawSpending("2023-10-31 23:59:59", allTransactions)



    #print(transactions[0]["merchant"]["category"])

if __name__ == '__main__':
    main()
