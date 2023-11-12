# # Membuat class
# class Mobil:
#     # Membuat atribut kelas
#     warna = "merah"

# # Membuat objek
# mobil_1 = Mobil()

# # Memanggil atribut objek yaitu warna
# print(mobil_1.warna)

# # Mengubah atribut sesuai dengan kebutuhan
# mobil_1.warna = "biru"

# print(mobil_1.warna)

# Atribut dibagi menjadi 2 => atribut kelas dan atribut objek atau instance

# # jenis atribut kelas memiliki kelemahan, yaitu ketika nilai atribut kelas diubah, perubahan tersebut akan memengaruhi semua objek yang dibuat berdasarkan kelas tersebut.
# class Kucing:
#     # Atribut kelas
#     jenis = "Anggora"

# kucing_1 = Kucing()
# print(kucing_1.jenis)

# kucing_2 = Kucing()
# print(kucing_2.jenis)

# # Mengubah atribut kelas
# Kucing.jenis = "Persia"

# print(kucing_1.jenis)
# print(kucing_2.jenis)

# Atribut object atau instance
# class Mobil:
#     # Atribut instance
#     def __init__(self):
#         self.warna = "Merah"

# mobil_1 = Mobil()
# mobil_2 = Mobil()

# print(mobil_1.warna)
# print(mobil_2.warna)

# # Mengubah atribut instance
# mobil_1.warna = "Hitam"

# # Menampilkan kembali atribut warna
# print(mobil_1.warna)
# print(mobil_2.warna)


# Membuat class dengan banyak parameter dalam class constructor
class Kucing:
    def __init__(self, jenis, warna, umur):
        self.jenis = jenis
        self.warna = warna
        self.umur = umur

    # Python membagi method menjadi 3 jeni => Object Method, Static Method, dan Class Method

    # Object Method
    # object method adalah metode yang melekat terhadap suatu objek dan menggunakan parameter self. Jadi, kita tidak bisa memanggil metode ini langsung melalui kelasnya.
    def ulang_tahun(self):
        self.umur += 1
    
    # Static Method
    @staticmethod
    def intro_kucing():
        print("Ini adalah metode dari kelas kucing")

    # Class Method
    # Penamaan cls merupakan kesepakatan bersama dari programmer Python untuk memudahkan pembacaan kode. Anda dapat mengganti namanya, tidak harus cls.
    @classmethod
    def intro_kucing2(cls):
        print("Ini adalah metode dari kelas kucing menggunakan class method")


# Memanggil Static Method
Kucing.intro_kucing()

# Memanggil Class Method
Kucing.intro_kucing2()

kucing_1 = Kucing("Anggora", "Putih Bersih", 2)

print(kucing_1.jenis)
print(kucing_1.warna)
print("Sebelum ditambahkan: ")
print(f"Umur kucing_1 : {kucing_1.umur} tahun")

kucing_1.ulang_tahun()  # Memanggil metode ulang tahun

print("Sesudah ditambahkan: ")
print(f"Umur kucing_1 : {kucing_1.umur} tahun")


# Static Method dan Class Method erat kaitannya dengan konsep dekorator
# Contoh sederhana dekorator
def my_decorator(func):
    def wrapper():
        print("Sebelum fungsi dieksekusi.")
        func()
        print("Setelah fungsi dieksekusi.")

    return wrapper


# Dekorasi fungsi dengan decorator
@my_decorator
def say_hello():
    print("Hello, World!")


# Memanggil fungsi yang sudah didekorasi
say_hello()

"""
1. Pertama, kita mendefinisikan sebuah fungsi bernama my_decorator. Dekorator ini menerima sebuah fungsi func sebagai parameternya.
2. Dalam fungsi my_decorator, kita mendefinisikan fungsi wrapper(). Fungsi wrapper() bertindak sebagai "pembungkus" 
yang menambahkan perilaku sebelum dan setelah eksekusi dari fungsi func.
3. Setelah itu, fungsi  my_decorator mengembalikan (return) fungsi wrapper sebagai hasilnya. 
Return ini juga menyebabkan fungsi wrapper dijalankan.
4. Kemudian, kita mendefinisikan fungsi say_hello(). Fungsi ini akan menjadi target dekorasi.
5. Untuk mendekorasi say_hello(), kita menggunakan simbol "@" diikuti dengan nama dekorator, 
yaitu @my_decorator sebelum mendefinisikan fungsi say_hello.
6. Jadi, secara alur, ketika fungsi say_hello() dipanggil, 
sebenarnya yang dieksekusi adalah fungsi wrapper() yang menjadi hasil dari dekorasi. 
Oleh karena itu, pesan "Sebelum fungsi dieksekusi." dicetak terlebih dahulu, kemudian 
fungsi say_hello() dieksekusi dan mencetak "Hello, world!", lalu akhirnya, pesan 
"Setelah fungsi dieksekusi." dicetak.

"""
