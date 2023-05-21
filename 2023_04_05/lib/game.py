import hashlib
import pickle

from game_state import GameState
from player import Player


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