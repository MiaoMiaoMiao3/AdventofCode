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
	relative_position[axis_idx] += count

	return relative_position

def update_tail_position(p2, delta_pos):
	filtered_delta_pos = dict((k, v) for k, v in delta_pos.items() if abs(v) > 0)
	step_change = 1
	for idx, delta in delta_pos.items():
			if (len(filtered_delta_pos) > 1) and \
				(2 in filtered_delta_pos.values() or -2 in filtered_delta_pos.values()):
				p2[idx] = update_position(p2[idx], step_change, delta, 0)
			elif len(filtered_delta_pos) == 1:
				p2[idx] = update_position(p2[idx], step_change, delta, 1)

	return p2

def update_position(pointer_value, step_change, delta, target_change):
	if delta > target_change:
		pointer_value += step_change
	elif delta < -target_change:
		pointer_value -= step_change

	return pointer_value

def update_grid_markers(grid, tail_position):
	x_pos = tail_position[1]
	y_pos = tail_position[0]
	grid[x_pos][y_pos] = "#"

	return grid