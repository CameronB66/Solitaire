import random

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

	def deal(self, card):
		self.cards_hidden.append(card)

	def turn(self):
		card = self.cards_hidden[-1]
		self.cards_hidden = self.cards_hidden[:-1]
		self.stack = [card]

class Deck_Turn:
	def __init__(self):
		self.cards = []
		self.index = -1
		self.card = None
		self.size = 0

	def add_card(self, card)
		self.cards.append(card)
		self.size += 1

	def turn(self):
		if self.size > 0:
			if self.index + 3 < self.size:
				self.index += 3
				self.card = self.cards[index]
			elif self.index == self.size -1:
				self.index = -1
				self.card = None
				self.turn()
			else:
				self.index = self.size-1
				self.card = self.cards[index]

	def take(self):
		card = self.card
		self.cards = self.cards[:index] + self.cards[index+1:]
		self.index -= 1
		return card

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

	def deal(self):
		random.shuffle(self.deck)
		deal_point = 0
		for i in range(7):
			for j in range(i+1):
				cols[i].deal(self.deck[deal_point])
				deal_point += 1

		while deal_point < 52:
			self.deck_turn.add_card(self.deck[deal_point])
			deal_point += 1

		for i in range(7):
			self.cols[i].turn()

		
	def move_valid_col(self, col_1, col_2):
		if len(self.cols[col_1].stack) == 0:
			return False
		stack_top = self.cols[col_1].stack[0]
		if len(self.cols[col_2].stack) == 0:
			if stack_top.val == 'K':
				return True
			else:
				return False
		stack_bot = self.cols[col_2].stack[-1]
		if stack_top.colour != stack_bot.colour:
			if stack_top.num_val + 1 == stack_bot.num_val:
				return True

		return False:

	def move_valid_deck_col(self, col_2):
		if self.deck_turn.size > 0:
			card = self.deck_turn.card
			if len(self.cols[col_2].stack) == 0:
				if card.val == 'K':
					return True
			else:
				stack_bot = self.cols[col_2].stack[-1]
				if card.colour != stack_bot.colour:
					if card.num_val + 1 == stack_bot.num_val:
						return True
		return False

	def move_valid_bank(self, col_1, bank_2):
		if len(self.cols[col_1].stack) == 0:
			return False
		stack_top = self.cols[col_1].stack[0]
		if stack_top.suit == self.bank[bank_2].suit:
			if len(self.bank[bank_2]) == 0:
				if stack_top.val == 'A':
					return True
			
			else:
				bank_top = self.bank[bank_2].top
				if stack_top.num_val == bank_top.num_val + 1:
					return True
		return False

	def move_valid_deck_bank(self, bank_2):
		if self.deck_turn.size > 0:
			card = self.deck_turn.card
			if card.suit == self.bank[bank_2].suit:
				if len(self.bank[bank_2]) == 0:
					if card.val == 'A':
						return True
				
				else:
					bank_top = self.bank[bank_2].top
					if card.num_val == bank_top.num_val + 1:
						return True
		return False



	def move_col(self, col_1, col_2):
		if self.move_valid_col(col_1, col_2):
			self.cols[col_2].stack += self.cols[col_1].stack
			self.cols[col_1].stack = []
			if len(self.cols[col_1].cards_hidden) > 0):
				self.cols[col_1].turn()
			
	def move_bank(self, col_1, bank_2):
		if self.move_valid_bank(col_1, bank_2):
			card = self.cols[col_1].stack[-1]
			self.cols[col_1].stack = self.cols[col_1].stack[:-1]
			self.bank[bank_2].add_card(card)

	def move_deck_col(self, col_2):
		if self.move_valid_deck_col(col_2):
			card = self.deck_turn.take()
			self.cols[col_2].stack.append(card)

	def move_deck_bank(self, bank_2):
		if self.move_valid_deck_bank(bank_2):
			card = self.deck_turn.take()
			self.bank[bank_2].add_card(card)

	def available_moves(self):
		move_dict = {'col_moves':[],'bank_moves':[],'deck_col_moves':[],'deck_bank_moves':[],'count':0}
		for col_1 in range (7):
			for col_2 in range(7):
				if self.move_valid_col(col_1, col_2):
					move_dict['col_moves'].append([col_1,col_2])
					move_dict['count'] += 1

			for bank_2 in range(4):
				if self.move_valid_bank(col_1, bank_2):
					move_dict['bank_moves'].append([col_1,bank_2])
					move_dict['count'] += 1
			
		for col_2 in range(7):
			if self.move_valid_deck_col(col_2)
				move_dict['deck_col_moves'].append(col_2)
				move_dict['count'] += 1

		for bank_2 in range(4):
			if self.move_valid_deck_bank(bank_2)
				move_dict['deck_bank_moves'].append(bank_2)
				move_dict['count'] += 1

		return move_dict


		



		
