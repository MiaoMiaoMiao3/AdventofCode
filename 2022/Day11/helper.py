import setters

def part1(input):
	monkeys = setters.batch_create_monkeys(input)
	for monkey in monkeys:
		print("items", monkey.items)
		print("inspection", monkey.inspection_input)
		print("transfer_monkey_true", monkey.transfer_monkey_true)
		print("transfer false", monkey.transfer_monkey_false)
		print("test", monkey.test_input)
		print(" ")
	

	return "PLACEHOLDER"

	