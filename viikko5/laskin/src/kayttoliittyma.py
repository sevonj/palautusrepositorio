from enum import Enum
from tkinter import ttk, constants, StringVar


class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4


class Summa:
    def __init__(self, sovellus, syöte):
        self._sovellus = sovellus
        self._syöte = syöte

    def suorita(self):
        self._sovellus.plus(int(self._syöte()))


class Erotus:
    def __init__(self, sovellus, syöte):
        self._sovellus = sovellus
        self._syöte = syöte

    def suorita(self):
        self._sovellus.plus(-int(self._syöte()))


class Nollaus:
    def __init__(self, sovellus, syöte):
        self._sovellus = sovellus
        self._syöte = syöte

    def suorita(self):
        self._sovellus.nollaa()


class Kumoa:
    def __init__(self, sovellus, syöte):
        self._sovellus = sovellus
        self._syöte = syöte

    def suorita(self):
        pass


class Kayttoliittyma:
    def __init__(self, sovellus, root):
        self._sovellus = sovellus
        self._root = root

        self.kaynnista()

        self._komennot = {
            Komento.SUMMA: Summa(sovellus, self._lue_syote),
            Komento.EROTUS: Erotus(sovellus, self._lue_syote),
            Komento.NOLLAUS: Nollaus(sovellus, self._lue_syote),
            Komento.KUMOA: Kumoa(sovellus, self._lue_syote),
        }

    def _lue_syote(self):
        return self._syote_kentta.get()

    def kaynnista(self):
        self._arvo_var = StringVar()
        self._arvo_var.set(self._sovellus.arvo())
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._arvo_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA),
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS),
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS),
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.KUMOA),
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)

    def _suorita_komento(self, komento):
        komentofunktio = self._komennot[komento]
        try:
            komentofunktio.suorita()
        except ValueError:
            print("Invalid input")
            return

        self._kumoa_painike["state"] = constants.NORMAL
        self._nollaus_painike["state"] = constants.NORMAL
        if komento is Komento.NOLLAUS:
            self._nollaus_painike["state"] = constants.DISABLED
            self._kumoa_painike["state"] = constants.DISABLED

        self._syote_kentta.delete(0, constants.END)
        self._arvo_var.set(self._sovellus.arvo())
