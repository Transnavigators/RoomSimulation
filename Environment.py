from tkinter import *
from Obstacle import *
from LocalinoAnchor import *
from LocalinoTag import *
from LocalinoService import *
from Lidar import *
from Alexa import *
from Pi import *
from Wheelchair import *
from Person import *


class Environment:
    def __init__(self, obstacles=[], localino_anchors=(), localino_tags=()):
        """Initialize all things present in the environment"""
        # Initialize the physical objects
        self.obstacles = obstacles
        self.wheelchair = Wheelchair(self)
        self.person = Person(self)

        # Initialize sensors
        self.lidar = Lidar(self)
        self.localino_anchors = localino_anchors
        self.localino_tags = localino_tags

        # Initialize the services
        self.localino_service = LocalinoService(anchors=localino_anchors, tags=localino_tags)
        self.alexa = Alexa()

        # Initialize the pi
        self.pi = Pi()

        if not self.verify():
            print("Invalid Initial State")
            exit()

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
