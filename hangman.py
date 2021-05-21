class Hangman:
    def __init__(self, word):
        self.word = word
        self._word_array = [char for char in word.lower()]
        self.guess = ['_' for i in range(len(self._word_array))]
        self._character = ""
        self.win = False
        self.guess_counter = 6

    def _get_guess(self):
        self._character = input("Enter a character: ").lower()

    def _check_if_valid_character(self):
        while not self._character.isalpha() or len(self._character) > 1:
            print("Invalid Guess")
            self._get_guess()

    def _is_character_in_word(self):
        return self._character in self._word_array
        

    def _add_character_to_guess(self):
        index = self._word_array.index(self._character)
        self.guess[index] = self._character

    def _replace_word_with_under(self):
        print(len(self._word_array))
        for i in range(len(self._word_array)):
            if self._word_array[i] == self._character:
                self._word_array[i] = '_'
                break   

    def _check_to_see_if_win(self):
        no_underscore_found = True
        for char in self.guess:
            if char == "_":
                no_underscore_found = False
        
        if no_underscore_found:
            self.win = True

    def _draw_hang_man(self):
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
        

    def play(self):
        while not self.win:
            if self.guess_counter == 0:
                break

            self._get_guess()

            self._check_if_valid_character()

            if self._is_character_in_word():
                self._add_character_to_guess()
                self._replace_word_with_under()
            else:
                print(f"{self._character} is not in the word")
                self.guess_counter -= 1
                

            self._check_to_see_if_win()
           
            self._draw_hang_man()

            print(self.guess)

        if self.win:
            print("You Win!!!")
        else:
            print("You lost")
        print(f"The word was {self.word}")