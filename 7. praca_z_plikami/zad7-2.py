import random
from os import path
import os

def wczytaj_dane(nazwa_pliku):
    dir_path = path.dirname(__file__)
    data_path = path.join(dir_path, nazwa_pliku)
    with open(data_path, 'r', encoding="utf-8") as plik:
        dane = plik.read().splitlines()
    return dane

def zapisz_do_pliku(kombinacje, nazwa_pliku):
    dir_path = path.dirname(__file__)
    output_path = path.join(dir_path, nazwa_pliku)
    with open(output_path, 'w', encoding="utf-8") as plik:
        for kombinacja in kombinacje:
            plik.write(kombinacja + '\n')

def generuj_kombinacje(imiona, nazwiska, liczba_kombinacji):
    kombinacje = []
    for _ in range(liczba_kombinacji):
        imie = random.choice(imiona)
        nazwisko = random.choice(nazwiska)
        kombinacja = f"{imie} {nazwisko}"
        kombinacje.append(kombinacja)
        print(kombinacja)
    return kombinacje

def main():
    imiona = wczytaj_dane('imiona.txt')
    nazwiska = wczytaj_dane('nazwiska.txt')

    liczba_kombinacji = int(input("Podaj liczbę kombinacji do wygenerowania: "))

    kombinacje = generuj_kombinacje(imiona, nazwiska, liczba_kombinacji)

    zapisz_do_pliku(kombinacje, 'kombinacje.txt')

    print(f"\nWygenerowano {liczba_kombinacji} kombinacji imion i nazwisk. Zapisano do pliku kombinacje.txt.")

if __name__ == "__main__":
    main()
print(os.getcwd())