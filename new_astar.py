import math

class Node:

	def __init__(self, y, x, Node):
		self.y = y
		self.x = x
		self.prev_node = Node
		self.g = 0
		self.h = 0
		self.f = 0

	def heuristic(self, ey, ex):
		dx = abs(self.x - ex)
		dy = abs(self.y - ey)
		D = 1
		D_2 = math.sqrt(2)
		return D * (dx+dy) + (D_2 - 2*D) * min(dx,dy)

	def goal_distance(self, ey, ex):
		return abs(self.x-ex)+abs(self.y-ey)

	


def a_star(map, start, end, grid_size):
	w,h = grid_size, grid_size
	sy,sx = start
	ey,ex = end
	node_start = Node(sy,sx,None)
	node_start.g = node_start.goal_distance(ey,ex)
	node_start.h = node_start.heuristic(ey,ex)
	node_start.f = node_start.g+node_start.h
	node_end = Node(ey,ex,None)
	open_list = [node_start]
	closed_list = []
	lowest_cost = open_list[0].f

	while len(open_list)>0:
		current_index = 0
		node_current = open_list[0]

		for index, node in enumerate(open_list):
			if node.f < node_current.f:
				node_current = node
				current_index = index

		if node_current.x == ex and node_current.y == ey:
			path = [(ey,ex)]
			while node_current.prev_node is not None:
				path.append((node_current.y, node_current.x))
				node_current = node_current.prev_node
			return list(reversed(path))

		open_list.pop(current_index)
		closed_list.append(node_current)
		children = []
		for (y,x) in [(0,-1),(0,1),(-1,0),(1,0),(-1,-1),(-1,1),(1,-1),(1,1)]:

			# Getting coordinates of a current node successor
			successor = (node_current.y + y, node_current.x + x)

			# Checking that the move is legitimate:
			if successor[0] > h-1 or successor[0] < 0 or successor[1] > w-1 or successor[1] < 0:
				continue

			# Also checking that the next move is not an obstacle:
			if map[y][x] == 1:
				continue

			for closed_node in closed_list:
				if closed_node.x == successor[1] and closed_node.y == successor[0]:
					continue

			for open_node in open_list:
				if open_node.y == successor[0] and open_node.x == successor[1]:
					continue
			node_successor = Node(successor[0], successor[1], node_current)
			node_successor.g = node_current.g+1
			node_successor.h = node_successor.heuristic(ey,ex)
			node_successor.f = node_successor.g+node_successor.h
			open_list.append(node_successor)


		'''	# Loop through chlidren (current node successors)
		for child in children:
			for closed_node in closed_list:
				if child.y == closed_node.y and child.x == closed_node.x:
					continue

			child.g = node_current.g + 1
			child.h = child.heuristic(ey,ex)
			child.f - child.g+child.h

				# Check if child is already in the open list
			for open_node in open_list:
				if (child.x == open_node.x and child.y == open_node.y) or child.g > open_node.g:

					continue

				# After exploring the child (successor) add it to the open list
			open_list.append(child) '''
	return []

