#pip install mysql.connector
import mysql.connector
#CREATE TKINTER
from tkinter import *
from tkinter import ttk,messagebox

def databaseproject():

    #tkinter window size, title, background color
    top = Tk()
    top.geometry("1500x1100")
    top.title("DATABASE PROJECT")
    top.config(bg="lightblue")

    # GET VALUE
    def get(event):
        no.delete(0, END)
        name.delete(0, END)
        age.delete(0, END)
        sec.delete(0, END)
        ph.delete(0, END)
        addr.delete(0, END)
        email.delete(0, END)

        ROW_ID = listbox.selection()[0]
        select = listbox.set(ROW_ID)

        no.insert(0, select["roll"])
        name.insert(0, select['name'])
        age.insert(0, select['age'])
        sec.insert(0, select['sec'])
        ph.insert(0, select['phno'])
        addr.insert(0, select['addr'])
        email.insert(0, select['email'])

    # ADD DATA
    def add():
        stuno = no.get()
        stuname = name.get()
        stuage = age.get()
        stusec = sec.get()
        stuph = ph.get()
        stuaddr = addr.get()
        stuemail = email.get()

        mysqldb = mysql.connector.connect(host="localhost", user="root", password="Kamalesh_2003",
                                          database="project_BCA")
        cur = mysqldb.cursor()

        try:
            sql = "INSERT INTO BCA(roll,name,age,sec,addr,phno,mail) VALUES(%s,%s,%s,%s,%s,%s,%s)"
            val = (stuno, stuname, stuage, stusec, stuaddr, stuph, stuemail)

            cur.execute(sql, val)

            mysqldb.commit()

            messagebox.showinfo("MESSAGE", "DATA ADDED SUCCESSFULLY")

            no.delete(0, END)
            name.delete(0, END)
            age.delete(0, END)
            sec.delete(0, END)
            ph.delete(0, END)
            addr.delete(0, END)
            email.delete(0, END)
            no.focus_set()

        except:
            messagebox.showinfo("MESSAGE", "PLEASE ENTER DATA FULLY")

    # UPDATE DATA
    def update():
        stuno = no.get()
        stuname = name.get()
        stuage = age.get()
        stusec = sec.get()
        stuph = ph.get()
        stuaddr = addr.get()
        stuemail = email.get()

        mysqldb = mysql.connector.connect(host="localhost", user="root", password="Kamalesh_2003",
                                          database="project_BCA")
        cur = mysqldb.cursor()

        try:
            sql = "UPDATE BCA set name=%s,age=%s,sec=%s,addr=%s,phno=%s,mail=%s where roll=%s"
            val = (stuname, stuage, stusec, stuaddr, stuph, stuemail, stuno)

            cur.execute(sql, val)

            mysqldb.commit()

            messagebox.showinfo("MESSAGE", "DATA UPDATE SUCCESSFULLY")

            no.delete(0, END)
            name.delete(0, END)
            age.delete(0, END)
            sec.delete(0, END)
            ph.delete(0, END)
            addr.delete(0, END)
            email.delete(0, END)
            no.focus_set()

        except:
            messagebox.showinfo("MESSAGE", "PLEASE ENTER DATA FULLY")

    # DELETE DATA
    def delete():
        stuno = no.get()

        mysqldb = mysql.connector.connect(host="localhost", user="root", password="Kamalesh_2003",
                                          database="project_BCA")
        cur = mysqldb.cursor()

        try:
            sql = "DELETE FROM BCA WHERE roll=%s"
            val = (stuno,)

            cur.execute(sql, val)

            mysqldb.commit()

            messagebox.showinfo("MESSAGE", "DATA DELETE SUCCESSFULLY")

            no.delete(0, END)
            name.delete(0, END)
            age.delete(0, END)
            sec.delete(0, END)
            ph.delete(0, END)
            addr.delete(0, END)
            email.delete(0, END)
            no.focus_set()

        except:

            messagebox.showinfo("MESSAGE", "PLEASE CLICK WHAT YOU WANT TO DELETE IN LISTED DATA")

    # SEARCH DATA BY USING REGNO
    def search():
        stuno = no.get()


        mysqldb = mysql.connector.connect(host="localhost", user="root", password="Kamalesh_2003",
                                          database="project_BCA")
        cur = mysqldb.cursor()

        try:
            cur.execute("SELECT * FROM BCA WHERE roll='"+ stuno +"'")

            myresult = cur.fetchall()

            for x in myresult:
                print(x)


            name.delete(0, END)
            age.delete(0, END)
            sec.delete(0, END)
            ph.delete(0, END)
            addr.delete(0, END)
            email.delete(0, END)



            name.insert(END,x[1])
            age.insert(END,x[2])
            sec.insert(END,x[3])
            ph.insert(END,x[4])
            addr.insert(END,x[5])
            email.insert(END,x[6])

        except :
            messagebox.showinfo("MESSAGE","PLS ENTER ONLY ROLL NUM BOX")

    # CLEAR DATA FROM INPUT BOX
    def clear():
        no.delete(0, END)
        name.delete(0, END)
        age.delete(0, END)
        sec.delete(0, END)
        ph.delete(0, END)
        addr.delete(0, END)
        email.delete(0, END)
        no.focus_set()

    #RELOAD TKINTER
    def reload():
        top.destroy()
        databaseproject()

    #EXIT TKINTER
    def exit():
        top.destroy()

    # VIEW DATA IN LIST BOX
    def view():

        mysqldb = mysql.connector.connect(host="localhost", user="root", password="Kamalesh_2003",
                                          database="project_BCA")
        cur = mysqldb.cursor()

        sql = "SELECT roll,name,age,sec,addr,phno,mail FROM BCA"
        cur.execute(sql)
        record = cur.fetchall()

        for i, (roll, name, age, sec, addr, phno, mail) in enumerate(record, start=1):
            listbox.insert('', 'end', values=(roll, name, age, sec, addr, phno, mail))
            mysqldb.close()

    # FRONT END

    # LABEL
    Label(top, text="RESISTER NO  :", font=("none", 20, "bold"), bg="lightblue").place(x=50, y=10)
    Label(top, text="STUDENT NAME :", font=("none", 20, "bold"), bg="lightblue").place(x=50, y=60)
    Label(top, text="STUDENT AGE  :", font=("none", 20, "bold"), bg="lightblue").place(x=50, y=110)
    Label(top, text="SECTION    :", font=("none", 20, "bold"), bg="lightblue").place(x=50, y=160)
    Label(top, text="PHONE NO      :", font=("none", 20, "bold"), bg="lightblue").place(x=50, y=210)
    Label(top, text="ADDRESS        :", font=("none", 20, "bold"), bg="lightblue").place(x=50, y=260)
    Label(top, text="EMAIL        :", font=("none", 20, "bold"), bg="lightblue").place(x=50, y=310)

    # ENTRY
    no = Entry(top, width=28, font=("times", 15, "bold"))
    name = Entry(top, width=28, font=("times", 15, "bold"))
    age = Entry(top, width=28, font=("times", 15, "bold"))
    sec = Entry(top, width=28, font=("times", 15, "bold"))
    ph = Entry(top, width=28, font=("times", 15, "bold"))
    addr = Entry(top, width=28, font=("times", 15, "bold"))
    email = Entry(top, width=28, font=("times", 15, "bold"))

    no.place(x=400, y=10)
    name.place(x=400, y=60)
    age.place(x=400, y=110)
    sec.place(x=400, y=160)
    ph.place(x=400, y=210)
    addr.place(x=400, y=260)
    email.place(x=400, y=310)

    # BUTTON
    Button(top, text="ADD DATA", width=20, height=3, bg="lightgreen", font=("times", 10, "bold"), command=add)\
        .place(x=150, y=400)
    Button(top, text="UPDATE DATA", width=20, height=3, bg="lightgreen", font=("times", 10, "bold"),command=update)\
        .place(x=350, y=400)
    Button(top, text="CLEAR", width=20, height=3, bg="lightgreen", font=("times", 10, "bold"), command=clear)\
        .place(x=150, y=500)
    Button(top, text="DELETE DATA", width=20, height=3, bg="lightgreen", font=("times", 10, "bold"),command=delete)\
        .place(x=350, y=500)
    Button(top, text="RELOAD", width=20, height=3, bg="lightgreen", font=("times", 10, "bold"),command=reload)\
        .place(x=150, y=600)
    Button(top, text="SEARCH BY ROLL", width=20, height=3, bg="lightgreen", font=("times", 10, "bold"), command=search) \
        .place(x=350, y=600)
    Button(top, text="EXIT", width=20, height=5, bg="black",fg="red", font=("times", 10, "bold"), command=exit) \
        .place(x=550, y=650)


    cols = ("roll", "name", "age", "sec", "phno", "addr", "email")
    listbox = ttk.Treeview(top, columns=cols, show="headings", height=1100)

    # SCROLL BAR IN X AXIS
    xscroll = Scrollbar(listbox, orient=HORIZONTAL, command=listbox.xview)
    xscroll.pack(side=BOTTOM, padx=300, pady=650)
    listbox.configure(xscrollcommand=xscroll.set)

    for col in cols:
        listbox.heading(col, text=col)
        listbox.place(x=700, y=3, )

    view()

    listbox.bind("<Double-Button-1>", get)

    top.mainloop()

