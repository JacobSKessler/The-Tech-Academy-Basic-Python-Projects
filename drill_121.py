#the buttons and fields in this gui don't actually do anything at this point

from tkinter import *
import tkinter as tk


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

     
        self.master = master
        self.master.minsize(500,300)
        self.master.maxsize(700,500)
        self.master.title("Check files")


        self.browseButton = Button(self.master,text="Browse...",width=12,height=1)
        self.browseButton.grid(row=0,column=0,padx=(20,0),pady=(40,0),sticky=S+W)
        self.browseButton2 = Button(self.master,text="Browse...",width=12,height=1)
        self.browseButton2.grid(row=1,column=0,padx=(20,0),pady=(20,0),sticky=S+W)

        #text entry boxes
        self.entry1 = tk.Entry(self.master, text='')
        self.entry1.grid(row=0,column=1,rowspan=1,columnspan=3,padx=(20,0),pady=(35,0))
        self.entry2 = tk.Entry(self.master, text='')
        self.entry2.grid(row=1,column=1,rowspan=1,columnspan=3,padx=(20,0),pady=(20,0))

        #grid placeholder
        #self.lbl_fname = tk.Label(self.master,text='')
        #self.lbl_fname.grid(row=0,column=2,padx=(20,0),pady=(10,0),sticky=N+W)

        self.ckeckButton = Button(self.master,text="Check for files...",width=12,height=2)
        self.ckeckButton.grid(row=2,column=0,padx=(20,0),pady=(20,0),sticky=S+W)
        
        self.closeButton = Button(self.master,text="Close Program",width=12,height=2)
        self.closeButton.grid(row=2,column=3,padx=(20,0),pady=(20,0),sticky=S+E)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
