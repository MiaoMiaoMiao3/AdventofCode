import setters
import update

def part1(input):
	for line in input:
		monkey_specs = line.split(": ")
		if "Monkey" in line:
			continue
		elif "Starting items" in line:
			monkey_items = monkey_specs[1].split(", ")
			monkey_items = list(map(lambda x: int(x), monkey_items))
		elif "Operation" in line:
			print("PLACEHOLDER")
		elif "Test" in line:
			monkey_test_input = monkey_specs[1]
		elif "If true" in line:
			transfer_monkey_true = find_transfer_monkey(monkey_specs[1].split(" "))
			transfer_monkey_true = transfer_monkey_true[len(transfer_monkey_true) - 1]
			transfer_monkey_true = int(transfer_monkey_true)
		elif "If false" in line:
			transfer_monkey_false = find_transfer_monkey(monkey_specs[1].split(" "))

	return "PLACEHOLDER"

def find_transfer_monkey(input):
	transfer_monkey = input[len(input) - 1]
	
	return int(transfer_monkey)
	