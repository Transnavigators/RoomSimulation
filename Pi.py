from LocalinoService import *
from Lidar import *
from Alexa import *

class Pi:
    """Pi Controller for the wheelchair
    
    """
    def __init__(self, localino_service = LocalinoService(), lidar = Lidar(), alexa = Alexa()):
        """initialize
        all data inputs
        """
        self.localino_service = localino_service
        self.lidar = lidar
        self.alexa = alexa
     
        
        
    