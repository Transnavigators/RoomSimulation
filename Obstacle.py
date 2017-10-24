class Obstacle:
    """Represents an obstacle
    Note: x1, y1, x2, y2 must represent upper left corner and lower right corner of the object
    """

    def __init__(self, x1=0, y1=0, x2=10, y2=10, color="black"):
        """initialize the obstacle
        x1,y1 is the upper left hand position of the obstacle
        x2,y2 is the lower right hand position of the obstacle
        color is the color of the object
        """
        self.x1 = min(x1,x2)
        self.y1 = min(y1,y2)
        self.x2 = max(x1,x2)
        self.y2 = max(y1,y2)
        self.color = color

    def draw(self, canvas):
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill=self.color)