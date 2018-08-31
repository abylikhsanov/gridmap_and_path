import numpy as np


def sliding_window(image, windowSize):
	step_size = windowSize[1]
	for y in range(0,image.shape[0],windowSize[0]):
		for x in range(0, image.shape[1], windowSize[1]):
			yield (x,y,image[y:y+windowSize[0], x:x+windowSize[1]])