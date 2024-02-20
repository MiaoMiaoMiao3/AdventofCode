from globals import DIMENSIONS

def set_start_position():

	return [0]*DIMENSIONS

def set_grid():
	# Make life easier -- set up grid to be a super large value instead of trying to set exact grid size
	grid = []
	for i in range(0, 500):
		grid.append(["." for j in range(0, 500)])

	return grid

def set_delta_position(p1, p2):
	delta_position = {}
	for idx in range(0, DIMENSIONS):
		delta_position[idx] = p1[idx] - p2[idx]

	return delta_position