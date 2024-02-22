from globals import DIMENSIONS
from update import update_relative_position

def set_start_position(series_motion):
	start_position = [0]*DIMENSIONS
	for direction, step_cnt in series_motion:
		start_position = update_relative_position(start_position, direction, step_cnt)
		for idx, val in enumerate(start_position):
			if val < 0:
				start_position[idx] += abs(val)

	print("START", start_position)
	return start_position

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