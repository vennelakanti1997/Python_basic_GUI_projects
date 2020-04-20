#!/usr/bin/python3

from tkinter import *
from PIL import Image, ImageTk
from random import randint
import os
directory = '/home/vennelakanti/Desktop/codes_practice/python/tkinter_codes/rps/'

def random_generate():
    return randint(1, 3)




        

#1:rock 2:paper 3:scissor
def rock():
    #a = 1
    canvas = Canvas(master, width = 500, height = 100, bg = 'white')
    canvas.place(x=400, y = 400)
    b = random_generate()
    if b == 1:
        canvas.create_text((50,50), text = "Draw")
    elif b==3:
        canvas.create_text((100,50), text = "You Win. Rock breaks Scissor")
    else:
        canvas.create_text((100,50), text = "You Lost. Paper beats rock " )
        
        
#1:rock 2:paper 3:scissor
def scissor():
    #a = 2
    canvas = Canvas(master, width = 500, height = 100, bg = 'white')
    canvas.place(x=400, y = 400)
    b = random_generate()
    if b == 3:
        canvas.create_text((50,50), text = "Draw")
    elif b == 2:
        canvas.create_text((100,50), text = "You Won!! Scissor Cuts paper")
    else:
        canvas.create_text((100,50), text = "You Lost. Rock breaks Scissor")

         

#1:rock 2:paper 3:scissor
def paper():
    #a = 3
    canvas = Canvas(master, width = 500, height = 100, bg = 'white')
    canvas.place(x=400, y = 400)
    b = random_generate()
    if b == 3:
        canvas.create_text((50,50), text = "Draw")
    elif b == 1:
        canvas.create_text((100,50), text = "You Win!! Paper beats Rock")
    else:
        canvas.create_text((100,50), text = "You lose. Scissors cut paper")

master = Tk()
master.geometry('1000x1000')

pil_rock_image = Image.open(directory+'rock.jpg')
pil_rock_image=pil_rock_image.resize((64,64))
rock_image = ImageTk.PhotoImage(pil_rock_image)


pil_paper_image = Image.open(directory+'paper.jpg')
pil_paper_image = pil_paper_image.resize((64,64))
paper_image = ImageTk.PhotoImage(pil_paper_image)

pil_scissor_image = Image.open(directory+'scissor.jpg')
pil_scissor_image = pil_scissor_image.resize((64,64))
scissor_image = ImageTk.PhotoImage(pil_scissor_image)



rock = Button(master, image = rock_image, command=rock)
rock.pack()
paper = Button(master, image = paper_image, command=paper)
paper.pack()
scissors = Button(master, image = scissor_image, command=scissor)
scissors.pack()

quitting = Button(master, text = "QUIT", command=master.quit)
quitting.pack(side=TOP)

master.mainloop()
