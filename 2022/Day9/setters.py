from globals import DIMENSIONS

def set_start_position():

	return [0]*DIMENSIONS

def set_grid(bounds):
	#TODO: would be nice to make this dynamically multi-dimensional
	x_max = bounds[0]
	y_max = bounds[1]
	grid = [["." for i in range(0, x_max)]]*y_max

	return grid

def set_delta_position(p1, p2):
	aggr_p1 = 0
	aggr_p2 = 0
	for idx in range(0, DIMENSIONS):
		aggr_p1 += p1[idx]
		aggr_p2 += p2[idx]

	return abs(aggr_p1 - aggr_p2)