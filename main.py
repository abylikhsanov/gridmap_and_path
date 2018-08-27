import cv2
import numpy as np
import time
import matplotlib.pyplot as plt


import astar

def sliding_window(image, windowSize):
	step_size = windowSize[1]
	for y in range(0,image.shape[0],windowSize[0]):
		for x in range(0, image.shape[1], windowSize[1]):
			yield (x,y,image[y:y+windowSize[0], x:x+windowSize[1]])

def main(image_filename, image_grids=60):

	occupied_grids = []
	planned_path = {}
	obstacles = []

	image = cv2.imread(image_filename)
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	image = cv2.resize(image, (1200,1200))
	#plt.imshow(image)
	#plt.show()
	(winH, winW) = (int(image.shape[0]/image_grids), int(image.shape[1]/image_grids))
	print(winH,winW)
	index = [1,1] # Robot starting point, FIXED

	blank_image = np.zeros((winW,winH,3), np.uint8)
	list_images = [[blank_image for i in range(image_grids)] for i in range(image_grids)] # Creates winWxwinH
	maze = [[0 for i in range(image_grids)] for i in range(image_grids)]

	for(x,y, window) in sliding_window(image, windowSize=(winH, winW)):

		image_clone = image.copy()
		cv2.rectangle(image_clone, (x,y), (x+winW, y+winH), (255,255,255), 2)
		cropped_image = image_clone[y:y+winH, x:x+winW]
		list_images[index[0]-1][index[1]-1] = cropped_image.copy()
		average_color_row = np.average(cropped_image, axis=0)
		average_color = np.average(average_color_row, axis=0)
		#average_color = np.uint8(average_color)

		
		if(average_color[2] > average_color[1] and average_color[2] > average_color[0]):
			#print("Occupied")
			#print(index)
			#print(x,y)
			occupied_grids.append(tuple(index))
			#plt.imshow(image_clone, interpolation='bicubic')
			#plt.xticks([])
			#plt.yticks([])
			#plt.show()

			'''  Index at [5,41] -> [832, 80] and [6,42] -> [858,100]   '''
		  	
		elif(average_color[1] < 225 and average_color[2] < 225):
			maze[index[1]-1][index[0]-1] = 1
			obstacles.append(tuple(index))
		
		#time.sleep(0.025)


		index[1] += 1
		if(index[1] > image_grids):
			index[0] += 1
			index[1] = 1

		if(index[0] > image_grids):
			break

	points = [i for i in occupied_grids]

	start_point = points[0]
	end_point = points[-1]
	#print(start_point, end_point)
	#image_clone = image.copy()
	#nx = start_point[1]*winW
	#ny = start_point[0]*winH
	#cv2.rectangle(image_clone, (nx,ny), (nx+winW, ny+winH), (244,0,0), 2)
	#plt.imshow(image_clone)
	#plt.show()



	result = astar.a_star(maze, (start_point[0]-1,start_point[1]-1),(end_point[0]-1,end_point[1]-1), image_grids)
	print(obstacles) # SOMETHING is wrong!! A star takes obstacles
	print(result)
	image_clone = image.copy()
	for (x,y) in result: # Visualize the path
		y_start = y*winH  # [5,41] -> 5 * 20 = 100
		x_start = x*winW
		cv2.rectangle(image_clone, (y_start,x_start), (y_start+winW, x_start+winH), (255,0,0), 2)
		#plt.imshow(image_clone)
		#plt.show()
	plt.imshow(image_clone)
	plt.show()

if __name__ == "__main__":

	image_name = "floor.png"
	main(image_name)

	#cv2.waitKey(0)
	#v2.destroyAllWindows()





