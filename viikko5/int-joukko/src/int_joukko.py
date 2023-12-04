KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, _kapasiteetti=KAPASITEETTI, _kasvatuskoko=OLETUSKASVATUS):
        self._kasvatuskoko = _kasvatuskoko
        self._kapasiteetti = _kapasiteetti
        self._size = 0
        self._list = self._luo_lista(self._kapasiteetti)

    def _luo_lista(self, koko) -> list:
        return [0] * koko

    def kuuluu(self, n: int) -> bool:
        return n in self

    def lisaa(self, n: int):
        if n in self:
            return

        if self._size == self._kapasiteetti:
            self._kapasiteetti += self._kasvatuskoko
            old = self._list
            self._list = self._luo_lista(self._kapasiteetti)
            for i, m in enumerate(old):
                self._list[i] = m

        self._list[self._size] = n
        self._size += 1

    def poista(self, n: int):
        if n not in self:
            return

        self._size -= 1
        idx = self._list.index(n)

        for i in range(idx, self._size):
            self._list[i] = self._list[i + 1]

    def mahtavuus(self):
        return self._size

    def to_int_list(self):
        return self._list[: self._size]

    @staticmethod
    def yhdiste(a, b):
        result = IntJoukko()
        for n in a:
            result.lisaa(n)
        for n in b:
            result.lisaa(n)
        return result

    @staticmethod
    def leikkaus(a, b):
        result = IntJoukko()
        for n in a:
            if n in b:
                result.lisaa(n)
        return result

    @staticmethod
    def erotus(a, b):
        result = IntJoukko()
        for n in a:
            if n not in b:
                result.lisaa(n)
        return result

    def __str__(self):
        # Example output: "{0, 1, 52}"
        return "{" + ", ".join(str(n) for n in self) + "}"

    def __iter__(self):
        return self._list[: self._size].__iter__()
