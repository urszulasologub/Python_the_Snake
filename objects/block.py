import pygame

black = (0, 0, 0)


class Block:

	def __init__(self, x, y, unit_width, unit_height, screen):
		self.x = x
		self.y = y
		self.width = unit_width
		self.height = unit_height
		self.screen = screen
		self.color = black

	def draw(self):
		pygame.draw.rect(self.screen, black, [self.x + 1, self.y + 1, self.width - 1, self.height - 1])

	def move(self, x, y):
		self.x = x
		self.y = y
