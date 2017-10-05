class Lidar:
    """Takes data from the environment and makes it available in the form provided by Lidar
    
    This is a service which 
    
    TODO: Reseach the Neato Lidar and determine in what form the data is coming
    so that this function returns information about the environment in the correct form
    """
    def __init__(self, xPos = 0, yPos = 0, orientation = 0, field_of_view = 120):
        """initialize
        positions and orientations are relative to the wheelchair
        """
        self.xPos = xPos
        self.yPos = yPos
        self.orientation = orientation
        self.field_of_view = field_of_view
    