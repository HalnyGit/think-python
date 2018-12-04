import random

class Card(object):
	""" Represents a standard playing card
	attributes: 
	suit: integer 0-3, 
	rank: integer 1-13
	"""
	
	def __init__(self, suit=0, rank=2):
		self.suit = suit
		self.rank = rank
	
	suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
	rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
				'8', '9', '10', 'Jack', 'Queen', 'King']
	
	def __str__(self):
		"""Returns a human-readable string representation."""
		return '{0:s} of {1:s}'.format(Card.rank_names[self.rank],
										Card.suit_names[self.suit])

	# def __cmp__(self, other):
		##check the suits
		# if self.suit > other.suit: return 1
		# if self.suit < other.suit: return -1
		
		##suits are the same... check ranks
		# if self.rank > other.rank: return 1
		# if self.rank < other.rank: return -1
		
		##ranks are the same... it's a tie
		# return 0
		
	def __cmp__(self, other):
		"""Compares this card to other, first bu suit, then rank.
		Returns a positive number if this > other, negative if other > this,
		and 0 if they are equivalent
		"""
		t1 = (self.suit, self.rank)
		t2 =(other.suit, other.rank)
		return  cmp(t1, t2)
	
	# def __lt__(self, other):
		# return (self.suit, self.rank) < (other.suit, other.rank)

class Deck(object):
	"""Represents deck of cards
		attributes: list of Card objects
	"""
	def __init__(self):
		self.cards = []
		for suit in range(4):
			for rank in range(1, 14):
				card = Card(suit, rank)
				self.cards.append(card)
			
	def	__str__(self):
		res = []
		for card in self.cards:
			res.append(str(card))
		return '\n'.join(res)
		
	def pop_card(self ):
		return self.cards.pop()
	
	def add_card(self, card):
		self.cards.append(card)
	
	def remove_card(self, card):
		"""Removes a card from the deck."""
		self.cards.remove(card)
	
	def shuffle(self):
		random.shuffle(self.cards)
	
	def sort(self):
		self.cards.sort()
	
	# uncomment while not using __lt__ or __cmp__ function within Card class
	# def sort(self):
		# self.cards.sort(lambda x: (x.suit, x.rank)
		
	def move_cards(self, hand, num):
		for i in range(num):
			hand.add_card(self.pop_card())
	
	def deal_hands(self, num_of_hands, num_of_cards):
		hands_lst = []
		for i in range(num_of_hands):
			hands_lst.append(Hand('hand_' + str(i)))
		for hand in hands_lst:
			self.move_cards(hand, num_of_cards)
		return hands_lst
			

class Hand(Deck):
	"""Represents a hand of playing card"""
	
	def __init__(self, label=''):
		self.cards = []
		self.label = label


		
new_deck = Deck()
print '>>>>>>>>>>>>>>>>>>>>new deck:'
print new_deck

new_deck.shuffle()
print '>>>>>>>>>>>>>>>>>>>>shuffled deck:'
print new_deck

new_deck.sort()
print '>>>>>>>>>>>>>>>>>>>>sorted deck:'
print new_deck

hand = Hand('new_hand')
print hand.cards
print hand.label

deck = Deck()
card = deck.pop_card()
hand.add_card(card)
print hand

list_of_hands = new_deck.deal_hands(4, 4)
for elem in list_of_hands:
	print elem
	print '\n'
	