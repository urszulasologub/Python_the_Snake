import pygame

black = (0, 0, 0)


def text_objects(text, font):
	text_surface = font.render(text, True, black)
	return text_surface, text_surface.get_rect()


def message_center_display(text, screen, font_size):
	large_text = pygame.font.Font('freesansbold.ttf', font_size)
	text_surf, text_rect = text_objects(text, large_text)
	text_rect.center = ((screen.get_width() / 2), (screen.get_height() / 2))
	screen.blit(text_surf, text_rect)
	pygame.display.update()
