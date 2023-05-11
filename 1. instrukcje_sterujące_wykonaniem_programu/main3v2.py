from random import randint

while True:
    losowana = randint(0, 100)
    proba = 0
    
    while True:
        proba = int(input("Podaj liczbę od 0 do 100: "))
        losowana += 1

        if proba == losowana:
            print(f"Gratulacje! Udało Ci się odgadnąć liczbę {losowana} w {proba} próbach.")
            break
        elif proba < losowana:
            print("Liczba jest większa.")
        else:
            print("Liczba jest mniejsza.")

    dalej = input("Jeszcze raz? (tak/nie): ")
    if dalej.lower() != "tak":
        break