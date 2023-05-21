from player import Player


class GameState:

    def __init__(self, users=None):
        self.main_word_wasnt_guessed = True
        if users is None:
            users = []
        self.users = users
        self.words = GameState.generate_words()
        self.category = ""
        self.main_word = None

    @staticmethod
    def generate_words():
        return {"Python": {"words": [
            {"word": "CONSOLE", "mainIndex": 3, "hint": "An application that provides I/O services to "
                                                        "character-mode applications"},
            {"word": "CLASS", "mainIndex": 0, "hint": "The foundation of Object-Oriented Programming"},
            {"word": "PYTHON", "mainIndex": 3, "hint": "The language this crossword is written in"},
            {"word": "JETBRAINS", "mainIndex": 7, "hint": "The company behind PyCharm"},
            {"word": "ENIGMA", "mainIndex": 0, "hint": "A cipher device developed and used in the early- to "
                                                       "mid-20th century to protect commercial, diplomatic, "
                                                       "and military communication, employed extensively by Nazi "
                                                       "Germany during World War II, in all branches of the "
                                                       "German military"},
            {"word": "IDE", "mainIndex": 0, "hint": "The acronym for Integrated Developer Environment"},
            {"word": "CONDA", "mainIndex": 3, "hint": "An open-source, cross-platform, language-agnostic package "
                                                      "manager and environment management system, originally "
                                                      "developed to solve difficult package management challenges "
                                                      "faced by Python data scientists"},
            {"word": "LIBRARIES", "mainIndex": 7, "hint": "A collection of related modules, containing bundles of "
                                                          "code that can be used repeatedly in different programs"},
            {"word": "REPL", "mainIndex": 0, "hint": "The acronym for Read-Eval-Print Loop"},
        ]}}

    def play(self):
        categories = list(self.words.keys())
        for category, index in enumerate(categories):
            print(f"{index + 1}. {category}")
        choice = int(input("Wybierz numer kategorii: ")) - 1
        self.category = categories[choice]
        if len(self.users) == 1:
            self.play_solo(self.users[0])
        elif len(self.users) == 2:
            self.play_multi(self.users)

    def play_multi(self, users):
        pass

    def play_solo(self, user: Player):
        self.main_word = GameState.get_main_word(self.words, self.category)
        while self.main_word_wasnt_guessed:
            import random
            next_word = random.choice(self.words)
            self.display_word(next_word, user)
            guess = input("Guess the word: ")
            self.validade_guess(guess, next_word)
        self.display_results()

    def display_word(self, next_word: str, user: Player):
        chars = next_word.split('')
        for letter in chars:
            if letter in user.progress[next_word].guessed_letters:
                print(letter, end=' ')
            else:
                print('', end=' ')
        print()
        for _ in range(len(chars)):
            print('_', end=' ')
        print()
        for index in range(len(chars)):
            if index in self.words[next_word].mainIndex:
                print(index, end=' ')
            else:
                print('', end=' ')
        print()

    def validade_guess(self, guess, word):
        pass

    def display_results(self):
        pass

    @staticmethod
    def get_main_word(words, category):
        category_words = words[category]["words"]
        output = ""
        for word in category_words:
            actual_word: str = word["word"]
            output += actual_word.index(word["mainIndex"])
        return output