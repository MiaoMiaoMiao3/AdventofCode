import setters
import update

def part1(input):
	register_tracker = setters.set_register_tracker()
	result = find_signal_strength(input, register_tracker)

	return result

def part2(input):
	register_tracker = setters.set_register_tracker()
	result = find_CRT_image(input, register_tracker)
	for row in result:
		print(''.join(row))
	return result

def find_signal_strength(input, register_tracker):
	signal_strength = 1
	target_cycle_count = 20
	for cpu_instruction in input:
		instruction = cpu_instruction.split(" ")
		register_tracker, signal_strength, target_cycle_count = update.update_register_part( \
			instruction, register_tracker, signal_strength, target_cycle_count)

	return signal_strength

def find_CRT_image(input, register_tracker):
	sprite = setters.set_sprite_position()
	crt_image = setters.set_crt_image()
	for cpu_instruction in input:
		instruction = cpu_instruction.split(" ")
		sprite, crt_image = update.update_CRT_image( \
			instruction, register_tracker, sprite, crt_image)

	return crt_image