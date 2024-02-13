from ElfPair import ElfPair

def part1(input):
	assigned_sections = []

	count = 0
	for line in input:
		result = parse_sections(line)
		assigned_sections.append(result)
		if is_full_overlapping(result):
			count +=1
	return count


def part2(input):
	assigned_sections = []

	count = 0
	for line in input:
		result = parse_sections(line)
		assigned_sections.append(result)
		if is_partly_overlapping(result):
			count +=1
	return count


# HELPER FUNCTIONS

def parse_sections(input):
	sections = input.split(",")
	elf1 = sections[0].split("-")
	elf2 = sections[1].split("-")
	result = ElfPair(elf1[0],elf1[1],elf2[0],elf2[1])
	return result

def is_full_overlapping(input):
	e1_start = int(input.elf1_start_section)
	e1_end = int(input.elf1_end_section)
	e2_start = int(input.elf2_start_section)
	e2_end = int(input.elf2_end_section)

	if (e1_start >= e2_start and e1_end <= e2_end) or \
	(e2_start >= e1_start and e2_end <= e1_end):
		return True
	
	return False

def is_partly_overlapping(input):
	e1_start = int(input.elf1_start_section)
	e1_end = int(input.elf1_end_section)
	e2_start = int(input.elf2_start_section)
	e2_end = int(input.elf2_end_section)
	e1_range =range(e1_start, e1_end+1)
	e2_range = range(e2_start, e2_end+1)

	if (e1_start in e2_range) or \
	(e1_end in e2_range) or \
	(e2_start in e1_range) or \
	(e2_end in e1_range):
		print(e1_start, e1_end, e2_start, e2_end)
		return True
	
	return False