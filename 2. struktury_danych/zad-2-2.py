slowo = input("Podaj słowo: ")
slowo = slowo.strip().lower()
odwrocone_slowo = slowo[::-1]
if slowo == odwrocone_slowo:
    print("Słowo jest palindromem!")
else:
    print("Słowo nie jest palindromem.")