HINTA = 5


class Kassapaate:
    def __init__(self):
        self.myytyja_lounaita = 0

    def lataa(self, kortti, summa):
        if summa < 0:
            return

        kortti.lataa(summa)

    def osta_lounas(self, kortti):
        # "Maksukortin tilaa ei myöskään ole tarkoitus tutkia suoraan, koska
        # Maksukortti on mock ei attribuuttien arvojen katsominen edes ole
        # mahdollista/mielekästä."

        # En kyllä keksi tähän mitään muuta keinoa, kuin lukea kortin tila
        # suoraan.

        if kortti.saldo < HINTA:
            return

        kortti.osta(HINTA)
        self.myytyja_lounaita = self.myytyja_lounaita + 1
