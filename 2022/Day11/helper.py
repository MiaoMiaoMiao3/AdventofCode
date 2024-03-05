import setters

def part1(input):
	number_of_rounds = 20
	monkeys = setters.batch_create_monkeys(input)
	for round in range(number_of_rounds):
		for monkey in monkeys:
			while len(monkey.items):
				item = monkey.items.pop(0)
				item = calculate_inspection(monkey.inspection_input, item)
				item = item // 3
				monkey.inspect_count += 1
				transfer_to_true_monkey = transfer_test(monkey.test_input, item)
				if transfer_to_true_monkey:
					monkeys[monkey.transfer_monkey_true].items.append(item)
				else:
					monkeys[monkey.transfer_monkey_false].items.append(item)
	print(find_monkey_business(monkeys))

#Reference: https://chasingdings.com/2022/12/11/advent-of-code-day-11-monkey-in-the-middle/
def part2(input):
	number_of_rounds = 10000
	monkeys = setters.batch_create_monkeys(input)
	common_divisor = find_common_divisor(monkeys)
	for round in range(number_of_rounds):
		for monkey in monkeys:
			while len(monkey.items):
				item = monkey.items.pop(0)
				item = calculate_inspection(monkey.inspection_input, item)
				item = item % common_divisor
				monkey.inspect_count += 1
				transfer_to_true_monkey = transfer_test(monkey.test_input, item)
				if transfer_to_true_monkey:
					monkeys[monkey.transfer_monkey_true].items.append(item)
				else:
					monkeys[monkey.transfer_monkey_false].items.append(item)
	print(find_monkey_business(monkeys))



def print_monkeys(monkeys):
	for monkey_idx, monkey in enumerate(monkeys):
		print("monkey_num", monkey_idx)
		print("items", monkey.items)
		print("inspect_count", monkey.inspect_count)
		print(" ")

def determine_value(inspection_text, worry_level):
	if inspection_text == 'old':
		return worry_level
	else:
		return int(inspection_text)

def calculate_inspection(inspection_input, worry_level_old):
	inspection_input_list = inspection_input.split(" ")
	# Remove first 3 elements since input list will initially consist of:
	# ['inspection', 'new', '=', ...]
	inspection_input_list = inspection_input_list[2:]

	value_1 = determine_value(inspection_input_list[0], worry_level_old)
	value_2 = determine_value(inspection_input_list[2], worry_level_old)
	operation = inspection_input_list[1]
	if operation == '+':
		new_value = value_1 + value_2
	elif operation == '-':
		new_value = value_1 - value_2
	elif operation == '*':
		new_value = value_1 * value_2
	else:
		return ValueError

	return new_value


def transfer_test(input_text, item):
	input_text = input_text.split(" ")
	test_value = int(input_text[len(input_text) - 1])
	if "divisible" in input_text:
		if (item % test_value) == 0:
			return True

	return False

def find_monkey_business(monkeys):
	all_monkey_business = setters.set_monkey_business(monkeys)
	all_monkey_business.sort(reverse=True)

	return all_monkey_business[0]*all_monkey_business[1]

def find_common_divisor(monkeys):
	common_divisor = 1
	for monkey in monkeys:
		input_text = monkey.test_input.split(" ")
		common_divisor *= int(input_text[len(input_text) - 1])
	
	return common_divisor