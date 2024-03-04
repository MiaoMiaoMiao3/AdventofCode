from Monkey import Monkey

def batch_create_monkeys(input):
	monkeys = []
	for line in input:
		monkey_specs = line.split(": ")
		if "Monkey 0" in line:
			continue
		elif "Starting items" in line:
			monkey_items = monkey_specs[1].split(", ")
			monkey_items = list(map(lambda x: int(x), monkey_items))
		elif "Operation" in line:
			monkey_inspection_input = monkey_specs[1]
		elif "Test" in line:
			monkey_test_input = monkey_specs[1]
		elif "If true" in line:
			transfer_monkey_true = find_transfer_monkey(monkey_specs[1].split(" "))
		elif "If false" in line:
			transfer_monkey_false = find_transfer_monkey(monkey_specs[1].split(" "))
		else: 
			new_monkey = Monkey(
				monkey_items,
				monkey_inspection_input,
				transfer_monkey_true,
				transfer_monkey_false,
				monkey_test_input,
			)

			
		# self.inspection_input = inspection_input
		# self.transfer_monkey_true = transfer_monkey_true
		# self.transfer_monkey_false = transfer_monkey_false
		# self.test_input = test_input
			monkeys.append(new_monkey)
	
	return monkeys

def find_transfer_monkey(input):
	transfer_monkey = input[len(input) - 1]
	
	return int(transfer_monkey)