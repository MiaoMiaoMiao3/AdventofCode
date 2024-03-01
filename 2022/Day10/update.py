import setters

# UPDATES
def update_register_part(instruction, register_tracker, signal_strength, target_cycle_count):
	new_register_tracker = register_tracker
	cycle_count_required = update_cycle_count(instruction[0])
	for cycle_count in range(0, cycle_count_required):
		new_register_tracker["cycle"] += 1
		signal_strength, target_cycle_count = update_signal_strength(new_register_tracker, signal_strength, target_cycle_count)
		if cycle_count == (cycle_count_required - 1):
			new_register_tracker["value"] = update_register_value(instruction, new_register_tracker["value"])
	return new_register_tracker, signal_strength, target_cycle_count

def update_CRT_image(instruction, register_tracker, sprite, crt_image):
	new_register_tracker = register_tracker
	cycle_count_required = update_cycle_count(instruction[0])

	for cycle_count in range(0, cycle_count_required):

		if new_register_tracker["cycle"] <= 240:
			crt_image = update_CRT_pixel(crt_image, sprite, new_register_tracker["cycle"])
			for row in crt_image:
				print(''.join(row))
			print(' ')
		new_register_tracker["cycle"] += 1
		if cycle_count == (cycle_count_required - 1):
			new_register_tracker["value"] = update_register_value(instruction, new_register_tracker["value"])
			sprite = update_sprites(new_register_tracker["value"])

	return sprite, crt_image

def update_sprites(register_value):
	sprite = setters.reset_sprites()
	for sprite_idx in range(-1, 2):
		register_value = register_value
		sprite[register_value + sprite_idx] = "#"

	return sprite

def update_CRT_pixel(crt_image, sprite, register_cycle):
	crt_image_target_row = setters.set_crt_target_row(register_cycle)
	crt_draw_position = setters.set_crt_draw_position(register_cycle)
	# print('register cycle', register_cycle, crt_draw_position)
	# print(sprite)
	# print('ROW, col', crt_image_target_row, crt_draw_position)
	crt_image[crt_image_target_row][crt_draw_position] = sprite[crt_draw_position]

	return crt_image
	
def update_cycle_count(instruction):
	cycle_count_mapper = { \
		"noop" : 1,
		"addx" : 2,
	}
	
	cycle_count_required = cycle_count_mapper[instruction]
	return cycle_count_required

def update_register_value(instruction, register_value):
	instruction_command = instruction[0]
	if len(instruction) > 1: 
		change_value = int(instruction[1])
	else:
		change_value = 0

	if instruction_command == "noop":
		return register_value
	elif instruction_command == "addx":
		register_value += change_value
	return register_value

def update_signal_strength(register_tracker, signal_strength, target_cycle_count):
	cycle_count = register_tracker["cycle"]
	target_cycle_increment = setters.set_target_cycle_increment()
	if cycle_count == 20:
		signal_strength =  (register_tracker["value"] * cycle_count)
		target_cycle_count += target_cycle_increment
	elif cycle_count == target_cycle_count:
		signal_strength = signal_strength + (register_tracker["value"] * cycle_count)
		if target_cycle_increment <= 220:
			target_cycle_count += target_cycle_increment
	return signal_strength, target_cycle_count