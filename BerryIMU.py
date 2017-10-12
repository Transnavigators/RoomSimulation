class BerryIMU:
    """BerryIMU sensor: http://ozzmaker.com/product/berryimu-accelerometer-gyroscope-magnetometer-barometricaltitude-sensor/"""
    def __init__(self, wheelchair):
        """initialize"""
        # save the environment
        self.wheelchair = wheelchair
        
        
        self.datafeed = []
    