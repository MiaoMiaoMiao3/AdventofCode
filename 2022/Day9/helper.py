from setters import set_start_position, set_delta_position, set_grid
from update import update_grid_markers, update_relative_position, \
	update_bounds_and_position, update_tail_position

def part1(input):
	series_motion = parse_input(input)
	grid = build_grid(series_motion)
	head_series_motion = find_head_motions(series_motion)
	tail_positions = find_tail_positions(grid, head_series_motion)
	grid = update_grid_markers(grid, tail_positions)
	# result = count_positions_visited(grid)
	for row in grid:
		print(row)
	return grid


# def part2(input):

# 	return result

def parse_input(input):
	series_motion = []
	for motion in input:
		direction, step_cnt = motion.split(" ")
		step_cnt = int(step_cnt)
		series_motion.append([direction, step_cnt])

	return series_motion

def build_grid(series_motion):
	grid_bounds = set_start_position()
	relative_position = set_start_position()
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
	tail_positions = [tail_position]
	for head_position in head_positions:
		delta_position = set_delta_position(head_position, tail_position)
		if delta_position <= 1:
			continue
		else:
			tail_position = update_tail_position(head_position, tail_position)
		tail_positions.append(tail_position)

	return tail_positions
