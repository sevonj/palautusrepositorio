class Pelaaja:
    def __init__(self, nimi: str):
        self._nimi = nimi

    def anna_siirto(self) -> str:
        return ""


class Ihminen(Pelaaja):
    def anna_siirto(self):
        return input(f"Pelaajan {self._nimi} siirto: ")


class Tekoaly(Pelaaja):
    def __init__(self, nimi: str):
        super().__init__(nimi)
        self._laskuri = 0

    def _päivitä_laskuri(self):
        self._laskuri += 1
        self._laskuri %= 3

    def anna_siirto(self) -> str:
        siirto: str
        match self._laskuri:
            case 0:
                siirto = "k"
            case 1:
                siirto = "p"
            case 2:
                siirto = "2"

        self._päivitä_laskuri()
        print(f"{self._nimi} valitsi: {siirto}")
        return siirto


# "Muistava tekoäly"
class TekoalyParannettu(Pelaaja):
    def __init__(self, nimi, muistin_koko):
        super().__init__(nimi)
        self._muisti = [None] * muistin_koko
        self._indeksi = -1

    def _päivitä_laskuri(self, siirto):
        self._indeksi += 1
        self._indeksi %= len(self._muisti)
        self._muisti[self._indeksi] = siirto

    def anna_siirto(self):
        k = self._muisti.count("k")
        p = self._muisti.count("p")
        s = self._muisti.count("s")

        # Tehdään siirron valinta esimerkiksi seuraavasti;
        # - jos kiviä eniten, annetaan aina paperi
        # - jos papereita eniten, annetaan aina sakset
        # muulloin annetaan aina kivi
        siirto: str
        if k > p or k > s:
            siirto = "p"
        elif p > k or p > s:
            siirto = "s"
        else:
            siirto = "k"

        # Tehokkaampiakin tapoja löytyy, mutta niistä lisää
        # Johdatus Tekoälyyn kurssilla!

        self._päivitä_laskuri(siirto)
        print(f"{self._nimi} valitsi: {siirto}")
        return siirto
