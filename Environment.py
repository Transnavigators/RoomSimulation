from tkinter import *


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)               
        self.master = master
        self.init_window()
        self.draw_room()

    def init_window(self):
        self.master.title("Room Simulation")
        self.canvas = Canvas(self.master, bg="WHITE")
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.place_person)
        
    def draw_room(self):
        print("draw room here")
       
       
    def place_person(self, event):
        self.canvas.delete("all")
        self.canvas.create_rectangle(event.x,event.y,event.x+10,event.y+10, fill="#fb0")
        
    def client_exit(self):
        exit()
        
        
root = Tk()

root.geometry("400x400")

app = Window(master=root)
root.mainloop()