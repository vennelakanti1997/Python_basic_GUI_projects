import secrets

#print(secrets.randbelow(7))

from tkinter import messagebox,filedialog, Button, Entry
import tkinter as tk

        
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        
        
    def create_widgets(self):
        self.entry = Entry(self, text = "Result of dice rolled")
        self.entry.pack()
        self.press_dice = Button(self, text = "Press to roll the dice", command = self.roll_dice)
        self.press_dice.pack(side='top')
        self.quit = Button(self, text="QUIT", fg="red",command=self.master.destroy)
        self.quit.pack(side="bottom")
        
    def roll_dice(self):
        self.entry.delete(0, "end")
        self.entry.insert(0, str(secrets.choice([1,2,3,4,5,6])))
        
        
                    
root = tk.Tk()

app = Application(master=root)
app.master.title("Roll dice")
app.mainloop()