import j2l.pytactx.agent as pytactx
import time
import random

arbitre = pytactx.Agent(playerId=input("👾 id: "),
                        arena="rattleslide",
                        username="demo",
                        password="demo",
                        server="mqtt.jusdeliens.com",
                        verbosity=2)

arbitre.ruleArena("mapImgs", ["", "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/3c77f9db-8565-47a2-b216-955e5b9840e9/dbpkj28-ff95a573-79e1-41bf-9540-396807ce7204.png/v1/fill/w_400,h_566/pixel_pumpkin_by_tanmo_dbpkj28-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzNjNzdmOWRiLTg1NjUtNDdhMi1iMjE2LTk1NWU1Yjk4NDBlOVwvZGJwa2oyOC1mZjk1YTU3My03OWUxLTQxYmYtOTU0MC0zOTY4MDdjZTcyMDQucG5nIiwiaGVpZ2h0IjoiPD01NjYiLCJ3aWR0aCI6Ijw9NDAwIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLndhdGVybWFyayJdLCJ3bWsiOnsicGF0aCI6Ilwvd21cLzNjNzdmOWRiLTg1NjUtNDdhMi1iMjE2LTk1NWU1Yjk4NDBlOVwvdGFubW8tNC5wbmciLCJvcGFjaXR5Ijo5NSwicHJvcG9ydGlvbnMiOjAuNDUsImdyYXZpdHkiOiJjZW50ZXIifX0.IgQBFaw1ySPYQBMiAB9mBgClLCznFzmCODo3LxR-Syk"])

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
	AddFoodV2(0.1)
	time.sleep(5)
