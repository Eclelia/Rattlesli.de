import j2l.pytactx.agent as pytactx

class ISnake:

	GAUCHE = -1
	DROITE = 1

	#Accesseurs
	def getCoordinates(self) -> tuple[int, int]:
		"""
		Return the coordinates x and y of the head of your snake
		"""

	def getDirection(self) -> int:
		"""
	    Return the direction your snake is looking at:
		 		0: Est
        1: South
        2: West
        3: North
		"""

	def getLength(self)-> int:
		"""
		Return the length of your snake
		"""

	def getFoodCoordinates(self) -> tuple[tuple[int,int]]:
		"""
			Return the x and y of every food present on the map
		"""

	def getPlayersHeads(self) -> tuple[tuple[int, int, int]]:
		"""
		 Return x and y of every players 'snakes' head on the map. 
		 Also return the length of each snakes.
		"""

	def getSegmentsPositions(self) -> tuple[tuple[int,int]]:
		"""
		 Return x and y of every segments of your own snake on the map.
		"""

#	def getRange(self) -> dict: 

	def update(self) -> None:
		"""
		Fetch the last values of player data from server and send all pending requests to the server.
		"""

	def lookAt(self, direction: int) -> None:
		"""
			Change the direction your snake is looking at.
	 		You can only turn 90° from your current direction at a time :
				-1 : to the left
				1 : to the right
		"""

class Snake(ISnake):

	def __init__(self, id, arena, username, password, server, port):
		self.__agent = pytactx.Agent(id, arena, username, password, server, port)
		self.__length = 4

	def getCoordinates(self):
		return (self.__agent.x, self.__agent.y)

	def getDirection(self):
		return self.__agent.dir

	def getLength(self):
		return self.__length

def getFoodCoordinates(self):
	res = []
	map = self.__agent.map
	for i in range (0, len(map)):
		for j in range (0, len(map[0])):
			if(map[i][j] == 2):
				res.append((i,j))
	return res

def __countlength(id):
	#used to count the length of the given snake (do not forget the head (id -1))
	pass

def getPlayersHeads(self):
	res = []
	map = self.__agent.map
	for i in range (0, len(map)):
		for j in range (0, len(map[0])):
			#if is the head of the player but isn't the texture for a wall (1)
			if(map[i][j] %2 == 1 and map[i][j] > 1): 
				length = __countlength(map[i][j] + 1)
				res.append([i,j, length]) #didn't registered the length of the snake yet
	return res
