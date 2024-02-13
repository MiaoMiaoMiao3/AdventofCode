def part1(rucksacks):
	rearrange_item = []
	total = 0
	for rucksack in rucksacks:
		items_considered = int(len(rucksack)/2)
		first_compartment = rucksack[0:items_considered]
		second_compartment = rucksack[items_considered:]
		rearrange_item.append(determine_item(first_compartment, second_compartment))
	
	for item in rearrange_item:
		if(item == item.lower()):
			priority = ord(item) - 96
		else:
			priority = ord(item) - 38

		total += priority

	return total

def determine_item(first_compartment, second_compartment):
	compartment_log = {}
	
	for item in first_compartment:
		if item in compartment_log:
			continue
		else:
			compartment_log[item] = 1
	for item in second_compartment:
		if item in compartment_log:
			return item

	

def part2(rucksacks):
	rearrange_item = []
	total = 0
	index = 0
	while index + 2 < len(rucksacks):
		elf1 = set(rucksacks[index])
		elf2 = set(rucksacks[index + 1])
		elf3 = set(rucksacks[index + 2])
		
		common_item = elf1.intersection(elf2)
		common_item = common_item.intersection(elf3)
		index += 3
		for item in common_item:
			rearrange_item.append(item)

	for item in rearrange_item:
		if(item == item.lower()):
			priority = ord(item) - 96
		else:
			priority = ord(item) - 38

		total += priority
	return total

