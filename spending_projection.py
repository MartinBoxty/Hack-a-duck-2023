def spendingProj(transactions):
    #mean = 0     not finished this yet
    #print("projected spendings = "+str(mean))
    # we need to look at the dates of the transactions. after that we look at all of the transactions
    # at that month and the other month (if there is one) and "return mean_average".
    # if there is not enough data to calculate a mean for the user, we return 0.

    Categories = {}  #  dic of categories by spendings and print from the highest to lowest
    amounts = [{}]
    highest_amount = 0
    for transaction in transactions:
        print(transaction)
        if transaction['merchant']["category"] not in Categories:
            Categories[transaction['merchant']["category"]] = transaction["amount"]
        else:
            Categories[transaction["category"]] += transaction["amount"]


        amounts.append({"date": transaction["timestamp"], "money":transaction["amount"]})


        if transaction["amount"] > highest_amount:
            highest_amount = transaction["amount"]
            highest_amount_transaction = transaction



    for key, value in Categories.items():
        print(f"{key}: {value}")

    difference = 0;         # how much you have spent so far compared to the prev month
    print ("difference = "+str(difference))

    # print the graph (in text format for now)
    transactionsThisYear = {"29.10.23":0} # dic of spendings this year with date. for a future bar chart
    for key, value in transactionsThisYear.items():
        print(f"{key}: {value}")