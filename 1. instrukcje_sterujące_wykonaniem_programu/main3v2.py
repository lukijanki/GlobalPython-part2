from random import randint

while True:
    losowana = randint(0, 100)
    strzal = 0
    
    while True:
        strzal = int(input("Podaj liczbę od 0 do 100: "))
        losowana += 1

        if strzal == losowana:
            print(f"Gratulacje! Odgadłeś liczbę {losowana} w {strzal} strzałach.")
            break
        elif strzal < losowana:
            print("Liczba jest większa.")
        else:
            print("Liczba jest mniejsza.")

    dalej = input("Czy chcesz zagrać jeszcze raz? (tak/nie): ")
    if dalej.lower() != "tak":
        break