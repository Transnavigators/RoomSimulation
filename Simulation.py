from tkinter import *
from Environment import *
from Obstacle import *
from Person import *
from Wheelchair import *
import time


class Simulation(Frame):
    def __init__(self, master=None):
        """Initializes the environment and the GUI"""
        Frame.__init__(self, master)
        self.master = master

        # generate environment
        obstacles = (Obstacle(10, 10, 40, 400), Obstacle(200, 130, 150, 80))
        
        self.environment = Environment(obstacles)

        self.init_window()
        self.draw_room()

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

    def draw_room(self):
        """Draws all obstacles in the room"""
        for obstacle in self.environment.obstacles:
            self.canvas.create_rectangle(obstacle.x1, obstacle.y1, obstacle.x2, obstacle.y2, fill=obstacle.color)

    def draw_wheelchair(self):
        """Draws the wheelchair"""
        self.environment.wheelchair.draw(self.canvas)

    def draw_person(self):
        """Draws the person"""
        self.environment.person.draw(self.canvas)

    def say(self):
        """Handles voice commands"""
        print("Saying:", self.command_text_box.get("1.0", "end-1c"))
        self.environment.say(self.command_text_box.get("1.0", "end-1c"))

    def step(self):
        """Takes one step in the simulation"""
        print("STEP")
        self.environment.step()

    def stop(self):
        """Stops the simulation from running"""
        print("STOP")

    def run(self):
        """Runs the simulation"""
        print("RUN")

    def place_person(self, event):
        """Edits the location of the person in the room"""
        self.canvas.delete("all")

        self.environment.person.set_pos(event.x, event.y)

        
        self.draw_room()
        self.draw_person()
        self.draw_wheelchair()
        # self.canvas.create_rectangle(event.x,event.y,event.x+10,event.y+10, fill="#fb0")
        # self.canvas.create_image(self.environment.person.x,self.environment.person.y,image=self.environment.person.image,anchor="nw")


root = Tk()

root.geometry("700x700")

app = Simulation(master=root)
root.mainloop()
