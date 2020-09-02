import pygame

from objects.game_object import GameObject

black = (0, 0, 0)


class Block(GameObject):

	def __init__(self, x, y, unit_width, unit_height, screen):
		self.x = x
		self.y = y
		self.width = unit_width
		self.height = unit_height
		self.screen = screen
		self.color = black

	def draw(self):
		pygame.draw.rect(self.screen, self.color, [self.x + 1, self.y + 1, self.width - 1, self.height - 1])

	def move_up(self):
		self.y -= self.height

	def move_down(self):
		self.y += self.height

	def move_left(self):
		self.x -= self.width

	def move_right(self):
		self.x += self.width

	def set_color(self, color):
		self.color = color
