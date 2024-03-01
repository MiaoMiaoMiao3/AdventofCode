def set_register_tracker():
	return {"cycle": 0, "value": 1}

def set_signal_strength():
	return 1

def set_target_cycle_increment():
	return 40

def set_sprite_position():
	default_sprite = ['#'] * 3
	default_sprite += ['.'] * 37
	return default_sprite

def reset_sprites():
	return ['.'] * 40

def set_crt_image():
	return [['.'] * 40 for i in range(0, 6)]

def set_crt_target_row(register_cycle):
	if register_cycle == 0 or (register_cycle > 0 and register_cycle < 40):
		return 0
	elif register_cycle >= 40 and register_cycle < 80:
		return 1
	elif register_cycle > 80 and register_cycle < 120:
		return 2
	elif register_cycle > 120 and register_cycle < 161:
		return 3
	elif register_cycle > 160 and register_cycle < 201:
		return 4
	else:
		return 5
	
def set_crt_draw_position(register_cycle):
	if register_cycle == 0 or (register_cycle > 0 and register_cycle < 40) :
		return register_cycle
	elif register_cycle >= 40 and register_cycle < 80:
		return register_cycle - 40
	elif register_cycle >= 80 and register_cycle < 120:
		print("I hit")
		return register_cycle - 80
	elif register_cycle >= 120 and register_cycle < 160:
		return register_cycle - 120
	elif register_cycle >= 160 and register_cycle < 200:
		return register_cycle - 160
	else:
		return register_cycle - 200