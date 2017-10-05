import tkinter
class Person:
    """Represents a physical person
    Note: x1, y1, x2, y2 must represent upper left corner and lower right corner of the object
    """
    def __init__(self, x=0, y=0):
        """initialize"""
        
        self.image = tkinter.PhotoImage(file="stickfigure.gif")
        
        self.width = self.image.width()
        self.height = self.image.height()
        
        self.set_pos(x,y)
        
    def draw(self,canvas):
        canvas.create_image(self.x1,self.y1,image=self.image,anchor="nw")
        
    def set_pos(self, x, y):
        self.x1 = x - self.width/2
        self.y1 = y - self.height/2
        self.x2 = x + self.width/2
        self.y2 = y + self.height/2
        