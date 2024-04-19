import player

def gluttony_math(ai_playing_card, player_playing_card, ai_gluttony, player_gluttony):
	
	ai_added_gluttony = 0
	player_added_gluttony = 0
	
	
	for x in player_playing_card:
		if x == "bun":
			ai_added_gluttony += 1
	
		elif x == "patty":
			ai_added_gluttony += 1
	
		elif x == "lettuce":
			ai_added_gluttony += 2
	
		elif x == "tomato":
			ai_added_gluttony += 2
		
		elif x == "onion":
			ai_added_gluttony += 3
	
		elif x == "pickle":
			ai_added_gluttony += 4
		
		elif x == "exercise":
			player_gluttony = player_gluttony - 2
		
		elif x == "laxative":
			player_gluttony = player_gluttony - 3
	
	for x in player_playing_card:
		if x == "ketchup":
			ai_added_gluttony *= 2
			
		if x == "mayo":
			ai_added_gluttony *= 3	

			
					
	for x in ai_playing_card:
		if x == "bun":
			player_added_gluttony += 1
	
		elif x == "patty":
			player_added_gluttony += 1
	
		elif x == "lettuce":
			player_added_gluttony += 2
	
		elif x == "tomato":
			player_added_gluttony += 2
		
		elif x == "onion":
			player_added_gluttony += 3
	
		elif x == "pickle":
			player_added_gluttony += 4
		
		elif x == "exercise":
			ai_gluttony = ai_gluttony - 2
		
		elif x == "laxative":
			ai_gluttony = ai_gluttony - 3
	
	for x in ai_playing_card:
		if x == "ketchup":
			player_added_gluttony *= 2
			
		if x == "mayo":
			player_added_gluttony *= 3	
	
	
	ai_gluttony = ai_gluttony + ai_added_gluttony
	player_gluttony = player_gluttony + player_added_gluttony
	
	return player_gluttony, ai_gluttony
