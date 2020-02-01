from tkinter import *
import sqlite3
def buyproduct(id,price):
    con=sqlite3.connect('mydatabase.db')
    cur=con.cursor()
    top = Tk()
    top.geometry("300x250")
    top.resizable(False,False)
    top.title("Product compare")
    head = Label(top, text = "    ODRER PLACED     ", fg = "red", bg = "white", relief=RIDGE,font = "Verdana 15 bold").pack(side=TOP)
    #////////////////////////////////////////////////
    divmain = Frame(top, highlightbackground="black", bg="white", highlightthickness=2, width=285, height=200, bd= 0)
    divmain.place(x = 10,y = 40)
    com = Label(divmain, text="COMPANY: ", font="Verdana 10")
    com.place(x=15, y=10)
    com = Entry(divmain, width=20, bd=1, relief=GROOVE, bg="white")  ######company
    com.place(x=140, y=10)

    mod = Label(divmain, text="MODEL: ", font="Verdana 10")
    mod.place(x=15, y=40)
    mod = Entry(divmain, width=20, bd=1, relief=GROOVE, bg="white")  ######company
    mod.place(x=140, y=40)

    ram = Label(divmain, text="RAM: ", font="Verdana 10")
    ram.place(x=15, y=70)
    ram = Entry(divmain, width=20, bd=1, relief=GROOVE, bg="white")  ######company
    ram.place(x=140, y=70)

    price1 = Entry(divmain, width=20, bd=1, relief=GROOVE, bg="white")  ######company
    price1.place(x=80, y=110)
    com1 = Label(divmain, text="PRODUCT PLACED PAY :COD ", font="Verdana 12",bg="green",fg="white").place(x=10, y=140)
    #---------*********************************--------------
    query = "select * from phones where id={}".format(id)
    result = cur.execute(query).fetchone()
    company = result[0]
    MODEL = result[2]
    RAM = result[3]
    com.insert(0, company)
    com.config(state='disabled')
    mod.insert(0, MODEL)
    mod.config(state='disabled')
    ram.insert(0, RAM)
    ram.config(state='disabled')

    price1.insert(0, price)
    price1.config(state='disabled')
    top.mainloop()
#buyproduct(3,14000)