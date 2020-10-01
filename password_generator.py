# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 20:03:24 2020

@author: Vennelakanti
"""

import string
from tkinter import *
from tkinter import messagebox
from secrets import choice
#from random import choice

master = Tk()
master.geometry('250x250')
master.config(bg='black')


e = Entry()
e.pack()
e.focus_set()


def getp():
    length = e.get()
    e.delete(0, END)
    if str(length) == '' or str(length) == ' ':
        length = 7

    password = "".join([choice(string.ascii_letters+string.digits+string.punctuation) for i in range(int(length))])
    messagebox.showinfo(title='PASSWORD', message = f'YOUR PASSWORD IS: {password}')

Label(text="========PASWWORD GENERATOR========").pack(fill='x', pady=6)
button1 = Button(text='Generate', command=getp,padx=10).pack(pady=2)
master.mainloop()