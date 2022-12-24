"""
Contains the important functionalities of the Hangman game.

Author: Colby Tse
Version: December 15, 2022
"""

MAX_WRONG_ATTEMPTS = 11

class GameEngine:
	"""
	This class provides a framework to store relevant game data.
	"""

	guessed_indexes = [] # indexes of word guessed
	guessed = [] # letters guessed
	wrong_attempts = 0 # number of wrong attempts by player
	prompt = "" # any game prompts

	def __init__(self, word):
		"""
		This is the constructor for the GameEngine class.
		"""
		self.word = word # the word the player needs to guess

		# initialise all indexes of word as not guessed (False)
		for i in range(0, len(word)):
			self.guessed_indexes.append(False)

	def handle_input(self, letter):
		"""
		This function handles the players input, setting a prompt,
		checks whether it is a correct guess and updates data in
		the GameEngine based on the input.
		"""
		letter = letter.upper()

		if letter in self.guessed:
			self.prompt = "You've already guessed this letter."
			return
		elif not letter.isalpha() or len(letter) != 1:
			self.prompt = "Please enter a letter a-z/A-Z."
			return
		else:
			self.guessed.append(letter)
			self.prompt = ""

		correct_guess = False
		for i in range(0, len(self.word)):
			if self.word[i] == letter:
				self.guessed_indexes[i] = True
				correct_guess = True

		if not correct_guess:
			self.wrong_attempts += 1