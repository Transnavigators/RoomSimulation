import tkinter
from Localino import *

class Person:
    """Represents a physical person
    Note: x1, y1, x2, y2 must represent upper left corner and lower right corner of the object
    """

    def __init__(self, localino_tag, x=0, y=0):
        """initialize variables:
        localino_tag is the tag connected to the person
        x,y are the center position of the person"""
        
        # save the localino tag
        self.localino_tag = localino_tag
        
        # upload image and get the width and height for the person
        self.image = tkinter.PhotoImage(file="stickfigure.gif")
        self.width = self.image.width()
        self.height = self.image.height()
        

        # default values for the boundaries of the person
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
        
        # update the boundaries of the person
        self.set_pos(x, y)

    def draw(self, canvas):
        canvas.create_image(self.x1, self.y1, image=self.image, anchor="nw")

    def set_pos(self, x, y):
        """Changes the person's position to be centered around x,y"""
        # update person's position
        self.x1 = x - self.width / 2
        self.y1 = y - self.height / 2
        self.x2 = x + self.width / 2
        self.y2 = y + self.height / 2
        
        # update localino_tag's position
        self.localino_tag.xPos = x
        self.localino_tag.yPos = y
