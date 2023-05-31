from random import randint


while True:
    losowana = randint(0, 100)
    liczba_strzalow = 0
    
    while True:
        strzal = int(input("Podaj liczbę od 0 do 100: "))
        liczba_strzalow += 1

        if strzal == losowana:
            print(f"Gratulacje! Odgadłeś liczbę {losowana} w {liczba_strzalow} strzałach.")
            break
        elif strzal < losowana:
            print("Liczba jest większa od podanej przez Ciebie.")
        else:
            print("Liczba jest mniejsza od podanej przez Ciebie.")

    dalej = input("Czy chcesz zagrać jeszcze raz? (tak/nie): ")
    if dalej.lower() != "tak":
        break