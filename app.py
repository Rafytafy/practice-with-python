from hangman import Hangman
from leaderboard import Leaderboard

hangman1 = Hangman("aaa")
hangman1.play()

name = input("Enter your name: ")

leaderboard1 = Leaderboard()
leaderboard1.update_leaderboard(name, hangman1.win)
