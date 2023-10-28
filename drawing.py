import json
import requests
import scratch
import tkinter as tk
import matplotlib.pyplot as plt
import csv
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg





root = tk.Tk()
root['bg'] = '#f4ffff'
root.title('app')
root.geometry('1024x600')
root.resizable(width=True, height=True)

data = [
    {"date": "2023-10-15", "money": 20},
    {"date": "2023-10-20", "money": 100},
    {"date": "2023-10-25", "money": 111},
]

dates = [entry["date"] for entry in data]
money = [entry["money"] for entry in data]

fig, ax = plt.subplots()
ax.plot(dates, money, marker='o', linestyle='-', color='b')
ax.grid(True)

data1 = [
    {"date": "2023-10-15", "money": 40},
    {"date": "2023-10-20", "money": 120},
    {"date": "2023-10-25", "money": 11},
]

dates = [entry["date"] for entry in data1]
money = [entry["money"] for entry in data1]

ax.plot(dates, money, marker='o', linestyle='-', color='r')
ax.grid(True)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack()

root.mainloop()