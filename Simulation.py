from tkinter import *
from Environment import *
from Obstacle import *
from Person import *
from Wheelchair import *
import threading
import time


class Simulation(Frame):
    def __init__(self, master=None):
        """Initializes the environment and the GUI"""
        Frame.__init__(self, master)
        self.master = master

        # generate environment
        obstacles = (Obstacle(10, 10, 40, 400), Obstacle(150, 80, 200, 180))
        
        self.environment = Environment(width=500, height=500, obstacles=obstacles)

        self.init_window()
        self.draw()
        self.running = False

    def init_window(self):
        """Prepares the window with all GUI elements"""
        # set title of the window
        self.master.title("Room Simulation")

        # create the GUI elements
        self.command_text_box = Text(self.master, height=1, width=55)
        self.say_button = Button(self.master, text="Say", command=self.say)
        self.canvas = Canvas(self.master, bg="WHITE", width=500, height=500)
        self.canvas.bind("<Button-1>", self.place_person)
        self.step_button = Button(self.master, text="Step", command=self.step)
        self.stop_button = Button(self.master, text="Stop", command=self.stop)
        self.run_button = Button(self.master, text="Run", command=self.run)

        # layout elements onto the frame
        self.command_text_box.grid(row=0, column=0)
        self.say_button.grid(row=0, column=2)
        self.canvas.grid(row=1, columnspan=3)
        self.step_button.grid(row=2, column=0)
        self.stop_button.grid(row=2, column=1)
        self.run_button.grid(row=2, column=2)


    def draw(self):
        """Draws the the environment"""
        self.canvas.delete("all")
        for obstacle in self.environment.obstacles:
            obstacle.draw(self.canvas)
        self.environment.wheelchair.draw(self.canvas)
        self.environment.person.draw(self.canvas)


    def say(self):
        """Handles voice commands"""
        print("Saying:", self.command_text_box.get("1.0", "end-1c"))
        self.environment.say(self.command_text_box.get("1.0", "end-1c"))

    def step(self):
        """Takes one step in the simulation"""
        print("STEP")
        self.environment.step()
        self.draw()

    def stop(self):
        """Stops the simulation from running"""
        print("STOP")
        self.running = False

    def run(self):
        """Runs the simulation"""
        print("RUN")
        self.running = True
        threading.Thread(target=self.runloop, daemon=True).start()

    def runloop(self):
        while self.running:
            self.step()

    def place_person(self, event):
        """Edits the location of the person in the room"""
        self.environment.move_person(event.x, event.y)
        self.draw()
        # self.canvas.create_rectangle(event.x,event.y,event.x+10,event.y+10, fill="#fb0")
        # self.canvas.create_image(self.environment.person.x,self.environment.person.y,image=self.environment.person.image,anchor="nw")


root = Tk()

root.geometry("700x700")

app = Simulation(master=root)
root.mainloop()
