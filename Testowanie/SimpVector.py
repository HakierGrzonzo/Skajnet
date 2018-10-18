class Vector2D:
	x1 = 0
	y1 = 0
	x2 = 0
	y2 = 0
	def x:
		return self.x2 - self.x1
	def y:
		return self.y2 - self.y1
	def setx(arg):
		self.x2 = self.x1 + arg
	def sety(arg):
		self.y2 = self.y1 + arg

def Vector0:
	vec1 = Vector2D()
	vec1.x1 = 0
	vec1.x2 = 0
	vec1.y1 = 0
	vec1.y2 = 0
	return vec1

