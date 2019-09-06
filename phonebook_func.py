#python 3.7.4

import os
from tkinter import *
import tkinter as tk
import sqlite3

import phonebook_main
import phonebook_gui

def center_window(self, w, h):
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()

    x = int((screen_width/2)-(w/2))
    y = int((screen_height/2)-(h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo



def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okey to exit application?"):
        self.master.destroy()
        os._exit(0)


#start of database stuff
def create_db(self):
    conn = sqlite3.connect('db_phonebook.db')
    with conn:
        cur = conn.cursor()
        cur.execute("create table if not exists tbl_phonebook( \
            ID integer primary key autoincrement, \
            col_fname text, \
            col_lname text, \
            col_fullname text, \
            col_phone text, \
            col_email text \
            );")
        conn.commit()
    conn.close()
    first_run(self)


def first_run(self):
    conn = sqlite3.connect('db_phonebook.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            cur.execute("""insert into tbl_phonebook (col_fname,col_lname,col_fullname,col_phone,col_email) values (?,?,?,?,?)""", ('John','Doe','John Doe','111-111-1111','jdoe@email.com'))
            conn.commit()
    conn.close()


def count_records(cur):
    count = ""
    cur.execute("""select count(*) from tbl_phonebook""")
    count = cur.fetchone()[0]
    return cur,count

#selecting items in list box
def onSelect(self,event):
    #calling this event is the lstList1 widget
    varList = event.widget
    select = varList.curselection()[0]
    value = varList.get(select)
    conn = sqlite3.connect('db_phonebook.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""select col_fname,col_lname,col_phone,col_email from tbl_phonebook where col_fullname = (?)""", [value])
        varBody = cursor.fetchall()
        for data in varBody:
            self.txt_fname.delete(0,END)
            self.txt_fname.insert(0,data[0])
            self.txt_lname.delete(0,END)
            self.txt_lname.insert(0,data[1])
            self.txt_phone.delete(0,END)
            self.txt_phone.insert(0,data[2])
            self.txt_email.delete(0,END)
            self.txt_email.insert(0,data[3])

def addToList(self):
    var_fname = self.txt_fname.get()
    var_lname = self.txt_lname.get()
    #data normailization
    var_fname = var_fname.strip()
    var_lname = var_lname.strip()
    var_fname = var_fname.title()
    var_lname = var_lname.title()
