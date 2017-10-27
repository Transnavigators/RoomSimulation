import threading
import time
import random
import math

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

        #Initialize datafeed with size 360
        self.datafeed = [0]*360
        threading.Thread(target=self.run).start()
    
    def run(self):
        while not hasattr(self.environment,'wheelchair'):
            print('waiting for wheelchair to be created')
            time.sleep(1/1000)
        angle = random.randint(0,360)
        while True:
            angle_rad = math.radians(angle)
            d = math.inf
            for obstacle in self.environment.obstacles:
                x1 = self.environment.wheelchair.xPos
                y1 = self.environment.wheelchair.yPos
                x2 = x1+100*math.cos(angle_rad)
                y2 = y1-100*math.sin(angle_rad)
                line = (x1,y1,x2,y2)
                new_d = self.environment.line_rect_intersection(line,obstacle)
                if new_d != 0:
                    d = min(d,new_d)
            if math.isinf(d):
                d = 0
            self.datafeed[angle] = d
            # f = 10Hz, 360 samples per rotation
            angle = (angle + 1) % 360
            time.sleep(1 / (360 * 10))