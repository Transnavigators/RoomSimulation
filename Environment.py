from tkinter import *
from Obstacle import *
from Localino import *
from Lidar import *
from Alexa import *
from Pi import *
from Wheelchair import *
from Person import *


class Environment:
    def __init__(self, width, height, obstacles=(), localino_anchors=[LocalinoAnchor(),LocalinoAnchor(),LocalinoAnchor()]):
        """Initialize all things present in the environment"""
        self.width = width
        self.height = height
        
        
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
            #exit()

    def move_person(self, x, y):
        self.person.set_pos(x,y)
        if not self.verify():
            print("Invalid State")
        
    def say(self, command):
        """Processes a say command in the environment"""
        self.alexa.say(command)

    def step(self):
        """Takes a step in the simulator
        Processes any movement the wheelchair will do and 
        """
        
        if not self.verify():
            print("Invalid State")

    def verify(self):
        """verifies boundaries of all physicals objects in the simulation
        If any objects are overlapping this state is an illegal one and verify should return false
        Limitations: Rounds values to the nearest integer
        
        Todo: wheelchair circular boundary
        
        returns True if state is legal
                False if state is illegal
        """
        # create a mock up environment to check bounds
        env_grid = [[False for j in range(self.height)] for i in range(self.width)]
        
        
        #check if anything is outside of the boundaries of the environment and if not then add it to the grid
        
        # check obstacles
        for obstacle in self.obstacles:
            if obstacle.x1<0 or obstacle.x1>self.width or obstacle.y1<0 or obstacle.y1>self.height or obstacle.x2<0 or obstacle.x2>self.width or obstacle.y2<0 or obstacle.y2>self.height:
                return False
            for i in range(round(obstacle.x1),round(obstacle.x2)):
                for j in range(round(obstacle.y1),round(obstacle.y2)):
                    if not env_grid[i][j]:
                        env_grid[i][j] = True
                    else:
                        return False
                        
        # check wheelchair boundary
        if self.wheelchair.x1<0 or self.wheelchair.x1>self.width or self.wheelchair.y1<0 or self.wheelchair.y1>self.height or self.wheelchair.x2<0 or self.wheelchair.x2>self.width or self.wheelchair.y2<0 or self.wheelchair.y2>self.height:
            return False
        for i in range(round(self.wheelchair.x1),round(self.wheelchair.x2)):
            for j in range(round(self.wheelchair.y1),round(self.wheelchair.y2)):
                if not env_grid[i][j]:
                    env_grid[i][j] = True
                else:
                    return False
                    
        # check person
        if self.person.x1<0 or self.person.x1>self.width or self.person.y1<0 or self.person.y1>self.height or self.person.x2<0 or self.person.x2>self.width or self.person.y2<0 or self.person.y2>self.height:
            return False
        for i in range(round(self.person.x1),round(self.person.x2)):
            for j in range(round(self.person.y1),round(self.person.y2)):
                if not env_grid[i][j]:
                    env_grid[i][j] = True
                else:
                    return False
        
        return True
