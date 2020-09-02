import time

import pygame

from interface.background import Background
from objects.block import Block
from objects.direction import Direction


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
		init_x, init_y = self.background.calculate_block_coordinates(int(self.background.width_blocks_count / 2),
																	 int(self.background.height_blocks_count / 2))
		test_object = Block(init_x, init_y, self.background.block_width, self.background.block_height(), self.screen)
		test_object.set_color((100, 100, 100))
		self.push_object(test_object)
		direction = Direction.DOWN
		while not game_exit:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()

			self.screen.fill((255, 255, 255))
			self.background.draw()

			test_object.move(direction)
			if test_object.is_collision(self.background.blocks_array):
				test_object.set_color((0, 255, 0))
				direction = Direction.UP
			for obj in self.objects:
				obj.draw()

			pygame.display.update()
			self.clock.tick(60)
			time.sleep(1)
