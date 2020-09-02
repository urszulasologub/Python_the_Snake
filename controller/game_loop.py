import pygame

from interface.background import Background


class GameLoop:
	def __init__(self, background):
		self.background = background
		self.screen = self.background.screen
		self.objects = []
		self.clock = pygame.time.Clock()

	def push_object(self, obj):
		self.objects.append(obj)

	def loop(self):
		game_exit = False
		while not game_exit:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()

			self.screen.fill((255, 255, 255))
			self.background.draw()

			for obj in self.objects:
				obj.draw()

			pygame.display.update()
			self.clock.tick(60)
