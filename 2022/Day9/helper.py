from setters import set_start_position, set_delta_position, set_grid
from update import update_grid_markers, update_relative_position, update_tail_position

def part1_2(input):
	series_motion = parse_input(input)
	start_position = set_start_position(series_motion)
	grid = build_grid()
	no_of_knots = 1
	find_head_tail_motions(grid, series_motion, start_position, no_of_knots)
	result = count_positions_visited(grid)
	return result

def parse_input(input):
	series_motion = []
	for motion in input:
		direction, step_cnt = motion.split(" ")
		step_cnt = int(step_cnt)
		series_motion.append([direction, step_cnt])

	return series_motion

def build_grid():
	grid = set_grid()

	return grid

def find_head_tail_motions(grid, series_motion, start_position, no_of_knots):
	head_position = start_position[:]
	tail_position = []
	for i in range (0,no_of_knots):
		tail_position.append(start_position[:])
	increment = 1
	for motion in series_motion:
		direction, step_cnt = motion[0], motion[1]
		for step_idx in range(0, step_cnt):
			head_position = update_relative_position(head_position, direction, increment)
			for i in range (0,no_of_knots):
				if i == 0:
					tail_position[i] = find_tail_position(head_position, tail_position[i])
				else:
					tail_position[i] = find_tail_position(tail_position[i-1], tail_position[i])
			grid = update_grid_markers(grid, tail_position[len(tail_position) - 1])

def find_tail_position(head_position, tail_position):
	delta_position = set_delta_position(head_position, tail_position)
	tail_position = update_tail_position(tail_position, delta_position)

	return tail_position

def count_positions_visited(grid):
	visited_position_counter = 0
	for row in grid:
		for value in row:
			if value == "#":
				visited_position_counter += 1
	
	return visited_position_counter