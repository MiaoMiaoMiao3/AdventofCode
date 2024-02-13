def part1(input):
	opponent_mapping = {"A":1,"B":2, "C":3}
	user_mapping = {"X":1, "Y":2, "Z":3}
	outcome_mapping = {"win":6,"draw":3, "lose":0}
	match_scenario = []
	for entry in input:
		match_scenario.append(entry.split(" "))
	total = 0
	
	for scenario in match_scenario:
		sub_total = 0
		opponent_action = opponent_mapping[scenario[0]]
		user_action = user_mapping[scenario[1]]
		if (opponent_action == user_action):
			outcome = outcome_mapping["draw"]
		elif(opponent_action == 1 and user_action == 2) or \
			(opponent_action == 2 and user_action == 3) or \
			(opponent_action == 3 and user_action == 1):
				outcome = outcome_mapping["win"]
		else:
			outcome = outcome_mapping["lose"]
		
		sub_total = user_action + outcome
		total  = total + sub_total
	
	return total

def part2(input):
	opponent_mapping = {"A":1,"B":2, "C":3}
	desired_outcome_mapping = {"X":"lose", "Y":"draw", "Z":"win"}
	outcome_mapping = {"win":6,"draw":3, "lose":0}
	win_mapping = {"A":2, "B":3, "C":1}
	losing_mapping = {"A":3, "B":1, "C":2}
	match_scenario = []
	for entry in input:
		match_scenario.append(entry.split(" "))
	total = 0
	
	for scenario in match_scenario:
		sub_total = 0
		opponent_action_letter = scenario[0]
		opponent_action = opponent_mapping[scenario[0]]
		desired_outcome = desired_outcome_mapping[scenario[1]]
		if (desired_outcome == "win"):
			user_action = win_mapping[opponent_action_letter]
			outcome = outcome_mapping["win"]
		elif(desired_outcome == "draw"):
			user_action = opponent_action
			outcome = outcome_mapping["draw"]
		else:
			user_action = losing_mapping[opponent_action_letter]
			outcome = outcome_mapping["lose"]
		
		sub_total = user_action + outcome
		total  = total + sub_total
	
	return total