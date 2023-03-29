"""
Lab04 - Game
"""

words = {
    "Zwierzęta": ["kot", "pies", "królik"],
    "Przedmioty": ["telefon", "komputer", "piłka"],
    "Budynki": ["PJATK", "dom", "praca"],
}

players = {1: {"score": 0, "foundLetters": 0}, 2: {"score": 0, "foundLetters": 0}}

categoryIndex = int(input("Podaj numer kategorii: "))
wordIndex = int(input("Podaj numer słowa: "))
print()

category = [x for x in words.keys()][categoryIndex - 1]
word = words[category][wordIndex - 1]

foundLetters = []

move = 0
while move != -1:
    print(f"Graczu {(move % 2) + 1}. Twój ruch!")
    print("Zgadnij słowo!")

    print(f"Kategoria: {category}")

    for letter in word:
        if letter in foundLetters:
            print(letter, end='')
        else:
            print('_', end='')
    print()

    guess = input("Podaj literę: ")
    guess = guess.lower()

    if guess in word.lower():
        players[(move % 2) + 1]["score"] += word.count(guess)
        players[(move % 2) + 1]["foundLetters"] += 1
        foundLetters.append(guess)
        print("Masz to!")

    move += 1

    if set(sorted(word.lower())) == set(sorted(foundLetters)):
        move = -1
        print("Koniec gry!")
        players[(move % 2) + 1]["score"] += (len(word) - players[(move % 2) + 1]["foundLetters"]) * 2
    print()

print(f'Wygrywa gracz {1 if players[1]["score"] > players[2]["score"] else 2} !!!'.upper())
print("#############################")
print("           Punkty            ")
print("#############################")
print(f'Gracz 1: {players[1]["score"]}')
print(f'Gracz 2: {players[2]["score"]}')
