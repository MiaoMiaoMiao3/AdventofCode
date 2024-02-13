from collections import deque 

def part1(input):
	packet_marker_length = 4
	start_of_packet_marker = 0
	sequence_tracker = set()
	while len(sequence_tracker) < packet_marker_length:
		temp_list = input[0][start_of_packet_marker:start_of_packet_marker + packet_marker_length]
		sequence_tracker = set(temp_list)
		start_of_packet_marker +=1
	result = start_of_packet_marker + packet_marker_length -1
	return result

def part2(input):
	packet_marker_length = 14
	start_of_packet_marker = 0
	sequence_tracker = set()
	while len(sequence_tracker) < packet_marker_length:
		temp_list = input[0][start_of_packet_marker:start_of_packet_marker + packet_marker_length]
		sequence_tracker = set(temp_list)
		start_of_packet_marker +=1
	result = start_of_packet_marker + packet_marker_length -1
	return result


# HELPER FUNCTIONS

def parser_help(input):
	unparsed_crates = []
	unparsed_procedures = []
	parsed_procedures = []
	for line in input:
		if "[" in line:
			unparsed_crates.append(line)
		elif "move" in line:
			unparsed_procedures.append(line.split(" "))
		elif len(line)>0:
			crate_rows = create_rows(line)
		else:
			continue
	crate_rows = parse_crates(unparsed_crates, crate_rows)
	parsed_procedures = parse_procedure(unparsed_procedures, parsed_procedures)

	return crate_rows, parsed_procedures

def create_rows(input):
	rows = input.split(" ")
	rows = list(filter(filter_blanks, rows))
	row_list = [deque([]) for i in range(len(rows))]
	return row_list

def filter_blanks(input):
	if input == "":
		return False
	return True

def parse_crates(unparsed_crates, crate_rows):
	for crate in unparsed_crates:
		index_iter = 0
		for i in range(0,len(crate)-1, 4):
			if crate[i]=="[":
				crate_rows[index_iter].appendleft(crate[i+1])
			index_iter += 1
	return crate_rows

def parse_procedure(unparsed_procedures, result):
	for procedure in unparsed_procedures:
		temp = []
		temp.append(int(procedure[1]))
		temp.append(int(procedure[3]))
		temp.append(int(procedure[5]))
		result.append(temp)
	return result

def move_crates(crate_rows, parsed_procedures, is_multiple):
	modded_crates = crate_rows
	for procedure in parsed_procedures:
		col_from = procedure[1] - 1
		col_to = procedure[2] - 1
		num_crates = procedure[0]
		temp = deque([])
		for i in range(num_crates):
			crate_to_move = modded_crates[col_from].pop()
			if is_multiple:
				temp.appendleft(crate_to_move)
			else:
				modded_crates[col_to].append(crate_to_move)
		if is_multiple:
			modded_crates[col_to].extend(list(temp))
	return modded_crates

def find_top_crate(crate_rows):
	result = ""
	for crate in crate_rows:
		if len(crate)>0:
			result += crate[len(crate)-1]
	return result