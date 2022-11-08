#pip install PyMySQL
import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

# DATABASE code -------------------------------------------------------------------
def connection():
    conn = pymysql.connect(
        host='localhost',
        user='subodh', 
        password='',
        db='flower',
    )
    return conn

# function to clear all the values from entry points (call from refresh button)
def refreshTable():     
    for data in my_tree.get_children():
        my_tree.delete(data)

    for array in read():
        my_tree.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE', font=('Arial', 12))
    my_tree.grid(row=8, column=0, columnspan=5, rowspan=11, padx=10, pady=20)

root = Tk()
root.title("Flourist database system")
my_tree = ttk.Treeview(root)

#placeholders for entry
ph1 = tk.StringVar()
ph2 = tk.StringVar()
ph3 = tk.StringVar()
ph4 = tk.StringVar()
ph5 = tk.StringVar()

#placeholder set value function
def setph(word,num):
    if num ==1:
        ph1.set(word)
    if num ==2:
        ph2.set(word)
    if num ==3:
        ph3.set(word)
    if num ==4:
        ph4.set(word)
    if num ==5:
        ph5.set(word)

# function for CRUD operations (Executed by Their respective Buttons)
def read():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM flower")
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results

def add():
    flower_id = str(flower_idEntry.get())
    flower_name = str(flower_nameEntry.get())
    quantity = str(quantityEntry.get())
    price = str(priceEntry.get())
    Timestamp = str(TimestampEntry.get())

    if (flower_id == "" or flower_id == " ") or (flower_name == "" or flower_name == " ") or (quantity == "" or quantity == " ") or (price == "" or price == " ") or (Timestamp == "" or Timestamp == " "):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO flower VALUES ('"+flower_id+"','"+flower_name+"','"+quantity+"','"+price+"','"+Timestamp+"') ")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "ID already exist")
            return

    refreshTable()
    

def reset():
    decision = messagebox.askquestion("Warning!!", "Delete all data?")
    if decision != "yes":
        return 
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM flower")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Sorry an error occured")
            return

        refreshTable()

def delete():
    decision = messagebox.askquestion("Warning!!", "Delete the selected data?")
    if decision != "yes":
        return 
    else:
        selected_item = my_tree.selection()[0]
        deleteData = str(my_tree.item(selected_item)['values'][0])
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM flower WHERE flower_id='"+str(deleteData)+"'")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Sorry an error occured")
            return

        refreshTable()

def select():
    try:
        selected_item = my_tree.selection()[0]
        flower_id = str(my_tree.item(selected_item)['values'][0])
        flower_name = str(my_tree.item(selected_item)['values'][1])
        quantity = str(my_tree.item(selected_item)['values'][2])
        price = str(my_tree.item(selected_item)['values'][3])
        Timestamp = str(my_tree.item(selected_item)['values'][4])

        setph(flower_id,1)
        setph(flower_name,2)
        setph(quantity,3)
        setph(price,4)
        setph(Timestamp,5)
    except:
        messagebox.showinfo("Error", "Please select a data row")

def search():
    flower_id = str(flower_idEntry.get())
    flower_name = str(flower_nameEntry.get())
    quantity = str(quantityEntry.get())
    price = str(priceEntry.get())
    Timestamp = str(TimestampEntry.get())

    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM flower WHERE flower_id='"+
    flower_id+"' or flower_name='"+
    flower_name+"' or quantity='"+
    quantity+"' or price='"+
    price+"' or Timestamp='"+
    Timestamp+"' ")
    
    try:
        result = cursor.fetchall()

        for num in range(0,5):
            setph(result[0][num],(num+1))

        conn.commit()
        conn.close()
    except:
        messagebox.showinfo("Error", "No data found")

def update():
    selectedflower_id = ""

    try:
        selected_item = my_tree.selection()[0]
        selectedflower_id = str(my_tree.item(selected_item)['values'][0])
    except:
        messagebox.showinfo("Error", "Please select a data row")

    flower_id = str(flower_idEntry.get())
    flower_name = str(flower_nameEntry.get())
    quantity = str(quantityEntry.get())
    price = str(priceEntry.get())
    Timestamp = str(TimestampEntry.get())

    if (flower_id == "" or flower_id == " ") or (flower_name == "" or flower_name == " ") or (quantity == "" or quantity == " ") or (price == "" or price == " ") or (Timestamp == "" or Timestamp == " "):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE flower SET flower_id='"+
            flower_id+"', flower_name='"+
            flower_name+"', quantity='"+
            quantity+"', price='"+
            price+"', Timestamp='"+
            Timestamp+"' WHERE flower_id='"+
            selectedflower_id+"' ")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "ID already exist")
            return

    refreshTable()

# UI Components ------------------------------------------------------------------

label = Label(root, text="Flourist Database System ", font=('Arial Bold', 25))
label.grid(row=0, column=0, columnspan=8, rowspan=2, padx=50, pady=20)

flower_idLabel = Label(root, text="ID", font=('Arial', 15))
flower_nameLabel = Label(root, text="Name", font=('Arial', 15))
quantityLabel = Label(root, text="Quantity", font=('Arial', 15))
priceLabel = Label(root, text="price", font=('Arial', 15))
TimestampLabel = Label(root, text="Timestamp", font=('Arial', 15))

flower_idLabel.grid(row=3, column=0, columnspan=1, padx=50, pady=5)
flower_nameLabel.grid(row=4, column=0, columnspan=1, padx=50, pady=5)
quantityLabel.grid(row=5, column=0, columnspan=1, padx=50, pady=5)
priceLabel.grid(row=6, column=0, columnspan=1, padx=50, pady=5)
TimestampLabel.grid(row=7, column=0, columnspan=1, padx=50, pady=5)

flower_idEntry = Entry(root, width=55, bd=2, font=('Arial', 15), textvariable = ph1)
flower_nameEntry = Entry(root, width=55, bd=2, font=('Arial', 15), textvariable = ph2)
quantityEntry = Entry(root, width=55, bd=2, font=('Arial', 15), textvariable = ph3)
priceEntry = Entry(root, width=55, bd=2, font=('Arial', 15), textvariable = ph4)
TimestampEntry = Entry(root, width=55, bd=2, font=('Arial', 15), textvariable = ph5)

flower_idEntry.grid(row=3, column=1, columnspan=4, padx=5, pady=0)
flower_nameEntry.grid(row=4, column=1, columnspan=4, padx=5, pady=0)
quantityEntry.grid(row=5, column=1, columnspan=4, padx=5, pady=0)
priceEntry.grid(row=6, column=1, columnspan=4, padx=5, pady=0)
TimestampEntry.grid(row=7, column=1, columnspan=4, padx=5, pady=0)

addBtn = Button(
    root, text="Add", padx=65, pady=25, width=10,
    bd=2, font=('Arial', 15), bg="#84F894", command=add)
updateBtn = Button(
    root, text="Update", padx=65, pady=25, width=10,
    bd=2, font=('Arial', 15), bg="#84E8F8", command=update)
deleteBtn = Button(
    root, text="Delete", padx=65, pady=25, width=10,
    bd=2, font=('Arial', 15), bg="#FF9999", command=delete)
searchBtn = Button(
    root, text="Search", padx=65, pady=25, width=10,
    bd=2, font=('Arial', 15), bg="#F4FE82", command=search)
resetBtn = Button(
    root, text="Reset", padx=65, pady=25, width=10,
    bd=2, font=('Arial', 15), bg="#F398FF", command=reset)
selectBtn = Button(
    root, text="Select", padx=65, pady=25, width=10,
    bd=2, font=('Arial', 15), bg="#b6fcec", command=select)

addBtn.grid(row=3, column=5, columnspan=1, rowspan=2)
updateBtn.grid(row=5, column=5, columnspan=1, rowspan=2)
deleteBtn.grid(row=7, column=5, columnspan=1, rowspan=2)
searchBtn.grid(row=9, column=5, columnspan=1, rowspan=2)
resetBtn.grid(row=11, column=5, columnspan=1, rowspan=2)
selectBtn.grid(row=13, column=5, columnspan=1, rowspan=2)

# Table Tree component for viewing data-----------------------------------------

style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial Bold', 15))

my_tree['columns'] = ("ID","Name","Quantity","price","Timestamp")

my_tree.column("#0", width=0, stretch=NO)
my_tree.column("ID", anchor=W, width=170)
my_tree.column("Name", anchor=W, width=150)
my_tree.column("Quantity", anchor=W, width=150)
my_tree.column("price", anchor=W, width=165)
my_tree.column("Timestamp", anchor=W, width=150)

my_tree.heading("ID", text="ID", anchor=W)
my_tree.heading("Name", text="Name", anchor=W)
my_tree.heading("Quantity", text="Quantity", anchor=W)
my_tree.heading("price", text="price", anchor=W)
my_tree.heading("Timestamp", text="Timestamp", anchor=W)

refreshTable()

root.mainloop()