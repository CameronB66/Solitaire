class Card:
	def __init__(self, suit, val):
		self.suit = suit
		self.val = val
		self.num_val = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13}[val]
		self.colour = {'S':'B','C':'B','D':'R','H':'R'}[suit]

class Column:
	def __init__(self):
		self.cards_hidden = []
		self.stack = []
		self.top = None

	def deal(self, card):
		self.cards_hidden.append(card)

	def turn(self):
		card = self.cards_hidden[-1]
		self.stack = [card]
		self.top = card

class Deck_Turn:
	def __init__(self):
		self.cards = []
		self.index = 0

	def add_card(self, card)
		self.cards.append(card)



class Game:
	def __init__(self):
		self.cols = [Column() for i in range(7)]
		self.deck = []
		for suit in ['H','D','C','S']:
			for val in ['A','2','3','4','5','6','7','8','9','10','J','Q','K','A']:
				self.deck.append(Card(suit, val)

	def deal(self):
		
