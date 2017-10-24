import math
import tkinter
from Lidar import *
from Encoder import *
from BerryIMU import *

class Wheelchair:
    """ Represents a the wheelchair
    Note: x1, y1, x2, y2 must represent upper left corner and lower right corner of the object

    
    CHALLENGE: HOW TO TURN
    """

    def __init__(self, environment, localino_tag, xPos=100, yPos=100, orientation=0,  height=32, width=32, mass=300, wheels=((32, 0), (32, 16))):
        """initialize
        environment is the environment that the wheelchair is in
        localino tag is the localino tag which is attached to the wheelchair
        orientation is a clockwise from the verticle  (rad)
        xPos, yPos are coordinates of the center of the chair
        width = length in x dir
        height = length in y dir
        """
        
        # save the wheelchair physical properties
        self.image = tkinter.PhotoImage(file="Wheelchair.png")
        self.height = height
        self.width = width
        self.mass = mass
        self.wheels = wheels
        

        # save the initial velocity and orientation
        self.orientation = orientation
        self.xPos = yPos
        self.yPos = xPos
        self.xVel = 0
        self.yVel = 0
        self.xAcc = 0
        self.yAcc = 0
        self.update_boundary_positions()
        
        # initialize sensors on the wheelchair
        self.localino_tag = localino_tag
        self.lidar = Lidar(environment, self.xPos, self.yPos, orientation) # lidar is in the center of the chair
        self.encoder = Encoder(wheelchair = self)
        self.berryimu = BerryIMU(wheelchair = self)
        
        # update positions for all the sensors
        self.update_sensor_positions()

    def update_sensor_positions(self):
        """Updates the position and orientation all sensors on the chair during a move"""

        # update the position of the localino tag (center of chair)
        self.localino_tag = self.xPos
        self.localino_tag = self.yPos
        
    def update_boundary_positions(self):
        """updates the boundary vairable x1,y1,x2,y2 of the chair"""
        # set the boundary variables for the chair
        self.x1 = self.xPos - self.width / 2
        self.y1 = self.yPos - self.height / 2
        self.x2 = self.xPos + self.width / 2
        self.y2 = self.yPos + self.height / 2    

    def draw(self, canvas):
        cosval = math.cos(self.orientation)
        sinval = math.sin(self.orientation)
        
        # create the rotated vertices
        vertices = []
        vertices.append([(self.x1-self.xPos)*cosval-(self.y1-self.yPos)*sinval+self.xPos,(self.x1-self.xPos)*sinval+(self.y1-self.yPos)*cosval+self.yPos])
        vertices.append([(self.x1+self.width-self.xPos)*cosval-(self.y1-self.yPos)*sinval+self.xPos,(self.x1+self.width-self.xPos)*sinval+(self.y1-self.yPos)*cosval+self.yPos])
        vertices.append([(self.x2-self.xPos)*cosval-(self.y2-self.yPos)*sinval+self.xPos,(self.x2-self.xPos)*sinval+(self.y2-self.yPos)*cosval+self.yPos])
        vertices.append([(self.x1-self.xPos)*cosval-(self.y1+self.height-self.yPos)*sinval+self.xPos,(self.x1-self.xPos)*sinval+(self.y1+self.height-self.yPos)*cosval+self.yPos])
        
        canvas.create_polygon(vertices, fill="yellow")

        