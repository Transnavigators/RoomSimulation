import tkinter
class Person:
	def __init__(self, x=0, y=0):
		"""initialize"""
		self.x = x
		self.y = y
		self.image = tkinter.PhotoImage(file="stickfigure.gif")
		self.width = self.image.width()
		self.height = self.image.height()
	def draw(self,canvas):
		canvas.create_image(self.x-self.width/2,self.y-self.height/2,image=self.image,anchor="nw")
		