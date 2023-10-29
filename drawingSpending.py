from AdditionalFunctions import compareDate
import json
import requests
import scratch
import tkinter as tk
import matplotlib.pyplot as plt
import csv
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure



def drawSpending(chosenDate, *allTransactions):

    spendingsInAMonth = []  # in a period of time
    spendingsInAYear = []




    year = int((chosenDate.split(" ")[0]).split("-")[0])
    month = int((chosenDate.split(" ")[0]).split("-")[1])
    mnth = month -1
    day = int((chosenDate.split(" ")[0]).split("-")[2])

    if month < 10:
        month = f"0{month}"

    if mnth < 10:
        mnth = f"0{mnth}"


    currentMonthSpendigsDatesStart = f"{year}-{month}-01 01:19:03"
    currentMonthSpendigsDatesEnd = f"{year}-{month}-31 01:19:03"

    currentYearSpendigsDatesStart = f"{year}-01-01 01:19:03"
    currentYearSpendigsDatesEnd = f"{year}-12-31 01:19:03"

    if (int((chosenDate.split(" ")[0]).split("-")[1]) == 0o01):
        prevMonthDateFirstDay = f"{year-1}-12-01 01:19:03"
        prevMonthEndDate = f"{year-1}-12-31 08:19:03"
    else:
        prevMonthDateFirstDay = f"{year}-{mnth}-01 08:19:03"
        prevMonthEndDate = f"{year}-{mnth}-31 08:19:03"



    yearPredictionStartDate = f"{year-1}-01-01 08:19:03"
    yearPredictionEndDate = f"{year-1}-12-31 08:19:03"


    prevMonthTotal = 0;
    prevYearTotal = 0;

    for tempElement in allTransactions:
        for transaction in tempElement:

            if (compareDate(transaction["date"], currentMonthSpendigsDatesStart) == 1) and (transaction["CreditDebit"] == "Credit") and (compareDate(transaction["date"], currentMonthSpendigsDatesEnd) == 0):
                print(transaction["date"])
                spendingsInAMonth.append({"money":transaction["money"], "date":transaction["date"]})

            if (compareDate(transaction["date"], currentYearSpendigsDatesStart) == 1) and (transaction["CreditDebit"] == "Credit") and (compareDate(transaction["date"], currentYearSpendigsDatesEnd) == 0):
                print(transaction["date"])
                spendingsInAYear.append({"money":transaction["money"], "date":transaction["date"]})

            if (compareDate(transaction["date"], prevMonthDateFirstDay) == 1) and (transaction["CreditDebit"] == "Credit") and (compareDate(transaction["date"], prevMonthEndDate) == 0):
                prevMonthTotal += transaction["money"]

            if (compareDate(transaction["date"], yearPredictionStartDate) == 1) and (transaction["CreditDebit"] == "Credit") and (compareDate(transaction["date"], yearPredictionEndDate) == 0):
                prevYearTotal += transaction["money"]

    monthPredictionStartDateDic = [{"money":0, "date":prevMonthDateFirstDay},{"money":prevMonthTotal, "date":prevMonthEndDate}]

    yearPredictionStartDic = [{"money":0, "date":yearPredictionStartDate},{"money":prevYearTotal, "date":yearPredictionEndDate}]


    print(monthPredictionStartDateDic)

    print(yearPredictionStartDic)


    root = tk.Tk()
    root['bg'] = '#ffffff'
    root.title('app')
    root.geometry('1024x600')
    root.resizable(width=True, height=True)

    login_label = tk.Label(root, text="Enter UserID: ", bg="white")

    # Pack the label to display it in the window
    login_label.pack()

    userID_entry = tk.Entry()
    userID_entry.pack()

    def login():
        loop = True
        while (loop == True):
            username = userID_entry.get()
            if username == "user":
                loop = False
            else:
                label = tk.Label(root, text="authentification failed, try again", font=("Arial", 18), bg="#ffffff")
                label.pack()


    def display_data(data, data1):
        ax = fig.add_subplot(121)

        dates = [entry["date"] for entry in data]
        money = [entry["money"] for entry in data]
        ax = fig.add_subplot(121)
        ax.plot(dates, money, marker='o', linestyle='-', color='b')
        ax.grid(True)

        dates = [entry["date"] for entry in data1]
        money = [entry["money"] for entry in data1]
        #
        ax.plot(dates, money, marker='o', linestyle='-', color='r')
        ax.grid(True)

        categories_spent_data = [
            {"category": "Bills & Utilities", "amount": 843.92},
            {"category": "Food & Dining", "amount": 517.06}
        ]

        categories = [begin["category"] for begin in categories_spent_data]
        amount = [begin["amount"] for begin in categories_spent_data]

        ax2 = fig.add_subplot(122)
        ax2.pie(amount, labels=categories, autopct='%1.1f%%', startangle=90, colors=['r', 'g', 'b', 'y'])

        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack()
    # here will be a function that will choose data for a month
    def show_for_month():
        data_for_analysis_of_spendings = spendingsInAMonth
        display_data(data_for_analysis_of_spendings, monthPredictionStartDateDic)

    # here will be a function that will choose data for a year
    def show_for_year():
        display_data(spendingsInAYear, yearPredictionStartDic)

    text = input()

    label = tk.Label(root, text=text, font=("Arial", 18), bg="#ffffff")
    label.pack()

    # after data u should put function from that will put needed data into data variable




    fig = Figure(figsize=(8, 4), dpi=100)

    # put here function that will give data of projection of spendings
    # projection = yearPredictionStartDic
    # projection = monthPredictionStartDateDic
    #     {"date": "2023-10-15", "money": 40},
    #     {"date": "2023-10-20", "money": 120},
    #     {"date": "2023-10-25", "money": 11},
    # ]
    #
    # dates = [entry["date"] for entry in projection]
    # money = [entry["money"] for entry in projection]
    #
    # ax.plot(dates, money, marker='o', linestyle='-', color='r')
    # ax.grid(True)




    button_frame = tk.Frame(root)
    button_frame.pack()

    month_button = tk.Button(button_frame, text="Month", command=show_for_month)
    month_button.configure(bg="white", highlightbackground="white", font=("Arial", 20))
    month_button.pack(side=tk.LEFT)
    year_button = tk.Button(button_frame, text="Year", command=show_for_year)
    year_button.configure(bg="white", highlightbackground="white", font=("Arial", 20))
    year_button.pack(side=tk.LEFT)

    root.mainloop()

