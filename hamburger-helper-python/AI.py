import cards_array;
import cards

def add_cards(hand, deck):
	while True:
		if len(hand) < 5:
			hand.append(deck[0])
			deck.remove(deck[0])
		else:
			break
	return hand, deck
	
def ai_main(hand, deck):
	is_bun = False
	is_patty = False
	is_topping = False
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
		ai_card_combo, hand, deck = ai_combo(hand, deck)
		hand, deck = add_cards(hand, deck)
		return ai_card_combo, hand, deck
	else:	
		ai_card, hand, deck = ai_single(hand, deck)
		hand, deck = add_cards(hand, deck)
		return ai_card, hand, deck
	
	#####################Single########################
def ai_single(hand, deck):
	test_card = cards.card("null", 0)
	current_largest = test_card
	for x in hand:
		if x.get_value() > current_largest.get_value() and x.get_name() != "Mayo" and x.get_name() != "Ketchup" and x.get_name() != "Laxative" and x.get_name() != "Exercise":
			current_largest = x;

	if current_largest.get_name() == "null":
		hand.remove(hand[0])
		ai_card = cards.card("Patty", 1)
	else:	
		hand.remove(current_largest)
		ai_card = current_largest
	hand, deck = add_cards(hand, deck)
	ai_card_choice = []
	ai_card_choice.append(ai_card.get_name().lower())
	return ai_card_choice, hand, deck

def ai_combo(hand, deck):
	choices = []
	for x in hand:
		if x.get_name() == "Bun":
			choices.append(x)
			break
	for x in hand:
		if x.get_name() == "Patty":
			choices.append(x)
			break
	for x in hand:
		if x.get_name() == "Lettuce" or x.get_name() == "Tomato" or x.get_name() == "Onion" or x.get_name() == "Pickle" or x.get_name() == "Ketchup" or x.get_name() == "Mayo":
			choices.append(x)
			break
	for x in hand:
		if x.get_name() == "Bun":
			hand.remove(x)
			break
	for x in hand:
		if x.get_name() == "Patty":
			hand.remove(x)
			break
	for x in hand:
		if x.get_name() == "Lettuce" or x.get_name() == "Tomato" or x.get_name() == "Onion" or x.get_name() == "Pickle" or x.get_name() == "Ketchup" or x.get_name() == "Mayo":
			hand.remove(x)
			break
	hand, deck = add_cards(hand, deck)
	ai_card_combo = []
	for x in choices:
		ai_card_combo.append(x.get_name().lower())
	return ai_card_combo, hand, deck
