
def part1(input):
	topography, topography_transposed = parse_input(input)
	result = find_visible_trees(topography, topography_transposed)
	return result

# def part2(input):



# HELPER FUNCTIONS

def parse_input(input):
	topography = []
	topography_transposed = [[] for i in range(len(input[1]))]
	for row in input:
		parsed_elevation = list(map(int, list(row)))
		topography.append(parsed_elevation)
		elevation_index = 0
		for elevation in parsed_elevation:
			topography_transposed[elevation_index].append(elevation)
			elevation_index += 1
	return topography, topography_transposed

def find_visible_trees(topography, topography_transposed):
	visible_tree_counter = 0
	for row_idx in range(1, len(topography) - 1):
		for col_idx in range(1, len(topography[0]) - 1):
			target_tree_height = topography[row_idx][col_idx]
			target_tree_row = topography[row_idx][0:]
			target_tree_col = topography_transposed[col_idx][0:]
			surrounding_tree_heights = find_surrounding_tree_heights(target_tree_row, target_tree_col, row_idx, col_idx)
			if is_visible(surrounding_tree_heights, target_tree_height):
				visible_tree_counter += 1
	visible_tree_counter += len(topography) * 2
	visible_tree_counter += len(topography[0]) * 2
	visible_tree_counter -= 4
	return visible_tree_counter

def find_surrounding_tree_heights(row, col, row_idx, col_idx):
	surrounding_trees = []
	# Trees left of target
	surrounding_trees.append(set(row[0:col_idx]))
	# Trees right of target
	surrounding_trees.append(set(row[col_idx + 1:len(row)]))
	# Trees above target
	surrounding_trees.append(set(col[0:row_idx]))
	# Trees below target
	surrounding_trees.append(set(col[row_idx + 1: len(col)]))
	
	return surrounding_trees

def is_visible(surrounding_trees, target_tree_height):
	max_tree_height = 9
	taller_tree_heights = set(range(target_tree_height, max_tree_height + 1))
	for trees in surrounding_trees:
			taller_trees = taller_tree_heights.intersection(trees)
			if len(taller_trees) == 0:
				return True
	return False
