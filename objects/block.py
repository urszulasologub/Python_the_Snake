import pygame

from objects.game_object import GameObject

black = (0, 0, 0)


class Block(GameObject):

	def __init__(self, x, y, unit_width, unit_height, screen):
		super(GameObject).__init__()
		self.x = x
		self.y = y
		self.width = unit_width
		self.height = unit_height
		self.screen = screen
		self.color = black

	def draw(self):
		pygame.draw.rect(self.screen, self.color, [self.x + 1, self.y + 1, self.width - 1, self.height - 1])

	def set_color(self, color):
		self.color = color

	def is_collision(self, game_object_list):
		for game_object in game_object_list:
			if self.is_collision_with_object(game_object):
				return True
		return False

	def is_collision_with_object(self, game_object):
		if game_object.x <= self.x < game_object.x + game_object.width:
			if game_object.y <= self.y < game_object.y + game_object.height:
				return True
		return False
