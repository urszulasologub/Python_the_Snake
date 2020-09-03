import time

import pygame

from controller.keyboard_controller import KeyboardController
from interface.captions import message_center_display
from objects.fruit import Fruit
from objects.snake import Snake


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
		snake = Snake(init_x, init_y, self.background.block_width, self.background.block_height(), self.background)
		snake.set_wait_time(1000)

		fruit = Fruit(init_x + snake.width,
					  init_y + snake.height,
					  self.background.block_width,
					  self.background.block_height(),
					  self.background,
					  'assets/extras/kivi.png')
		self.push_object(fruit)
		self.push_object(snake)
		keyboard_controller = KeyboardController(snake)
		while not game_exit:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				keyboard_controller.read_movement(event)
			snake.move(keyboard_controller.last_direction)

			self.screen.fill((255, 255, 255))
			self.background.draw()
			for obj in self.objects:
				obj.draw()
			if snake.is_collision_with_background():
				message_center_display('Game over', self.screen, 72)
				time.sleep(5)
				break

			pygame.display.update()
			self.clock.tick(60)
