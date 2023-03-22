binary_str = input("Podaj liczbę w systemie dwójkowym:\nbin=")
octal_str = input("Podaj liczbę w systemie ósemkowym:\noct=")
hex_str = input("Podaj liczbę w systemie szesnastkowym:\nhex=")

bin = int(binary_str, 2)
oct = int(octal_str, 8)
hex = int(hex_str, 16)

print("Zmienna bin zawiera liczbę {} zapisaną w systemie dwójkowym, a po konwersji na system dziesiętny jej wartość wynosi {}".format(binary_str, bin))
print("Zmienna oct zawiera liczbę {} zapisaną w systemie dwójkowym, a po konwersji na system dziesiętny jej wartość wynosi {}".format(octal_str, oct))
print("Zmienna hex zawiera liczbę {} zapisaną w systemie dwójkowym, a po konwersji na system dziesiętny jej wartość wynosi {}".format(hex_str, hex))
