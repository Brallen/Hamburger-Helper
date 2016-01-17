import cards_array
import cards
import AI
import player
import hand
import gluttony
import player

ai_gluttony = 0
player_gluttony = 0

#makes the deck and hand for player
player_deck = cards_array.create_deck()
player_hand, player_deck = hand.make_hand(player_deck)

#makes the deck and hand for AI
ai_deck = cards_array.create_deck()
ai_hand, ai_deck = hand.make_hand(ai_deck)

print("")
print("Hello! And welcome to Hamburger Helper!")
print("Rules are simple. You are given ingredient cards that can be used to force feed your opponent.")
print("Both the player and the AI are given gluttony levels that keep track of how close their stomachs are to being over-filled.")
print("The first player to reach 30 gluttony will lose.")
print("In order to beat your opponent, you have options to deal more gluttony by making burgers from the ingredients.")
print(" ")
print("Each ingredient has a point value which are as follows:")
print("Bun: 1        Patty: 1")
print("Lettuce: 2    Tomato: 2")
print("Onion: 3      Pickle: 4")
print("")
print("There are also some topings that are multipliers! They are:")
print("Ketchup: 2x   Mayo: 3x")
print("")
print("Finally, there are some action cards that lower your gluttony level")
print("These actions are:")
print("Exercise: -2  Laxative: -3")
print("")
print("Now that you know the rules, it's time to play!")
print("Good luck!")
print(" ")
username = input("Enter your name: ")
print("----------------------------------------")
print(" ")


#################################GAME#################################
while True:
	player_playing_card, player_hand, player_deck = player.player_main(player_hand, player_deck)
	ai_playing_card, ai_hand, ai_deck = AI.ai_main(ai_hand, ai_deck)

	player_gluttony, ai_gluttony = gluttony.gluttony_math(ai_playing_card, player_playing_card, ai_gluttony, player_gluttony)

	print("----------------------------------------")
	print("AI used " + str(ai_playing_card))
	print(" ")
	print("      " + str(username) + "'s gluttony level: " + str(player_gluttony))
	print("      AI's gluttony level: " + str(ai_gluttony))
	print("----------------------------------------")
	
	if ai_gluttony >= 30 or len(ai_deck) <= 0:
		print("You win!")
		break;
	elif player_gluttony >= 30 or len(player_deck) <= 0:
		print("You have lost!")
		break;
