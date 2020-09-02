from objects.direction import Direction


class GameObject:
	def move(self, direction):
		return {
			Direction.UP: self.move_up(),
			Direction.DOWN: self.move_down(),
			Direction.LEFT: self.move_left(),
			Direction.RIGHT: self.move_right()
		}[direction]

	def move_up(self):
		pass

	def move_down(self):
		pass

	def move_left(self):
		pass

	def move_right(self):
		pass

	def draw(self):
		pass