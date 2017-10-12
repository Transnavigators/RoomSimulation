
class LocalinoService:
    """Takes data from the environment and makes it available in the form provided by localino
    TODO: Research localino and determine what data it will give the PI
          Implement get_position
    
    """

    def __init__(self, anchors=[], tags=[]):
        """initialize
        """
        self.anchors = anchors
        self.tags = tags

    def add_tag(tag):
        """adds a tag to the service"""
        self.tags.append(tag)
        
    def add_anchor(anchor):
        """adds an anchor to the service"""
        self.anchors.append(anchor)
    
    def get_position(tag):
        """Gets position of specified tag"""
    
        
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
