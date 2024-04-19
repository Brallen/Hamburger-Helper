import cards_array

#Gets: the single playing card used for the turn; gets the new hand after the turn; gets the new deck after the turn.
#Returns: The playing card chosen for the turn.
def player_main(hand, deck):
	is_bun = False
	is_patty = False
	is_topping = False
	
	print("Your hand: ")
	print(hand)
	print(" ")
	
	for x in hand:
		if x.get_name() == "Bun":
			is_bun = True
	for x in hand:
		if x.get_name() == "Patty":
			is_patty = True
	for x in hand:
		if x.get_name() == "Lettuce" or x.get_name() == "Tomato" or x.get_name() == "Onion" or x.get_name() == "Pickle" or x.get_name() == "Ketchup" or x.get_name() == "Mayo":
			is_topping = True
	
	if is_bun == True and is_patty == True and is_topping == True:
			possibilities = []
			for x in hand:
				if x.get_name().lower() != "exercise" and x.get_name().lower() != "laxative":
					is_in = False
					for y in possibilities:
						if x.get_name().lower() == y.get_name().lower():
							is_in = True
					if is_in == False:
						possibilities.append(x)
			print(" ")

			
			while True:
				combo_input = input("Would you like to play a combo? Y/n: ").lower()
				if combo_input == "y":		
					playing_card, hand, deck = get_card_combo(hand, deck, len(possibilities))
					hand, deck = add_cards(hand, deck)
					return playing_card, hand, deck
				elif combo_input == "n":
					playing_card, hand, deck = get_card(hand, deck)
					hand, deck = add_cards(hand, deck)
					return playing_card, hand, deck
				else:
					print("Invalid input.")
				
	else:	
		playing_card, hand, deck = get_card(hand, deck)
		hand, deck = add_cards(hand, deck)
		return playing_card, hand, deck
#Asks the user for what card they are playing, then removes that from their hand and returns it.
def get_card(hand, deck):
	while True:
		chosen_card = input("Enter playing card: ").lower()
		if chosen_card == "ketchup" or chosen_card == "mayo":
			print("Multipliers can't be used for single attacks! ")
			print("")
		elif chosen_card != "bun" and chosen_card != "patty" and chosen_card !=  "lettuce" and chosen_card != "tomato" and chosen_card != "onion" and chosen_card !=  "pickle" and chosen_card != "exercise" and chosen_card != "laxative":
			print("You don't have this card! (Make sure to check spelling!)")
			print("")
		else:
			playing_card = hand[0]
			for x in hand:
				if chosen_card == x.get_name().lower():
					playing_card = x
					hand.remove(playing_card)
					break
			break
	playing_card_name = []
	playing_card_name.append(playing_card.get_name().lower())
	return playing_card_name, hand, deck

#Asks the user if they want to play a combo and if so what cards they choose
def get_card_combo(hand, deck, possibilities):
	
	playing_card = []
	
	while True:
		while True:
			amount = input("Enter how many cards you would like to use: ")
			try:
				amount = int(amount)
				if amount > possibilities:
					print("Number to high for valid inputs in your hand")
				else:
					break
			except:
				print("That is not a number")
		if int(amount) >= 3 and int(amount) <= 5:
			break
		else:
			print("You must enter a combo greater than or equal to three and less then or equal to five")
			print("")
			
	for x in range(int(amount)):
		while True:
			items = input("What would you like to add? ").lower()
			if items == "exercise" or items == "laxatives":
				print("You can't use healing items in a combo.")
			else:
				if items in playing_card:
					print("Only one ingredient of the same type per burger")
					print("")
				elif items != "bun" and items != "patty" and items!=  "lettuce" and items != "tomato" and items != "onion" and items !=  "pickle" and items != "exercise" and items!= "laxative" and items!= "ketchup" and items!= "mayo":
					print("You don't have this card! (Make sure to check spelling!)")
					print("")
				else:
					playing_card.append(items)
					break
			
	playing_card_temp = playing_card
	hand_temp = hand
	counter = 0
	for x in playing_card_temp:
		for y in hand_temp:
			if x == y.get_name().lower():
				hand.remove(y)
				break
			counter += 1
	return playing_card, hand, deck
		
		
		
		
#Add cards to the player's hand when it drops below 5 by removing the next cards in the deck.
def add_cards(hand, deck):
	while True:
		if len(hand) < 5:
			hand.append(deck[0])
			deck.remove(deck[0])
		else:
			break
	return hand, deck
