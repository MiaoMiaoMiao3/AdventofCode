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

def update_tail_position(p1, p2, delta_pos):
	# if delta_axis > 1 then iterate through delta axis and add or subtract 1
	# if delta_axis = 1 then if difference is greater than 1, add/subtract 1
	unique_delta_pos_list = list(filter(lambda x: abs(x) > 0, delta_pos.values()))
	unique_delta_pos_set = set(filter(lambda x: abs(x) > 0, delta_pos.values()))
	print("UNIQUE", delta_pos.keys(), unique_delta_pos_list)
	for idx, delta in delta_pos.items():
			if (len(unique_delta_pos_list) > 1) and (2 in unique_delta_pos_set or -2 in unique_delta_pos_set):
				if delta > 0:
					p2[idx] += 1
				elif delta < 0:
					p2[idx] -= 1
			elif len(unique_delta_pos_list) == 1:
				if delta > 1:
					p2[idx] += 1
				elif delta < -1:
					p2[idx] -=1
	return p2

def update_grid_markers(grid, tail_position):
	x_pos = tail_position[1]
	y_pos = tail_position[0]
	grid[x_pos][y_pos] = "#"

	return grid