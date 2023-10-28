def getData(transactions):
    amounts = [{}]

    for transaction in transactions:
        amounts.append({"date": transaction["timestamp"], "money": transaction["amount"], "CreditDebit": transaction["creditDebitIndicator"]})

        
    return amounts