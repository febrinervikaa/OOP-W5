class Karakter:
    def __init__(self, nama, kekuatan):
        self.nama = nama  
        self.kekuatan = kekuatan
    
    def perkenalan(self):
        return f"Saya {self.nama}, kekuatan saya adalah {self.kekuatan}."

class BoboiboyAPI(Karakter):
    def __init__(self):
        super().__init__("Boboiboy API", "Mengeluarkan api supaya robot Adudu meledak")

class BoboiboyAIR(Karakter):
    def __init__(self):
        super().__init__("Boboiboy AIR", "Mengeluarkan air supaya robot Adudu rusak")

class BoboiboyTANAH(Karakter):
    def __init__(self):
        super().__init__("Boboiboy TANAH", "Mengeluarkan serangan gempa agar markas Adudu hancur")

def main():
    Karakter_list = [BoboiboyAPI(), BoboiboyAIR(), BoboiboyTANAH()]
    for Karakter in Karakter_list:
        print(Karakter.perkenalan())

if __name__ == "__main__":
    main()
