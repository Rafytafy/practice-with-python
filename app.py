from hangman import Hangman
from leaderboard import Leaderboard

hangman = Hangman("aaa")
hangman.play()

name = input("Enter your name: ")

Leaderboard().update_leaderboard(name, hangman.win)
