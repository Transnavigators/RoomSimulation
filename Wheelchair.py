class Wheelchair:
    """Holds all data relevant to the wheelchair"""
    def __init__(self, xPos = 0, yPos = 0, xVel = 0, yVel = 0, orientation = 0, length = 32, width = 32):
        """initialize"""
        self.length = length
        self.width = width
        self.xPos = xPos
        self.yPos = yPos
        self.xVel = xVel
        self.yVel = yVel
        self.orientation = orientation

        
    