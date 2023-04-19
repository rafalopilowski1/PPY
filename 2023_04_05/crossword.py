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

import os.path

from lib.game import Game

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
