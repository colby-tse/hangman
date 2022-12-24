"""
Contains the main function of the Hangman game and starts the game.

Author: Colby Tse
Version: December 15, 2022
"""

import sys
import os
import random
from urllib.request import urlopen
from GameEngine import *
from GUI import *

MAX_WRONG_ATTEMPTS = 11

def generate_word(wordlist, difficulty):
	"""
	This function returns a specific length word depending on the
	difficulty given.
	"""
	word = wordlist[random.randint(0, len(wordlist))].upper()

	if difficulty == "1":
		while len(word) >= 5:
			word = wordlist[random.randint(0, len(wordlist))].upper()
	elif difficulty == "2":
		while len(word) < 5 or len(word) >= 9:
			word = wordlist[random.randint(0, len(wordlist))].upper()
	elif difficulty == "3":
		while len(word) < 9:
			word = wordlist[random.randint(0, len(wordlist))].upper()
	else:
		word = wordlist[random.randint(0,len(wordlist))].upper()

	return word

def main():

	# source words from given site and choose one at random
	word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

	response = urlopen(word_site)
	txt = response.read().decode("utf-8")
	wordlist = txt.splitlines()

	# generate a random word based on difficulty (if given)
	if len(sys.argv) > 1:
		word = generate_word(wordlist, sys.argv[1])
	else:
		word = wordlist[random.randint(0,len(wordlist))].upper()
			

	# initialise GameEngine and GUI
	engine = GameEngine(word)
	gui = GUI()

	# main game loop
	while True:

		# store whether game has been won or lost
		win = False
		loss = False
		if False not in engine.guessed_indexes:
			win = True
		elif engine.wrong_attempts == MAX_WRONG_ATTEMPTS:
			loss = True

		# display win or loss message and finish
		if False not in engine.guessed_indexes or \
		engine.wrong_attempts >= MAX_WRONG_ATTEMPTS:
			os.system("cls||clear")
			gui.display_gui(engine.word, engine.guessed_indexes,
				engine.guessed, engine.wrong_attempts, win, loss)
			return

		os.system("cls||clear")
		gui.display_gui(engine.word, engine.guessed_indexes,
			engine.guessed, engine.wrong_attempts, win, loss)
		if engine.prompt != None:
			print(engine.prompt)
		letter = input("Enter a letter: ")
		engine.handle_input(letter)
			
if __name__ == "__main__":
	main()
