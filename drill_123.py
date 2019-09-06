#the buttons and fields in this gui don't actually do anything at this point
#author Jacob Kessler

import sqlite3
import shutil
import os
import time
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askdirectory



class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

     
        self.master = master
        self.master.minsize(500,300)
        self.master.maxsize(700,500)
        self.master.title("Check files")

        #btn for file source
        self.browseButton = Button(self.master,text="Browse source",width=14,height=1,command = lambda: get_path1(self))
        self.browseButton.grid(row=0,column=0,padx=(20,0),pady=(40,0),sticky=S+W)

        #text entry box1
        self.entry1 = tk.Entry(self.master, text='')
        self.entry1.grid(row=0,column=1,rowspan=1,columnspan=3,padx=(20,0),pady=(35,0))

        #btn for file destination
        self.browseButton2 = Button(self.master,text="Browse destination",width=14,height=1,command = lambda: get_path2(self))
        self.browseButton2.grid(row=1,column=0,padx=(20,0),pady=(20,0),sticky=S+W)

        #text entry box2
        self.entry2 = tk.Entry(self.master, text='')
        self.entry2.grid(row=1,column=1,rowspan=1,columnspan=3,padx=(20,0),pady=(35,0))

        #triggers file movement
        self.moveButton = Button(self.master,text="Move files...",width=12,height=2,command = lambda: move_files(self))
        self.moveButton.grid(row=2,column=0,padx=(20,0),pady=(20,0),sticky=S+W)

        #does nothing, but is placeholder for close button
        self.closeButton = Button(self.master,text="Close Program",width=12,height=2)
        self.closeButton.grid(row=2,column=3,padx=(20,0),pady=(20,0),sticky=S+E)

#gets file path for dir
def get_path1(self):
    global sourcePath1
    sourcePath1 = filedialog.askdirectory()
    print(sourcePath1)#confirms path is grabbed correctly
    self.entry1.delete(0, END)
    self.entry1.insert(0, sourcePath1)
    
def get_path2(self):
    global sourcePath2
    sourcePath2 = filedialog.askdirectory()
    print(sourcePath2)#confirms path is grabbed correctly
    self.entry2.delete(0, END)
    self.entry2.insert(0, sourcePath2)

def move_files(self):
    source = sourcePath1
    dest = sourcePath2
    for file in os.listdir(source):
        if file.endswith(".txt"):
            fullPath = os.path.join(source, file)
            print(fullPath) #test to see of file path concatinates correctly
            modification_time = os.path.getmtime(fullPath)
            local_time = time.ctime(modification_time)
            print("Last modification time(Local time):", local_time) #test time modified
            newDest = shutil.move(fullPath, dest)
            print("New destination path: ", newDest) #test to check if move worked correctly
            dbStorage(file, fullPath, local_time)

def dbStorage(file, fullPath, local_time):
    conn = sqlite3.connect('drill_123.db')
    with conn:
        cur = conn.cursor()
        #makes sure table exists to recieve data
        cur.execute("""create table if not exists tbl_files(\
            ID integer primary key autoincrement, \
            col_fname, \
            col_fpath, \
            col_time
            )""")
    conn.commit()
    cur.execute("""insert into tbl_files(col_fname, col_fpath, col_time) values (?,?,?)""", (file, fullPath, local_time))
    conn.close()

            

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
