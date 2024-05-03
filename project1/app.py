import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

DATA_FILE = 'advertising_agency_data.csv'

try:
    df = pd.read_csv(DATA_FILE)
except FileNotFoundError:
    df = pd.DataFrame(columns=['Date', 'Campaign', 'Client', 'Expense'])
    df.to_csv(DATA_FILE, index=False)


def add_entry():
    global df
    date = datetime.now().strftime('%Y-%m-%d')
    campaign = campaign_entry.get()
    client = client_entry.get()
    expense = expense_entry.get()

    new_entry = pd.DataFrame([[date, campaign, client, expense]],
                             columns=['Date', 'Campaign', 'Client', 'Expense'])
    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_csv(DATA_FILE, index=False)
    messagebox.showinfo("Успіх", "Запис успішно додано.")
    refresh_display()


def show_graph():
    campaign_expenses = df.groupby('Campaign')['Expense'].sum()

    plt.figure(figsize=(8, 6))
    plt.bar(campaign_expenses.index, campaign_expenses.values, color='skyblue')
    plt.xlabel('Кампанія')
    plt.ylabel('Витрати')
    plt.title('Загальні витрати за кампаніями')
    plt.xticks(rotation=45)
    plt.show()


def search_entry():
    campaign = campaign_search_entry.get()
    search_result = df[df['Campaign'] == campaign]
    search_result_window = tk.Toplevel(root)
    search_result_window.title("Результат пошуку")
    tree = ttk.Treeview(search_result_window)
    tree["columns"] = ("Date", "Campaign", "Client", "Expense")
    tree.heading('#0', text='Індекс')
    tree.heading('Date', text='Дата')
    tree.heading('Campaign', text='Кампанія')
    tree.heading('Client', text='Клієнт')
    tree.heading('Expense', text='Витрати')
    for index, row in search_result.iterrows():
        tree.insert("", tk.END, text=index, values=row.tolist())
    tree.pack()


root = tk.Tk()
root.title("Інформаційно-пошукова система для рекламної агенції")

tk.Label(root, text="Новий запис").grid(row=0, column=0, columnspan=2)
tk.Label(root, text="Кампанія:").grid(row=1, column=0)
campaign_entry = tk.Entry(root)
campaign_entry.grid(row=1, column=1)
tk.Label(root, text="Клієнт:").grid(row=2, column=0)
client_entry = tk.Entry(root)
client_entry.grid(row=2, column=1)
tk.Label(root, text="Витрати:").grid(row=3, column=0)
expense_entry = tk.Entry(root)
expense_entry.grid(row=3, column=1)
add_button = tk.Button(root, text="Додати запис", command=add_entry)
add_button.grid(row=4, column=0, columnspan=2)

show_graph_button = tk.Button(root, text="Показати графік", command=show_graph)
show_graph_button.grid(row=5, column=0, columnspan=2)

tk.Label(root, text="Пошук запису").grid(row=6, column=0, columnspan=2)
tk.Label(root, text="Кампанія:").grid(row=7, column=0)
campaign_search_entry = tk.Entry(root)
campaign_search_entry.grid(row=7, column=1)
search_button = tk.Button(root, text="Знайти запис", command=search_entry)
search_button.grid(row=8, column=0, columnspan=2)

tk.Label(root, text="Дані").grid(row=0, column=2, columnspan=3)
treeview = ttk.Treeview(root, columns=('Date', 'Campaign', 'Client', 'Expense'))
treeview.heading('#0', text='Індекс')
treeview.heading('Date', text='Дата')
treeview.heading('Campaign', text='Кампанія')
treeview.heading('Client', text='Клієнт')
treeview.heading('Expense', text='Витрати')
treeview.grid(row=1, column=2, rowspan=8, columnspan=3)


def refresh_display():
    global treeview
    for i in treeview.get_children():
        treeview.delete(i)
    for index, row in df.iterrows():
        treeview.insert("", "end", text=index, values=row.tolist())


refresh_display()

root.mainloop()
