from tkinter import *
from tkinter import ttk
import sqlite3
import codecs
# from wand.display import display

import cv2
import glob
import os
from tkcalendar import DateEntry
from tkinter import messagebox
import datetime as dt
from googleapiclient.http import MediaFileUpload
from Google import Create_Service
import schedule
import time
import threading
from PIL import Image
import io
import os
from PIL import ImageFont
from PIL import ImageDraw
import PIL
con = sqlite3.connect("newnew1.db")
# con.execute("""CREATE TABLE IF NOT EXISTS image(
#     images BLOB,
#     parent_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     FOREIGN KEY(parent_id) REFERENCES customer_jj(id))
# """)
con.execute(""" CREATE TABLE IF NOT EXISTS customer_jj(
    id  INTEGER PRIMARY KEY AUTOINCREMENT,
    name  VARCHAR,
    phone INTEGER,
    l VARCHAR,
    ch VARCHAR,
    s VARCHAR,
    t VARCHAR,
    n VARCHAR,
    w VARCHAR,
    l1 VARCHAR,
    w1 VARCHAR,
    h VARCHAR,
    l2 VARCHAR,
    m VARCHAR,
    g VARCHAR,
    o1 VARCHAR,
    o2 VARCHAR,
    o3 VARCHAR,
    o4 VARCHAR,
    others VARCHAR,
    del TIMESTAMP,
    date TIMESTAMP,
    image BLOB)
""")
class Student:
    can_path = ''

    def __init__(self, root):
        self.root = root
        self.root.title("King Tailors")
        self.root.geometry("1350x700+0+0")
        DEFAULT_PEN_SIZE = 5.0
        DEFAULT_COLOR = 'black'

        title = Label(self.root, text="King Tailors", bd=10, relief=GROOVE, font=("times new roman", 40, "bold"),
                      bg="white", fg="black", highlightbackground="gray", highlightthickness=4)
        title.pack(side=TOP, fill=X)


        self.date = StringVar()

        self.id = StringVar()
        self.customer_name = StringVar()
        self.phone = StringVar()
        self.del_date = StringVar()
        self.l = StringVar()
        self.ch = StringVar()
        self.s = StringVar()
        self.t = StringVar()
        self.n = StringVar()
        self.w = StringVar()
        self.l1 = StringVar()
        self.w1 = StringVar()
        self.h = StringVar()
        self.l2 = StringVar()
        self.m = StringVar()
        self.g = StringVar()
        self.o = StringVar()
        self.o1 = StringVar()
        self.o2 = StringVar()
        self.o3 = StringVar()
        self.o4 = StringVar()
        self.txt_date = StringVar()
        self.photo = StringVar()
        self.date = StringVar()

        self.search_by = StringVar()
        self.search_text = StringVar()
        self.can_path = ""

        manage_frame1 = Frame(self.root, bd=4, relief=GROOVE, highlightbackground="gray", highlightthickness=1)

        detail_frame = Frame(self.root, bd=2, relief=SUNKEN, highlightbackground="gray", highlightthickness=1)
        manage_frame1.place(x=10, y=100, width=690, height=590)
        detail_frame.place(x=700, y=100, width=620, height=590)

        date1 = dt.datetime.now()
        format_date = f"{date1: %b %d %y}"
        self.format_date = f"{date1: %b %d %y}"
        lbl_date = Label(manage_frame1, text="Date", font=("times new roman", 15, "bold"), bg="white", fg="black")
        lbl_date.grid(row=0, column=0, pady=5, padx=5, sticky="w")
        self.pen_button = Button(manage_frame1, text='pen', command=self.use_pen,width=5)
        self.pen_button.place(x=250,y=450,width=80)
        self.c = Canvas(manage_frame1, bg='white', width=200, height=130)
        self.c.grid(row=14, column=0)

        self.button3 = Button(manage_frame1, text="Done!", width=2, bg='white', command=self.save)
        self.button3.place(x=250, y=540, width=80)
        self.button1 = Button(manage_frame1, text="Clear!", width=2, bg='white', command=self.clear1)
        self.button1.place(x=250,y=510,width=80)
        self.eraser_button2 = Button(manage_frame1, text='eraser', command=self.use_eraser)
        self.eraser_button2.place(x=250,y=480,width=80)
        self.setup()
        self.image = PIL.Image.new("RGB",(200,200),(255,255,255))
        self.draw = ImageDraw.Draw(self.image)

        self.choose_size_button = Scale(manage_frame1, from_=1, to=8, orient=HORIZONTAL)
        self.choose_size_button.grid(row=13, column=1)

        txt_date = Entry(manage_frame1, textvariable=self.date, font=("times new roman", 15, "bold"), bd=5,
                         relief=RAISED)

        txt_date1 = DateEntry(manage_frame1, textvariable=self.del_date, selectmode='day', width=18)

        txt_date1.grid(row=1, column=1, pady=5, padx=5, sticky="w")

        lbl_date1 = Label(manage_frame1, text="Delivery Date", font=("times new roman", 15, "bold"), bg="white",
                          fg="black")
        lbl_date1.grid(row=1, column=0, pady=5, padx=5, sticky="w")

        txt_date = Entry(manage_frame1, textvariable=self.date, width=12, font=("times new roman", 15, "bold"), bd=5,
                         relief=RAISED)
        txt_date.insert(END, format_date)
        print(format_date)
        txt_date.grid(row=0, column=1, pady=5, padx=5, sticky="w")
        lbl_roll = Label(manage_frame1, text="Customer Name", font=("times new roman", 15, "bold"), bg="white", bd=5,
                         fg="black")
        lbl_roll.grid(row=2, column=0, pady=5, padx=5, sticky="w")
        #
        txt_roll = Entry(manage_frame1, textvariable=self.customer_name, width=15, font=("times new roman", 15, "bold"),
                         bd=5,
                         relief=RAISED)
        txt_roll.grid(row=2, column=1, pady=5, padx=5, sticky="w")

        lbl_age = Label(manage_frame1, text="Phone No", font=("times new roman", 15, "bold"), bg="white", fg="black")
        lbl_age.grid(row=3, column=0, pady=5, padx=5, sticky="w")

        txt_age = Entry(manage_frame1, textvariable=self.phone, width=15, font=("times new roman", 15, "bold"), bd=5,
                        relief=RAISED)
        txt_age.grid(row=3, column=1, pady=5, padx=5, sticky="w")

        lbl_add = Label(manage_frame1, text="S. L", font=("times new roman", 15, "bold"), bg="white", fg="black")
        lbl_add.grid(row=7, column=0, pady=5, padx=5, sticky="w")

        txt_add = Entry(manage_frame1, textvariable=self.l, width=5, font=("times new roman", 15, "bold"), bd=5,
                        relief=RAISED)
        txt_add.grid(row=7, column=0, pady=5, padx=5, sticky="e")
        txt_add = Entry(manage_frame1, textvariable=self.l, width=5, font=("times new roman", 15, "bold"), bd=5,
                        relief=RAISED)
        txt_add.grid(row=7, column=1, pady=5, padx=5, sticky="w")


        lbl_addd = Label(manage_frame1, text="P. L", font=("times new roman", 15, "bold"), bg="white", fg="black")
        lbl_addd.grid(row=7, column=1, pady=5, padx=5, sticky="e")

        txt_addd = Entry(manage_frame1, textvariable=self.l1, width=5, font=("times new roman", 15, "bold"), bd=5,
                         relief=RAISED)
        txt_addd.grid(row=7, column=2, pady=5, padx=5, sticky="s")
        lbl_add1 = Label(manage_frame1, text="S. CH", font=("times new roman", 15, "bold"), bg="white", fg="black")
        lbl_add1.grid(row=8, column=0, pady=5, padx=5, sticky="w")
        txt_add1 = Entry(manage_frame1, textvariable=self.ch, width=5, font=("times new roman", 15, "bold"), bd=5,
                         relief=RAISED)
        txt_add1.grid(row=8, column=1, pady=5, padx=5, sticky="w")

        txt_add1 = Entry(manage_frame1, textvariable=self.ch, width=5, font=("times new roman", 15, "bold"), bd=5,
                         relief=RAISED)
        txt_add1.grid(row=8, column=0, pady=5, padx=5, sticky="e")
        lbl_addp = Label(manage_frame1, text="P. W", font=("times new roman", 15, "bold"), bg="white", fg="black")
        lbl_addp.grid(row=8, column=1, pady=5, padx=5, sticky="e")

        txt_addp = Entry(manage_frame1, textvariable=self.w1, width=5, font=("times new roman", 15, "bold"), bd=5,
                         relief=RAISED)
        txt_addp.grid(row=8, column=2, pady=5, padx=5, sticky="s")

        lbl_add2 = Label(manage_frame1, text="S. S", font=("times new roman", 15, "bold"), bg="white", fg="black")
        lbl_add2.grid(row=9, column=0, pady=5, padx=5, sticky="w")
        #
        txt_add2 = Entry(manage_frame1, textvariable=self.s, width=5, font=("times new roman", 15, "bold"), bd=5,
                         relief=RAISED)
        txt_add2.grid(row=9, column=0, pady=5, padx=5, sticky="e")
        txt_add2 = Entry(manage_frame1, textvariable=self.s, width=5, font=("times new roman", 15, "bold"), bd=5,
                         relief=RAISED)
        txt_add2.grid(row=9, column=1, pady=5, padx=5, sticky="w")

        lbl_add2p = Label(manage_frame1, text="P. H", font=("times new roman", 15, "bold"), bg="white", fg="black")
        lbl_add2p.grid(row=9, column=1, pady=5, padx=5, sticky="e")

        txt_add2p = Entry(manage_frame1, textvariable=self.h, width=5, font=("times new roman", 15, "bold"), bd=5,
                          relief=RAISED)
        txt_add2p.grid(row=9, column=2, pady=5, padx=5, sticky="s")
        lbl_add3 = Label(manage_frame1, text="S. T", font=("times new roman", 15, "bold"), bg="white", fg="black")
        lbl_add3.grid(row=10, column=0, pady=5, padx=5, sticky="w")

        txt_add3 = Entry(manage_frame1, textvariable=self.t, width=5, font=("times new roman", 15, "bold"), bd=5,
                         relief=RAISED)
        txt_add3.grid(row=10, column=0, pady=5, padx=5, sticky="e")
        txt_add3 = Entry(manage_frame1, textvariable=self.t, width=5, font=("times new roman", 15, "bold"), bd=5,
                         relief=RAISED)
        txt_add3.grid(row=10, column=1, pady=5, padx=5, sticky="w")

        lbl_add3p = Label(manage_frame1, text="P. L", font=("times new roman", 15, "bold"), bg="white", fg="black")
        lbl_add3p.grid(row=10, column=1, pady=5, padx=5, sticky="e")

        txt_add3p = Entry(manage_frame1, textvariable=self.l2, width=5, font=("times new roman", 15, "bold"), bd=5,
                          relief=RAISED)
        txt_add3p.grid(row=10, column=2, pady=5, padx=5, sticky="s")
        lbl_o1 = Label(manage_frame1, text="Shirt", font=("times new roman", 15, "bold"), bg="white", fg="black")
        lbl_o1.grid(row=0, column=2, pady=5, padx=5, sticky="w")

        txt_o1 = Entry(manage_frame1, textvariable=self.o1, width=5, font=("times new roman", 15, "bold"), bd=5,
                          relief=RAISED)
        txt_o1.grid(row=0, column=3, pady=5, padx=5, sticky="w")
        lbl_o2 = Label(manage_frame1, text="Pant", font=("times new roman", 15, "bold"), bg="white", fg="black")
        lbl_o2.grid(row=0, column=4, pady=5, padx=5, sticky="n")

        txt_o2 = Entry(manage_frame1, textvariable=self.o2, width=5, font=("times new roman", 15, "bold"), bd=5,
                       relief=RAISED)
        txt_o2.grid(row=0, column=5, pady=5, padx=5, sticky="w")
        lbl_o3 = Label(manage_frame1, text="Coat", font=("times new roman", 15, "bold"), bg="white", fg="black")
        lbl_o3.grid(row=1, column=2, pady=5, padx=5, sticky="w")

        txt_o3 = Entry(manage_frame1, textvariable=self.o3, width=5, font=("times new roman", 15, "bold"), bd=5,
                       relief=RAISED)
        txt_o3.grid(row=1, column=3, pady=5, padx=5, sticky="w")

        lbl_o3 = Label(manage_frame1, text="Kurta", font=("times new roman", 15, "bold"), bg="white", fg="black")
        lbl_o3.grid(row=2, column=2, pady=5, padx=5, sticky="w")

        txt_o3 = Entry(manage_frame1, textvariable=self.o4, width=5, font=("times new roman", 15, "bold"), bd=5,
                       relief=RAISED)
        txt_o3.grid(row=2, column=3, pady=5, padx=5, sticky="w")

        lbl_add4 = Label(manage_frame1, text="S. N", font=("times new roman", 15, "bold"), bg="white", fg="black")
        lbl_add4.grid(row=11, column=0, pady=5, padx=5, sticky="w")

        txt_add4 = Entry(manage_frame1, textvariable=self.n, width=5, font=("times new roman", 15, "bold"), bd=5,
                         relief=RAISED)
        txt_add4.grid(row=11, column=0, pady=5, padx=5, sticky="e")
        txt_add4 = Entry(manage_frame1, textvariable=self.n, width=5, font=("times new roman", 15, "bold"), bd=5,
                         relief=RAISED)
        txt_add4.grid(row=11, column=1, pady=5, padx=5, sticky="w")

        lbl_add4p = Label(manage_frame1, text="P. M", font=("times new roman", 15, "bold"), bg="white", fg="black")
        lbl_add4p.grid(row=11, column=1, pady=5, padx=5, sticky="e")

        txt_add4p = Entry(manage_frame1, textvariable=self.m, width=5, font=("times new roman", 15, "bold"), bd=5,
                          relief=RAISED)
        txt_add4p.grid(row=11, column=2, pady=5, padx=5, sticky="s")

        lbl_add5 = Label(manage_frame1, text="S. W", font=("times new roman", 15, "bold"), bg="white",
                         fg="black")
        lbl_add5.grid(row=12, column=0, pady=5, padx=5, sticky="w")

        txt_add5 = Entry(manage_frame1, textvariable=self.w, width=5, font=("times new roman", 15, "bold"), bd=5,
                         relief=RAISED)
        txt_add5.grid(row=12, column=0, pady=5, padx=5, sticky="e")
        txt_add5 = Entry(manage_frame1, textvariable=self.w, width=5, font=("times new roman", 15, "bold"), bd=5,
                         relief=RAISED)
        txt_add5.grid(row=12, column=1, pady=5, padx=5, sticky="w")

        lbl_add5p = Label(manage_frame1, text="P. G", font=("times new roman", 15, "bold"), bg="white",
                          fg="black")
        lbl_add5p.grid(row=12, column=1, pady=5, padx=5, sticky="e")

        txt_add5p = Entry(manage_frame1, textvariable=self.g, width=5, font=("times new roman", 15, "bold"), bd=5,
                          relief=RAISED)
        txt_add5p.grid(row=12, column=2, pady=5, padx=5, sticky="s")
        txt_add5p = Entry(manage_frame1, textvariable=self.g, width=5, font=("times new roman", 15, "bold"), bd=5,
                          relief=RAISED)
        txt_add5p.grid(row=12, column=3, pady=5, padx=5, sticky="s")

        lbl_others = Label(manage_frame1, text="Others", font=("times new roman", 15, "bold"), bg="white",
                           fg="black")
        lbl_others.grid(row=1, column=4, pady=5, padx=5, sticky="n")

        txt_others = Entry(manage_frame1, textvariable=self.o, width=5, font=("times new roman", 15, "bold"), bd=5,
                           relief=RAISED)

        txt_others.grid(row=1, column=5, pady=5, padx=5, sticky="w")


        btn_frame = Frame(manage_frame1, bd=2, relief=RIDGE, bg="white", highlightbackground="gray",
                          highlightthickness=2)

        btn_frame.place(x=360, y=470, width=320)

        addbtn = Button(btn_frame, text="Add", width=8, command=self.add_customer).grid(row=0, column=0, padx=5)
        updatebtn = Button(btn_frame, text="Update", width=8, command=self.update_data).grid(row=0, column=1, padx=5)
        deletebtn = Button(btn_frame, text="Delete", width=8, command=self.delete_data).grid(row=0, column=2, padx=5)
        clearbtn = Button(btn_frame, text="Clear", width=8, command=self.clear).grid(row=0, column=3, padx=5)

        lbl_search = Label(detail_frame, text="Search By", bg="white", font=("times new roman", 15, "bold"), fg="black")
        lbl_search.grid(row=0, column=0, pady=10, padx=10, sticky="w")

        combo_search = ttk.Combobox(detail_frame, textvariable=self.search_by, width=6,
                                    font=("times new roman", 13, "bold"), state="readonly")
        combo_search['values'] = ("name", "phone", "id", "date")
        combo_search.grid(row=0, column=1, padx=10, pady=10)

        txt_search = Entry(detail_frame, textvariable=self.search_text, width=10, font=("times new roman", 10, "bold"),
                           bd=5, relief=GROOVE, highlightbackground="gray", highlightthickness=2)
        txt_search.grid(row=0, column=2, pady=10, padx=10, sticky="w")

        search_btn = Button(detail_frame, relief=GROOVE, command=self.search_data, text="Search", width=8, pady=5).grid(
            row=0,
            column=3,
            padx=5)
        show_all_btn = Button(detail_frame, relief=GROOVE, command=self.fetch_data, text="Show All", width=5,
                              pady=5).grid(row=0,
                                           column=4,
                                           padx=5)
        rec_btn = Button(detail_frame, text="Save", relief=GROOVE, command=threading.Thread(target=self.save_data).start(), width=5, pady=4).grid(row=0,
                                                                                                                 column=6,
                                                                                                                 padx=5)

        table_frame = Frame(detail_frame, bd=5, relief=GROOVE, bg="white")
        table_frame.place(x=5, y=60, width=600, height=520)
        rec_btn = Button(detail_frame, text="Receipt", command=self.rec, width=8, pady=5).grid(row=0, column=5, padx=5)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.customer_table = ttk.Treeview(table_frame, columns=(
        "id", "name", "phone", "l", "ch", "s", "t", "n", "w", "l1", "w1", "h", "l2", "m", "g", "others","o1","o2","o3","o4","del", "date"),
                                           xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set, )
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.customer_table.xview)
        scroll_y.config(command=self.customer_table.yview)
        self.customer_table.heading("id", text="Customer ID")
        self.customer_table.heading("name", text="customer name")
        self.customer_table.heading("phone", text="phone no")
        self.customer_table.heading("l", text="S. L")
        self.customer_table.heading("ch", text="S. CH")
        self.customer_table.heading("s", text="S. S")
        self.customer_table.heading("t", text="S. T")
        self.customer_table.heading("n", text="S. N")
        self.customer_table.heading("w", text="S. W")
        self.customer_table.heading("l1", text="P. L")
        self.customer_table.heading("w1", text="P. W")
        self.customer_table.heading("h", text="P. H")
        self.customer_table.heading("l2", text="P. L")
        self.customer_table.heading("m", text="P. M")
        self.customer_table.heading("g", text="P. G")
        self.customer_table.heading("others", text="Others")
        self.customer_table.heading("o1", text="Shirt Q.")
        self.customer_table.heading("o2", text="Pant Q.")
        self.customer_table.heading("o3", text="Coat")
        self.customer_table.heading("o4", text="Kurta")
        self.customer_table.heading("del", text="Delivery Date")
        self.customer_table.heading("date", text="Date")
        self.customer_table['show'] = 'headings'
        self.fetch_data()
        self.customer_table.pack(fill=BOTH, expand=2)
        self.customer_table.bind("<ButtonRelease-1>", self.get_cur)

    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'


    def setup(self):
        self.old_x = None
        self.old_y = None
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.pen_button
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def use_pen(self):
        self.activate_button(self.pen_button)

    def use_eraser(self):
        self.activate_button(self.eraser_button2, eraser_mode=True)

    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        self.line_width = self.choose_size_button.get()
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None

    def clear1(self):
        self.c.delete("all")
        self.image=Image.new("RGB",(200,200),(255,255,255))
        self.draw=ImageDraw.Draw(self.image)

    def convertToBinaryData(self,filename):
        with open(self.can_path, 'rb') as file:
            blobData = file.read()
        return blobData

    def add_customer(self):
        if self.phone.get() == "" or self.customer_name.get() == "":
            messagebox.showerror("Error", "All fields are required!")
        else:
            con = sqlite3.connect("newnew1.db")
            cur = con.cursor()
            blobData = ""
            print(self.can_path)
            if self.can_path!="":
                blobData =self.convertToBinaryData(self.can_path)

            cur.execute("insert into customer_jj  (name,phone,l,ch,s,t,n,w,l1,w1,h,l2,m,g,others,o1,o2,o3,o4,del,date,image)  values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (self.customer_name.get(), self.phone.get(), self.l.get(), self.ch.get(),
                 self.s.get(), self.t.get(), self.n.get(), self.w.get(), self.l1.get(), self.w1.get(), self.h.get(),
                 self.l2.get(), self.m.get(), self.g.get(), self.o.get(), self.o1.get(),self.o2.get(),self.o3.get(),self.o4.get(),self.del_date.get(), self.date.get(),blobData))

            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success", "Record has been inserted")
    def fetch_data(self):
        con = sqlite3.connect("newnew1.db")
        cur = con.cursor()
        cur.execute("select * from customer_jj ORDER BY id DESC")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.customer_table.delete(*self.customer_table.get_children())
            for row in rows:
                self.customer_table.insert('', END, values=row)
                self.search1()
            con.commit()
        con.close()
    def clear(self):
        self.id.set("")
        self.customer_name.set("")
        self.l.set("")
        self.phone.set("")
        self.ch.set("")
        self.s.set("")
        self.t.set("")
        self.n.set("")
        self.w.set("")
        self.l1.set("")
        self.w1.set("")
        self.h.set("")
        self.l2.set("")
        self.m.set("")
        self.g.set("")
        self.o.set("")
        self.o1.set("")
        self.o2.set("")
        self.o3.set("")
        self.o4.set("")
        self.del_date.set("")
        self.clear1()

        self.date.set(self.format_date)
    def get_cur(self, ev):
        cursor_row = self.customer_table.focus()
        contents = self.customer_table.item(cursor_row)

        row = contents['values']

        self.id.set(row[0])
        self.customer_name.set(row[1])
        self.l.set(row[3])
        self.phone.set(row[2])
        self.ch.set(row[4])
        self.s.set(row[5])
        self.t.set(row[6])
        self.n.set(row[7])
        self.w.set(row[8])
        self.l1.set(row[9])
        self.w1.set(row[10])
        self.h.set(row[11])
        self.l2.set(row[12])
        self.m.set(row[13])
        self.g.set(row[14])
        self.o.set(row[15])
        self.o1.set(row[16])
        self.o2.set(row[17])
        self.o3.set(row[18])
        self.o4.set(row[19])
        self.date.set(row[21])
        self.del_date.set(row[20])
        self.can_path =  row[22]
        if not os.path.exists('IMAGES'):
            os.makedirs('IMAGES')
        # with open("IMAGES", 'w') as file:
        #     file.write(self.can_path)

    def update_data(self):
        con = sqlite3.connect("newnew1.db")
        cur = con.cursor()

        cur.execute("update customer_jj set name=?,l=?,ch=?,s=?,t=?,n=?,w=?,l1=?,w1=?,h=?,l2=?,m=?,g=?,others=?,o1=?,o2=?,o3=?,o4=?,del=?,date=? where phone=?",(self.customer_name.get(), self.l.get(), self.ch.get(), self.s.get(),self.t.get(), self.n.get(), self.w.get(), self.l1.get(), self.w1.get(), self.h.get(), self.l2.get(),self.m.get(), self.g.get(), self.o.get(), self.o1.get(), self.o2.get(), self.o3.get(), self.o4.get(),self.del_date.get(), self.date.get(), self.phone.get(),))
        if self.phone.get() != int:
            messagebox.showerror("Please Enter a number")
        else:
            pass
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()


    def delete_data(self):
        con = sqlite3.connect("newnew1.db")
        cur = con.cursor()

        cur.execute("delete from customer_jj where id=?", (self.id.get(),))
        con.commit()

        self.fetch_data()
        self.clear()
        con.close()

    def search_data(self):
        con = sqlite3.connect("newnew1.db")
        cur = con.cursor()
        cur.execute("select * from customer_jj where " + str(self.search_by.get()) + " Like '%" + str(
            self.search_text.get()) + "%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.customer_table.delete(*self.customer_table.get_children())

        for row in rows:
            self.customer_table.insert('', END, values=row)
        self.search1()
        con.commit()
        self.clear()
        con.close()
    def search1(self):
        con = sqlite3.connect("newnew1.db")
        cur = con.cursor()
        # blobData = ""

        # cur.execute("select image from customer_jj where " + str(self.search_by.get()) + " Like '%" + str(
        #     self.search_text.get()) + "%'")
        fn = 'new.jpg'
        cur.execute("select image from customer_jj where " + str(self.search_by.get()) + " Like '%" + str(
            self.search_text.get()) + "%'")
        r = cur.fetchall()
        for i in r:
            data = i[0]
        with open(fn, 'wb') as f:
            f.write(data)
        im = Image.open('new.jpg')
        im.show()
        f.close()
        con.commit()
        con.close()
    #
    def rec(self):
        top = Toplevel()
        top.geometry("600x400")
        top.config(bg='white')
        l = Label(top, text='_______RECEIPT______')
        l1 = Label(top, text='KING TAILORS', font=("times new roman", 40, "bold"))
        l1.pack()
        l.pack()
        l.config(bg='white')
        heading2 = Label(top, text="Customer Phone No  " f'{self.phone.get()}\t')
        heading1 = Label(top, text="    Date   " f'{self.date.get()}\t')
        heading2.pack()
        heading1.pack()
        l.config(bg='white')
        item2 = Label(top, text="Customer ID\t" f'{self.id.get()}', bd=5, font=("times new roman", 20, "bold"),
                      bg="white", fg="black")
        item3 = Label(top, text="Customer Name\t" f'{self.customer_name.get()}', bd=5,
                      font=("times new roman", 20, "bold"), bg="white", fg="black")
        item1 = Label(top, text="Delivery Date\t" f'{self.del_date.get()}', bd=5, font=("times new roman", 20, "bold"),
                      bg="white", fg="black")

        item2.pack()
        item3.pack()
        item1.pack()
        item1.config(bg='white')

    def save_data(self):

        # con = sqlite3.connect("new1.db")
        # cur = con.cursor()
        # cur.execute("select * from customer_jj")
        # rows = cur.fetchall()
        # r = str(rows)
        # m = codecs.open("text_file3.txt","r")
        # m1 = list(m)
        # # print(m1)
        # if r == m1:
        #     pass
        # else:
        #     with open("text_file3.txt", "a") as f:
        #         f.write(r)
        #         f.close()
            #{"installed":{"client_id":"743572129208-ummoe9fhr7airesnv2b312r5tfdc1g43.apps.googleusercontent.com","project_id":"vast-arena-334107","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://oauth2.googleapis.com/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_secret":"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","redirect_uris":["urn:ietf:wg:oauth:2.0:oob","http://localhost"]}}
        CLIENT_SECRET_FILE = 'client_secret.json'
        API_NAME = 'drive'
        API_VERSION = 'v3'
        SCOPES = ['https://www.googleapis.com/auth/drive']

        service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
        # file_id = '1YuT-k_ESMb0rHquVQ0FEyyyyrAtmYKxR'

        # Upload
        # a
        # file
        # print(dir(service))
        file_metadata = {
            'name': 'newnew1.db',
            'parents': ['15Zg3StNDDi_G2MQeFUHjvnR3gW5WgewD']
        }

        # media_content = MediaFileUpload('newnew1.db', mimetype='/')

        # file = service.files().create(body=file_metadata,media_body=media_content).execute()

        # print(file)
        # TO ADD CONTENT TO EXISTING FILE ON DRIVE
        file_id = '1-IO4NUv0hcYnanYglR-9MeLhHCvuVeop'

        media_content = MediaFileUpload('newnew1.db', mimetype='/')

        service.files().update(fileId=file_id, media_body=media_content).execute()

        schedule.every(5).seconds.do(self.save_data)
        while True:
            schedule.run_pending()
            time.sleep(1)

    def checkname(self, name):
        if name.isalpha():
            return True
        if name.isalnum():
            return False
        if len(str(name)) == 0:
            return True
        else:
            messagebox.showerror('Invalid', 'Name should be in Characters')

    #
    def checkphone(self, phone):
        if phone.isalpha():
            return False
        if phone.isalnum():
            return True
        if len(str(phone)) == 0:
            return True
        else:
            messagebox.showerror('Invalid', 'Phone No should be in numbers')
            return False

    def save(self):
        import uuid
        filename = str(uuid.uuid4())
        dir_path = os.getcwd()
        if not os.path.exists('IMAGES'):
            os.makedirs('IMAGES')
        ps = self.c.postscript(colormode='color')
        img = Image.open(io.BytesIO(ps.encode('utf-8')))
        filename1 =os.path.join(dir_path,"IMAGES", f'image_{filename}.jpg')
        img.save(filename1)
        self.can_path = filename1
    def validation(self):
        if self.customer_name.get() == '':
            messagebox.showerror('Error', 'Please enter your name', parent=self.root)


def __init__(self):
    self.root = Tk()


DEFAULT_PEN_SIZE = 5.0
DEFAULT_COLOR = 'black'
root = Tk()
ob = Student(root)
root.mainloop()