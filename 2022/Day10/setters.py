def set_register_tracker():
	return {"cycle": 0, "value": 1}

def set_signal_strength():
	return 1

def set_target_cycle_increment():
	return 40

def set_sprite_position():
	default_sprite = ['#'] * 3
	default_sprite += ['.'] * 36
	return default_sprite

def reset_sprites():
	return ['.'] * 39

def set_crt():
	return [['.'] * 39 for i in range(0, 6)]