import pygame

from objects.direction import Direction


def read_keyboard(event, movable_object):
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_LEFT:
			movable_object.move(Direction.LEFT)
		elif event.key == pygame.K_RIGHT:
			movable_object.move(Direction.RIGHT)
		elif event.key == pygame.K_UP:
			movable_object.move(Direction.UP)
		elif event.key == pygame.K_DOWN:
			movable_object.move(Direction.DOWN)
