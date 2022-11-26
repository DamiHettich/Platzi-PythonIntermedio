data = [
    'ahorcado', 'palabra','adivinanza','intento'
]

data_upper = [element.upper for element in data]

import os
import random
import unicodedata

class HangManGame:

    """"Creates the instance to make a game"""

    def __init__(self, data):
        print("_____________HANGMAN game_____________")
        self.strikes = 0
        self.word = None
        self.words = self.__load_words()
        
        self.reset_game_params()
        self.user_input()

    def __randomly_choose_a_word(self):
        length = len(self.words)
        idx = random.randint(0, length-1)
        return self.words[idx]

    def set_word_for_game(self, selected_word):
        assert isinstance(selected_word, str), 'La palabra elegida debe ser un string'
        self.word = selected_word
        return None

    def reset_game_params(self):
        self.accurate_guesses = set()
        self.set_word_for_game(self.__randomly_choose_a_word())


    def __load_words(self):
        base_dir = os.path.dirname(os.path.realpath(__file__))
        imported_words = []
        with open(os.path.join(base_dir, 'data.txt'), 'r', encoding='UTF-8') as file:
            for line in file:
                word = line.strip().upper()
                imported_words.append(word)
        assert len(imported_words) > 0, 'There are not words in the data file'
        return imported_words

    def user_input(self):
        switch = True
        while switch == True:
            my_letter = input('Ingresa una letra: ')
            if self.__validate_input(my_letter):
                is_valid = self.__check_letter_in_word(my_letter)
                if not is_valid:
                    self.strikes +=1
                    print(f"Strikes: {self.strikes}")
                else:
                    print('Le achuntaste esta vez')
                    self.__keep_guessing()

    def __keep_guessing(self):
        if len([char for char in self.word if char not in self.accurate_guesses]) > 0:
            print('keep guessing')

    def __validate_input(self, user_input):
        assert len(user_input )== 1, "ERROR: You can only input a single letter!"
        try:
            user_input = int(user_input)
            return None
        except:
            return user_input.upper()


    def __check_letter_in_word(self, guessed_letter):
        valid_guess = False
        for character in self.word:
            _char = character
            print(_char)
            _letter = guessed_letter
            if _char == _letter:
                self.accurate_guesses.add(guessed_letter)
                valid_guess = True
                return valid_guess



if __name__ == "__main__":
    game = HangManGame(data)