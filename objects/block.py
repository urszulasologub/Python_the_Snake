import pygame

from objects.game_object import GameObject

black = (0, 0, 0)


class Block(GameObject):

	def __init__(self, x, y, unit_width, unit_height, background):
		super(GameObject).__init__()
		self.x = x
		self.y = y
		self.width = unit_width
		self.height = unit_height
		self.background = background
		self.color = black

	def draw(self):
		pygame.draw.rect(self.background.screen, self.color, [self.x + 1, self.y + 1, self.width - 1, self.height - 1])

	def set_color(self, color):
		self.color = color

	def is_collision(self, game_object_list):
		for game_object in game_object_list:
			if self.is_collision_with_object(game_object):
				return True
		return False

	def is_collision_with_object(self, game_object):
		return game_object.has_something_collided(self.x, self.y)

	def is_collision_with_background(self):
		if self.x < self.background.block_width or \
				self.x > self.background.width - (2 * self.background.block_width):
			return True
		if self.y < self.background.block_height() or \
				self.y > self.background.height - (2 * self.background.block_height()):
			return True
		return False

	def has_something_collided(self, x, y):
		if self.x <= x < self.x + self.width:
			if self.y <= y < self.y + self.height:
				return True
		return False
