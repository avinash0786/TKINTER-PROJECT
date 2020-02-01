from tkinter import *
import sqlite3
from yog import entry
con=sqlite3.connect('mydatabase.db')
cur=con.cursor()

class Application(object):
    def __init__(self,master):
        self.master=master
        self.top = Frame(master, width=450, height=100,bg='red')
        self.top.pack(fill=X)
        #***************************************************************
        self.head = Label(self.top, text="           YOUR WISHLIST         ", fg="blue", bg="white", relief=RIDGE,font="Verdana 15 bold").pack(side=TOP)
        self.add = Button(self.top, text="ADD PRODUCT", fg="green", font="Verdana 10 bold")
        self.add.pack()
        self.remove = Button(self.top, text="REMOVE PRODUCT", fg="red", font="Verdana 10 bold")
        self.remove.pack()
        #**/*////////////////////////////////////////////////////
        #divisions
        ######################   \\\ DIVISIONS
        self.divmain = Frame(self.top, highlightbackground="black", bg="white", highlightthickness=2, width=480, height=100, bd=0)
        self.divmain.place(x=10, y=80)

        self.com = Label(self.divmain, text="ID: ", font="Verdana 10")
        self.com.place(x=5, y=5)
        self.comentry = Entry(self.divmain, width=20, bd=1, relief=GROOVE, bg="white")  ######company
        self.comentry.place(x=90, y=5)

        self.idno = Label(self.divmain, text="Company: ", font="Verdana 10")
        self.idno.place(x=5, y=35)
        self.idno = Entry(self.divmain, width=20, bd=1, relief=GROOVE, bg="white")  ######id
        self.idno.place(x=90, y=35)

        self.model = Label(self.divmain, text="Model: ", font="Verdana 10")
        self.model.place(x=5, y=65)
        self.model = Entry(self.divmain, width=20, bd=1, relief=GROOVE, bg="white")  ######model
        self.model.place(x=90, y=65)

        details = Button(self.divmain, text="SEE DETAILS", fg="green", font="Verdana 10 bold").place(x=350,
                                                                                                y=30)  # SEE DETAILS

        # -------------------------------------------------------------------------------
        # ----------------------------------------------------------------

        ######################   \\\ DIVISIONS
        # *****************************************************
        query = "select * from phones where id=1"
        result = cur.execute(query).fetchone()
        id = result[0]
        mod = result[2]
        cmp = result[1]
        self.comentry.insert(0, cmp)
        self.comentry.config(state='disabled')
        self.idno.insert(0, id)
        self.idno.config(state='disabled')
        self.model.insert(0, mod)
        self.model.config(state='disabled')






def main():
    root=Tk()
    app=Application(root)
    root.title('APP')
    root.geometry("500x700")
    root.resizable(False, False)
    root.mainloop()
if __name__=='__main__':
    main()