import abc

from objects.direction import Direction


class GameObject:

	def move(self, direction):
		return {
			Direction.UP: self.move_up,
			Direction.DOWN: self.move_down,
			Direction.LEFT: self.move_left,
			Direction.RIGHT: self.move_right
		}[direction]()

	def move_up(self):
		self.y -= self.height

	def move_down(self):
		self.y += self.height

	def move_left(self):
		self.x -= self.width

	def move_right(self):
		self.x += self.width

	@abc.abstractmethod
	def draw(self):
		pass
