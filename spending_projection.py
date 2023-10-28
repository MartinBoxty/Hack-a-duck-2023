def spendingProj(transactions):
    mean = 0
    print("projected spendings = "+mean)
    # we need to look at the dates of the transactions. after that we look at all of the transactions
    # at that month and the other month (if there is one) and "return mean_average".
    # if there is not enough data to calculate a mean for the user, we return 0.


    highestCategory = {'mcdonalds':100000} # sorted dic of categories by spendings and print from the highest to lowest
    print(highestCategory)

    difference = 0; # how much you have spent so far compared to the prev month
    print ("difference = "+difference)

    # print the graph (in text format for now)
    transactionsThisYear = {"29.10.23":0} # dic of spendings this year with date
    for key, value in transactionsThisYear.items():
        print(f"{key}: {value}")