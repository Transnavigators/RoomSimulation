class Wheelchair:
    """ Represents a the wheelchair
    Note: x1, y1, x2, y2 must represent upper left corner and lower right corner of the object
    """
    def __init__(self, xc = 50, yc = 50, xVel = 0, yVel = 0, orientation = 0, length = 32, width = 32, mass = 300, wheels=((32,0),(32,16))):
        """initialize"""
        self.length = length
        self.width = width
        self.mass = mass
        self.x1= xc - width/2
        self.y1= yc - length/2
        self.x2= xc + width/2
        self.y2= yc + length/2
        
        self.xVel = xVel
        self.yVel = yVel
        self.orientation = orientation

    def draw(self, canvas):
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill="yellow")
    