"""
Contains functions that visualise the GUI of the Hangman game.

Author: Colby Tse
Version: December 15, 2022
"""

BORDER_MAX_WIDTH = 29
WORD_MAX_LEN = 29

class GUI:
	"""
	This class provides utility functions for displaying the GUI.
	"""

	def display_gui(self, word, guessed_indexes, guessed,
		wrong_attempts, win, loss):
		"""
		This function calls other utiltiy functions that put together
		the GUI.
		"""
		self.display_header()
		self.display_word(word, guessed_indexes, loss)
		self.display_guessed(guessed)
		self.display_drawing(wrong_attempts)
		self.display_footer(win, loss)


	def display_header(self):
		"""
		This function displays the header of the GUI.
		"""
		print("+-------------------------------+\n" +
			  "|         H A N G M A N         |\n" +
			  "+-------------------------------+\n" +
			  "|                               |")

	def display_word(self, word, guessed_indexes, loss):
		"""
		This function displays the letters correctly guessed by the
		player, with _ as a placeholder for letters not guessed.
		"""

		# number of blank characters on each side of word to
		# display word in the centre of the GUI
		space = (WORD_MAX_LEN - len(word)) // 2

		# list to hold structure of string to be printed
		ls = ["| ", " " * space, "", " " * space, " |"]
		if space * 2 + len(word) != WORD_MAX_LEN:
			ls[3] += " "

		# reveal letters that have been guessed correctly by player,
		# or when player has lost the game
		for i in range(0, len(word)):
			if guessed_indexes[i] == True or loss:
				ls[2] += word[i]
			else:
				ls[2] += "_"

		print("".join(ls))

	def display_guessed(self, guessed):
		"""
		This function displays all letters guessed by the player,
		including incorrect attempts.
		"""
		print("|                               |")

		# lists to hold structure of strings to be printed
		first_row = ["| ", "", " |"]
		second_row = ["| ", "", " |"]

		# add letters guessed to the rows
		for i in range(0, len(guessed)):
			if i in range(0, 15):
				first_row[1] += guessed[i]
				if i != 14:
					first_row[1] += " " # space out letters
			else:
				second_row[1] += guessed[i]
				if i != 25:
					second_row[1] += " " # space out letters

		# add filler whitespace
		first_row[1] += " " * (BORDER_MAX_WIDTH - len(first_row[1]))
		second_row[1] += " " * (BORDER_MAX_WIDTH - len (second_row[1]))

		print("".join(first_row))
		print("".join(second_row))

	def display_drawing(self, wrong_attempts):
		"""
		This function displays the strokes of the Hangman drawing
		depending on how many wrong attempts the player has made.
		"""
		if wrong_attempts == 0:
			for i in range(0, 7):
				print("|                               |")
		elif wrong_attempts == 1:
			for i in range(0, 6):
				print("|                               |")
			print("|          -+------             |")
		elif wrong_attempts == 2:
			print("|                               |")
			for i in range(0, 5):
				print("|           |                   |")
			print("|          -+------             |")
		elif wrong_attempts == 3:
			print("|            ____               |")
			for i in range(0, 5):
				print("|           |                   |")
			print("|          -+------             |")
		elif wrong_attempts == 4:
			print("|            ____               |")
			print("|           | /                 |")
			print("|           |/                  |")
			for i in range(0, 3):
				print("|           |                   |")
			print("|          -+------             |")
		elif wrong_attempts == 5:
			print("|            ____               |")
			print("|           | /  |              |")
			print("|           |/                  |")
			for i in range(0, 3):
				print("|           |                   |")
			print("|          -+------             |")
		elif wrong_attempts == 6:
			print("|            ____               |")
			print("|           | /  |              |")
			print("|           |/   O              |")
			for i in range(0, 3):
				print("|           |                   |")
			print("|          -+------             |")
		elif wrong_attempts == 7:
			print("|            ____               |")
			print("|           | /  |              |")
			print("|           |/   O              |")
			print("|           |    |              |")
			for i in range(0, 2):
				print("|           |                   |")
			print("|          -+------             |")
		elif wrong_attempts == 8:
			print("|            ____               |")
			print("|           | /  |              |")
			print("|           |/   O              |")
			print("|           |    |              |")
			print("|           |   /               |")
			print("|           |                   |")
			print("|          -+------             |")
		elif wrong_attempts == 9:
			print("|            ____               |")
			print("|           | /  |              |")
			print("|           |/   O              |")
			print("|           |    |              |")
			print("|           |   / \\             |")
			print("|           |                   |")
			print("|          -+------             |")
		elif wrong_attempts == 10:
			print("|            ____               |")
			print("|           | /  |              |")
			print("|           |/   O              |")
			print("|           |   -|              |")
			print("|           |   / \\             |")
			print("|           |                   |")
			print("|          -+------             |")
		elif wrong_attempts == 11:
			print("|            ____               |")
			print("|           | /  |              |")
			print("|           |/   O              |")
			print("|           |   -|-             |")
			print("|           |   / \\             |")
			print("|           |                   |")
			print("|          -+------             |")


	def display_footer(self, win, loss):
		"""
		This function displays the footer of the GUI, with the win
		or loss message displayed when appropriate.
		"""
		print("|                               |")
		if win:
			print("|             WIN!              |")
		elif loss:
			print("|           GAME OVER           |")
		else:
			print("|                               |")

		print("+-------------------------------+")