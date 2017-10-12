from tkinter import *
from Obstacle import *
from Localino import *
from Lidar import *
from Alexa import *
from Pi import *
from Wheelchair import *
from Person import *


class Environment:
    def __init__(self, obstacles=(), localino_anchors=[LocalinoAnchor(),LocalinoAnchor(),LocalinoAnchor()]):
        """Initialize all things present in the environment"""
        
        # Generate Localino Tags
        wheelchair_tag = LocalinoTag()
        person_tag = LocalinoTag()
        
        # Initialize sensors
        self.localino_anchors = localino_anchors
        
        # Initialize the physical objects
        self.obstacles = obstacles 
        self.person = Person(localino_tag = person_tag) # person does not need to know the environment but needs a localino tag
        self.wheelchair = Wheelchair(environment = self, localino_tag = wheelchair_tag) # wheelchair's sensors need to know the environement and it contains a localino tag


        # Initialize the services
        self.localino_service = LocalinoService(anchors=localino_anchors, tags=[wheelchair_tag, person_tag])
        self.alexa = Alexa()

        # Initialize the pi
        self.pi = Pi(alexa = self.alexa, lidar = self.wheelchair.lidar, localino = self.localino_service, encoder = self.wheelchair.encoder, berryimu = self.wheelchair.berryimu)

        # Verify that all objects are in a valid position
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
