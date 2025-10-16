import random

class Player:
	def __init__(self, letter:str):
		self.letter = letter

	def get_move(self, game):
		pass

class RandomComputerPlayer(Player):
	def __init__(self, letter):
		super().__init__(letter)

	def get_move(self, game):
		return random.choice(game.available_moves())

class HumanPlayer(Player):
	def __init__(self, letter):
		super().__init__(letter)
	
	def get_move(self, game):
		valid = False
		val = None
		while not valid:
			square = input(self.letter + "'s turn. Input move (0-8): ")
			try:
				val = int(square)
				if val not in game.available_moves():
					raise ValueError
				valid = True
			except ValueError as e:
				print("Invalid square. Try again!")
		return val