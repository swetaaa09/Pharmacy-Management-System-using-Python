import mysql.connector
from tkinter import *
from tkinter import messagebox

# MySQL Database Connection
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="SWeta@09",
        database="pharma"
    )

# Initialize the main application window
root = Tk()
root.title("Simple Pharmacy Management System")
root.configure(width=1500, height=600, bg='BLACK')

# Define Entry widgets globally
entry1 = None
entry2 = None
entry3 = None
entry4 = None
entry5 = None

# Function to clear entry fields
def clearitem():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)

# Function to add an item
def additem():
    conn = connect_db()
    cursor = conn.cursor()

    e1 = entry1.get()
    e2 = entry2.get()
    e3 = entry3.get()
    e4 = entry4.get()
    e5 = entry5.get()

    cursor.execute("INSERT INTO items (name, price, quantity, category, discount) VALUES (%s, %s, %s, %s, %s)",
                   (e1, e2, e3, e4, e5))
    conn.commit()
    cursor.close()
    conn.close()

    clearitem()

# Function to delete an item
def deleteitem():
    conn = connect_db()
    cursor = conn.cursor()

    e1 = entry1.get()
    cursor.execute("DELETE FROM items WHERE name = %s", (e1,))
    conn.commit()
    cursor.close()
    conn.close()

    clearitem()

# Function to view the first item
def firstitem():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM items LIMIT 1")
    row = cursor.fetchone()
    if row:
        populate_fields(row)

    cursor.close()
    conn.close()

# Helper function to populate entry fields
def populate_fields(row):
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)

    entry1.insert(0, row[1])  # name
    entry2.insert(0, row[2])  # price
    entry3.insert(0, row[3])  # quantity
    entry4.insert(0, row[4])  # category
    entry5.insert(0, row[5])  # discount

# Create Labels and Entry widgets
label0 = Label(root, text="PHARMACY MANAGEMENT SYSTEM", bg="black", fg="white", font=("Times", 30))
label0.grid(columnspan=6, padx=10, pady=10)

label1 = Label(root, text="ENTER ITEM NAME", bg="red", relief="ridge", fg="white", font=("Times", 12), width=25)
label1.grid(row=1, column=0, sticky=W, padx=10, pady=10)
entry1 = Entry(root, font=("Times", 12))
entry1.grid(row=1, column=1, padx=40, pady=10)

label2 = Label(root, text="ENTER ITEM PRICE", bg="red", relief="ridge", fg="white", font=("Times", 12), width=25)
label2.grid(row=2, column=0, sticky=W, padx=10, pady=10)
entry2 = Entry(root, font=("Times", 12))
entry2.grid(row=2, column=1, padx=40, pady=10)

label3 = Label(root, text="ENTER ITEM QUANTITY", bg="red", relief="ridge", fg="white", font=("Times", 12), width=25)
label3.grid(row=3, column=0, sticky=W, padx=10, pady=10)
entry3 = Entry(root, font=("Times", 12))
entry3.grid(row=3, column=1, padx=40, pady=10)

label4 = Label(root, text="ENTER ITEM CATEGORY", bg="red", relief="ridge", fg="white", font=("Times", 12), width=25)
label4.grid(row=4, column=0, sticky=W, padx=10, pady=10)
entry4 = Entry(root, font=("Times", 12))
entry4.grid(row=4, column=1, padx=40, pady=10)

label5 = Label(root, text="ENTER ITEM DISCOUNT", bg="red", relief="ridge", fg="white", font=("Times", 12), width=25)
label5.grid(row=5, column=0, sticky=W, padx=10, pady=10)
entry5 = Entry(root, font=("Times", 12))
entry5.grid(row=5, column=1, padx=40, pady=10)

# Create Buttons
button1 = Button(root, text="ADD ITEM", bg="white", fg="black", width=20, font=("Times", 12), command=additem)
button1.grid(row=1, column=4, padx=40, pady=10)

button2 = Button(root, text="DELETE ITEM", bg="white", fg="black", width=20, font=("Times", 12), command=deleteitem)
button2.grid(row=1, column=5, padx=40, pady=10)

button3 = Button(root, text="VIEW FIRST ITEM", bg="white", fg="black", width=20, font=("Times", 12), command=firstitem)
button3.grid(row=2, column=4, padx=40, pady=10)

# Add additional buttons here...

root.mainloop()
