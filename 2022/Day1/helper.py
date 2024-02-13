def find_max_total(all_calories):
	total_calories_per_elf = []
	sub_total = 0
	for input in all_calories:
		if (input):
			sub_total += input
		else:
			total_calories_per_elf.append(sub_total)
			sub_total=0
	
	return max(total_calories_per_elf)