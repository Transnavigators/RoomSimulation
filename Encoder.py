import threading

class Encoder:
    """Encoder sensor for the wheelchair
    """

    def __init__(self, wheelchair):
        """initialize"""
        # save the wheelchair
        self.wheelchair = wheelchair

        self.datafeed = []
        #threading.Thread(target=self.run).start()
    
    def run(self):
        #while True:
            #do stuff
        #    pass
        pass