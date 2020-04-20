

from tkinter import *
from random import randint
master = Tk()
master.geometry('700x600')


frame = Frame(master)
frame.pack()

e = Entry(master)
e.pack()

e.focus_set()

def callback():
    a = e.get()
    e.delete(0, END)
    b = randint(0, 100)
    #b = a
    canvas = Canvas(master, width = 500, height = 100, bg='white')
    canvas.place(x=100, y=100)
    if a == b:
        canvas.create_text((50,50),text = "You Won")
    else:
        canvas.create_text((200,50),text = "You Lost. The generated number is:"+str(b))
     

b = Button(master, text="get", width=10, command=callback)

b.pack()
b1 = Button(frame, text = "QUIT", command = frame.quit)
b1.pack() 


mainloop()
