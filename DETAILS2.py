from tkinter import *
import sqlite3
import buy
idn=0
f=0
a=0
p=0
s=0
def runcompare(x):
    global idn
    idn=idn+x
    con=sqlite3.connect('mydatabase.db')
    cur=con.cursor()
    top = Tk()
    top.geometry("300x450")
    top.resizable(False,False)
    top.title("Product compare")
    head = Label(top, text = "    PRODUCT DETAILS    ", fg = "red", bg = "white", relief=RIDGE,font = "Verdana 15 bold").pack(side=TOP)
    #////////////////////////////////////////////////
    divmain = Frame(top, highlightbackground="black", bg="white", highlightthickness=2, width=285, height=400, bd= 0)
    divmain.place(x = 10,y = 40)


    com=Label(divmain, text="COMPANY: ",font = "Verdana 10")
    com.place(x = 15,y = 10)
    com=Entry(divmain,width=20, bd=1,relief=GROOVE,bg="white")         ######company
    com.place(x = 150,y = 10)

    mod=Label(divmain, text="MODEL: ",font = "Verdana 10")
    mod.place(x = 15,y = 40)
    mod=Entry(divmain,width=20, bd=1,relief=GROOVE,bg="white")         ######company
    mod.place(x = 150,y = 40)

    ram=Label(divmain, text="RAM: ",font = "Verdana 10")
    ram.place(x = 15,y = 70)
    ram=Entry(divmain,width=20, bd=1,relief=GROOVE,bg="white")         ######company
    ram.place(x = 150,y = 70)

    stor=Label(divmain, text="STORAGE: ",font = "Verdana 10")
    stor.place(x = 15,y = 100)
    stor=Entry(divmain,width=20, bd=1,relief=GROOVE,bg="white")         ######company
    stor.place(x = 150,y = 100)

    fcam=Label(divmain, text="FRONT CAMERA: ",font = "Verdana 10")
    fcam.place(x = 15,y = 130)
    fcam=Entry(divmain,width=20, bd=1,relief=GROOVE,bg="white")         ######company
    fcam.place(x = 150,y = 130)

    rcam=Label(divmain, text="REAR CAMERA: ",font = "Verdana 10")
    rcam.place(x = 15,y = 160)
    rcam=Entry(divmain,width=20, bd=1,relief=GROOVE,bg="white")         ######company
    rcam.place(x = 150,y = 160)

    bat=Label(divmain, text="BATTERY: ",font = "Verdana 10")
    bat.place(x = 15,y = 190)
    bat=Entry(divmain,width=20, bd=1,relief=GROOVE,bg="white")         ######company
    bat.place(x = 150,y = 190)

    head = Label(divmain, text = "PRICE", fg = "GREEN", bg = "white",font = "Verdana 10 bold").place(x = 120,y = 220)

    flip=Label(divmain, text="FLIPKART : ",font = "Verdana 10")
    flip.place(x = 15,y = 260)
    flip=Entry(divmain,width=10, bd=1,relief=GROOVE,bg="white")         ######company
    flip.place(x = 120,y = 260)

    amz=Label(divmain, text="AMAZON: ",font = "Verdana 10")
    amz.place(x = 15,y = 290)
    amz=Entry(divmain,width=10, bd=1,relief=GROOVE,bg="white")         ######company
    amz.place(x = 120,y = 290)

    pay=Label(divmain, text="PAYTM: ",font = "Verdana 10")
    pay.place(x = 15,y = 320)
    pay=Entry(divmain,width=10, bd=1,relief=GROOVE,bg="white")         ######company
    pay.place(x = 120,y = 320)

    sanp=Label(divmain, text="SNAPDEAL: ",font = "Verdana 10")
    sanp.place(x = 15,y = 350)
    sanp=Entry(divmain,width=10, bd=1,relief=GROOVE,bg="white")         ######company
    sanp.place(x = 120,y = 350)


    #****************************************************************************
    def fun1():               #flipkart
        global idn
        global f
        buy.buyproduct(idn,f)
    def fun2():               #amazon
        global idn
        global a
        buy.buyproduct(idn,a)
    def fun3():               #paytm
        global idn
        global p
        buy.buyproduct(idn,p)
    def fun4():               #snapdeal
        global idn
        global s
        buy.buyproduct(idn,s)

    buy1 = Button(top, text="BUY", fg="green", font="Verdana 8 bold",command=fun1).place(x=210, y=300)
    buy2 = Button(top, text="BUY", fg="green", font="Verdana 8 bold",command=fun2).place(x=210, y=330)
    buy3 = Button(top, text="BUY", fg="green", font="Verdana 8 bold",command=fun3).place(x=210, y=360)
    buy4 = Button(top, text="BUY", fg="green", font="Verdana 8 bold",command=fun4).place(x=210, y=390)

    #////////////////////////////////////


    #**********************QUERY******************************
    query="select * from phones where id={}".format(x)
    result=cur.execute(query).fetchone()
    print(result)
    company=result[0]
    MODEL=result[2]
    RAM=result[3]
    STORAGE=result[4]
    FCAM=result[5]
    RCAM=result[6]
    BAT=result[7]
    FLIP=result[8]
    AMAZ=result[9]
    PAYT=result[10]
    SNAP=result[11]

    global f
    f = FLIP
    global a
    a = AMAZ
    global p
    p =PAYT
    global s
    s =SNAP

    com.insert(0,company)
    com.config(state='disabled')
    mod.insert(0,MODEL)
    mod.config(state='disabled')
    ram.insert(0,RAM)
    ram.config(state='disabled')
    stor.insert(0,STORAGE)
    stor.config(state='disabled')
    fcam.insert(0,FCAM)
    fcam.config(state='disabled')
    rcam.insert(0,RCAM)
    rcam.config(state='disabled')
    bat.insert(0,BAT)
    bat.config(state='disabled')
    flip.insert(0,FLIP)
    flip.config(state='disabled')
    amz.insert(0,AMAZ)
    amz.config(state='disabled')
    pay.insert(0,PAYT)
    pay.config(state='disabled')
    sanp.insert(0,SNAP)
    sanp.config(state='disabled')


    top.mainloop()