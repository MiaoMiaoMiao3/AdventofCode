# GLOBAL
DIMENSIONS = 2

def part1(input):
	series_motion = parse_input(input)
	grid = build_grid(series_motion)
	head_series_motion = find_head_motions(series_motion)
	result = find_tail_positions(grid, head_series_motion)

	return result

# def part2(input):

# 	return result


# TOP LEVEL HELPER FUNCTIONS
def parse_input(input):
	series_motion = []
	for motion in input:
		direction, step_cnt = motion.split(" ")
		step_cnt = int(step_cnt)
		series_motion.append([direction, step_cnt])
	return series_motion

def build_grid(series_motion):
	grid_bounds = set_start_position(DIMENSIONS)
	relative_position = set_start_position(DIMENSIONS)
	for motion in series_motion:
		direction, step_cnt = motion[0], motion[1]
		relative_position = update_relative_position(relative_position, direction, step_cnt)
		relative_position, grid_bounds = update_bounds_and_position(relative_position, grid_bounds)
	grid = set_grid(grid_bounds)
	return grid

#Pretty duplicative of 'build_grid'
def find_head_motions(series_motion):
	grid_bounds = set_start_position()
	relative_position = set_start_position()
	head_series_motion = [set_start_position()]
	for motion in series_motion:
		direction, step_cnt = motion[0], motion[1]
		relative_position = update_relative_position(relative_position, direction, step_cnt)
		relative_position, grid_bounds = update_bounds_and_position(relative_position, grid_bounds)
		head_series_motion.append(relative_position)
	return head_series_motion

def find_tail_positions(grid, head_positions):
	tail_position = set_start_position()
	for motion in head_positions:
		print("test")
	return tail_position


# SETTERS
def set_start_position():
	return [0]*DIMENSIONS

def set_grid(bounds):
	#TODO: would be nice to make this dynamically multi-dimensional
	x_max = bounds[0]
	y_max = bounds[1]
	grid = [["." for i in range(0, x_max)]]*y_max
	return grid

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
