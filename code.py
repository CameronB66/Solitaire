import random

class Card:
	def __init__(self, suit, val):
		self.suit = suit
		self.val = val
		self.num_val = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13}[val]
		self.colour = {'S':'B','C':'B','D':'R','H':'R'}[suit]
		self.on = None
		
	def goes_on(self, card):
		if card == None:
			return self.val == 'K'
		
		if card.colour != self.colour:
			if self.num_val + 1 == card.num_val:
				return True
		
		return False

class Column:
	def __init__(self):
		self.cards_hidden = [None]
		self.top = None

	def deal(self, card):
		self.cards_hidden.append(card)

	def turn(self):
		card = self.cards_hidden[-1]
		self.cards_hidden = self.cards_hidden[:-1]
		self.top = card

class Deck_Turn:
	def __init__(self):
		self.deck = []
		self.turned = []

	def turn(self):
		if len(self.deck) == 0:
			if len(self.turned) > 0:
				self.deck = self.turned
				self.turn()
		else:
			size = len(self.deck)
			for i in range (min(3, size)):
				card = self.deck[-1]
				self.deck = self.deck[:-1]
				self.turned.append(card)

	def card(self):
		if len(self.turned) == 0:
			return None
		else:
			return self.turned[-1]

	def take(self):
		if len(self.turned) == 0:
			return None
		else:
			card = self.deck[-1]
			self.turned = self.turned[:-1]
			return self.turned[-1]
		

class Bank_Col:
	def __init__(self, suit):
		self.suit = suit
		self.cards = []
		self.top = None

	def add_card(self, card):
		self.cards.append(card)
		self.top = card

	def complete(self):
		return len(self.cards) == 13

class Game:
	def __init__(self):
		self.cols = [Column() for i in range(7)]
		self.deck = []
		self.bank = [Bank_Col(suit) for suit in ['D','H','C','S']]
		self.deck_turn = Deck_Turn()
		for suit in ['H','D','C','S']:
			for val in ['A','2','3','4','5','6','7','8','9','10','J','Q','K','A']:
				self.deck.append(Card(suit, val)



		



		
