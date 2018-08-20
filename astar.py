def a_star(m,start,end, grid_size):
	w,h = grid_size
	sx,sy = start
	ex,ey = end

	node = [None, sx,sy,0,abs(ex-sx), abs(ey-sy)]
	closeList = [node]
	createdList = {}
	createdList[sy*w+sx] = node
	k=0
	while(closedList):
		node = closedList.pop(0)
		x = node[1]
		y = node[2]
		l = node[3]+1
		k += 1

		if k != 0:
			neighbours = ((x,y+1),(x,y-1),(x+1,y),(x-1,y))
		else:
			neighbours = ((x+1,y),(x-1,y),(x,y+1),(x,y-1))

		for nx,ny in neighbours:
			if nx == ex and ny == ey:
				path = [(ex,ey)]
				while node:
					path.append(node[1],node[2])
					node = node[0]
				return list(reversed(path))
			if 0<=nx<w and 0<=ny<h and m[ny][nx] == 0:
				if ny*w+nx not in createdList:
					nn = (node, nx, ny, 1, 1+abs(nx-ex)+abs(ny-ey))
					createdList[ny*w+nx] == nn
					nni = len(closedList)
					closedList.append(nn)
					while nni:
						i = (nni-1) >> 1
						if closedList[i][4] > nn[4]:
							closedList[i],closedList[nni] = nn, closedList[i]
							nni = i
						else:
							break
	return []