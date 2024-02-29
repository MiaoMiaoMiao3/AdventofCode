def set_register_tracker():
	return {"cycle": 0, "value": 1}

def set_signal_strength():
	return 1

def set_target_cycle_increment():
	return 40

def set_sprite_position():
	return '###.....................................'

def reset_sprites():
	return '........................................'

def set_crt():
	return [['.' * 40] for i in range(0, 6)]