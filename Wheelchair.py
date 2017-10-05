class Wheelchair:
    """ Represents a the wheelchair
    Note: x1, y1, x2, y2 must represent upper left corner and lower right corner of the object
    """
    def __init__(self, xPos = 0, yPos = 0, xVel = 0, yVel = 0, orientation = 0, length = 32, width = 32):
        """initialize"""
        self.length = length
        self.width = width
        self.xPos = xPos
        self.yPos = yPos
        self.xVel = xVel
        self.yVel = yVel
        self.orientation = orientation

        
    