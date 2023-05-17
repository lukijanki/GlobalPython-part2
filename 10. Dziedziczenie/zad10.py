class Pojazd:
    def __init__(self, marka, model, rok_produkcji, kolor):
        self.marka = marka
        self.model = model
        self.rok_produkcji = rok_produkcji
        self.kolor = kolor

    def klaskson(self):
        print("Bip, bip!")

    def __str__(self):
        return f"{self.marka} {self.model}, rok produkcji: {self.rok_produkcji}, kolor: {self.kolor}"

class Jednoslad(Pojazd):
    def __init__(self, marka, model, rok_produkcji, kolor, rodzaj_napedu):
        super().__init__(marka, model, rok_produkcji, kolor)
        self.rodzaj_napedu = rodzaj_napedu

    def przyspiesz(self):
        print("przyspiesza!")

    def __str__(self):
        return super().__str__() + f", rodzaj napędu: {self.rodzaj_napedu}"

class Wieloslad(Pojazd):
    def __init__(self, marka, model, rok_produkcji, kolor, liczba_kol):
        super().__init__(marka, model, rok_produkcji, kolor)
        self.liczba_kol = liczba_kol

    def zatrzymaj(self):
        print("zatrzymuje!")

    def __str__(self):
        return super().__str__() + f", liczba kół: {self.liczba_kol}"