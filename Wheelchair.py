from Lidar import *
from Encoder import *
from BerryIMU import *

class Wheelchair:
    """ Represents a the wheelchair
    Note: x1, y1, x2, y2 must represent upper left corner and lower right corner of the object
    
    CHALLENGE: HOW TO TURN
    """

    def __init__(self, environment, localino_tag, xc=50, yc=50, xVel=0, yVel=0, orientation=0,  length=32, width=32, mass=300,
                 wheels=((32, 0), (32, 16))):
        """initialize"""
        
        # save the wheelchair physical properties
        self.length = length
        self.width = width
        self.mass = mass
        self.wheels = wheels
        
        # set the boundary variables for the chair
        self.x1 = xc - width / 2
        self.y1 = yc - length / 2
        self.x2 = xc + width / 2
        self.y2 = yc + length / 2

        # save the initial velocity and orientation
        self.xVel = xVel
        self.yVel = yVel
        self.orientation = orientation
        
        
        # initialize sensors on the wheelchair
        self.lidar = Lidar(environment, xc, yc, orientation) # lidar is in the center of the chair
        self.encoder = Encoder(environment)
        self.berryimu = BerryIMU(environment)
        
        

    def move_sensors(self):
        """Updates the position and orientation all sensors on the chair during a move"""
        #update lidar
        self.lidar.xPos = self.lidar.xPos + self.x1
        self.lidar.yPos = self.lidar.yPos + self.y1
        self.lidar.orientation = self.lidar.orientation + self.orientation
        
        
        
    def draw(self, canvas):
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill="yellow")
