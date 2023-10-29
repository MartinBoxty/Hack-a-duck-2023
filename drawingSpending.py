from AdditionalFunctions import compareDate

def drawSpending(chosenDate, *allTransactions):

    year = int((chosenDate.split(" ")[0]).split("-")[0])
    month = int((chosenDate.split(" ")[0]).split("-")[1])
    day = int((chosenDate.split(" ")[0]).split("-")[2])

    if month < 10:
        month = f"0{month}"

    if (int((chosenDate.split(" ")[0]).split("-")[1]) == 0o01):
        prevMonthDateFirstDay = f"{year-1}-12-01 01:19:03"
        prevMonthEndDate = f"{year-1}-12-31 08:19:03"
    else:
        prevMonthDateFirstDay = f"{year}-{month}-01 08:19:03"
        prevMonthEndDate = f"{year}-{month}-31 08:19:03"


    yearPredictionStartDate = f"{year-1}-01-01 08:19:03"
    yearPredictionEndDate = f"{year - 1}-12-31 08:19:03"


    prevMonthTotal = 0;
    prevYearTotal = 0;

    for tempElement in allTransactions:
        for transaction in tempElement:

            if (compareDate(transaction["date"], chosenDate) == 1) and (transaction["CreditDebit"] == "Credit"):
                print(transaction["date"])

            if (compareDate(transaction["date"], prevMonthDateFirstDay) == 0) and (transaction["CreditDebit"] == "Credit") and (compareDate(transaction["date"], prevMonthEndDate) == 1):
                prevMonthTotal += transaction["amount"]

            if (compareDate(transaction["date"], yearPredictionStartDate) == 0) and (transaction["CreditDebit"] == "Credit") and (compareDate(transaction["date"], yearPredictionEndDate) == 1):
                prevYearTotal += transaction["amount"]

    monthPredictionStartDateDic = {"money":0, "date":prevMonthDateFirstDay}
    monthPredictionDic = {"money":prevMonthTotal, "date":prevMonthEndDate}

    yearPredictionStartDic = {"money":0, "date":yearPredictionStartDate}
    yearPredictionDic = {"money":prevYearTotal, "date":yearPredictionEndDate}

    print(monthPredictionStartDateDic)
    print(monthPredictionDic)
    print(yearPredictionStartDic)
    print(yearPredictionDic)




