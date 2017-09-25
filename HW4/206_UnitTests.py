import random
import unittest

# SI 206 Fall 2017
# Homework 3 - Code

##COMMENT YOUR CODE WITH:
# Section Day/Time: 
# People you worked with: 

######### DO NOT CHANGE PROVIDED CODE #########
### Below is the same cards.py code you saw in lecture.
### Scroll down for assignment instructions.
#########

class Card(object):
	suit_names =  ["Diamonds","Clubs","Hearts","Spades"]
	rank_levels = [1,2,3,4,5,6,7,8,9,10,11,12,13]
	faces = {1:"Ace",11:"Jack",12:"Queen",13:"King"}

	def __init__(self, suit=0,rank=2):
		self.suit = self.suit_names[suit]
		if rank in self.faces: # self.rank handles printed representation
			self.rank = self.faces[rank]
		else:
			self.rank = rank
		self.rank_num = rank # To handle winning comparison 

	def __str__(self):
		return "{} of {}".format(self.rank,self.suit)

class Deck(object):
	def __init__(self): # Don't need any input to create a deck of cards
		# This working depends on Card class existing above
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card) # appends in a sorted order

	def __str__(self):
		total = []
		for card in self.cards:
			total.append(card.__str__())
		# shows up in whatever order the cards are in
		return "\n".join(total) # returns a multi-line string listing each card

	def pop_card(self, i=-1):
		# removes and returns a card from the Deck
		# default is the last card in the Deck
		return self.cards.pop(i) # this card is no longer in the deck -- taken off

	def shuffle(self):
		random.shuffle(self.cards)

	def replace_card(self, card):
		card_strs = [] # forming an empty list
		for c in self.cards: # each card in self.cards (the initial list)
			card_strs.append(c.__str__()) # appends the string that represents that card to the empty list 
		if card.__str__() not in card_strs: # if the string representing this card is not in the list already
			self.cards.append(card) # append it to the list

	def sort_cards(self):
		# Basically, remake the deck in a sorted way
		# This is assuming you cannot have more than the normal 52 cars in a deck
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card)


def play_war_game(testing=False):
	# Call this with testing = True and it won't print out all the game stuff -- makes it hard to see test results
	player1 = Deck()
	player2 = Deck()

	p1_score = 0
	p2_score = 0

	player1.shuffle()
	player2.shuffle()
	if not testing:
		print("\n*** BEGIN THE GAME ***\n")
	for i in range(52):
		p1_card = player1.pop_card()
		p2_card = player2.pop_card()
		if not testing:
			print("Player 1 plays", p1_card,"& Player 2 plays", p2_card)

		if p1_card.rank_num > p2_card.rank_num:
			if not testing:
				print("Player 1 wins a point!")
			p1_score += 1
		elif p1_card.rank_num < p2_card.rank_num:
			if not testing:
				print("Player 2 wins a point!")
			p2_score += 1
		else:
			if not testing:
				print("Tie. Next turn.")

	if p1_score > p2_score:
		return "Player1", p1_score, p2_score
	elif p2_score > p1_score:
		return "Player2", p1_score, p2_score
	else:
		return "Tie", p1_score, p2_score

# if __name__ == "__main__":
# 	result = play_war_game()
# 	print("""\n\n******\nTOTAL SCORES:\nPlayer 1: {}\nPlayer 2: {}\n\n""".format(result[1],result[2]))
# 	if result[0] != "Tie":
# 		print(result[0], "wins")
# 	else:
# 		print("TIE!")


######### DO NOT CHANGE CODE ABOVE THIS LINE #########

## You can write any additional debugging/trying stuff out code here... 
## OK to add debugging print statements, but do NOT change functionality of existing code.
## Also OK to add comments!

#########







##**##**##**##@##**##**##**## # DO NOT CHANGE OR DELETE THIS COMMENT LINE -- we use it for grading your file
###############################################

### Write unit tests below this line for the cards code above.

class coolandawesomeTests(unittest.TestCase):
	def test01testrank12(self):
		self.assertEqual(str(Card(0,12)).split()[0],"Queen")
	def test02testrank1(self):
		self.assertEqual(str(Card(0,1)).split()[0],"Ace")
	def test03testrank3(self):
		self.assertEqual(str(Card(0,3)).split()[0],"3")
	def test04testsuit1(self):
		self.assertEqual(str(Card(1)).split()[2].lower(),"clubs")
	def test05testsuit2(self):
		self.assertEqual(str(Card(2)).split()[2].lower(),"hearts")
	def test06testvarlist(self):
		self.assertEqual(Card().suit_names,["Diamonds","Clubs","Hearts","Spades"])
	def test07strmeth(self):
		self.assertEqual(Card(2,7).__str__(),"7 of Hearts")
	def test08deckinst52(self):
		self.assertEqual(len(Deck().cards),52)
	def test09popcard(self):
		self.assertEqual(type(Deck().pop_card()),type(Card()))
	def test10wargametupleandstring(self):
		self.assertEqual(type(play_war_game(testing=True)),type(tuple()))
		self.assertEqual(type(play_war_game(testing=True)[0]),type(str()))
	def test11decksort(self): #Test to see if sorting works, first card in sorted deck should be Ace of Diamonds, second 2 of Diamonds, and fifteenth 3 of clubs
		newdeck = Deck()
		newdeck.sort_cards()
		self.assertEqual(str(newdeck.cards[0]),str(Card(0,1)))
		self.assertEqual(str(newdeck.cards[1]),str(Card(0,2)))
		self.assertEqual(str(newdeck.cards[15]),str(Card(1,3)))
	def test12cardreplace(self): #Testing to see if popping cards off deck and replacing them with replace_card method works
		deck = Deck()
		removedcard = deck.pop_card()
		self.assertEqual(len(deck.cards),51)
		deck.replace_card(removedcard)
		self.assertEqual(str(deck.cards[-1]),str(removedcard))
		self.assertEqual(len(deck.cards),52)

#############
## The following is a line to run all of the tests you include:
unittest.main(verbosity=2)
## verbosity 2 to see detail about the tests the code fails/passes/etc.