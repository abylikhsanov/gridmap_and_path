import cv2
import numpy as np
import time
import matplotlib.pyplot as plt


import astar

def sliding_window(image, windowSize=60):
	step_size = windowSize[1]
	for y in range(0,image.shape[1],windowSize[0]):
		for x in range(0, image.shape[0], windowSize[1]):
			yield (x,y,image[y:y+windowSize[0], x:x+windowSize[1]])

def main(image_filename, image_grids=10):

	occupied_grids = []
	planned_path = {}

	image = cv2.imread(image_filename)
	(winH, winW) = (int(image.shape[0]/image_grids), int(image.shape[1]/image_grids))

	index = [1,1] # Robot starting point, FIXED

	blank_image = np.zeros((winW,winH,3), np.uint8)
	list_images = [[blank_image for i in range(winW) for i in range(winH)]] # Creates winWxwinH
	print(len(list_images))
	maze = [[0 for i in range(winW) for i in range(winH)]]

	for(x,y, window) in sliding_window(image, windowSize=(winH, winW)):

		image_clone = image.copy()
		cv2.rectangle(image_clone, (x,y), (x+winW, y+winH), (255,0,0), 2)
		cropped_image = image_clone[x:x+winW, y:y+winH]
		list_images[index[0]-1][index[1]-1] = cropped_image.copy()

		average_color_row = np.average(cropped_image, axis=1)
		average_color = np.average(average_color_row, axis=0)
		average_color = np.uint8(average_color)

		if(any(i <= 240 for i in average_color)):
			maze[index[0]-1][index[1]-1] = 1
			occupied_grids.append(tuple(index))
		if(any(i <= 20 for i in average_color)):
			obstacles.append(tuple(index))

		#plt.imshow(image_clone, cmap='gray', interpolation='bicubic')
		#plt.xticks([])
		#plt.yticks([])
		#plt.show()
		#time.sleep(0.025)

		index[1] += 1
		if(index[1] > image_grids):
			index[0] += 1
			index[1] = 1

	points = [i for i in occupied_grids if i not in obstacles]

	start_point = points[0]
	end_point = points[-1]

	result = astar.a_star(maze, (start_point[0]-1,start_image[1]-1),(end_point[0]-1,end_point[1]-1))

if __name__ == "__main__":

	image_name = "test_image1.jpg"
	main(image_name)

	cv2.waitKey(0)
	cv2.destroyAllWindows()





