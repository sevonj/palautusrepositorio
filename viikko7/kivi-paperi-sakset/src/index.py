from kps_peli import KPSPeli, KPSPelaajaVsPelaaja, KPSTekoaly, KPSParempiTekoaly


def main():
    while True:
        peli: KPSPeli

        valinta = (
            input(
                "Valitse pelataanko"
                "\n (a) Ihmistä vastaan"
                "\n (b) Tekoälyä vastaan"
                "\n (c) Parannettua tekoälyä vastaan"
                "\nMuilla valinnoilla lopetetaan"
                "\n> "
            )
            .lower()
            .strip()
        )
        match valinta:
            case "a":
                peli = KPSPelaajaVsPelaaja()
            case "b":
                peli = KPSTekoaly()
            case "c":
                peli = KPSParempiTekoaly()
            case _:
                break
        peli.pelaa()

    print("Pelisessio on nyt ohi.")


if __name__ == "__main__":
    main()
