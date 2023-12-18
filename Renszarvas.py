class Renszarvas:

    def __init__(self, nev: str, magassag: str, hely: str, leiras: str):
        self.nev = nev
        nevdarabolt = nev.split(" – ")
        self.nevAngol = nevdarabolt[0]
        self.nevMagyar = nevdarabolt[1]
        self.magassag = int(magassag)
        self.hely = int(hely)
        self.leiras = leiras

    def kiir(self) -> str:
        return f"Rénszarvas neve: {self.nev}, magassága: {self.magassag}"

    def __str__(self) -> str:
        return f"Rénszarvas adatai: Angolnév: {self.nevAngol}, magyar neve: {self.nevMagyar}, magassága: {self.magassag}sorban elfoglalt helye: {self.hely}, leírás: {self.leiras}  "
