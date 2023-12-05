import j2l.pytactx.agent as pytactx
import time
import random

arbitre = pytactx.Agent(playerId=input("👾 id: "),
                        arena="rattleslide",
                        username="demo",
                        password="demo",
                        server="mqtt.jusdeliens.com",
                        verbosity=2)

arbitre.ruleArena("mapImgs", ["", "https://cdn.discordapp.com/attachments/887336850719641651/1181522395509575701/fraise.png?ex=65815d7a&is=656ee87a&hm=61ad4520a6ad43c56c2f122bc0df9346e7b462dd4cf750076d4e04645bc8250b&"])

arbitre.ruleArena("mapFriction",[0.0, 0.0])

arbitre.fire(False)

def AddFoodV2(frequency):
	
	"""
	Function AddFoodV2

	Create fruits on the arena

	Arguments :

	frequency - Wanted frequency of fruits on map

	"""
	
	resetArenaFruits()
	arbitre.update()
	map = arbitre.map
	number_food_chunk = len(map)*len(map[0])*frequency
	number_food_chunk = int(number_food_chunk)
	for i in range(number_food_chunk):
		x = random.randint(0, len(map[0])-1)
		y = random.randint(0,len(map)-1)
		if map[y][x] in [0,1] :
			map[y][x] = 1
	arbitre.ruleArena('map', map)
	arbitre.update()

def AddFood(number_food_chunk):
	
	"""
	Function AddFood

 	Create a number_food_chunk fruits on the arena

	Arguments :
		
	number_food_chunk - Number of chunk of food to create, must be int

	"""
	
	resetArenaFruits()
	arbitre.update()
	map = arbitre.map
	for i in range(number_food_chunk):
		x = random.randint(0, len(map[0])-1)
		y = random.randint(0,len(map)-1)
		if map[y][x] in [0,1] :
			map[y][x] = 1
	arbitre.ruleArena('map', map)
	arbitre.update()



def setTileAsFood(x, y):
	"""
	Function setTileAsFood

 	Create a fruit at x, y coordinateq

	Arguments :
 
	x - Coordinate x of new fruit to create, must be int
 
 	y - Coordinate y of new fruit to create, must be int

	"""
	
	arbitre.update()
	map = arbitre.map
	if x < len(map[0]) and y < len(map):
		if map[y][x] == 0 :
			map[y][x] = 1
	arbitre.ruleArena('map', map)
	arbitre.update()

def destroyFruit(x, y):
	"""
	Function destroyFruit

 	Destroy fruit at x, y coordinates

	Arguments :

	x - Coordinate x of fruit to destroy, must be int

	y - Coordinate y of fruit to destroy, must be int

	"""
	
	arbitre.update()
	map = arbitre.map
	if x < len(map[0]) and y < len(map):
		if map[y][x] == 1 :
			map[y][x] = 0
	arbitre.ruleArena('map', map)
	arbitre.update()

def resetArenaFruits():
	"""
	Function resetArenaFruits

 	Destroy all fruits on the arena

	"""
	
	arbitre.update()
	map = arbitre.map
	for y in range(len(map)):
		for x in range(len(map[0])):
			if map[y][x] == 1:
				map[y][x] = 0
	arbitre.ruleArena('map', map)
	arbitre.update()

resetArenaFruits()

while True:
	AddFoodV2(0.05)
	time.sleep(25)
