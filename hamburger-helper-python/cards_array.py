import cards
import random

def create_deck():
	deck = []
	counter = 1
	while counter <= 40:
		if counter <= 8:
			deck.append(cards.card("Bun", 1))
		elif counter > 8 and counter <= 16:
			deck.append(cards.card("Patty", 1))
		elif counter > 16 and counter <= 20:
			deck.append(cards.card("Lettuce", 2))
		elif counter > 20 and counter <= 24:
			deck.append(cards.card("Tomato", 2))
		elif counter > 24 and counter <= 27:
			deck.append(cards.card("Onion", 3))
		elif counter > 27 and counter <= 29:
			deck.append(cards.card("Pickle", 4))
		elif counter > 29 and counter <= 34:
			deck.append(cards.card("Exercise", -2))
		elif counter > 34 and counter <= 37:
			deck.append(cards.card("Laxative", -3))
		elif counter > 37 and counter <= 39:
			deck.append(cards.card("Ketchup", 2))
		elif counter == 40:
			deck.append(cards.card("Mayo", 3))
		counter += 1
	random.shuffle(deck)
	return deck
