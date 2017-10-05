class Localino:
    """Takes data from the environment and makes it available in the form provided by localino
    TODO: Research localino and determine what data it will give the PI
    
    """
    def __init__(self, xPos = 0, yPos = 0, orientation = 0):
        """initialize
        positions and orientations are relative to the wheelchair
        """
        self.xPos = xPos
        self.yPos = yPos
        self.orientation = orientation
        
    