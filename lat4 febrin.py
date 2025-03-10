class AlatBerat:
    def __init__(self, nama, berat):
        self.nama = nama
        self.berat = berat  # dalam kg

    def __add__(self, other):
        return AlatBerat(f"{self.nama} & {other.nama}", self.berat + other.berat)

    def info(self):
        berat_ton = self.berat / 1000 
        return f"Alat berat {self.nama} memiliki total berat {berat_ton:.3f} ton"
    
Excavator = AlatBerat("Excavator", 6820)  # 6.82 ton
Bulldozer = AlatBerat("Bulldozer", 12500)  # 12.5 ton

total_berat = Excavator + Bulldozer
print(total_berat.info())
