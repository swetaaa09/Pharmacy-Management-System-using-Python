import mysql.connector
from mysql.connector import Error
from tkinter import *
from tkinter import messagebox

# Function to connect to the MySQL database
def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="pharma"
        )
        if connection.is_connected():
            print("Successfully connected to the 'pharma' database.")
            return connection
    except Error as e:
        print(f"Error: {e}")
    return None

# Create the database connection
db_connection = create_connection()

root = Tk()
root.title("Simple Pharmacy Management System")
root.configure(width=1500, height=600, bg='BLACK')

def additem():
    e1 = entry1.get()
    e2 = entry2.get()
    e3 = entry3.get()
    e4 = entry4.get()
    e5 = entry5.get()
    
    if db_connection:
        cursor = db_connection.cursor()
        cursor.execute("INSERT INTO pharmacy_item (item_name, item_price, item_quantity, item_category, item_discount) VALUES (%s, %s, %s, %s, %s)", (e1, e2, e3, e4, e5))
        db_connection.commit()
        cursor.close()
        clearitem()
        messagebox.showinfo("Success", "Item added successfully.")

def deleteitem():
    e1 = entry1.get()
    
    if db_connection:
        cursor = db_connection.cursor()
        cursor.execute("DELETE FROM pharmacy_item WHERE item_name = %s", (e1,))
        db_connection.commit()
        cursor.close()
        clearitem()
        messagebox.showinfo("Success", "Item deleted successfully.")

def firstitem():
    if db_connection:
        cursor = db_connection.cursor()
        cursor.execute("SELECT * FROM pharmacy_item LIMIT 1")
        item = cursor.fetchone()
        if item:
            populate_fields(item)
        else:
            messagebox.showinfo("Info", "No items found.")
        cursor.close()

def nextitem():
    if db_connection:
        cursor = db_connection.cursor()
        cursor.execute("SELECT * FROM pharmacy_item")
        items = cursor.fetchall()
        if items:
            global var
            var += 1
            if var < len(items):
                populate_fields(items[var])
            else:
                var = len(items) - 1
                messagebox.showinfo("Info", "No more records.")
        cursor.close()

def previousitem():
    if db_connection:
        cursor = db_connection.cursor()
        cursor.execute("SELECT * FROM pharmacy_item")
        items = cursor.fetchall()
        if items:
            global var
            var -= 1
            if var >= 0:
                populate_fields(items[var])
            else:
                var = 0
                messagebox.showinfo("Info", "No previous records.")
        cursor.close()

def lastitem():
    if db_connection:
        cursor = db_connection.cursor()
        cursor.execute("SELECT * FROM pharmacy_item ORDER BY item_id DESC LIMIT 1")
        item = cursor.fetchone()
        if item:
            populate_fields(item)
        else:
            messagebox.showinfo("Info", "No items found.")
        cursor.close()

def updateitem():
    e1 = entry1.get()
    e2 = entry2.get()
    e3 = entry3.get()
    e4 = entry4.get()
    e5 = entry5.get()
    
    if db_connection:
        cursor = db_connection.cursor()
        cursor.execute("UPDATE pharmacy_item SET item_price = %s, item_quantity = %s, item_category = %s, item_discount = %s WHERE item_name = %s", (e2, e3, e4, e5, e1))
        db_connection.commit()
        cursor.close()
        clearitem()
        messagebox.showinfo("Success", "Item updated successfully.")

def searchitem():
    e1 = entry1.get()
    
    if db_connection:
        cursor = db_connection.cursor()
        cursor.execute("SELECT * FROM pharmacy_item WHERE item_name = %s", (e1,))
        item = cursor.fetchone()
        if item:
            populate_fields(item)
        else:
            messagebox.showinfo("Not Found", "Item not found.")
        cursor.close()

def populate_fields(item):
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)

    entry1.insert(0, item[1])  # Name
    entry2.insert(0, item[2])  # Price
    entry3.insert(0, item[3])  # Quantity
    entry4.insert(0, item[4])  # Category
    entry5.insert(0, item[5])  # Discount

def clearitem():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)

# UI Setup
label0 = Label(root, text="PHARMACY MANAGEMENT SYSTEM", bg="black", fg="white", font=("Times", 30))
label1 = Label(root, text="ENTER ITEM NAME", bg="red", fg="white", font=("Times", 12), width=25)
entry1 = Entry(root, font=("Times", 12))
label2 = Label(root, text="ENTER ITEM PRICE", bg="red", fg="white", font=("Times", 12), width=25)
entry2 = Entry(root, font=("Times", 12))
label3 = Label(root, text="ENTER ITEM QUANTITY", bg="red", fg="white", font=("Times", 12), width=25)
entry3 = Entry(root, font=("Times", 12))
label4 = Label(root, text="ENTER ITEM CATEGORY", bg="red", fg="white", font=("Times", 12), width=25)
entry4 = Entry(root, font=("Times", 12))
label5 = Label(root, text="ENTER ITEM DISCOUNT", bg="red", fg="white", font=("Times", 12), width=25)
entry5 = Entry(root, font=("Times", 12))

# Buttons
button1 = Button(root, text="ADD ITEM", bg="white", fg="black", width=20, font=("Times", 12), command=additem)
button2 = Button(root, text="DELETE ITEM", bg="white", fg="black", width=20, font=("Times", 12), command=deleteitem)
button3 = Button(root, text="VIEW FIRST ITEM", bg="white", fg="black", width=20, font=("Times", 12), command=firstitem)
button4 = Button(root, text="VIEW NEXT ITEM", bg="white", fg="black", width=20, font=("Times", 12), command=nextitem)
button5 = Button(root, text="VIEW PREVIOUS ITEM", bg="white", fg="black", width=20, font=("Times", 12), command=previousitem)
button6 = Button(root, text="VIEW LAST ITEM", bg="white", fg="black", width=20, font=("Times", 12), command=lastitem)
button7 = Button(root, text="UPDATE ITEM", bg="white", fg="black", width=20, font=("Times", 12), command=updateitem)
button8 = Button(root, text="SEARCH ITEM", bg="white", fg="black", width=20, font=("Times", 12), command=searchitem)
button9 = Button(root, text="CLEAR SCREEN", bg="white", fg="black", width=20, font=("Times", 12), command=clearitem)

# Grid layout
label0.grid(columnspan=6, padx=10, pady=10)
label1.grid(row=1, column=0, sticky=W, padx=10, pady=10)
label2.grid(row=2, column=0, sticky=W, padx=10, pady=10)
label3.grid(row=3, column=0, sticky=W, padx=10, pady=10)
label4.grid(row=4, column=0, sticky=W, padx=10, pady=10)
label5.grid(row=5, column=0, sticky=W, padx=10, pady=10)
entry1.grid(row=1, column=1, padx=40, pady=10)
entry2.grid(row=2, column=1, padx=10, pady=10)
entry3.grid(row=3, column=1, padx=10, pady=10)
entry4.grid(row=4, column=1, padx=10, pady=10)
entry5.grid(row=5, column=1, padx=10, pady=10)
button1.grid(row=1, column=4, padx=40, pady=10)
button2.grid(row=1, column=5, padx=40, pady=10)
button3.grid(row=2, column=4, padx=40, pady=10)
button4.grid(row=2, column=5, padx=40, pady=10)
button5.grid(row=3, column=4, padx=40, pady=10)
button6.grid(row=3, column=5, padx=40, pady=10)
button7.grid(row=4, column=4, padx=40, pady=10)
button8.grid(row=4, column=5, padx=40, pady=10)
button9.grid(row=5, column=5, padx=40, pady=10)

# Global variable for current index
var = 0

root.mainloop()

# Close the database connection when done
if db_connection and db_connection.is_connected():
    db_connection.close()
