from globals import DIMENSIONS

def set_start_position():

	return [0]*DIMENSIONS

def set_grid(bounds):
	grid = []
	x_max = bounds[0]
	y_max = bounds[1]
	for i in range(0, y_max + 1):
		grid.append(["." for j in range(0, x_max + 1)])

	return grid

def set_delta_position(p1, p2):
	delta_position = {}
	for idx in range(0, DIMENSIONS):
		delta_position[idx] = p1[idx] - p2[idx]

	return delta_position