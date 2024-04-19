def make_hand(deck):
	hand = []
	for x in deck:
		while len(hand) < 5:
			hand.append(deck[0])
			deck.remove(deck[0])
		break
	return hand, deck
