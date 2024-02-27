import setters
import update

def part1(input):
	register_tracker = setters.set_register_tracker()
	result = find_signal_strength(input, register_tracker)
	return result

def find_signal_strength(input, register_tracker):
	signal_strength = 1
	target_cycle_count = 20
	for cpu_instruction in input:
		instruction = cpu_instruction.split(" ")
		register_tracker, signal_strength = update.update_register( \
			instruction, register_tracker, signal_strength, target_cycle_count)

	return signal_strength
