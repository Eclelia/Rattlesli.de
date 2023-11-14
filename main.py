import j2l.pytactx.agent as pytactx
import random

arbitre = pytactx.Agent(playerId=input("👾 id: "),
						arena="rattleslide",
						username="demo",
						password="demo",
						server="mqtt.jusdeliens.com",
						verbosity=2)

arbitre.fire(False)

def AddFood(number_food_chunk):
	for i in range (number_food_chunk):
		spawn_height = random.randint(0, arbitre.gridRows)
		spawn_width = random.randint(0, arbitre.gridColumns)
		arbitre.ruleArena()


while True:
	arbitre.update()
	arbitre.lookAt((arbitre.dir + 1) % 4)