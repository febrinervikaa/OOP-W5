class EXOSubUnit:
    def __init__(self, nama_subunit, anggota, jumlah_album):
        self.nama_subunit = nama_subunit
        self.anggota = anggota
        self.jumlah_album = jumlah_album
        print(f'Jumlah album yang terjual oleh {self.nama_subunit}:', jumlah_album, 'kopi')
        self.total_penjualan = jumlah_album * 100  # Misalnya 100 ribu unit per album

class Penjualan:
    def __init__(self, nama_subunit, jumlah_album):
        self.nama_subunit = nama_subunit
        self.jumlah_album = jumlah_album

cbx = EXOSubUnit("EXO-CBX", ["Chen", "Baekhyun", "Xiumin"], 1000)
sc = EXOSubUnit("EXO-SC", ["Sehun", "Chanyeol"], 500)

print(f"Total penjualan {cbx.nama_subunit}: {cbx.total_penjualan} ribu kopi")
print(f"Total penjualan {sc.nama_subunit}: {sc.total_penjualan} ribu kopi")

