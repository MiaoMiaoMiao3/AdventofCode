def part1(input):
	dimensions = 2
	grid = build_grid(input, dimensions)
	result = grid

	return result

# def part2(input):

# 	return result


# HELPER FUNCTIONS

def build_grid(input, dimensions):
	grid_bounds = [0]*dimensions
	relative_position = [0]*dimensions # x, y position for now
	for motion in input:
		direction, step_cnt = motion.split(" ")
		relative_position = update_relative_position(relative_position, direction, int(step_cnt))
		relative_position, grid_bounds = update_bounds_and_position(relative_position, grid_bounds, dimensions)
	grid = set_grid(grid_bounds, dimensions)
	return grid

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

def update_bounds_and_position(curr_relative_position, curr_bounds, dimensions):
	#Rebaseline so that starting position 's' is always at '0' coordinates
	new_bounds = curr_bounds
	new_relative_position = curr_relative_position
	for axis_idx in range(0,dimensions):
		if new_relative_position[axis_idx] > new_bounds[axis_idx]:
			new_bounds[axis_idx] = new_relative_position[axis_idx]
		elif new_relative_position[axis_idx] < 0:
			new_bounds[axis_idx] += abs(new_relative_position[axis_idx])
			new_relative_position[axis_idx] = new_bounds[axis_idx]
	return new_relative_position, new_bounds

def set_grid(bounds, dimensions):
	#TODO: would be nice to make this dynamically multi-dimensional
	x_max = bounds[0]
	y_max = bounds[1]
	print(x_max, y_max)
	grid = [["." for i in range(0, x_max)]]*y_max
	return grid