from tkinter import *
import sqlite3
import compare
from tkinter import StringVar
from tkinter import messagebox
#import yog
import DETAILS2

con=sqlite3.connect('mydatabase.db')
cur=con.cursor()
#main window create list of phones
query="select count(*) from phones"
cont=cur.execute(query).fetchone()
count=cont[0]
print(count)

top = Tk()
top.geometry("500x700")
top.resizable(False,False)
top.title("Product compare")


def rucompare():
    compare.runcompare()
def entfun():
    import yog


head = Label(top, text = "           YOUR WISHLIST         ", fg = "blue", bg = "white", relief=RIDGE,font = "Verdana 15 bold").pack(side=TOP)
head2 = Label(top, text = "ENTER ID", fg = "BLACK", bg = "white", relief=RIDGE,font = "Verdana 10 bold").pack(side=TOP)

add= Button(top, text="ADD PRODUCT",fg="green",font = "Verdana 10 bold", command=entfun).place(x = 10,y = 50)

v1=StringVar()
v2=StringVar()
c1=Entry(top,width=5, bd=1,relief=GROOVE,bg="white", textvariable=v1) .place(x = 180,y = 50)
com=Label(top, text="<--> ",font = "Verdana 10").place(x = 220,y = 50)
c2=Entry(top,width=5, bd=1,relief=GROOVE,bg="white", textvariable=v2).place(x = 260,y = 50)
cmp1=v1.get()
cmp2=v2.get()
def cmp_transf():
    x=v1.get()
    y=v2.get()
    compare.runcompare(x,y)



remove= Button(top, text="COMPARE PRODUCT",command=cmp_transf, fg="red", font ="Verdana 10 bold").place(x = 340, y = 50)

#********************************************************************************************SEE DETAILS

######################   \\\ DIVISIONS
divmain = Frame(top, highlightbackground="black", bg="white", highlightthickness=2, width=480, height=100, bd= 0)
divmain.place(x = 10,y = 80)

com=Label(divmain, text="ID: ",font = "Verdana 10")
com.place(x = 5,y = 5)
comentry=Entry(divmain,width=20, bd=1,relief=GROOVE,bg="white")         ######company
comentry.place(x = 90,y = 5)

idno=Label(divmain, text="Company: ",font = "Verdana 10")
idno.place(x = 5,y = 35)
idno=Entry(divmain,width=20, bd=1,relief=GROOVE,bg="white")          ######id
idno.place(x = 90,y = 35)

model=Label(divmain, text="Model: ",font = "Verdana 10")
model.place(x = 5,y = 65)
model=Entry(divmain,width=20, bd=1,relief=GROOVE,bg="white")          ######model
model.place(x = 90,y = 65)
def callfn():
    x=count
    DETAILS2.runcompare(x)
details= Button(divmain, text="SEE DETAILS",fg="green",font = "Verdana 10 bold",command=callfn).place(x = 350,y = 30)  #SEE DETAILS

#-------------------------------------------------------------------------------
#----------------------------------------------------------------

######################   \\\ DIVISIONS
#*****************************************************
query="select * from phones where id={}".format(count)
result=cur.execute(query).fetchone()
id=result[0]
mod=result[2]
cmp=result[1]
comentry.insert(0,cmp)
comentry.config(state='disabled')
idno.insert(0,id)
idno.config(state='disabled')
model.insert(0,mod)
model.config(state='disabled')

#*******************************************************
divmain1 = Frame(top, highlightbackground="black", bg="white", highlightthickness=2, width=480, height=100, bd= 0)
divmain1.place(x = 10,y = 185)


com=Label(divmain1, text="ID: ",font = "Verdana 10")
com.place(x = 5,y = 5)
comentry=Entry(divmain1,width=20, bd=1,relief=GROOVE,bg="white")         ######company
comentry.place(x = 90,y = 5)

idno=Label(divmain1, text="Company: ",font = "Verdana 10")
idno.place(x = 5,y = 35)
idno=Entry(divmain1,width=20, bd=1,relief=GROOVE,bg="white")          ######id
idno.place(x = 90,y = 35)

model=Label(divmain1, text="Model: ",font = "Verdana 10")
model.place(x = 5,y = 65)
model=Entry(divmain1,width=20, bd=1,relief=GROOVE,bg="white")          ######model
model.place(x = 90,y = 65)
def callfn1():
    x = count-1
    DETAILS2.runcompare(x)
details= Button(divmain1, text="SEE DETAILS",fg="green",font = "Verdana 10 bold",command=callfn1).place(x = 350,y = 30)


query="select * from phones where id={}".format(count-1)
result=cur.execute(query).fetchone()
id=result[0]
mod=result[2]
cmp=result[1]
del result
comentry.insert(0,cmp)
comentry.config(state='disabled')
idno.insert(0,id)
idno.config(state='disabled')
model.insert(0,mod)
model.config(state='disabled')

#-------------------------------------------------------------------------------
#----------------------------------------------------------------

######################   \\\ DIVISIONS
divmain2 = Frame(top, highlightbackground="black", bg="white", highlightthickness=2, width=480, height=100, bd= 0)
divmain2.place(x = 10,y = 290)


com=Label(divmain2, text="ID: ",font = "Verdana 10")
com.place(x = 5,y = 5)
comentry=Entry(divmain2,width=20, bd=1,relief=GROOVE,bg="white")         ######company
comentry.place(x = 90,y = 5)

idno=Label(divmain2, text="Company: ",font = "Verdana 10")
idno.place(x = 5,y = 35)
idno=Entry(divmain2,width=20, bd=1,relief=GROOVE,bg="white")          ######id
idno.place(x = 90,y = 35)

model=Label(divmain2, text="Model: ",font = "Verdana 10")
model.place(x = 5,y = 65)
model=Entry(divmain2,width=20, bd=1,relief=GROOVE,bg="white")          ######model
model.place(x = 90,y = 65)
def callfn2():
    x =count-2
    DETAILS2.runcompare(x)
details= Button(divmain2, text="SEE DETAILS",fg="green",font = "Verdana 10 bold",command=callfn2).place(x = 350,y = 30)

query="select * from phones where id={}".format(count-2)
result=cur.execute(query).fetchone()
id=result[0]
mod=result[2]
cmp=result[1]
del result
comentry.insert(0,cmp)
comentry.config(state='disabled')
idno.insert(0,id)
idno.config(state='disabled')
model.insert(0,mod)
model.config(state='disabled')
#-------------------------------------------------------------------------------
#----------------------------------------------------------------

######################   \\\ DIVISIONS
divmain3 = Frame(top, highlightbackground="black", bg="white", highlightthickness=2, width=480, height=100, bd= 0)
divmain3.place(x = 10,y = 396)

com=Label(divmain3, text="ID: ",font = "Verdana 10")
com.place(x = 5,y = 5)
comentry=Entry(divmain3,width=20, bd=1,relief=GROOVE,bg="white")         ######company
comentry.place(x = 90,y = 5)

idno=Label(divmain3, text="Company: ",font = "Verdana 10")
idno.place(x = 5,y = 35)
idno=Entry(divmain3,width=20, bd=1,relief=GROOVE,bg="white")          ######id
idno.place(x = 90,y = 35)

model=Label(divmain3, text="Model: ",font = "Verdana 10")
model.place(x = 5,y = 65)
model=Entry(divmain3,width=20, bd=1,relief=GROOVE,bg="white")          ######model
model.place(x = 90,y = 65)
def callfn3():
    x = count-3
    DETAILS2.runcompare(x)
details= Button(divmain3, text="SEE DETAILS",fg="green",font = "Verdana 10 bold",command=callfn3).place(x = 350,y = 30)

query="select * from phones where id={}".format(count-3)
result=cur.execute(query).fetchone()
id=result[0]
mod=result[2]
cmp=result[1]
del result
comentry.insert(0,cmp)
comentry.config(state='disabled')
idno.insert(0,id)
idno.config(state='disabled')
model.insert(0,mod)
model.config(state='disabled')
#-----------------------------------------------------------------
#----------------------------------------------------------------

######################   \\\ DIVISIONS
divmain4 = Frame(top, highlightbackground="black", bg="white", highlightthickness=2, width=480, height=100, bd= 0)
divmain4.place(x = 10,y = 494)



com=Label(divmain4, text="ID: ",font = "Verdana 10")
com.place(x = 5,y = 5)
comentry=Entry(divmain4,width=20, bd=1,relief=GROOVE,bg="white")         ######company
comentry.place(x = 90,y = 5)

idno=Label(divmain4, text="Company: ",font = "Verdana 10")
idno.place(x = 5,y = 35)
idno=Entry(divmain4,width=20, bd=1,relief=GROOVE,bg="white")          ######id
idno.place(x = 90,y = 35)

model=Label(divmain4, text="Model: ",font = "Verdana 10")
model.place(x = 5,y = 65)
model=Entry(divmain4,width=20, bd=1,relief=GROOVE,bg="white")          ######model
model.place(x = 90,y = 65)
def callfn4():
    x = count-4
    DETAILS2.runcompare(x)
details= Button(divmain4, text="SEE DETAILS",fg="green",font = "Verdana 10 bold",command=callfn4).place(x = 350,y = 30)

query="select * from phones where id={}".format(count-4)
result=cur.execute(query).fetchone()
id=result[0]
mod=result[2]
cmp=result[1]
del result
comentry.insert(0,cmp)
comentry.config(state='disabled')
idno.insert(0,id)
idno.config(state='disabled')
model.insert(0,mod)
model.config(state='disabled')

#-------------------------------------------------------------------------------
#----------------------------------------------------------------

######################   \\\ DIVISIONS
divmain5 = Frame(top, highlightbackground="black", bg="white", highlightthickness=2, width=480, height=100, bd= 0)
divmain5.place(x = 10,y = 596)




com=Label(divmain5, text="ID: ",font = "Verdana 10")
com.place(x = 5,y = 5)
comentry=Entry(divmain5,width=20, bd=1,relief=GROOVE,bg="white")         ######company
comentry.place(x = 90,y = 5)

idno=Label(divmain5, text="Company: ",font = "Verdana 10")
idno.place(x = 5,y = 35)
idno=Entry(divmain5,width=20, bd=1,relief=GROOVE,bg="white")          ######id
idno.place(x = 90,y = 35)

model=Label(divmain5, text="Model: ",font = "Verdana 10")
model.place(x = 5,y = 65)
model=Entry(divmain5,width=20, bd=1,relief=GROOVE,bg="white")          ######model
model.place(x = 90,y = 65)
def callfn5():
    x =count-5
    DETAILS2.runcompare(x)
details= Button(divmain5, text="SEE DETAILS",fg="green",font = "Verdana 10 bold",command=callfn5).place(x = 350,y = 30)

query="select * from phones where id={}".format(count-5)
result=cur.execute(query).fetchone()
id=result[0]
mod=result[2]
cmp=result[1]
del result
comentry.insert(0,cmp)
comentry.config(state='disabled')
idno.insert(0,id)
idno.config(state='disabled')
model.insert(0,mod)
model.config(state='disabled')
#-------------------------------------------------------------------------------
#----------------------------------------------------------------

#query="select * from phones where id=1"
#result=cur.execute(query).fetchone()
#id=result[1]
#model=result[2]
#cmp=result[0]
#del result

top.mainloop()

