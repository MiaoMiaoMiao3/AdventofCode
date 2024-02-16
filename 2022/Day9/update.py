from globals import DIMENSIONS

# UPDATES
def update_relative_position(relative_position, direction, step_cnt):
	grid_mapper = { \
		"R" : [0, step_cnt],
		"L" : [0, -step_cnt],
		"U" : [1, step_cnt],
		"D" : [1, -step_cnt],
	}
	
	axis_idx = grid_mapper[direction][0]
	count = grid_mapper[direction][1]
	relative_position[axis_idx] = relative_position[axis_idx] + count

	return relative_position

def update_bounds_and_position(curr_relative_position, curr_bounds):
	#Rebaseline so that starting position 's' is always at '0' coordinates
	new_bounds = curr_bounds
	new_relative_position = curr_relative_position
	for axis_idx in range(0,DIMENSIONS):
		if new_relative_position[axis_idx] > new_bounds[axis_idx]:
			new_bounds[axis_idx] = new_relative_position[axis_idx]
		elif new_relative_position[axis_idx] < 0:
			new_bounds[axis_idx] += abs(new_relative_position[axis_idx])
			new_relative_position[axis_idx] = new_bounds[axis_idx]

	return new_relative_position, new_bounds

def update_tail_position(p1, p2):
	for idx in range(0,DIMENSIONS):
		position_difference = p1[idx] - p2[idx]
		if position_difference > 0:
			p2[idx] += 1
		else:
			p2[idx] -= 1

	return p2

def update_grid_markers(grid, tail_positions):
	for pos in tail_positions:
		x_pos = pos[0]
		y_pos = pos[1]
		print("POSITIONS", x_pos, y_pos)
		grid[x_pos][y_pos] = "#"

	return grid