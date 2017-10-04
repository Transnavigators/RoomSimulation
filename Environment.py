from tkinter import *
from Obstacle import *

class Environment:
    def __init__(self, obstacles = None, wheelchair = None, person = None):
        """initialize all things present in the environment"""
        self.obstacles = obstacles
        self.wheelchair = wheelchair
        self.person = person
        if not self.verify():
            print("Invalid Initial State")
            exit();
            
    
    def step(self):
        """Takes a step in the simulator
        Processes any movement the wheelchair will do and 
        verifies that the environment is in a valid state afterwards
        """
        
    
    def verify(self):
        """verify boundaries
        returns True if state is legal
        returns False if state is illegal
        """
        return True