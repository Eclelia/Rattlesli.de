from src.api.rattleslide import Snake

import src.api.rattleslide as rattle
'''construction d/'un serpent'''
snake = rattle.Snake(id="demo",
                     arena="rattleslide ",
                     username="TEST",
                     password="demo",
                     server="mqtt.jusdel")


def test_spawnSerpent():
  '''test si un serpent apparait bien dans les limites de la carte
  '''
  x, y = snake.getCoordinates()
  assert 0 <= x < 30 and 0 <= y < 30, f"le serpent n'apparait pas dans les limites de la carte x={x} et y={y}"


def test_lookAt():
  '''test de la fonction lookAt'''

  #cas de test 2


def test_getSegmentsPositions():
  '''test de la fonction getSegmentsPositions'''
  #cas de test 1

  #cas de test 2
