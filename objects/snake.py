import random
import pygame

from objects.block import Block
from objects.direction import Direction
from objects.game_object import GameObject


class Snake(GameObject):

	def __init__(self, x, y, unit_width, unit_height, background, wait_time=0):
		super(GameObject).__init__()
		self.x = x
		self.y = y
		self.width = unit_width
		self.height = unit_height
		self.background = background
		self.block_objects = [Block(self.x,
									self.y,
									self.width,
									self.height,
									self.background)]

		pygame.time.Clock()
		self.last_move_time = 0
		self.wait_time = wait_time

	def draw(self):
		for block in self.block_objects:
			block.draw()

	def has_something_collided(self, x, y):
		for block in self.block_objects:
			if block.has_something_collided(x, y):
				return True
		return False

	def move(self, direction):
		time = pygame.time.get_ticks()
		if time > self.last_move_time + self.wait_time:
			self.spawn_block(direction)
			for block in self.block_objects:
				block.move(direction)
			#for i in range(1, len(self.block_objects)):

			self.last_move_time = time

	def is_collision_with_background(self):
		for block in self.block_objects:
			if block.is_collision_with_background():
				return True
		return False

	def set_wait_time(self, wait_time):
		self.wait_time = wait_time

	def spawn_block(self, direction):
		block_x = self.block_objects[-1].x
		block_y = self.block_objects[-1].y
		if direction == Direction.LEFT:
			block_x += self.width
		elif direction == Direction.RIGHT:
			block_x -= self.width
		elif direction == Direction.UP:
			block_y += self.height
		elif direction == Direction.DOWN:
			block_y -= self.height
		block = Block(block_x, block_y, self.width, self.height, self.background)
		block.set_color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
		self.block_objects.append(block)
