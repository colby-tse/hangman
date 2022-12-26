# hangman
A simple in-terminal Hangman game, written in Python.

## Usage
To start the game, use the command
```
python3 run.py <difficulty>
```
along with an optional difficulty parameter. To choose the difficulty:
* `1` for easy (length less than 5)
* `2` for intermediate (length 5 to 8)
* `3` for hard (length greater than 9).

## How to play
The objective of the game is to guess the hidden word by guessing its letters. Each incorrect guess brings you closer to being 'hanged'.
