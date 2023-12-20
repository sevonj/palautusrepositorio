from tuomari import Tuomari
from pelaajat import Ihminen, Tekoaly, TekoalyParannettu


class KPSPeli:
    def __init__(self) -> None:
        self._ohje = "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
        self._tuomari = Tuomari()
        self.alusta_peli()

    def alusta_peli(self):
        """Tämä metodi ylikirjoitetaan toteutuksen mukaan"""
        self._p1 = None
        self._p2 = None
        self._pelin_nimi = "KPS"
        raise RuntimeError("KPSPeli-luokkaa itseään ei ole tarkoitus pelata!")

    def pelaa(self):
        print(self._pelin_nimi)
        print(self._ohje)

        while True:
            p1_siirto = self._p1.anna_siirto()
            if not self._ovatko_siirrot_ok(p1_siirto):
                break
            p2_siirto = self._p2.anna_siirto()
            if not self._ovatko_siirrot_ok(p2_siirto):
                break

            self._tuomari.kirjaa_siirto(p1_siirto, p2_siirto)
            print(self._tuomari)

        print("Kiitos!")
        print(self._tuomari)

    def _ovatko_siirrot_ok(self, *siirrot: str) -> bool:
        """Tarkistaa yhden tai useamman siirron."""
        for siirto in siirrot:
            if siirto not in {"k", "p", "s"}:
                return False
        return True


class KPSPelaajaVsPelaaja(KPSPeli):
    def alusta_peli(self):
        self._p1 = Ihminen("P1")
        self._p2 = Ihminen("P2")
        self._pelin_nimi = "Kaksinpeli"


class KPSTekoaly(KPSPeli):
    def alusta_peli(self):
        self._p1 = Ihminen("P1")
        self._p2 = Tekoaly("Tietokone")
        self._pelin_nimi = "Yksinpeli"


class KPSParempiTekoaly(KPSPeli):
    def alusta_peli(self):
        self._p1 = Ihminen("P1")
        self._p2 = TekoalyParannettu("Tietokone", 10)
        self._pelin_nimi = "Haastava yksinpeli"
