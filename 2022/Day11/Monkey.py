class Monkey:
	def __init__(self, items, inspection_input, transfer_monkey_true, transfer_monkey_false, test_input):
		self.items = items
		self.inspection_input = inspection_input
		self.transfer_monkey_true = transfer_monkey_true
		self.transfer_monkey_false = transfer_monkey_false
		self.test_input = test_input

	def inspection_operation(inspection_input):
		return "Placeholder"

	def transfer_test(self, item):
		test_value = int(self.test_input.split(" ")[len(self.test_input) - 1])
		if "divisible" in self.test_input:
			if (item / test_value) == (item // test_value):
				return True

		return False
