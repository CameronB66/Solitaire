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

	def print(self):
		string = self.suit + '-' + self.val
		if len(string) == 3:
			string += ' '
		return string

class Column:
	def __init__(self):
		self.cards_hidden = [None]
		self.top = None
		self.bot = None

	def deal(self, card):
		self.cards_hidden.append(card)

	def add(self, top, bot):
		top.on = self.bot
		self.bot = bot

	def turn(self):
		card = self.cards_hidden[-1]
		if card != None:
			self.cards_hidden = self.cards_hidden[:-1]
		self.top = card
		self.bot = card

	def take(self):
		card1 = self.bot
		card2 = card1.on
		if card2 != None:
			self.bot = card2
		else:
			self.turn()
		return card1

class Deck_Turn:
	def __init__(self):
		self.deck = []
		self.turned = []

	def deal(self, card):
		self.deck.append(card)

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

	def print(self):
		if len(self.turned) < 3:
			string = ''
			for card in self.turned:
				string += ' - ' + card.print()
		else:
			string = ''
			for card in self.turned[-3:]:
				string += ' - ' + card.print()
		return string
		

class Bank_Col:
	def __init__(self, suit):
		self.suit = suit
		self.cards = []
		self.top = None

	def add_card(self, card):
		self.cards.append(card)
		card.on = self.top
		self.top = card

	def complete(self):
		return len(self.cards) == 13
		

class Game:
	def __init__(self):
		self.cols = [Column() for i in range(7)]
		self.deck = []
		self.bank = {suit:Bank_Col(suit) for suit in ['D','H','C','S']}
		self.deck_turn = Deck_Turn()
		for suit in ['H','D','C','S']:
			for val in ['A','2','3','4','5','6','7','8','9','10','J','Q','K','A']:
				self.deck.append(Card(suit, val))


	def deal(self):
		random.shuffle(self.deck)
		deck_point = 0
		for i in range(7):
			for j in range(i+1):
				self.cols[i].deal(self.deck[deck_point])
				deck_point += 1

		while deck_point < 52:
			self.deck_turn.deal(self.deck[deck_point])
			deck_point += 1

		for i in range(7):
			self.cols[i].turn()

	def valid_col1_col2(self, col1, col2):
		col_1 = self.cols[col1]
		if col_1.top == None:
			return False
		col_2 = self.cols[col2]
		return col_1.top.goes_on(col_2.bot)
		
	def move_col1_col2(self, col1, col2):
		if self.valid_col1_col2(col1, col2):
			col_1 = self.cols[col1]
			col_2 = self.cols[col2]
			col_2.add(col_1.top, col_1.bot)
			col_1.turn()

	def valid_deck_col2(self, col2):
		card = self.deck_turn.card()
		if card == None:
			return False
		else:
			return card.goes_on(self.cols[col2].bot)

	def move_deck_col2(self, col2):
		if self.valid_deck_col2(col2):
			card = self.deck_turn.take()
			col_2 = self.cols[col2]
			card.on = col_2.bot
			col_2.bot = card

	def valid_col1_bank(self, col1):
		col_1 = self.cols[col1]
		card = col_1.bot
		if card != None:
			suit = card.suit
			top = self.bank[suit].top
			if top == None:
				if card.val == 'A':
					return True
			else:
				if card.num_val == top.num_val + 1:
					return True
		return False

	def move_col1_bank(self, col1):
		if self.valid_col1_bank(col1):
			col_1 = self.cols[col1]
			card = col_1.take()
			self.bank[card.suit].add_card(card)

	def check_win(self):
		bank = self.bank
		flag1 = bank['S'].complete()
		flag2 = bank['C'].complete()
		flag3 = bank['H'].complete()
		flag4 = bank['D'].complete()
		if flag1 and flag2 and flag3 and flag4:
			return True
		return False

	def print(self):
		for i in range (7):
			print('#' + str(len(self.cols[i].cards_hidden)-1) + '#: ', end='')
			col = self.cols[i]
			card = col.bot
			string = ''
			while card != None:
				string = card.print() + ' - ' + string 
				card = card.on
			print(string)
			print('')

		print('')
		print('Deck:' + self.deck_turn.print(), end='  ')

		string = ''
		for suit in ['C','D','S','H']:
			card = self.bank[suit].top
			if card == None:
				string += '-  -'
			else:
				string += card.print()

		print('Bank:' + string)

















		

