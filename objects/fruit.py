import pygame

from objects.block import Block


class Fruit(Block):

	def __init__(self, x, y, unit_width, unit_height, background, image):
		super().__init__(x, y, unit_width, unit_height, background)
		self.unit_width = unit_width
		self.unit_height = unit_height
		self.image = pygame.image.load(image)
		self.scale_image()

	def scale_image(self):
		unit_width = self.unit_width
		unit_height = self.unit_height
		if unit_width > unit_height:
			self.image = pygame.transform.scale(self.image,
												(unit_width,
												 int(self.image.get_height() / (self.image.get_width() / unit_width))))
		else:
			self.image = pygame.transform.scale(self.image,
												(int(self.image.get_width() / (self.image.get_height() / unit_height)),
												 unit_height))

	def set_image(self, image_path):
		self.image = pygame.image.load(image_path)
		self.scale_image()

	def draw(self):
		self.background.screen.blit(self.image, (self.x, self.y))
