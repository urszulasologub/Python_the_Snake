from objects.block import Block
from objects.game_object import GameObject


class Snake(GameObject):
	def __init__(self, x, y, unit_width, unit_height, background):
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
									self.background)
							  ]

	def draw(self):
		for block in self.block_objects:
			block.draw()

	def has_something_collided(self, x, y):
		for block in self.block_objects[1:]:
			if block.has_something_collided(x, y):
				return True
		return False

	def move(self, direction):
		for block in self.block_objects:
			block.move(direction)

	def is_collision_with_background(self):
		for block in self.block_objects:
			if block.is_collision_with_background():
				return True
		return False