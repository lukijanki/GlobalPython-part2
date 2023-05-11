class Czytelnik:
    def __init__(self,
                 imie: str, nazwisko: str, numer_karty: int):
        self.imie = imie
        self.nazwisko = nazwisko
        self.__numer_karty = numer_karty

    def __str__(self):
        return f"{self.imie} {self.nazwisko} - numer karty: {self.__numer_karty}"

czytelnik1 = Czytelnik(
    imie = "Jan",
    nazwisko = "Kowalksi",
    numer_karty = 123451
    )

print(czytelnik1)

def pobierz_numer(self):
     return self.__numer_karty



print(pobierz_numer(czytelnik1))
