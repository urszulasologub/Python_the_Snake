import pygame
from objects.block import Block


class Background:
	def __init__(self, screen, screen_width, screen_height, block_width):
		self.screen = screen
		self.width = screen_width
		self.height = screen_height
		self.block_width = block_width
		self.blocks_array = []
		self.width_blocks_count = 0
		self.height_blocks_count = 0;
		lowest_y = 0
		for i in range(self.block_height(), self.height - self.block_height(), self.block_height()):
			self.height_blocks_count += 1
			self.blocks_array.append(
				Block(0, i, self.block_width, self.block_height(), self.screen))
			self.blocks_array.append(
				Block(self.width - self.block_width, i, self.block_width, self.block_height(), self.screen))
			lowest_y = i + self.block_height()
		for i in range(0, self.width, self.block_width):
			self.width_blocks_count += 1
			self.blocks_array.append(
				Block(i, 0, self.block_width, self.block_height(), self.screen))
			self.blocks_array.append(
				Block(i, lowest_y, self.block_width, self.block_height(), self.screen))

	def block_height(self):
		return int((self.height / self.width) * self.block_width)

	def draw(self):
		for block in self.blocks_array:
			block.draw()

	def calculate_block_coordinates(self, width_position, height_position):
		return width_position * self.block_width, height_position * self.block_height()
