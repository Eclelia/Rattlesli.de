import j2l.pytactx.agent as pytactx

class Snake:

	GAUCHE = -1
	DROITE = 1
	
	def __init__(self, id, arena, username, password, server):
		self.__agent = pytactx.Agent(id, arena, username, password, server)

	def spawnSerpent():
		pass
		
	def lookAt(direction):
		#ne peux pas lookAt dans la direction de son corps
		pass

	def getSegmentsPositions():
		pass
