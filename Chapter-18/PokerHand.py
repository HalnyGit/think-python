"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

from Card import *

class Hist(dict):
	"""A map from each item (x) to its frequency."""

	def __init__(self, seq=[]):
		"Increments the counter associated with item x."
		for x in seq:
			self.count(x)
			
	def count(self, x, f=1):
		"Increments the counter associated with item x."
		self[x] = self.get(x, 0) + f
		if self[x] ==0:
			del self[x]

class PokerHand(Hand):

	all_labels = ['straightflush', 'four', 'full', 'flush', 'straight', 'three', 'twopair', 'pair']

	def suit_hist(self):
		"""Builds a histogram of the suits that appear in the hand.
		Stores the result in attribute suits.
		"""
		self.suits = {}
		for card in self.cards:
			self.suits[card.suit] = self.suits.get(card.suit, 0) + 1
			
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
			
	def has_twopair(self):
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

	def has_flush(self):
		"""Returns True if the hand has a flush, False otherwise.
		Note that this works correctly for hands with more than 5 cards.
		"""
		self.suit_hist()
		for val in self.suits.values():
			if val >= 5:
				return True
		return False
		
	def has_full(self):
		"""Returns True if the hand has straight, False otherwise.
		"""
		self.rank_hist()
		if 3 in self.ranks.values() and 2 in self.ranks.values():
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
		"""Returns True if the hand has a straightflush, False otherwise.
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

	def classify(self):
		""" Classifies the hand
		creates attributes: labels
		"""
		self.labels = []
		for label in PokerHand.all_labels:
			f = getattr(self, 'has_' + label)
			if f():
				self.labels.append(label)
				

		
	
if __name__ == '__main__':
	#the label histogram: map from label to number of occurances
	lhist = Hist()
	
	n = 10000 
	for i in range(n):
		#make a deck
		deck = Deck()
		deck.shuffle()

		#deal the cards and classify the hands
		for i in range(7):
			hand = PokerHand()
			deck.move_cards(hand, 7)
			hand.classify()
			for label in hand.labels:
				lhist.count(label)
		
	for key, value in lhist.iteritems():
		print '{0:15s}{1:}'.format(key, value)

	total_hands = n * 7
	print 'Total hands dealt:', total_hands	
	for label in PokerHand.all_labels:
		freq = lhist.get(label, 0)
		if freq == 0:
			continue
		p = total_hands / freq
		print '{0:15s} happens one time in {1:10.2f} which gives {2:6.2f}% chance'.format(label, p, (1.0/p)*100)

# test
# random_cards = [Card(0, 1), Card(0, 10), Card(0, 11), Card(0, 12), Card(0, 13), Card(2, 1), Card(2, 3)]
# hand = PokerHand()
# for card in random_cards:
	# hand.add_card(card)
# print hand
# print hand.has_full()
# hand.classify()
# print hand.labels	

