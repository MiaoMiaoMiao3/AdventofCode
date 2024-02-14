def part1(input):
	topography, topography_transposed = parse_input(input)
	result = find_visible_trees(topography, topography_transposed)

	return result

def part2(input):
	topography, topography_transposed = parse_input(input)
	result = find_most_scenic_score(topography, topography_transposed)

	return result


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
	# All edge trees are visible
	visible_tree_counter = len(topography) + len(topography[0]) - 4
	for row_idx in range(1, len(topography) - 1):
		for col_idx in range(1, len(topography[0]) - 1):

			target_tree_height, target_tree_row, target_tree_col = \
			find_target_data(topography, topography_transposed, row_idx, col_idx)

			surrounding_tree_heights = find_surrounding_tree_heights_set( \
			target_tree_row, target_tree_col, row_idx, col_idx)

			if is_visible(surrounding_tree_heights, target_tree_height):
				visible_tree_counter += 1

	return visible_tree_counter

def find_target_data(topography, topography_transposed, row_idx, col_idx):
	target_tree_height = topography[row_idx][col_idx]
	target_tree_row = topography[row_idx][0:]
	target_tree_col = topography_transposed[col_idx][0:]
	return target_tree_height, target_tree_row, target_tree_col

def find_surrounding_tree_heights_set(row, col, row_idx, col_idx):
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

def find_surrounding_tree_heights_map(row, col, row_idx, col_idx):
	surrounding_trees = {}
	surrounding_trees["left"] = (row[0:col_idx])
	surrounding_trees["right"] = row[col_idx + 1:len(row)]
	surrounding_trees["above"] = col[0:row_idx]
	surrounding_trees["below"] = col[row_idx + 1: len(col)]
	return surrounding_trees

def is_visible(surrounding_trees, target_tree_height):
	max_tree_height = 9
	taller_tree_heights = set(range(target_tree_height, max_tree_height + 1))
	for trees in surrounding_trees:
			taller_trees = taller_tree_heights.intersection(trees)
			if len(taller_trees) == 0:
				return True

	return False

def find_most_scenic_score(topography, topography_transposed):
	max_scenic_score = 0
	for row_idx in range(1, len(topography) - 1):
		for col_idx in range(1, len(topography[0]) - 1):

			target_tree_height, target_tree_row, target_tree_col = \
			find_target_data(topography, topography_transposed, row_idx, col_idx)

			surrounding_tree_heights = find_surrounding_tree_heights_map( \
			target_tree_row, target_tree_col, row_idx, col_idx)
			target_tree_scenic_score = find_scenic_score(target_tree_height, surrounding_tree_heights)
			if target_tree_scenic_score > max_scenic_score:
				max_scenic_score = target_tree_scenic_score

	return max_scenic_score

def find_scenic_score(target_tree_height, surrounding_tree_heights):
	scenic_score = 1
	for direction, trees in surrounding_tree_heights.items():
		# Need to start search from inside out relative to target tree
		if direction == "left" or direction == "above":
			start_idx = len(trees) - 1
			end_idx = -1
			increment = -1
		else:
			start_idx = 0
			end_idx = len(trees)
			increment = 1

		visible_tree_counter = find_last_visible_tree( \
		trees, start_idx, end_idx, increment, target_tree_height)

		scenic_score *= visible_tree_counter
	return scenic_score

def find_last_visible_tree(trees, start_idx, end_idx, increment, target_tree_height):
	visible_tree_counter = 0
	for tree_idx in range(start_idx, end_idx, increment):
		if trees[tree_idx] < target_tree_height:
			visible_tree_counter += 1
		else:
			visible_tree_counter += 1
			break
	return visible_tree_counter