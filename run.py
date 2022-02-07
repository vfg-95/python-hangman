from slides import tries
from words import easy_words, hard_words
import os, random

def run_game():
  word = random.choice(easy_words).upper()
  hidden_word = "_ " * len(word)
  print(tries[0])
  print(hidden_word)

def main():
  print("""
         _______  _______  ______    __    _  _______  ______   _______ 
        |       ||       ||    _ |  |  |  | ||   _   ||      | |       |
        |_     _||   _   ||   | ||  |   |_| ||  |_|  ||  _    ||   _   |
          |   |  |  | |  ||   |_||_ |       ||       || | |   ||  | |  |
          |   |  |  |_|  ||    __  ||  _    ||       || |_|   ||  |_|  |
          |   |  |       ||   |  | || | |   ||   _   ||       ||       |
          |___|  |_______||___|  |_||_|  |__||__| |__||______| |_______| 
        """)

  print('Welcome to Tornado, do you think you have what it takes to save the household?')
  print("\nThe rules are very simple:",
    "\n- A word is chosen and you must guess the word by inputting letters",
    "\n- If you guess correct, the letter will appear and you can make a new guess",
    "\n- If your guess is incorrect you will lose a life",
    "\n- You have 5 lives. At 0 the tornado will wipe out the household and it's game over")
  play = input("Press p to play: ")
  if play == 'p':
    run_game()

main()