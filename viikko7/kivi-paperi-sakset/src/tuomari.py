from enum import Enum


class Voittaja(Enum):
    TASA = 0
    P1 = 1
    P2 = 2


# Luokka pitää kirjaa ensimmäisen ja toisen pelaajan pisteistä sekä tasapelien määrästä.
class Tuomari:
    def __init__(self):
        self._p1_pisteet = 0
        self._p2_pisteet = 0
        self._tasapelit = 0

    def __str__(self):
        return f"Pelitilanne: {self._p1_pisteet} - {self._p2_pisteet}\nTasapelit: {self._tasapelit}"

    def kirjaa_siirto(self, p1_siirto, p2_siirto):
        match self._ratko_voittaja(p1_siirto, p2_siirto):
            case Voittaja.TASA:
                self._tasapelit += 1
            case Voittaja.P1:
                self._p1_pisteet += 1
            case Voittaja.P2:
                self._p2_pisteet += 1

    def _ratko_voittaja(self, p1, p2) -> Voittaja:
        if p1 == p2:
            return Voittaja.TASA

        if p1 == "k" and p2 == "s":
            return Voittaja.P1
        if p1 == "s" and p2 == "p":
            return Voittaja.P1
        if p1 == "p" and p2 == "k":
            return Voittaja.P1

        return Voittaja.P2
