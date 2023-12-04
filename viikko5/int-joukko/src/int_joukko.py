
class IntJoukko:
    def __init__(self, _kapasiteetti=None, _kasvatuskoko=None):
        self._set = set()

    def kuuluu(self, n: int) -> bool:
        return n in self

    def lisaa(self, n: int):
        if n not in self:
            self._set.add(n)

    def poista(self, n: int):
        if n in self:
            self._set.remove(n)

    def mahtavuus(self):
        return len(self._set)

    def to_int_list(self):
        return list(self._set)

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
        # Example result: "{0, 1, 52}"
        return "{" + ", ".join(str(n) for n in self) + "}"

    def __iter__(self):
        return self._set.__iter__()
