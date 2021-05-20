class Hangman:
    def __init__(self, word):
        self.word = [char for char in word.lower()]
        self.guess = ['_' for i in range(len(self.word))]
        self.character = ""
        self.win = False
        self.guess_counter = 6

    def get_guess(self):
        self.character = input("Enter a character: ").lower()

    def check_if_valid_character(self):
        while not self.character.isalpha() or len(self.character) > 1:
            print("Invalid Guess")
            self.get_guess()

    def check_if_character_in_word(self):
        if self.character in self.word:
            self.add_character_to_guess(self.word.index(self.character))
            self.replace_word_with_under()
        else:
            print(f"{self.character} is not in the word")
            self.guess_counter -= 1

    def add_character_to_guess(self, index):
        self.guess[index] = self.character

    def replace_word_with_under(self):
        print(len(self.word))
        for i in range(len(self.word)):
            if self.word[i] == self.character:
                self.word[i] = '_'
                break   

    def check_to_see_if_win(self):
        no_under_found = True
        for i in range(len(self.guess)):
            if self.guess[i] == "_":
                no_under_found = False
        
        if no_under_found:
            self.win = True

    def draw_hang_man(self):
        stage1= "-------\n|     |\n|\n|\n|\n|\n=========="
        stage2= "-------\n|     |\n|     O\n|\n|\n|\n=========="
        stage3= "-------\n|     |\n|     O\n|     |\n|\n|\n=========="
        stage4= "-------\n|     |\n|     O\n|    /|\n|\n|\n=========="
        stage5= "-------\n|     |\n|     O\n|    /|\ \n|\n|\n=========="
        stage6= "-------\n|     |\n|     O\n|    /|\ \n|    /\n|\n=========="
        stage7= "-------\n|     |\n|     O\n|    /|\ \n|    / \ \n|\n=========="
      
        if self.guess_counter == 6:
            print(stage1)
        elif self.guess_counter == 5:
            print(stage2)
        elif self.guess_counter == 4:
            print(stage3)
        elif self.guess_counter == 3:
            print(stage4)
        elif self.guess_counter == 2:
            print(stage5)
        elif self.guess_counter == 1:
            print(stage6)
        elif self.guess_counter == 0:
            print(stage7)
        
        pass

    def play(self):
        while not self.win:
            if self.guess_counter == 0:
                break

            self.get_guess()

            self.check_if_valid_character()

            self.check_if_character_in_word()

            self.check_to_see_if_win()
           
            self.draw_hang_man()

            print(self.guess)

        if self.win:
            print("You Win!!!")
        else:
            print("You lost")
        
    


hangman = Hangman("Oakland")

hangman.play()

