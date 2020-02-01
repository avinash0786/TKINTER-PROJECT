from tkinter import *
import sqlite3
from tkinter import messagebox


def entryfun():
    top = Tk()
    top.geometry("300x420")
    top.resizable(False, False)
    top.title("Product compare")

    # img1=ImageTk.PhotoImage(Image.open("C:\\Users\\Hp\\Desktop\\flipkart.jpg"))
    # p1=Label(window,image=img1,relief=GROOVE)
    # ************************************************************QUERY
    v1 = StringVar()
    v2 = StringVar()
    v3 = StringVar()
    v4 = StringVar()
    v5 = StringVar()
    v6 = StringVar()
    v7 = StringVar()
    v8 = StringVar()
    v9 = StringVar()
    v10 = StringVar()
    v11 = StringVar()


    head = Label(top, text="           DETAILS         ", fg="blue", bg="white", relief=RIDGE,font="Verdana 15 bold").pack(side=TOP)

    lbl = Label(top, text="Company: ", font="Verdana 10").place(x=5, y=65)
    lbl = Entry(top, width=15, bd=1, relief=GROOVE, bg="white", textvariable=v1).place(x=130, y=65)  ######id

    model = Label(top, text="Model: ", font="Verdana 10").place(x=5, y=95)
    model = Entry(top, width=15, bd=1, relief=GROOVE, bg="white", textvariable=v2).place(x=130, y=95)  ######model

    RAM = Label(top, text="RAM: ", font="Verdana 10").place(x=5, y=125)
    ram = Entry(top, width=15, bd=1, relief=GROOVE, bg="white", textvariable=v3).place(x=130, y=125)  ######company

    storage = Label(top, text="STORAGE: ", font="Verdana 10").place(x=5, y=155)
    storage = Entry(top, width=15, bd=1, relief=GROOVE, bg="white", textvariable=v4).place(x=130, y=155)  ######id

    Front_camera = Label(top, text="FRONT_CAMERA: ", font="Verdana 10").place(x=1, y=185)
    Front_camera = Entry(top, width=15, bd=1, relief=GROOVE, bg="white", textvariable=v5).place(x=130, y=185)  ######model

    REAR_CAMERA = Label(top, text="REAR_CAMERA: ", font="Verdana 10").place(x=5, y=215)
    REAR_CAMERA = Entry(top, width=15, bd=1, relief=GROOVE, bg="white", textvariable=v6).place(x=130, y=215)  ######id

    batt = Label(top, text="BATTERY: ", font="Verdana 10").place(x=5, y=240)
    batt = Entry(top, width=15, bd=1, relief=GROOVE, bg="white", textvariable=v11).place(x=130, y=240)  ######id

    flip = Label(top, text="FLIPKART : ", font="Verdana 10")
    flip.place(x=5, y=270)
    flip = Entry(top, width=15, bd=1, relief=GROOVE, bg="white", textvariable=v7)  ######company
    flip.place(x=130, y=270)

    amz = Label(top, text="AMAZON: ", font="Verdana 10")
    amz.place(x=5, y=305)
    amz = Entry(top, width=15, bd=1, relief=GROOVE, bg="white", textvariable=v8)  ######company
    amz.place(x=130, y=305)

    pay = Label(top, text="PAYTM: ", font="Verdana 10")
    pay.place(x=5, y=340)
    pay = Entry(top, width=15, bd=1, relief=GROOVE, bg="white", textvariable=v9)  ######company
    pay.place(x=130, y=340)

    sanp = Label(top, text="SNAPDEAL: ", font="Verdana 10")
    sanp.place(x=5, y=370)
    sanp = Entry(top, width=15, bd=1, relief=GROOVE, bg="white", textvariable=v10)  ######company
    sanp.place(x=130, y=370)


    #******************************************************************************************

    def funt():
        con = sqlite3.connect('mydatabase.db')
        cur = con.cursor()
        a=v1.get()
        b = v2.get()
        c = v3.get()
        d = v4.get()
        e = v5.get()
        f = v6.get()
        g = v7.get()
        h = v8.get()
        i = v9.get()
        j = v10.get()
        k = v11.get()
        query = "insert into 'phones'(company,model,ram,storage,battery,f_camera,r_camera,flipkart,amazon,paytm,snapdeal) values(?,?,?,?,?,?,?,?,?,?,?)"
        data_tuple = (a, b, c, d, e, f,k, g, h, i, j)
        cur.execute(query, data_tuple).fetchone()
        con.commit()
        cur.close()
        messagebox.showinfo("SUCCESS ! ", "DATA SAVED TO DATABASE")

    SUBMIT = Button(top, text="SUBMIT", fg="green", font="Verdana 10 bold", command=funt ).place(x=110, y=390)
    top.mainloop()
entryfun()
    #**************************ENTRY DATA TO DATABASE



