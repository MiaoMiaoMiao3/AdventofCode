from setters import set_start_position, set_delta_position, set_grid
from update import update_grid_markers, update_tail_position

def part1(input):
	series_motion = parse_input(input)
	grid = build_grid()
	print(len(grid), len(grid[0]))
	find_head_tail_motions(grid, series_motion)
	result = count_positions_visited(grid)
	return result


# def part2(input):

# 	return result

def parse_input(input):
	series_motion = []
	for motion in input:
		direction, step_cnt = motion.split(" ")
		step_cnt = int(step_cnt)
		series_motion.append([direction, step_cnt])

	return series_motion

def build_grid():
	grid_bounds = set_start_position()
	grid = set_grid(grid_bounds)

	return grid

def find_head_tail_motions(grid, series_motion):
	head_position = set_start_position()
	tail_position = set_start_position()
	i=0
	for motion in series_motion:
		i+=1
		direction, step_cnt = motion[0], motion[1]
		for step in range(0, step_cnt):
			increment = 1
			head_position = update_relative_position(head_position, direction, increment)
			grid, tail_position = find_tail_position(grid, head_position, tail_position)
			# print(i, direction, step_cnt, step + 1, head_position, tail_position)
def find_tail_position(grid, head_position, tail_position):
	delta_position = set_delta_position(head_position, tail_position)
	tail_position = update_tail_position(head_position, tail_position, delta_position)
	grid = update_grid_markers(grid, tail_position)

	return grid, tail_position

def count_positions_visited(grid):
	visited_position_counter = 0
	for row in grid:
		for value in row:
			if value == "#":
				visited_position_counter += 1
	
	return visited_position_counter