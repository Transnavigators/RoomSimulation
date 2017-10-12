class Obstacle:
    """Represents an obstacle
    Note: x1, y1, x2, y2 must represent upper left corner and lower right corner of the object
    """

    def __init__(self, x1=0, y1=0, x2=10, y2=10, color="black"):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
