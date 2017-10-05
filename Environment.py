from tkinter import *
from Obstacle import *
from LocalinoAnchor import *
from LocalinoTag import *
from LocalinoService import *
from Lidar import *
from Alexa import *
from Pi import *


class Environment:
    def __init__(self, obstacles = None, wheelchair = None, person = None, localino_anchors=(), localino_tags=(), lidar = Lidar()):
        """initialize all things present in the environment"""
        # initialize the physical objects
        self.obstacles = obstacles
        self.wheelchair = wheelchair
        self.person = person
        
        # initialize sensors
        self.lidar = lidar
        self.localino_anchors = localino_anchors
        self.localino_tags = localino_tags
        
        # initialize the services
        self.localino_service = LocalinoService(anchors = localino_anchors, tags = localino_tags)
        self.alexa = Alexa()
        
        #initialize the pi
        self.pi = Pi(localino_service = self.localino_service, lidar = self.lidar, alexa = self.alexa)
        
        if not self.verify():
            print("Invalid Initial State")
            exit();
            
    def say(self, command):
        """Processes a say command in the environment"""
        self.alexa.say(command)
    
    def step(self):
        """Takes a step in the simulator
        Processes any movement the wheelchair will do and 
        """
        
        self.verify()
        
    
    def verify(self):
        """verifies boundaries of all physicals objects in the simulation
        If any objects are overlapping this state is an illegal one and verify should return false
        
        returns True if state is legal
                False if state is illegal
        """
        return True