def compareDate(firstDate, secondDate):  # comparing if firstdate > seconddate

    result = False

    cleanedFirstDate = firstDate.replace("-", "")
    cleanedSecondDate = secondDate.replace("-", "")

    firstYear = int(cleanedFirstDate[:4])
    secondYear = int(cleanedSecondDate[:4])

    firstMonth = int(cleanedFirstDate[4:6])
    secondMonth = int(cleanedSecondDate[4:6])

    firstDay = int(cleanedFirstDate[6:8])
    secondDay = int(cleanedSecondDate[6:8])

    if firstYear > secondYear:
        result = True
    elif firstMonth > secondMonth:
        result = True
    elif firstDay > secondDay:
        result = True

    return result