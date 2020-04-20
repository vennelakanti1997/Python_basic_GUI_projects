#!usr/bin/python3


import string
from tkinter import *
from tkinter import messagebox
from random import choice

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
