"""
Napisz  skrypt  dla  miłośników  krzyżówek.
Skrypt  powinien działaćw  trybie  tekstowym  i umożliwić rozwiązywanie krzyżówek.
Admini też potrzebują rozrywki :D
 - [X] Skrypt powinien być przeznaczony  dla 1 lub  2  graczy.
 - [X] Na  początku  powinna  się  pojawić  opcja logowania  lub rejestracji  graczy.
 - [X] Przy  rejestracji  gracz  podaje unikalny  nick,  e-mail  oraz  haslo.
 - [X] Dane zapisywane są w postaci zaszyfrowanej do pliku.
 - [X] Po zalogowaniu każdego gracza następuje losowanie kategorii hasła głównego oraz wyświetlenie krzyżówki.
 - [] Po wyświetlenie krzyżówki losowany jest gracz, który rozpocznie rozgrywkę jako pierwszy.
     - [] Funkcja ta jest niedostępna, gdy gra tylko 1 gracz.
 - [] Gracz decyduje, które słowo z krzyżówki chce odgadnąć.
 - [] Po wybraniu słowa  wyświetla  się  pytanie do  danego  słowa.
 - [] Po poprawnym odgadnięciu hasła gracz otrzymuje ilość pkt zgodną z ilością liter w słowie i ma możliwość odgadnięcia hasła głównego.
 - [] Za każdą nieodkrytą literkę w haśle zwiększa się mnożnik ostatecznych pkt za krzyżówkę np.hasło główne składa się z 5 liter. Użytkownik odkrył 3 litery i ma 10 pkt na koncie. Ostateczna liczba pkt za krzyżówkę wyniesie 2*10 = 20 pkt.
 - [] W przypadku gdy gracz poda błędne słowo z krzyżówki  to  od  jego  konta  odejmowane są  pkt  zgodnie  z  ilością  liter  w słowie.
 - [] Za błędne odgadniecie hasła głównego nie traci się pkt.
 - [] Powinny być prowadzone statystyki rozgrywek oraz wyświetlane pkt.
"""

import hashlib
import pickle
import os.path


class Player:

    def __init__(self, nick, e_mail, passwd, points=0):
        self.progress = {}
        self.nick = nick
        self.e_mail = e_mail
        self.passwd = passwd
        self.points = points

    def __str__(self):
        return f"{self.nick},{self.e_mail},{self.points},{self.passwd}"


class Game:
    def __init__(self):
        self.game_state = GameState()
        self.current_users = []

    def register_players(self):
        number_of_users = int(input("W ile osób będziesz grać?: "))
        if number_of_users < 0 or number_of_users > 2:
            print("Nie wspieramy takiej liczby graczy :(")
        else:
            sha256 = hashlib.sha256()
            for i in range(number_of_users):
                print(f"Graczu {i + 1}...")
                nick = input("Podaj nick: ")
                e_mail = input("Podaj e-mail: ")
                sha256.update(str.encode(input("Podaj hasło: ")))
                passwd = sha256.hexdigest()
                self.game_state.users.append(Player(nick, e_mail, passwd))
            with open("crossword.bin", "wb") as state_file:
                pickle.dump(self.game_state, state_file)

    def load_saved_players(self):
        with open("crossword.bin", "rb") as state:
            self.game_state = pickle.load(state)

    def log_in(self, user_choice):
        while len(self.current_users) == 0:
            chosen_users = list(filter(lambda u: u.nick == user_choice, self.game_state.users))
            if len(chosen_users) == 0:
                print("Brak takiego gracza!")
                register_choice = input("Czy chcesz się zarejestrować? [tak/nie]: ")
                if register_choice == "tak":
                    self.register_players()
                break
            chosen_user = chosen_users[0]
            saved_hash = chosen_user.passwd
            sha256 = hashlib.sha256()
            sha256.update(str.encode(input("Podaj hasło: ")))
            check_hash = sha256.hexdigest()
            if saved_hash == check_hash:
                print("Zalogowano!")
                self.current_users.append(chosen_user)
            else:
                print("Niepoprawne hasło!")


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


if __name__ == '__main__':
    print("Krzyżówka!")
    game = Game()
    no_of_players = int(input("Podaj liczbę graczy: "))
    if os.path.isfile("crossword.bin"):
        game.load_saved_players()
    while len(game.current_users) != no_of_players:
        nick = input("Podaj nick: ")
        if nick in map(lambda user: user.name, game.current_users):
            game.log_in(nick)
        else:
            print("Jesteś nowy! Zarejestruj się!")
            game.register_players()
    game.game_state.play()
