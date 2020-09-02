import time

import pygame

from interface.background import Background
from objects.block import Block


class GameLoop:
	def __init__(self, background):
		self.background = background
		self.screen = self.background.screen
		self.objects = []
		self.clock = pygame.time.Clock()

	def push_object(self, obj):
		self.objects.append(obj)

	def loop(self):
		game_exit = False
		test_object = Block(0, 0, self.background.block_width, self.background.block_height(), self.screen)
		test_object.set_color((100, 100, 100))
		self.push_object(test_object)
		while not game_exit:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()

			self.screen.fill((255, 255, 255))
			self.background.draw()

			test_object.move_right()

			for obj in self.objects:
				obj.draw()

			pygame.display.update()
			self.clock.tick(60)
			time.sleep(1)
