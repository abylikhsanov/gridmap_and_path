

class Node:

	def __init__(self, sx, sy, ex, ey, Node):
		self.sx = sx
		self.sy = sy
		self.ex = ex
		self.ey = ey
		self.prev_node = Node

	def heuristic(self):
		dx = abs(self.sx - self.ex)
		dy = abs(self.sy - self.ey)
		D = 1
		D_2 = sqrt(2)
		return D * (dx+dy) + (D_2 - 2*D) * min(dx,dy)

	def goal_distance(self):
		return abs(self.sx-self.ex)+abs(self.sy-self.ey)

	def successors(self, w, h):
		if (self.sx != 0 and self.sy != 0)
		


def a_star(map, start, end, grid_size):
	w,h = grid_size, grid_size
	sy,sx = start
	ey,ex = end
	node_start = Node(sx,sy,ex,ey,None)
	open_list = [node_start]
	closed_list = []
	node_current = node_start
	index = 0
	while open_list:
		lowest_cost = open_list[0].goal_distance()+open_list[0].heuristic()
		for node in open_list:
			cost = node.goal_distance()+node.heuristic()
			if lowest_cost <= cost:
				lowest_cost = cost
				node_current = node
		if node_current.sx = ex and node_current.sy = ey:
			path = [(ey,ex)]
			while node_current.prev_node != None:
				path.append((node_current.sy, node_current.sx))
				node_current = node_current.prev_node
			return list(reversed(path))
		else:
			for successor in node_current.successors(w,h):
				





