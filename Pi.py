from Alexa import *
from Lidar import *
from Localino import *
from Encoder import *
from BerryIMU import *
import math

class Pi:
    """Pi Controller for the wheelchair
        "The brains"
    """

    def __init__(self, alexa, lidar, localino, encoder, berryimu):
        """initialize
        all data inputs
        """
        self.alexa = alexa
        self.lidar = lidar
        self.localino = localino
        self.encoder = encoder
        self.berryimu = berryimu
        
        self.dir = 0
        self.vel = (0,0)
    
    def step(self):
        person_loc = self.localino.get_person()
        wheelchair_loc = self.localino.get_wheelchair()
        
        x = person_loc.xPos-wheelchair_loc.xPos
        y = person_loc.yPos-wheelchair_loc.yPos
        
        self.dir = math.atan2(x,y)
        self.vel = 4
        