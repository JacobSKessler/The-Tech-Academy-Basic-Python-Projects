# python ver 3.7.4
#
# Student Author: Jacob Kessler
#
# purpose: phonebook demo, demonstrate OOP, Tkinter GUI, Tkinter parent child relationship
#
# tested os: windows 10

from tkinter import *
import tkinter as tk

#other files we need
import phonebook_gui
import phonebook_func

#main frame
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #define master frame config
        self.master = master
        self.master.minsize(500,300) #hight, width
        self.master.maxsize(500,300)

        phonebook_func.center_window(self,500,300)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.configure(bg="#f0f0f0")

        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_funct.ask_quit(self))
        arg = self.master

        phonebook_gui.load_gui(self)




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
