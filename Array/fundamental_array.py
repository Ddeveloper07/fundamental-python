# Array => nilai di dalamnya harus memiliki tipe data yang sama
# List => nilai di dalamnya bisa memiliki tipe data yang berbeda
# Array => tipe struktur data yang berjenis linear
# Struktur Data => cara untuk mengatur dan menyimpan data sehingga data-data tersebut dapat diakses dan bekerja secara efisien

# Menggunakan list sebagai array dalam python
# x = [1, 2, 3, 4, 5]
# print(x)

# Menggunakan modul atau library untuk membuat array
# import array

# y = array.array("i",[1, 2, 3, 4, 5])
# print(y)
# print(type(y))

# Latihan Studi Kasus
# Selepas berakhirnya semester genap, para guru dari SMA Dicoding perlu merekap semua nilai ujian akhir semester. 
# Salah satunya adalah guru matematika, guru tersebut perlu merekap nilai dari seluruh siswa yang ada di kelas IPA 1.
# Guru tersebut membuat program menggunakan Python untuk mempermudah proses rekap nilai.

# Penyelesaian kurang efektif
# nama_siswa1 = 90
# nama_siswa2 = 100
# nama_siswa3 = 50
# nama_siswa4 = 80
# nama_siswa5 = 85
# nama_siswa6 = 45
# nama_siswa7 = 80
# nama_siswa8 = 75
# nama_siswa9 = 50
# nama_siswa10 = 60

# print(nama_siswa1)
# print(nama_siswa2)
# print(nama_siswa3)
# print(nama_siswa4)
# print(nama_siswa5)
# print(nama_siswa6)
# print(nama_siswa7)
# print(nama_siswa8)
# print(nama_siswa9)
# print(nama_siswa10)

# Penyelesaian efektif menggunakan array
siswa = [90, 100, 50, 80, 85, 45, 80, 75, 50, 60]

print(siswa)
print(siswa[0])