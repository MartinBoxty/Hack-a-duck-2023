def compareDate(firstDate, secondDate):  # comparing if firstdate > seconddate

    result = 2

    # 0 - First Date is later than the Second (First < Second)
    # 1 - Second Date is later than the First (First > Second)
    # 2 - Both are the same (First = Second)

    YearOfFirstDate = (firstDate.split(" ")[0]).split("-")[0]
    MonthOfFirstDate = (firstDate.split(" ")[0]).split("-")[1]
    DayOfFirstDate = (firstDate.split(" ")[0]).split("-")[2]
    HourOfFirstDate = (firstDate.split(" ")[1]).split(":")[0]
    MinuteOfFirstDate = (firstDate.split(" ")[1]).split(":")[1]
    SecondOfFirstDate = ((firstDate.split(" ")[1]).split(":")[2])

    YearOfSecondDate = (secondDate.split(" ")[0]).split("-")[0]
    MonthOfSecondDate = (secondDate.split(" ")[0]).split("-")[1]
    DayOfSecondDate = (secondDate.split(" ")[0]).split("-")[2]
    HourOfSecondDate = (secondDate.split(" ")[1]).split(":")[0]
    MinuteOfSecondDate = (secondDate.split(" ")[1]).split(":")[1]
    SecondOfSecondDate = ((secondDate.split(" ")[1]).split(":")[2])

    if YearOfFirstDate < YearOfSecondDate:
        result = 0
    elif YearOfFirstDate > YearOfSecondDate:
        result = 1
    else:
        # Compare month
        if MonthOfFirstDate < MonthOfSecondDate:
            result = 0
        elif MonthOfFirstDate > MonthOfSecondDate:
            result = 1
        else:
            # Compare day
            if DayOfFirstDate < DayOfSecondDate:
                result = 0
            elif DayOfFirstDate > DayOfSecondDate:
                result = 1
            else:
                # Compare hour
                if HourOfFirstDate < HourOfSecondDate:
                    result = 0
                elif HourOfFirstDate > HourOfSecondDate:
                    result = 1
                else:
                    # Compare minute
                    if MinuteOfFirstDate < MinuteOfSecondDate:
                        result = 0
                    elif MinuteOfFirstDate > MinuteOfSecondDate:
                        result = 1
                    else:
                        # Compare second
                        if SecondOfFirstDate < SecondOfSecondDate:
                            result = 0
                        elif SecondOfFirstDate > SecondOfSecondDate:
                            result = 1

    # 2019-12-16 10:37:34
    # cleanedFirstDate = firstDate.replace("-", "")
    # cleanedSecondDate = secondDate.replace("-", "")
    #
    # firstYear = int(cleanedFirstDate[:4])
    # secondYear = int(cleanedSecondDate[:4])
    #
    # firstMonth = int(cleanedFirstDate[4:6])
    # secondMonth = int(cleanedSecondDate[4:6])
    #
    # firstDay = int(cleanedFirstDate[6:8])
    # secondDay = int(cleanedSecondDate[6:8])


    return result