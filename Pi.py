from LocalinoServer import *
from Lidor import *

class Pi:
    """Pi Controller for the wheelchair
    
    """
    def __init__(self, localino_server = LocalinoServer(), lidar = Lidar(), alexa = Alexa()):
        """initialize
        all data inputs
        """
        self.localino_server = localino_server
        self.lidar = lidar
        self.alexa = alexa
     
        
        
    