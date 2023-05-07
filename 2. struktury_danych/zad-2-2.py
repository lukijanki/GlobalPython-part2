slowo = input("Podaj słowo: ")
slowo = slowo.strip().lower()
reversed_slowo = slowo[::-1]
if slowo == reversed_slowo:
    print("Słowo jest palindromem!")
else:
    print("Słowo nie jest palindromem.")