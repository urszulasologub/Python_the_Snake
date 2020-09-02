import pygame
from controller.game_loop import GameLoop
from interface.background import Background


if __name__ == '__main__':
	pygame.init()
	map_width = 500
	map_height = 600
	screen = pygame.display.set_mode((map_width, map_height))
	pygame.display.set_caption('Python The Snake!')
	game = GameLoop(Background(screen, map_width, map_height, int(map_width / 20)))
	game.loop()
