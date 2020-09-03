import time

import pygame

from controller.keyboard_controller import read_keyboard
from interface.background import Background
from objects.block import Block
from objects.direction import Direction
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
		self.push_object(snake)
		while not game_exit:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				read_keyboard(event, snake)

			self.screen.fill((255, 255, 255))
			self.background.draw()
			for obj in self.objects:
				obj.draw()
			if snake.is_collision_with_background():
				text = 'Game over'
				largeText = pygame.font.Font('freesansbold.ttf', 64)
				TextSurf, TextRect = text_objects(text, largeText)
				TextRect.center = ((self.background.width / 2), (self.background.height / 2))
				self.screen.blit(TextSurf, TextRect)

			pygame.display.update()
			self.clock.tick(60)


def text_objects(text, font):
	textSurface = font.render(text, True, (0, 0, 0))
	return textSurface, textSurface.get_rect()