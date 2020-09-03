import pygame

from objects.direction import Direction


class KeyboardController:

	def __init__(self, movable_object):
		self.movable_object = movable_object
		self.last_direction = Direction.UP

	def read_movement(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				self.last_direction = Direction.LEFT
			elif event.key == pygame.K_RIGHT:
				self.last_direction = Direction.RIGHT
			elif event.key == pygame.K_UP:
				self.last_direction = Direction.UP
			elif event.key == pygame.K_DOWN:
				self.last_direction = Direction.DOWN
