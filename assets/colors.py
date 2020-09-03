import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
DARK_RED = (150, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


def random_color():
	return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def random_green():
	return 0, random.randint(100, 255), 0
