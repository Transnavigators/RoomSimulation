import threading

class LocalinoService:
    """Takes data from the environment and makes it available in the form provided by localino
    TODO: Research localino and determine what data it will give the PI
          Implement get_position
    
    """

    def __init__(self, person_tag, wheelchair_tag, anchors=[]):
        """initialize
        """
        self.anchors = anchors
        self.wheelchair_tag = wheelchair_tag
        self.person_tag = person_tag
        threading.Thread(target=self.run).start()
    
    def run(self):
        #while True:
            #do stuff
        #    pass
        pass

    def add_tag(self, tag):
        """adds a tag to the service"""
        self.tags.append(tag)
        
    def add_anchor(self, anchor):
        """adds an anchor to the service"""
        self.anchors.append(anchor)
    
    def get_person(self):
        """Gets position of person tag"""
        return self.person_tag
        
    def get_wheelchair(self):
        """Gets position of person tag"""
        return self.wheelchair_tag
    
        
class LocalinoTag:
    """Localino Tag object"""

    def __init__(self, xPos=0, yPos=0):
        """initialize
        :type xPos: integer
        :type yPos: integer
        """
        self.xPos = xPos
        self.yPos = yPos

class LocalinoAnchor:
    """Localino Anchor device"""

    def __init__(self, xPos=0, yPos=0):
        """initialize
        """
        self.xPos = xPos
        self.yPos = yPos
