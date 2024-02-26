import setters
from update import update_grid_markers, update_relative_position, update_tail_position

def part1(input):
	register_value = setters.set_register_value()
	signal_strength = find_signal_strength(input, register_value)
	start_position = set_start_position(series_motion)
	grid = build_grid()
	no_of_knots = 1
	find_head_tail_motions(grid, series_motion, start_position, no_of_knots)
	result = count_positions_visited(grid)
	return result

def find_signal_strength(input, register_value):
	register_tracker = {}


	return series_motion
