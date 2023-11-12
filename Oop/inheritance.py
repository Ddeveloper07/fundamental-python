# Kelas Dasar Mobil
class Mobil():
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self):
        self.kecepatan += 10


# Kelas Mobil Sport
class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50
    # Penggunaan Super untuk menghindari overriding
    def tambah_kecepatan(self):
        super().tambah_kecepatan()
        print("Kecepatan Anda Meningkat! Hati-hati!")

# Memanggil kelas mobil dasar
mobil_1 = Mobil("Pink", "Lambogati", 300)
print(mobil_1.kecepatan)

# Memanggil kelas mobil sport
mobil_sport_1 = MobilSport("Ijo", "Avangate", 450)
print(mobil_sport_1.kecepatan)
mobil_sport_1.turbo()
print(mobil_sport_1.kecepatan)
