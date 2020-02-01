from tkinter import *
import sqlite3
def runcompare(x,y):
    con=sqlite3.connect('mydatabase.db')
    cur=con.cursor()
    top = Tk()
    top.geometry("600x450")
    top.resizable(False,False)
    top.title("Product compare")
    head = Label(top, text = "    PRODUCT COMPARE    ", fg = "red", bg = "white", relief=RIDGE,font = "Verdana 15 bold").pack(side=TOP)
    #////////////////////////////////////////////////
    divmain = Frame(top, highlightbackground="black", bg="white", highlightthickness=2, width=285, height=400, bd= 0)
    divmain.place(x = 10,y = 40)
    divmain2 = Frame(top, highlightbackground="black", bg="white", highlightthickness=2, width=285, height=400, bd= 0)
    divmain2.place(x = 305,y = 40)


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

    head = Label(top, text = "PRICE", fg = "GREEN", bg = "white",font = "Verdana 10 bold").place(x = 125,y = 270)





    flip=Label(divmain, text="FLIPKART : ",font = "Verdana 10")
    flip.place(x = 15,y = 260)
    flip=Entry(divmain,width=20, bd=1,relief=GROOVE,bg="white")         ######company
    flip.place(x = 150,y = 260)

    amz=Label(divmain, text="AMAZON: ",font = "Verdana 10")
    amz.place(x = 15,y = 290)
    amz=Entry(divmain,width=20, bd=1,relief=GROOVE,bg="white")         ######company
    amz.place(x = 150,y = 290)

    pay=Label(divmain, text="PAYTM: ",font = "Verdana 10")
    pay.place(x = 15,y = 320)
    pay=Entry(divmain,width=20, bd=1,relief=GROOVE,bg="white")         ######company
    pay.place(x = 150,y = 320)

    sanp=Label(divmain, text="SNAPDEAL: ",font = "Verdana 10")
    sanp.place(x = 15,y = 350)
    sanp=Entry(divmain,width=20, bd=1,relief=GROOVE,bg="white")         ######company
    sanp.place(x = 150,y = 350)

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

    #/////////////////////////////////////////////////////////
    #***************************************************


    com=Label(divmain2, text="COMPANY: ",font = "Verdana 10")
    com.place(x = 15,y = 10)
    com=Entry(divmain2,width=20, bd=1,relief=GROOVE,bg="white")         ######company
    com.place(x = 150,y = 10)

    mod=Label(divmain2, text="MODEL: ",font = "Verdana 10")
    mod.place(x = 15,y = 40)
    mod=Entry(divmain2,width=20, bd=1,relief=GROOVE,bg="white")         ######company
    mod.place(x = 150,y = 40)

    ram=Label(divmain2, text="RAM: ",font = "Verdana 10")
    ram.place(x = 15,y = 70)
    ram=Entry(divmain2,width=20, bd=1,relief=GROOVE,bg="white")         ######company
    ram.place(x = 150,y = 70)

    stor=Label(divmain2, text="STORAGE: ",font = "Verdana 10")
    stor.place(x = 15,y = 100)
    stor=Entry(divmain2,width=20, bd=1,relief=GROOVE,bg="white")         ######company
    stor.place(x = 150,y = 100)

    fcam=Label(divmain2, text="FRONT CAMERA: ",font = "Verdana 10")
    fcam.place(x = 15,y = 130)
    fcam=Entry(divmain2,width=20, bd=1,relief=GROOVE,bg="white")         ######company
    fcam.place(x = 150,y = 130)

    rcam=Label(divmain2, text="REAR CAMERA: ",font = "Verdana 10")
    rcam.place(x = 15,y = 160)
    rcam=Entry(divmain2,width=20, bd=1,relief=GROOVE,bg="white")         ######company
    rcam.place(x = 150,y = 160)

    bat=Label(divmain2, text="BATTERY: ",font = "Verdana 10")
    bat.place(x = 15,y = 190)
    bat=Entry(divmain2,width=20, bd=1,relief=GROOVE,bg="white")         ######company
    bat.place(x = 150,y = 190)

    head = Label(top, text = "PRICE", fg = "GREEN", bg = "white",font = "Verdana 10 bold").place(x = 420,y = 270)





    flip=Label(divmain2, text="FLIPKART : ",font = "Verdana 10")
    flip.place(x = 15,y = 260)
    flip=Entry(divmain2,width=20, bd=1,relief=GROOVE,bg="white")         ######company
    flip.place(x = 150,y = 260)

    amz=Label(divmain2, text="AMAZON: ",font = "Verdana 10")
    amz.place(x = 15,y = 290)
    amz=Entry(divmain2,width=20, bd=1,relief=GROOVE,bg="white")         ######company
    amz.place(x = 150,y = 290)

    pay=Label(divmain2, text="PAYTM: ",font = "Verdana 10")
    pay.place(x = 15,y = 320)
    pay=Entry(divmain2,width=20, bd=1,relief=GROOVE,bg="white")         ######company
    pay.place(x = 150,y = 320)

    sanp=Label(divmain2, text="SNAPDEAL: ",font = "Verdana 10")
    sanp.place(x = 15,y = 350)
    sanp=Entry(divmain2,width=20, bd=1,relief=GROOVE,bg="white")         ######company
    sanp.place(x = 150,y = 350)

    #**********************QUERY******************************
    query="select * from phones where id={}".format(y)
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