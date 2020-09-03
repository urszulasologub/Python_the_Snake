import os
import random


def get_all_fruits_images_names(directory):
	file_list = os.listdir(directory)
	for file in file_list[:]:
		if not file.endswith(".png"):
			file_list.remove(file)
	return file_list


def get_random_fruit_image_path(directory):
	return directory + '/' + random.choice(get_all_fruits_images_names(directory))

