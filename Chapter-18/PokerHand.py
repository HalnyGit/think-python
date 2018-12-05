"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

from Card import *


class PokerHand(Hand):

	def suit_hist(self):
		"""Builds a histogram of the suits that appear in the hand.
		Stores the result in attribute suits.
		"""
		self.suits = {}
		for card in self.cards:
			self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

	def has_flush(self):
		"""Returns True if the hand has a flush, False otherwise.
		Note that this works correctly for hands with more than 5 cards.
		"""
		self.suit_hist()
		for val in self.suits.values():
			if val >= 5:
				return True
		return False

	def rank_hist(self):
		"""Builds a histogram of the ranks that appear in the hand.
		Stores the result in attribute ranks.
		"""
		self.ranks = {}
		for card in self.cards:
			self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

	def has_pair(self):
		"""Returns True if the hand has a pair, False otherwise.
		"""
		self.rank_hist()
		for val in self.ranks.values():
			if val >= 2:
				return True
		return False
			
	def has_twopairs(self):
		"""Returns True if the hand has two pairs, False otherwise.
		"""
		self.rank_hist()
		pair_counter = 0
		for val in self.ranks.values():
			if val >= 2:
				pair_counter += 1
		if pair_counter >= 2:
			return True
		return False
		
	def has_three(self):
		"""Returns True if the hand has three of a kind, False otherwise.
		"""
		self.rank_hist()
		for val in self.ranks.values():
			if val >= 3:
				return True
		return False
	
	def has_straight(self):
		"""Returns True if the hand has straight, False otherwise.
		"""
		self.rank_hist()
		card_ranks = self.ranks.keys()
		#if ace in the list create additional list to check consecutivity while substitute ace rank from 1 to 14 
		card_ranks_topace = [14 if x==1 else x for x in card_ranks]
		return self.has_consecutive(5, card_ranks) or self.has_consecutive(5, card_ranks_topace)
	
	def has_full(self):
		"""Returns True if the hand has straight, False otherwise.
		"""
		self.rank_hist()
		if 2 and 3 in self.ranks.values():
			return True
		return False
		
	def has_four(self):
		"""Returns True if the hand has four of a kind, False otherwise.
		"""
		self.rank_hist()
		for val in self.ranks.values():
			if val >= 4:
				return True
		return False
		
	def has_straightflush(self):
		"""Returns True if the hand has four of a kind, False otherwise.
		"""
		self.suit_ranks_map = {}
		for card in self.cards:
			self.suit_ranks_map.setdefault(card.suit, []).append(card.rank)
		##if ace in the list add additional rank 14 to the list to check consecutivity
		for suit, ranks in self.suit_ranks_map.iteritems():
			if 1 in self.suit_ranks_map[suit]:
				self.suit_ranks_map[suit].append(14)
		##check consecutivity of ranks
		for ranks in self.suit_ranks_map.values():
			if self.has_consecutive(5, ranks):
				return True
		return False
		
	def has_consecutive(self, n, lt):
		"""Check if a list contains n-element sub list with consecutive numbers
		n: lenght of sub list
		lst: list with integers
		return: True if conatins or False if not
		"""		
		##without list comprehension
		# subs = []
		# for i in range(len(lt)):
			# if len(lt[i:i+n]) == n:
				# subs.append(lt[i:i+n])
		# for sub in subs:
			# if sub == range(min(sub), max(sub)+1):
				# return True
		# return False
		
		##using list comprehension
		lt.sort()
		subs = [lt[i:i+n] for i in range(len(lt)) if len(lt[i:i+n]) == n]
		return any([sub == range(min(sub), max(sub)+1) for sub in subs])	

	
if __name__ == '__main__':
	#make a deck
	deck = Deck()
	deck.shuffle()

	#deal the cards and classify the hands
	for i in range(7):
		hand = PokerHand()
		deck.move_cards(hand, 7)
		hand.sort()
		print hand
		print hand.has_straightflush()
		print ''

# random_cards = [Card(0, 1), Card(0, 10), Card(0, 11), Card(0, 12), Card(0, 13), Card(2, 2), Card(2, 3), Card(2, 4), Card(2, 5), Card(2, 10)]
# hand = PokerHand()
# for card in random_cards:
	# hand.add_card(card)
#print hand
# hand.has_straightflush()	

