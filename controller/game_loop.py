import time
import pygame
import random

from assets.colors import WHITE
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

	def get_empty_tiles_array(self):
		empty_tiles = []
		bgr = self.background
		for x in range(bgr.block_width, bgr.width - bgr.block_width, bgr.block_width):
			for y in range(bgr.block_height(), bgr.height - bgr.block_height(), bgr.block_height()):
				for game_object in self.objects:
					if not game_object.has_something_collided(x, y):
						empty_tiles.append((x, y))
		return empty_tiles

	def get_random_empty_tile(self):
		return random.choice(self.get_empty_tiles_array())

	def push_object(self, obj):
		self.objects.append(obj)

	def loop(self):
		game_exit = False
		init_x, init_y = self.background.calculate_block_coordinates(int(self.background.width_blocks_count / 2),
																	 int(self.background.height_blocks_count / 2))
		snake = Snake(init_x, init_y, self.background.block_width, self.background.block_height(), self.background)
		snake.set_wait_time(1000)
		self.push_object(snake)

		rand_x, rand_y = self.get_random_empty_tile()
		fruit = Fruit(rand_x,
					  rand_y,
					  self.background.block_width,
					  self.background.block_height(),
					  self.background,
					  'assets/extras/kivi.png')
		self.push_object(fruit)
		keyboard_controller = KeyboardController(snake)
		while not game_exit:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				keyboard_controller.read_movement(event)
			if fruit.has_something_collided(snake.x, snake.y):
				fruit.x, fruit.y = self.get_random_empty_tile()
				snake.spawn_block(keyboard_controller.last_direction)
				snake.speed_up()
			snake.move(keyboard_controller.last_direction)

			self.screen.fill(WHITE)
			self.background.draw()
			for obj in self.objects:
				obj.draw()
			if snake.is_collision():
				message_center_display('Game over', self.screen, 72)
				time.sleep(5)
				break

			pygame.display.update()
			self.clock.tick(60)
