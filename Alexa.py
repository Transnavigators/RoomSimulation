class Alexa:
    """Alexa Voice Service: https://developer.amazon.com/alexa-voice-service"""
    def __init__(self):
        """initialize"""
        
        
        self.datafeed = []

    def say(self, command):
        """Process a voice command"""
        