import threading

class Lidar:
    """Takes data from the environment and makes it available in the form provided by Lidar
    
    
    TODO: Reseach the Neato Lidar and determine in what form the data is coming
    so that this function returns information about the environment in the correct form
    """

    def __init__(self, environment, xPos=0, yPos=0, orientation=0, field_of_view=120):
        """initialize
        positions and orientations are relative to the wheelchair
        orientation is a clockwise from the verticle
        """
        
        # save the environment
        self.environment = environment
        
        # save x and y position relative to the wheelchair
        self.xPos = xPos
        self.yPos = yPos
        
        # save orientation relative to the wheelchair
        self.orientation = orientation
        
        # save the field of view
        self.field_of_view = field_of_view
        
        
        self.datafeed = []
        #threading.Thread(target=self.run).start()
    
    def run(self):
        #while True:
            #do stuff
        #    pass
        pass