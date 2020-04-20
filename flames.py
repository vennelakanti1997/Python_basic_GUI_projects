
#Works only with Python3


from collections import Counter
from tkinter import *
from tkinter import messagebox
from functools import partial

def flames(name1, name2):
    string1 = name1.get()
    #name1.delete(0, END)
    string2 = name2.get()
    #name2.delete(0, END)
    if not string1 or not string2:
        #canvas.create_text((250, 40), text = "You did not enter either of the names. Please check your inputs")
        messagebox.showerror(title = "Flames Result", message = "You did not enter either of the names. Please check your inputs")
    elif string1 == " " or string2 == " ":
        #canvas.create_text((250,40), text = "Either of the names are empty. Please check your inputs")
        messagebox.showerror(title = "Flames Result", message = "Either of the names are empty. Please check your inputs" )
    else:
        flames_list= ["Friends", "Lovers", "Attraction", "Marriage", "Enemies", "Siblings"]
        #flames_list = ["Sibliings", "Enemies", "Marriage", "Attraction", "Lovers", "Friends"]
        temp_string1 = string1.replace(" ", "").casefold()
        temp_string2 = string2.replace(" ", "").casefold()
    
        temp_dict_1 = Counter(temp_string1)
        temp_dict_2 = Counter(temp_string2)
    
        common_elements = set(temp_dict_1).intersection(set(temp_dict_2))
        summation_1 = 0
        temp_sum_1 = 0
        temp_sum_2 = 0
        for i in common_elements:
            temp_sum_1 += temp_dict_1.get(i)
            temp_sum_2 += temp_dict_2.get(i)
            summation_1 += abs(temp_dict_1.get(i) - temp_dict_2.get(i))
    
        result = (len(temp_string1) + len(temp_string2)- temp_sum_1 - temp_sum_2 + summation_1)%6 - 1
        #canvas.create_text((250,40), text = flames_list[result])
        messagebox.showinfo(title="Flames Result", message = flames_list[result])
            
        
    
    
#flames(string1, string2)
#print(flames(input("Enter First name:"), input("Enter second Name:")))

master = Tk()
master.geometry('700x600')

Label(master, text = "Name1:").place(x=30, y = 50)
Label(master, text = "Name2:").place(x = 30, y = 90)


na1 = StringVar()
na2 = StringVar()
Entry(master, textvariable = na1).place(x = 80, y = 50)
#name1.pack()
#name1.focus_set()

Entry(master, textvariable = na2).place(x = 80, y = 90)
#name2.pack()

flames = partial(flames, na1, na2)
Button(master, text = "Get FLAMES", width = 25, command = flames).place(x=80, y=150)



Button(master, text = "QUIT", width = 10, command = master.quit).place(x =30,y = 150)


mainloop()


