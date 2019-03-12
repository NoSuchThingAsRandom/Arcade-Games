MAX_SIZE= 2
dimensions=4


def print_grid(dims,grid):
    global dimensions
    if dims==0:
        print("		"*(dimensions)+str(grid))
    else:
        print("		"*(dimensions-dims)+"Printing dimensions "+str(dims))
        for x in range(0,MAX_SIZE):
            print_grid(dims-1,grid[x])

			
def count_neighbours(dims,coords):
	global dimensions
	adjust=[-1, 0, 1]
	neighbours=[]
	
    
	if dims==0:
        print("		"*(dimensions)+str(grid))
    else:
        for x in range(0,MAX_SIZE):
            count_neighbours(dims-1,coords[x])
	
	for c in coords:
		for a in adjust:
			
			
def main():
	grid=[]
	for x in range(0,MAX_SIZE):
		grid.append(False)


	for dims in range(1,dimensions):
		new=[]
		for x in range(0,MAX_SIZE):
			new.append(grid)


		grid=new
	print_grid(dimensions,grid)



