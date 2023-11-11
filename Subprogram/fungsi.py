# Tujuan dari fungsi adalah mengubah suatu bentuk menjadi bentuk lain dengan aturan yang sama. 
# Fungsi => ada 2 jenis yaitu:
# 1. Built-in functions => kumpulan fungsi yang sudah terintegrasi dengan bahasa pemrograman Python sehingga tidak perlu mengimpor modul atau library tambahan. Fungsi bawaan ini menyediakan fungsi-fungsi inti dan dasar dari bahasa Python. Contoh dari fungsi bawaan adalah print(), len(), type(), range(), dan sebagainya.
# 2. User-defined functions => jenis fungsi yang kita definisikan sendiri untuk melakukan tugas spesifik tertentu. Contoh dari user-defined functions adalah fungsi yang telah kita buat di awal materi ini tentang mencari luas persegi panjang.

# Docstring => akronim dari documentation string
# Contoh penerapannya

def mencari_luas_persegi_panjang(panjang,lebar):
    """
    Fungsi ini digunakan untuk menghitung luas persegi panjang.

    Args:
        panjang (int): Panjang persegi panjang.
        lebar (int): Lebar persegi panjang.

    Returns:
        int: Luas persegi panjang hasil perhitungan.
    """

    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)
print(persegi_panjang_pertama)

# Parameter
# 1. Positional-or-keyword
def greeting(nama, pesan):
    return "Halo, " + nama + "! " + pesan

print(greeting("Dicoding", "Selamat pagi!"))
print(greeting(pesan="Selamat sore!", nama="Dicoding"))

# 2. Positional-Only => ditentukan menggunakan sintaks "/"
def penjumlahan(a, b, /):
    return a + b
# print(penjumlahan(a=3, b=5)) # wrong
print(penjumlahan(3, 5)) # right

# 3. Keyword-Only => ditentukan menggunakan sintaks "*" (asterik)
def greeting_key_only(*, nama, pesan):
    return "Halo, " + nama + "! " + pesan

print(greeting(pesan="Selamat petang!", nama="Dicoding")) # right
print(greeting("Selamat petang!", "Dicoding")) # wrong

# 4. Var-Positional (Variadic Positional Parameter) => ditentukan menggunakan *args
def hitung_total(*args):
    print(type(args))
    total = sum(args)
    return total

print(hitung_total(1, 2, 3, 4, 5, 6, 7, 8, 9))

# 5. Var-Keyword (variadic Keyword parameter) => ditentukan menggunakan sintaks **kwargs
def cetak_info(**kwargs):
    info=""
    for key, value in kwargs.items():
        info += key + ': ' + value + ', '
    return info

print(cetak_info(nama="Dicoding", usia="17", pekerjaan="Python Programmer", tempat_lahir='Bandung', lulusan='ITB'))

# Fungsi Anonim (Lambda Expression)
mencari_luas_persegi_panjang1 = lambda panjang, lebar: panjang*lebar
print(mencari_luas_persegi_panjang1(5,10))

# Variabel Global => suatu variabel yang didefinisikan di luar fungsi atau blok kode apa pun dan dapat diakses dari seluruh bagian program
a = 10

def add(b):
    result = a + b
    return result

bilanganPertama = add(20)
print(bilanganPertama)

# Variabel Lokal => Hanya dapat diakses dari dalam fungsi atau blok kode tempat variabel tersebut didefinisikan
def add(a,b):
    lokal_var = 5
    result = a+b-lokal_var
    return result

bilanganPertama1 = add(10, 20)
print(bilanganPertama1)
