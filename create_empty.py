grid = []
def create():
	global grid
	for i in range(1000):
		grid.append([])
		for j in range(1000):
			grid[i].append(0)
create()
#print grid